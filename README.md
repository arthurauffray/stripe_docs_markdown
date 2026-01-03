# 💳 Stripe Docs Markdown

> **Mirroring the Stripe API Reference in clean, structured Markdown.**

An offline-first, LLM-optimized collection of the entire Stripe API documentation. Every endpoint, every object, and every guide — organized and ready for your next project.

---

## ✨ Features

- 🏎️ **Optimized for LLMs**: Perfectly formatted for RAG (Retrieval Augmented Generation) and AI context.
- 📂 **Structured Layout**: Mirrors the official [Stripe API Documentation](https://docs.stripe.com/api).
- 💻 **Multi-Language**: Comprehensive code snippets for `curl`, `Python`, `Ruby`, `PHP`, `Node.js`, `Go`, `Java`, and `.NET`.
- 🔍 **Searchable**: Grep your way through the entire Stripe ecosystem in milliseconds.
- 📄 **Clean Markdown**: Zero fluff, just the docs.

## 📁 Repository Structure

The documentation is organized by main categories and subcategories:

```text
docs/
├── Introduction/           # Authentication, Errors, Pagination...
├── Core Resources/         # Accounts, Customers, Payment Intents...
├── Payment Methods/        # Cards, Bank Accounts, Sources...
├── Products/               # Prices, Coupons, Tax Rates...
├── Checkout/               # Checkout Sessions...
├── Billing/                # Invoices, Subscriptions, Plans...
└── ... and 20+ more categories
```



## 🚀 Getting Started

Simply clone the repo and start reading. If you're using this with an AI assistant (like Claude or ChatGPT), pointed it towards specific files for instant context:

```bash
# Example: Using grep to find expansion examples
grep -rn "expand" docs/introduction/
```

## 🛠️ Built for Developers

Whether you're building a new integration or debugging a complex subscription flow, having the docs at your fingertips (without the browser overhead) is a game changer.

- **Fast**: No loading states, just text.
- **Offline**: Works in the air, on a train, or in a bunker.
- **Accurate**: Scraped manually & directly from the source.

---

## ☕ Support

If you find this mirror useful, consider buying me a coffee!

[**Buy me a coffee**](https://donate.stripe.com/eVq14m1Cc5oPfXFcsD6Ri05)

---

*Note: This repository is a community-maintained mirror and is not affiliated with Stripe, Inc.*
