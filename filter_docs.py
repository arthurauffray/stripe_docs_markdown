# Use this script to create a clone of the /docs
# directory with codeblocks of only your
# language of choice.

import argparse
import shutil
import os

# Languages that are considered mutually exclusive "request" languages.
# If we keep one of these, we drop the others (unless they are the fallback).
EXCLUSIVE_LANGS = {
    'ruby', 'python', 'php', 'java', 'node', 'go', 'dotnet', 'curl', 'cli', 'csharp'
}

def get_block_lang(line):
    """
    Returns the language of a code block start line, or None if not a start line.
    Returns '' for empty code blocks (```).
    """
    stripped = line.lstrip()
    if stripped.startswith('```'):
        # It's a block boundary.
        # Check if it has a language specified
        parts = stripped.split('```', 1)
        if len(parts) > 1:
            return parts[1].strip().lower()
        return ''
    return None

def get_file_languages(filepath):
    """
    Scans a markdown file and returns a set of all languages found in code blocks.
    """
    langs = set()
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        in_block = False
        for line in f:
            stripped = line.lstrip()
            if stripped.startswith('```'):
                if not in_block:
                    # Start of block
                    lang = get_block_lang(line)
                    if lang:
                        langs.add(lang)
                    in_block = True
                else:
                    # End of block
                    in_block = False
    return langs

def filter_file_content(filepath, target_langs):
    """
    Reads the file, keeps only the appropriate code blocks, and overwrites the file.
    target_langs: a list of strings (e.g., ['python', 'ruby'])
    """
    # 1. Identify available languages
    available_langs = get_file_languages(filepath)
    
    # Normalize target languages
    target_lower_list = [l.lower() for l in target_langs]
    
    # 2. Determine Keep Strategy
    keep_langs = set()
    
    # Strategy:
    # - non-exclusive languages (json, text, etc) are ALWAYS kept.
    # - for each requested language in target_lower_list, if it is present in the file, keep it.
    # - if NO requested language is present, check for 'curl'.
    #   - if 'curl' is present, keep 'curl' (fallback).
    #   - otherwise, keep none of the exclusive languages.
    
    any_target_found = False
    for t_lang in target_lower_list:
        if t_lang in available_langs:
            keep_langs.add(t_lang)
            any_target_found = True
            
    if not any_target_found and 'curl' in available_langs:
        # Fallback to curl if no target found
        keep_langs.add('curl')
    
    # Read content
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        
    filtered_lines = []
    in_block = False
    skipping = False
    
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith('```'):
            if not in_block:
                # START of block
                lang = get_block_lang(line)
                
                # Check if this block should be skipped
                # It is skipped if it is in EXCLUSIVE_LANGS AND not in keep_langs
                if lang in EXCLUSIVE_LANGS:
                    if lang in keep_langs:
                        skipping = False
                    else:
                        skipping = True
                else:
                    # Not an exclusive lang (e.g. json, text), always keep
                    skipping = False
                
                if not skipping:
                    filtered_lines.append(line)
                
                in_block = True
            else:
                # END of block
                if not skipping:
                    filtered_lines.append(line)
                in_block = False
                skipping = False # Reset for next text
        else:
            if not skipping:
                filtered_lines.append(line)
                
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(filtered_lines)

def process_directory(source_dir, dest_dir, target_langs):
    # 1. Copy entire directory structure
    if os.path.exists(dest_dir):
        print(f"Destination {dest_dir} already exists. Removing it to start fresh...")
        shutil.rmtree(dest_dir)
    
    print(f"Copying {source_dir} to {dest_dir}...")
    shutil.copytree(source_dir, dest_dir)
    
    # 2. Walk through destination and filter .md files
    print(f"Filtering markdown files for languages: {target_langs}")
    count = 0
    for root, dirs, files in os.walk(dest_dir):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                filter_file_content(filepath, target_langs)
                count += 1
                
    print(f"Processed {count} markdown files.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy docs and filter code blocks by language.")
    parser.add_argument("--source", "-s", required=True, help="Source directory (e.g. docs)")
    parser.add_argument("--destination", "-d", required=True, help="Destination directory (e.g. docs_python)")
    parser.add_argument("--languages", "-l", nargs='+', required=True, help="Target languages (e.g. python ruby)")
    
    args = parser.parse_args()
    
    process_directory(args.source, args.destination, args.languages)
