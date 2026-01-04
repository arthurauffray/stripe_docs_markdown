# The Card object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `brand` (string)
  The brand of the card.

- `cancellation_reason` (enum, nullable)
  The reason why the card was canceled.
Possible enum values:
  - `design_rejected`
    The design of this card was rejected by Stripe for violating our [partner guidelines](https://docs.stripe.com/docs/issuing/cards/physical.md#design-review).

  - `lost`
    The card was lost.

  - `stolen`
    The card was stolen.

- `cardholder` (object)
  The [Cardholder](https://docs.stripe.com/docs/api.md#issuing_cardholder_object) object to which the card belongs.

  - `cardholder.id` (string)
    Unique identifier for the object.

  - `cardholder.object` (string)
    String representing the object’s type. Objects of the same type share the same value.

  - `cardholder.billing` (object)
    The cardholder’s billing information.

    - `cardholder.billing.address` (object)
      The cardholder’s billing address.

      - `cardholder.billing.address.city` (string, nullable)
        City, district, suburb, town, or village.

      - `cardholder.billing.address.country` (string, nullable)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `cardholder.billing.address.line1` (string, nullable)
        Address line 1, such as the street, PO Box, or company name.

      - `cardholder.billing.address.line2` (string, nullable)
        Address line 2, such as the apartment, suite, unit, or building.

      - `cardholder.billing.address.postal_code` (string, nullable)
        ZIP or postal code.

      - `cardholder.billing.address.state` (string, nullable)
        State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

  - `cardholder.company` (object, nullable)
    Additional information about a `company` cardholder.

    - `cardholder.company.tax_id_provided` (boolean)
      Whether the company’s business ID number was provided.

  - `cardholder.created` (timestamp)
    Time at which the object was created. Measured in seconds since the Unix epoch.

  - `cardholder.email` (string, nullable)
    The cardholder’s email address.

  - `cardholder.individual` (object, nullable)
    Additional information about an `individual` cardholder.

    - `cardholder.individual.card_issuing` (object, nullable)
      Information related to the card_issuing program for this cardholder.

      - `cardholder.individual.card_issuing.user_terms_acceptance` (object, nullable)
        Information about cardholder acceptance of Celtic [Authorized User Terms](https://stripe.com/docs/issuing/cards#accept-authorized-user-terms). Required for cards backed by a Celtic program.

        - `cardholder.individual.card_issuing.user_terms_acceptance.date` (timestamp, nullable)
          The Unix timestamp marking when the cardholder accepted the Authorized User Terms.

        - `cardholder.individual.card_issuing.user_terms_acceptance.ip` (string, nullable)
          The IP address from which the cardholder accepted the Authorized User Terms.

        - `cardholder.individual.card_issuing.user_terms_acceptance.user_agent` (string, nullable)
          The user agent of the browser from which the cardholder accepted the Authorized User Terms.

    - `cardholder.individual.dob` (object, nullable)
      The date of birth of this cardholder.

      - `cardholder.individual.dob.day` (integer, nullable)
        The day of birth, between 1 and 31.

      - `cardholder.individual.dob.month` (integer, nullable)
        The month of birth, between 1 and 12.

      - `cardholder.individual.dob.year` (integer, nullable)
        The four-digit year of birth.

    - `cardholder.individual.first_name` (string, nullable)
      The first name of this cardholder. Required before activating Cards. This field cannot contain any numbers, special characters (except periods, commas, hyphens, spaces and apostrophes) or non-latin letters.

    - `cardholder.individual.last_name` (string, nullable)
      The last name of this cardholder.  Required before activating Cards. This field cannot contain any numbers, special characters (except periods, commas, hyphens, spaces and apostrophes) or non-latin letters.

    - `cardholder.individual.verification` (object, nullable)
      Government-issued ID document for this cardholder.

      - `cardholder.individual.verification.document` (object, nullable)
        An identifying document, either a passport or local ID card.

        - `cardholder.individual.verification.document.back` (string, nullable)
          The back of a document returned by a [file upload](https://docs.stripe.com/api/issuing/cards/object.md#create_file) with a `purpose` value of `identity_document`.

        - `cardholder.individual.verification.document.front` (string, nullable)
          The front of a document returned by a [file upload](https://docs.stripe.com/api/issuing/cards/object.md#create_file) with a `purpose` value of `identity_document`.

  - `cardholder.livemode` (boolean)
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

  - `cardholder.metadata` (object)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

  - `cardholder.name` (string)
    The cardholder’s name. This will be printed on cards issued to them.

  - `cardholder.phone_number` (string, nullable)
    The cardholder’s phone number. This is required for all cardholders who will be creating EU cards. See the [3D Secure documentation](https://docs.stripe.com/docs/issuing/3d-secure.md#when-is-3d-secure-applied) for more details.

  - `cardholder.preferred_locales` (array of enums, nullable)
    The cardholder’s preferred locales (languages), ordered by preference. Locales can be `de`, `en`, `es`, `fr`, or `it`. This changes the language of the [3D Secure flow](https://docs.stripe.com/docs/issuing/3d-secure.md) and one-time password messages sent to the cardholder.

  - `cardholder.requirements` (object)
    Information about verification requirements for the cardholder.

    - `cardholder.requirements.disabled_reason` (enum, nullable)
      If `disabled_reason` is present, all cards will decline authorizations with `cardholder_verification_required` reason.
Possible enum values:
      - `listed`
        Account might be on a prohibited persons or companies list. The `past_due` field contains information that you need to provide before the cardholder can approve authorizations.

      - `rejected.listed`
        Cardholder is rejected because they are on a third-party prohibited persons or companies list (such as financial services provider or government). Their status will be `blocked`.

      - `requirements.past_due`
        Cardholder has outstanding requirements. The `past_due` field contains information that you need to provide before the cardholder can activate cards.

      - `under_review`
        This cardholder has raised additional review. Stripe will make a decision and update the `disabled_reason` field.

    - `cardholder.requirements.past_due` (array of enums, nullable)
      Array of fields that need to be collected in order to verify and re-enable the cardholder.
Possible enum values:
      - `company.tax_id`
        The cardholder’s business number (Tax ID).

      - `individual.card_issuing.user_terms_acceptance.date`
        The Unix timestamp marking when the Cardholder accepted their Authorized User Terms. Required for Celtic Spend Card users.

      - `individual.card_issuing.user_terms_acceptance.ip`
        The IP address from which the Cardholder accepted their Authorized User Terms. Required for Celtic Spend Card users.

      - `individual.dob.day`
        The cardholder’s date of birth’s day.

      - `individual.dob.month`
        The cardholder’s date of birth’s month.

      - `individual.dob.year`
        The cardholder’s date of birth’s year.

      - `individual.first_name`
        The cardholder’s legal first name.

      - `individual.last_name`
        The cardholder’s legal last name.

      - `individual.verification.document`
        The front and back of a government-issued form of identification.

  - `cardholder.spending_controls` (object, nullable)
    Rules that control spending across this cardholder’s cards. Refer to our [documentation](https://docs.stripe.com/docs/issuing/controls/spending-controls.md) for more details.

    - `cardholder.spending_controls.allowed_categories` (array of enums, nullable)
      Array of strings containing [categories](https://docs.stripe.com/docs/api.md#issuing_authorization_object-merchant_data-category) of authorizations to allow. All other categories will be blocked. Cannot be set with `blocked_categories`.
Possible enum values:
      - `ac_refrigeration_repair`
      - `accounting_bookkeeping_services`
      - `advertising_services`
      - `agricultural_cooperative`
      - `airlines_air_carriers`
      - `airports_flying_fields`
      - `ambulance_services`
      - `amusement_parks_carnivals`
      - `antique_reproductions`
      - `antique_shops`
      - `aquariums`
      - `architectural_surveying_services`
      - `art_dealers_and_galleries`
      - `artists_supply_and_craft_shops`
      - `auto_and_home_supply_stores`
      - `auto_body_repair_shops`
      - `auto_paint_shops`
      - `auto_service_shops`
      - `automated_cash_disburse`
      - `automated_fuel_dispensers`
      - `automobile_associations`
      - `automotive_parts_and_accessories_stores`
      - `automotive_tire_stores`
      - `bail_and_bond_payments`
      - `bakeries`
      - `bands_orchestras`
      - `barber_and_beauty_shops`
      - `betting_casino_gambling`
      - `bicycle_shops`
      - `billiard_pool_establishments`
      - `boat_dealers`
      - `boat_rentals_and_leases`
      - `book_stores`
      - `books_periodicals_and_newspapers`
      - `bowling_alleys`
      - `bus_lines`
      - `business_secretarial_schools`
      - `buying_shopping_services`
      - `cable_satellite_and_other_pay_television_and_radio`
      - `camera_and_photographic_supply_stores`
      - `candy_nut_and_confectionery_stores`
      - `car_and_truck_dealers_new_used`
      - `car_and_truck_dealers_used_only`
      - `car_rental_agencies`
      - `car_washes`
      - `carpentry_services`
      - `carpet_upholstery_cleaning`
      - `caterers`
      - `charitable_and_social_service_organizations_fundraising`
      - `chemicals_and_allied_products`
      - `child_care_services`
      - `childrens_and_infants_wear_stores`
      - `chiropodists_podiatrists`
      - `chiropractors`
      - `cigar_stores_and_stands`
      - `civic_social_fraternal_associations`
      - `cleaning_and_maintenance`
      - `clothing_rental`
      - `colleges_universities`
      - `commercial_equipment`
      - `commercial_footwear`
      - `commercial_photography_art_and_graphics`
      - `commuter_transport_and_ferries`
      - `computer_network_services`
      - `computer_programming`
      - `computer_repair`
      - `computer_software_stores`
      - `computers_peripherals_and_software`
      - `concrete_work_services`
      - `construction_materials`
      - `consulting_public_relations`
      - `correspondence_schools`
      - `cosmetic_stores`
      - `counseling_services`
      - `country_clubs`
      - `courier_services`
      - `court_costs`
      - `credit_reporting_agencies`
      - `cruise_lines`
      - `dairy_products_stores`
      - `dance_hall_studios_schools`
      - `dating_escort_services`
      - `dentists_orthodontists`
      - `department_stores`
      - `detective_agencies`
      - `digital_goods_applications`
      - `digital_goods_games`
      - `digital_goods_large_volume`
      - `digital_goods_media`
      - `direct_marketing_catalog_merchant`
      - `direct_marketing_combination_catalog_and_retail_merchant`
      - `direct_marketing_inbound_telemarketing`
      - `direct_marketing_insurance_services`
      - `direct_marketing_other`
      - `direct_marketing_outbound_telemarketing`
      - `direct_marketing_subscription`
      - `direct_marketing_travel`
      - `discount_stores`
      - `doctors`
      - `door_to_door_sales`
      - `drapery_window_covering_and_upholstery_stores`
      - `drinking_places`
      - `drug_stores_and_pharmacies`
      - `drugs_drug_proprietaries_and_druggist_sundries`
      - `dry_cleaners`
      - `durable_goods`
      - `duty_free_stores`
      - `eating_places_restaurants`
      - `educational_services`
      - `electric_razor_stores`
      - `electric_vehicle_charging`
      - `electrical_parts_and_equipment`
      - `electrical_services`
      - `electronics_repair_shops`
      - `electronics_stores`
      - `elementary_secondary_schools`
      - `emergency_services_gcas_visa_use_only`
      - `employment_temp_agencies`
      - `equipment_rental`
      - `exterminating_services`
      - `family_clothing_stores`
      - `fast_food_restaurants`
      - `financial_institutions`
      - `fines_government_administrative_entities`
      - `fireplace_fireplace_screens_and_accessories_stores`
      - `floor_covering_stores`
      - `florists`
      - `florists_supplies_nursery_stock_and_flowers`
      - `freezer_and_locker_meat_provisioners`
      - `fuel_dealers_non_automotive`
      - `funeral_services_crematories`
      - `furniture_home_furnishings_and_equipment_stores_except_appliances`
      - `furniture_repair_refinishing`
      - `furriers_and_fur_shops`
      - `general_services`
      - `gift_card_novelty_and_souvenir_shops`
      - `glass_paint_and_wallpaper_stores`
      - `glassware_crystal_stores`
      - `golf_courses_public`
      - `government_licensed_horse_dog_racing_us_region_only`
      - `government_licensed_online_casions_online_gambling_us_region_only`
      - `government_owned_lotteries_non_us_region`
      - `government_owned_lotteries_us_region_only`
      - `government_services`
      - `grocery_stores_supermarkets`
      - `hardware_equipment_and_supplies`
      - `hardware_stores`
      - `health_and_beauty_spas`
      - `hearing_aids_sales_and_supplies`
      - `heating_plumbing_a_c`
      - `hobby_toy_and_game_shops`
      - `home_supply_warehouse_stores`
      - `hospitals`
      - `hotels_motels_and_resorts`
      - `household_appliance_stores`
      - `industrial_supplies`
      - `information_retrieval_services`
      - `insurance_default`
      - `insurance_underwriting_premiums`
      - `intra_company_purchases`
      - `jewelry_stores_watches_clocks_and_silverware_stores`
      - `landscaping_services`
      - `laundries`
      - `laundry_cleaning_services`
      - `legal_services_attorneys`
      - `luggage_and_leather_goods_stores`
      - `lumber_building_materials_stores`
      - `manual_cash_disburse`
      - `marinas_service_and_supplies`
      - `marketplaces`
      - `masonry_stonework_and_plaster`
      - `massage_parlors`
      - `medical_and_dental_labs`
      - `medical_dental_ophthalmic_and_hospital_equipment_and_supplies`
      - `medical_services`
      - `membership_organizations`
      - `mens_and_boys_clothing_and_accessories_stores`
      - `mens_womens_clothing_stores`
      - `metal_service_centers`
      - `miscellaneous`
      - `miscellaneous_apparel_and_accessory_shops`
      - `miscellaneous_auto_dealers`
      - `miscellaneous_business_services`
      - `miscellaneous_food_stores`
      - `miscellaneous_general_merchandise`
      - `miscellaneous_general_services`
      - `miscellaneous_home_furnishing_specialty_stores`
      - `miscellaneous_publishing_and_printing`
      - `miscellaneous_recreation_services`
      - `miscellaneous_repair_shops`
      - `miscellaneous_specialty_retail`
      - `mobile_home_dealers`
      - `motion_picture_theaters`
      - `motor_freight_carriers_and_trucking`
      - `motor_homes_dealers`
      - `motor_vehicle_supplies_and_new_parts`
      - `motorcycle_shops_and_dealers`
      - `motorcycle_shops_dealers`
      - `music_stores_musical_instruments_pianos_and_sheet_music`
      - `news_dealers_and_newsstands`
      - `non_fi_money_orders`
      - `non_fi_stored_value_card_purchase_load`
      - `nondurable_goods`
      - `nurseries_lawn_and_garden_supply_stores`
      - `nursing_personal_care`
      - `office_and_commercial_furniture`
      - `opticians_eyeglasses`
      - `optometrists_ophthalmologist`
      - `orthopedic_goods_prosthetic_devices`
      - `osteopaths`
      - `package_stores_beer_wine_and_liquor`
      - `paints_varnishes_and_supplies`
      - `parking_lots_garages`
      - `passenger_railways`
      - `pawn_shops`
      - `pet_shops_pet_food_and_supplies`
      - `petroleum_and_petroleum_products`
      - `photo_developing`
      - `photographic_photocopy_microfilm_equipment_and_supplies`
      - `photographic_studios`
      - `picture_video_production`
      - `piece_goods_notions_and_other_dry_goods`
      - `plumbing_heating_equipment_and_supplies`
      - `political_organizations`
      - `postal_services_government_only`
      - `precious_stones_and_metals_watches_and_jewelry`
      - `professional_services`
      - `public_warehousing_and_storage`
      - `quick_copy_repro_and_blueprint`
      - `railroads`
      - `real_estate_agents_and_managers_rentals`
      - `record_stores`
      - `recreational_vehicle_rentals`
      - `religious_goods_stores`
      - `religious_organizations`
      - `roofing_siding_sheet_metal`
      - `secretarial_support_services`
      - `security_brokers_dealers`
      - `service_stations`
      - `sewing_needlework_fabric_and_piece_goods_stores`
      - `shoe_repair_hat_cleaning`
      - `shoe_stores`
      - `small_appliance_repair`
      - `snowmobile_dealers`
      - `special_trade_services`
      - `specialty_cleaning`
      - `sporting_goods_stores`
      - `sporting_recreation_camps`
      - `sports_and_riding_apparel_stores`
      - `sports_clubs_fields`
      - `stamp_and_coin_stores`
      - `stationary_office_supplies_printing_and_writing_paper`
      - `stationery_stores_office_and_school_supply_stores`
      - `swimming_pools_sales`
      - `t_ui_travel_germany`
      - `tailors_alterations`
      - `tax_payments_government_agencies`
      - `tax_preparation_services`
      - `taxicabs_limousines`
      - `telecommunication_equipment_and_telephone_sales`
      - `telecommunication_services`
      - `telegraph_services`
      - `tent_and_awning_shops`
      - `testing_laboratories`
      - `theatrical_ticket_agencies`
      - `timeshares`
      - `tire_retreading_and_repair`
      - `tolls_bridge_fees`
      - `tourist_attractions_and_exhibits`
      - `towing_services`
      - `trailer_parks_campgrounds`
      - `transportation_services`
      - `travel_agencies_tour_operators`
      - `truck_stop_iteration`
      - `truck_utility_trailer_rentals`
      - `typesetting_plate_making_and_related_services`
      - `typewriter_stores`
      - `u_s_federal_government_agencies_or_departments`
      - `uniforms_commercial_clothing`
      - `used_merchandise_and_secondhand_stores`
      - `utilities`
      - `variety_stores`
      - `veterinary_services`
      - `video_amusement_game_supplies`
      - `video_game_arcades`
      - `video_tape_rental_stores`
      - `vocational_trade_schools`
      - `watch_jewelry_repair`
      - `welding_repair`
      - `wholesale_clubs`
      - `wig_and_toupee_stores`
      - `wires_money_orders`
      - `womens_accessory_and_specialty_shops`
      - `womens_ready_to_wear_stores`
      - `wrecking_and_salvage_yards`

    - `cardholder.spending_controls.allowed_merchant_countries` (array of strings, nullable)
      Array of strings containing representing countries from which authorizations will be allowed. Authorizations from merchants in all other countries will be declined. Country codes should be ISO 3166 alpha-2 country codes (e.g. `US`). Cannot be set with `blocked_merchant_countries`. Provide an empty value to unset this control.

    - `cardholder.spending_controls.blocked_categories` (array of enums, nullable)
      Array of strings containing [categories](https://docs.stripe.com/docs/api.md#issuing_authorization_object-merchant_data-category) of authorizations to decline. All other categories will be allowed. Cannot be set with `allowed_categories`.
Possible enum values:
      - `ac_refrigeration_repair`
      - `accounting_bookkeeping_services`
      - `advertising_services`
      - `agricultural_cooperative`
      - `airlines_air_carriers`
      - `airports_flying_fields`
      - `ambulance_services`
      - `amusement_parks_carnivals`
      - `antique_reproductions`
      - `antique_shops`
      - `aquariums`
      - `architectural_surveying_services`
      - `art_dealers_and_galleries`
      - `artists_supply_and_craft_shops`
      - `auto_and_home_supply_stores`
      - `auto_body_repair_shops`
      - `auto_paint_shops`
      - `auto_service_shops`
      - `automated_cash_disburse`
      - `automated_fuel_dispensers`
      - `automobile_associations`
      - `automotive_parts_and_accessories_stores`
      - `automotive_tire_stores`
      - `bail_and_bond_payments`
      - `bakeries`
      - `bands_orchestras`
      - `barber_and_beauty_shops`
      - `betting_casino_gambling`
      - `bicycle_shops`
      - `billiard_pool_establishments`
      - `boat_dealers`
      - `boat_rentals_and_leases`
      - `book_stores`
      - `books_periodicals_and_newspapers`
      - `bowling_alleys`
      - `bus_lines`
      - `business_secretarial_schools`
      - `buying_shopping_services`
      - `cable_satellite_and_other_pay_television_and_radio`
      - `camera_and_photographic_supply_stores`
      - `candy_nut_and_confectionery_stores`
      - `car_and_truck_dealers_new_used`
      - `car_and_truck_dealers_used_only`
      - `car_rental_agencies`
      - `car_washes`
      - `carpentry_services`
      - `carpet_upholstery_cleaning`
      - `caterers`
      - `charitable_and_social_service_organizations_fundraising`
      - `chemicals_and_allied_products`
      - `child_care_services`
      - `childrens_and_infants_wear_stores`
      - `chiropodists_podiatrists`
      - `chiropractors`
      - `cigar_stores_and_stands`
      - `civic_social_fraternal_associations`
      - `cleaning_and_maintenance`
      - `clothing_rental`
      - `colleges_universities`
      - `commercial_equipment`
      - `commercial_footwear`
      - `commercial_photography_art_and_graphics`
      - `commuter_transport_and_ferries`
      - `computer_network_services`
      - `computer_programming`
      - `computer_repair`
      - `computer_software_stores`
      - `computers_peripherals_and_software`
      - `concrete_work_services`
      - `construction_materials`
      - `consulting_public_relations`
      - `correspondence_schools`
      - `cosmetic_stores`
      - `counseling_services`
      - `country_clubs`
      - `courier_services`
      - `court_costs`
      - `credit_reporting_agencies`
      - `cruise_lines`
      - `dairy_products_stores`
      - `dance_hall_studios_schools`
      - `dating_escort_services`
      - `dentists_orthodontists`
      - `department_stores`
      - `detective_agencies`
      - `digital_goods_applications`
      - `digital_goods_games`
      - `digital_goods_large_volume`
      - `digital_goods_media`
      - `direct_marketing_catalog_merchant`
      - `direct_marketing_combination_catalog_and_retail_merchant`
      - `direct_marketing_inbound_telemarketing`
      - `direct_marketing_insurance_services`
      - `direct_marketing_other`
      - `direct_marketing_outbound_telemarketing`
      - `direct_marketing_subscription`
      - `direct_marketing_travel`
      - `discount_stores`
      - `doctors`
      - `door_to_door_sales`
      - `drapery_window_covering_and_upholstery_stores`
      - `drinking_places`
      - `drug_stores_and_pharmacies`
      - `drugs_drug_proprietaries_and_druggist_sundries`
      - `dry_cleaners`
      - `durable_goods`
      - `duty_free_stores`
      - `eating_places_restaurants`
      - `educational_services`
      - `electric_razor_stores`
      - `electric_vehicle_charging`
      - `electrical_parts_and_equipment`
      - `electrical_services`
      - `electronics_repair_shops`
      - `electronics_stores`
      - `elementary_secondary_schools`
      - `emergency_services_gcas_visa_use_only`
      - `employment_temp_agencies`
      - `equipment_rental`
      - `exterminating_services`
      - `family_clothing_stores`
      - `fast_food_restaurants`
      - `financial_institutions`
      - `fines_government_administrative_entities`
      - `fireplace_fireplace_screens_and_accessories_stores`
      - `floor_covering_stores`
      - `florists`
      - `florists_supplies_nursery_stock_and_flowers`
      - `freezer_and_locker_meat_provisioners`
      - `fuel_dealers_non_automotive`
      - `funeral_services_crematories`
      - `furniture_home_furnishings_and_equipment_stores_except_appliances`
      - `furniture_repair_refinishing`
      - `furriers_and_fur_shops`
      - `general_services`
      - `gift_card_novelty_and_souvenir_shops`
      - `glass_paint_and_wallpaper_stores`
      - `glassware_crystal_stores`
      - `golf_courses_public`
      - `government_licensed_horse_dog_racing_us_region_only`
      - `government_licensed_online_casions_online_gambling_us_region_only`
      - `government_owned_lotteries_non_us_region`
      - `government_owned_lotteries_us_region_only`
      - `government_services`
      - `grocery_stores_supermarkets`
      - `hardware_equipment_and_supplies`
      - `hardware_stores`
      - `health_and_beauty_spas`
      - `hearing_aids_sales_and_supplies`
      - `heating_plumbing_a_c`
      - `hobby_toy_and_game_shops`
      - `home_supply_warehouse_stores`
      - `hospitals`
      - `hotels_motels_and_resorts`
      - `household_appliance_stores`
      - `industrial_supplies`
      - `information_retrieval_services`
      - `insurance_default`
      - `insurance_underwriting_premiums`
      - `intra_company_purchases`
      - `jewelry_stores_watches_clocks_and_silverware_stores`
      - `landscaping_services`
      - `laundries`
      - `laundry_cleaning_services`
      - `legal_services_attorneys`
      - `luggage_and_leather_goods_stores`
      - `lumber_building_materials_stores`
      - `manual_cash_disburse`
      - `marinas_service_and_supplies`
      - `marketplaces`
      - `masonry_stonework_and_plaster`
      - `massage_parlors`
      - `medical_and_dental_labs`
      - `medical_dental_ophthalmic_and_hospital_equipment_and_supplies`
      - `medical_services`
      - `membership_organizations`
      - `mens_and_boys_clothing_and_accessories_stores`
      - `mens_womens_clothing_stores`
      - `metal_service_centers`
      - `miscellaneous`
      - `miscellaneous_apparel_and_accessory_shops`
      - `miscellaneous_auto_dealers`
      - `miscellaneous_business_services`
      - `miscellaneous_food_stores`
      - `miscellaneous_general_merchandise`
      - `miscellaneous_general_services`
      - `miscellaneous_home_furnishing_specialty_stores`
      - `miscellaneous_publishing_and_printing`
      - `miscellaneous_recreation_services`
      - `miscellaneous_repair_shops`
      - `miscellaneous_specialty_retail`
      - `mobile_home_dealers`
      - `motion_picture_theaters`
      - `motor_freight_carriers_and_trucking`
      - `motor_homes_dealers`
      - `motor_vehicle_supplies_and_new_parts`
      - `motorcycle_shops_and_dealers`
      - `motorcycle_shops_dealers`
      - `music_stores_musical_instruments_pianos_and_sheet_music`
      - `news_dealers_and_newsstands`
      - `non_fi_money_orders`
      - `non_fi_stored_value_card_purchase_load`
      - `nondurable_goods`
      - `nurseries_lawn_and_garden_supply_stores`
      - `nursing_personal_care`
      - `office_and_commercial_furniture`
      - `opticians_eyeglasses`
      - `optometrists_ophthalmologist`
      - `orthopedic_goods_prosthetic_devices`
      - `osteopaths`
      - `package_stores_beer_wine_and_liquor`
      - `paints_varnishes_and_supplies`
      - `parking_lots_garages`
      - `passenger_railways`
      - `pawn_shops`
      - `pet_shops_pet_food_and_supplies`
      - `petroleum_and_petroleum_products`
      - `photo_developing`
      - `photographic_photocopy_microfilm_equipment_and_supplies`
      - `photographic_studios`
      - `picture_video_production`
      - `piece_goods_notions_and_other_dry_goods`
      - `plumbing_heating_equipment_and_supplies`
      - `political_organizations`
      - `postal_services_government_only`
      - `precious_stones_and_metals_watches_and_jewelry`
      - `professional_services`
      - `public_warehousing_and_storage`
      - `quick_copy_repro_and_blueprint`
      - `railroads`
      - `real_estate_agents_and_managers_rentals`
      - `record_stores`
      - `recreational_vehicle_rentals`
      - `religious_goods_stores`
      - `religious_organizations`
      - `roofing_siding_sheet_metal`
      - `secretarial_support_services`
      - `security_brokers_dealers`
      - `service_stations`
      - `sewing_needlework_fabric_and_piece_goods_stores`
      - `shoe_repair_hat_cleaning`
      - `shoe_stores`
      - `small_appliance_repair`
      - `snowmobile_dealers`
      - `special_trade_services`
      - `specialty_cleaning`
      - `sporting_goods_stores`
      - `sporting_recreation_camps`
      - `sports_and_riding_apparel_stores`
      - `sports_clubs_fields`
      - `stamp_and_coin_stores`
      - `stationary_office_supplies_printing_and_writing_paper`
      - `stationery_stores_office_and_school_supply_stores`
      - `swimming_pools_sales`
      - `t_ui_travel_germany`
      - `tailors_alterations`
      - `tax_payments_government_agencies`
      - `tax_preparation_services`
      - `taxicabs_limousines`
      - `telecommunication_equipment_and_telephone_sales`
      - `telecommunication_services`
      - `telegraph_services`
      - `tent_and_awning_shops`
      - `testing_laboratories`
      - `theatrical_ticket_agencies`
      - `timeshares`
      - `tire_retreading_and_repair`
      - `tolls_bridge_fees`
      - `tourist_attractions_and_exhibits`
      - `towing_services`
      - `trailer_parks_campgrounds`
      - `transportation_services`
      - `travel_agencies_tour_operators`
      - `truck_stop_iteration`
      - `truck_utility_trailer_rentals`
      - `typesetting_plate_making_and_related_services`
      - `typewriter_stores`
      - `u_s_federal_government_agencies_or_departments`
      - `uniforms_commercial_clothing`
      - `used_merchandise_and_secondhand_stores`
      - `utilities`
      - `variety_stores`
      - `veterinary_services`
      - `video_amusement_game_supplies`
      - `video_game_arcades`
      - `video_tape_rental_stores`
      - `vocational_trade_schools`
      - `watch_jewelry_repair`
      - `welding_repair`
      - `wholesale_clubs`
      - `wig_and_toupee_stores`
      - `wires_money_orders`
      - `womens_accessory_and_specialty_shops`
      - `womens_ready_to_wear_stores`
      - `wrecking_and_salvage_yards`

    - `cardholder.spending_controls.blocked_merchant_countries` (array of strings, nullable)
      Array of strings containing representing countries from which authorizations will be declined. Country codes should be ISO 3166 alpha-2 country codes (e.g. `US`). Cannot be set with `allowed_merchant_countries`. Provide an empty value to unset this control.

    - `cardholder.spending_controls.spending_limits` (array of objects, nullable)
      Limit spending with amount-based rules that apply across this cardholder’s cards.

      - `cardholder.spending_controls.spending_limits.amount` (integer)
        Maximum amount allowed to spend per interval. This amount is in the card’s currency and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

      - `cardholder.spending_controls.spending_limits.categories` (array of enums, nullable)
        Array of strings containing [categories](https://docs.stripe.com/docs/api.md#issuing_authorization_object-merchant_data-category) this limit applies to. Omitting this field will apply the limit to all categories.
Possible enum values:
        - `ac_refrigeration_repair`
        - `accounting_bookkeeping_services`
        - `advertising_services`
        - `agricultural_cooperative`
        - `airlines_air_carriers`
        - `airports_flying_fields`
        - `ambulance_services`
        - `amusement_parks_carnivals`
        - `antique_reproductions`
        - `antique_shops`
        - `aquariums`
        - `architectural_surveying_services`
        - `art_dealers_and_galleries`
        - `artists_supply_and_craft_shops`
        - `auto_and_home_supply_stores`
        - `auto_body_repair_shops`
        - `auto_paint_shops`
        - `auto_service_shops`
        - `automated_cash_disburse`
        - `automated_fuel_dispensers`
        - `automobile_associations`
        - `automotive_parts_and_accessories_stores`
        - `automotive_tire_stores`
        - `bail_and_bond_payments`
        - `bakeries`
        - `bands_orchestras`
        - `barber_and_beauty_shops`
        - `betting_casino_gambling`
        - `bicycle_shops`
        - `billiard_pool_establishments`
        - `boat_dealers`
        - `boat_rentals_and_leases`
        - `book_stores`
        - `books_periodicals_and_newspapers`
        - `bowling_alleys`
        - `bus_lines`
        - `business_secretarial_schools`
        - `buying_shopping_services`
        - `cable_satellite_and_other_pay_television_and_radio`
        - `camera_and_photographic_supply_stores`
        - `candy_nut_and_confectionery_stores`
        - `car_and_truck_dealers_new_used`
        - `car_and_truck_dealers_used_only`
        - `car_rental_agencies`
        - `car_washes`
        - `carpentry_services`
        - `carpet_upholstery_cleaning`
        - `caterers`
        - `charitable_and_social_service_organizations_fundraising`
        - `chemicals_and_allied_products`
        - `child_care_services`
        - `childrens_and_infants_wear_stores`
        - `chiropodists_podiatrists`
        - `chiropractors`
        - `cigar_stores_and_stands`
        - `civic_social_fraternal_associations`
        - `cleaning_and_maintenance`
        - `clothing_rental`
        - `colleges_universities`
        - `commercial_equipment`
        - `commercial_footwear`
        - `commercial_photography_art_and_graphics`
        - `commuter_transport_and_ferries`
        - `computer_network_services`
        - `computer_programming`
        - `computer_repair`
        - `computer_software_stores`
        - `computers_peripherals_and_software`
        - `concrete_work_services`
        - `construction_materials`
        - `consulting_public_relations`
        - `correspondence_schools`
        - `cosmetic_stores`
        - `counseling_services`
        - `country_clubs`
        - `courier_services`
        - `court_costs`
        - `credit_reporting_agencies`
        - `cruise_lines`
        - `dairy_products_stores`
        - `dance_hall_studios_schools`
        - `dating_escort_services`
        - `dentists_orthodontists`
        - `department_stores`
        - `detective_agencies`
        - `digital_goods_applications`
        - `digital_goods_games`
        - `digital_goods_large_volume`
        - `digital_goods_media`
        - `direct_marketing_catalog_merchant`
        - `direct_marketing_combination_catalog_and_retail_merchant`
        - `direct_marketing_inbound_telemarketing`
        - `direct_marketing_insurance_services`
        - `direct_marketing_other`
        - `direct_marketing_outbound_telemarketing`
        - `direct_marketing_subscription`
        - `direct_marketing_travel`
        - `discount_stores`
        - `doctors`
        - `door_to_door_sales`
        - `drapery_window_covering_and_upholstery_stores`
        - `drinking_places`
        - `drug_stores_and_pharmacies`
        - `drugs_drug_proprietaries_and_druggist_sundries`
        - `dry_cleaners`
        - `durable_goods`
        - `duty_free_stores`
        - `eating_places_restaurants`
        - `educational_services`
        - `electric_razor_stores`
        - `electric_vehicle_charging`
        - `electrical_parts_and_equipment`
        - `electrical_services`
        - `electronics_repair_shops`
        - `electronics_stores`
        - `elementary_secondary_schools`
        - `emergency_services_gcas_visa_use_only`
        - `employment_temp_agencies`
        - `equipment_rental`
        - `exterminating_services`
        - `family_clothing_stores`
        - `fast_food_restaurants`
        - `financial_institutions`
        - `fines_government_administrative_entities`
        - `fireplace_fireplace_screens_and_accessories_stores`
        - `floor_covering_stores`
        - `florists`
        - `florists_supplies_nursery_stock_and_flowers`
        - `freezer_and_locker_meat_provisioners`
        - `fuel_dealers_non_automotive`
        - `funeral_services_crematories`
        - `furniture_home_furnishings_and_equipment_stores_except_appliances`
        - `furniture_repair_refinishing`
        - `furriers_and_fur_shops`
        - `general_services`
        - `gift_card_novelty_and_souvenir_shops`
        - `glass_paint_and_wallpaper_stores`
        - `glassware_crystal_stores`
        - `golf_courses_public`
        - `government_licensed_horse_dog_racing_us_region_only`
        - `government_licensed_online_casions_online_gambling_us_region_only`
        - `government_owned_lotteries_non_us_region`
        - `government_owned_lotteries_us_region_only`
        - `government_services`
        - `grocery_stores_supermarkets`
        - `hardware_equipment_and_supplies`
        - `hardware_stores`
        - `health_and_beauty_spas`
        - `hearing_aids_sales_and_supplies`
        - `heating_plumbing_a_c`
        - `hobby_toy_and_game_shops`
        - `home_supply_warehouse_stores`
        - `hospitals`
        - `hotels_motels_and_resorts`
        - `household_appliance_stores`
        - `industrial_supplies`
        - `information_retrieval_services`
        - `insurance_default`
        - `insurance_underwriting_premiums`
        - `intra_company_purchases`
        - `jewelry_stores_watches_clocks_and_silverware_stores`
        - `landscaping_services`
        - `laundries`
        - `laundry_cleaning_services`
        - `legal_services_attorneys`
        - `luggage_and_leather_goods_stores`
        - `lumber_building_materials_stores`
        - `manual_cash_disburse`
        - `marinas_service_and_supplies`
        - `marketplaces`
        - `masonry_stonework_and_plaster`
        - `massage_parlors`
        - `medical_and_dental_labs`
        - `medical_dental_ophthalmic_and_hospital_equipment_and_supplies`
        - `medical_services`
        - `membership_organizations`
        - `mens_and_boys_clothing_and_accessories_stores`
        - `mens_womens_clothing_stores`
        - `metal_service_centers`
        - `miscellaneous`
        - `miscellaneous_apparel_and_accessory_shops`
        - `miscellaneous_auto_dealers`
        - `miscellaneous_business_services`
        - `miscellaneous_food_stores`
        - `miscellaneous_general_merchandise`
        - `miscellaneous_general_services`
        - `miscellaneous_home_furnishing_specialty_stores`
        - `miscellaneous_publishing_and_printing`
        - `miscellaneous_recreation_services`
        - `miscellaneous_repair_shops`
        - `miscellaneous_specialty_retail`
        - `mobile_home_dealers`
        - `motion_picture_theaters`
        - `motor_freight_carriers_and_trucking`
        - `motor_homes_dealers`
        - `motor_vehicle_supplies_and_new_parts`
        - `motorcycle_shops_and_dealers`
        - `motorcycle_shops_dealers`
        - `music_stores_musical_instruments_pianos_and_sheet_music`
        - `news_dealers_and_newsstands`
        - `non_fi_money_orders`
        - `non_fi_stored_value_card_purchase_load`
        - `nondurable_goods`
        - `nurseries_lawn_and_garden_supply_stores`
        - `nursing_personal_care`
        - `office_and_commercial_furniture`
        - `opticians_eyeglasses`
        - `optometrists_ophthalmologist`
        - `orthopedic_goods_prosthetic_devices`
        - `osteopaths`
        - `package_stores_beer_wine_and_liquor`
        - `paints_varnishes_and_supplies`
        - `parking_lots_garages`
        - `passenger_railways`
        - `pawn_shops`
        - `pet_shops_pet_food_and_supplies`
        - `petroleum_and_petroleum_products`
        - `photo_developing`
        - `photographic_photocopy_microfilm_equipment_and_supplies`
        - `photographic_studios`
        - `picture_video_production`
        - `piece_goods_notions_and_other_dry_goods`
        - `plumbing_heating_equipment_and_supplies`
        - `political_organizations`
        - `postal_services_government_only`
        - `precious_stones_and_metals_watches_and_jewelry`
        - `professional_services`
        - `public_warehousing_and_storage`
        - `quick_copy_repro_and_blueprint`
        - `railroads`
        - `real_estate_agents_and_managers_rentals`
        - `record_stores`
        - `recreational_vehicle_rentals`
        - `religious_goods_stores`
        - `religious_organizations`
        - `roofing_siding_sheet_metal`
        - `secretarial_support_services`
        - `security_brokers_dealers`
        - `service_stations`
        - `sewing_needlework_fabric_and_piece_goods_stores`
        - `shoe_repair_hat_cleaning`
        - `shoe_stores`
        - `small_appliance_repair`
        - `snowmobile_dealers`
        - `special_trade_services`
        - `specialty_cleaning`
        - `sporting_goods_stores`
        - `sporting_recreation_camps`
        - `sports_and_riding_apparel_stores`
        - `sports_clubs_fields`
        - `stamp_and_coin_stores`
        - `stationary_office_supplies_printing_and_writing_paper`
        - `stationery_stores_office_and_school_supply_stores`
        - `swimming_pools_sales`
        - `t_ui_travel_germany`
        - `tailors_alterations`
        - `tax_payments_government_agencies`
        - `tax_preparation_services`
        - `taxicabs_limousines`
        - `telecommunication_equipment_and_telephone_sales`
        - `telecommunication_services`
        - `telegraph_services`
        - `tent_and_awning_shops`
        - `testing_laboratories`
        - `theatrical_ticket_agencies`
        - `timeshares`
        - `tire_retreading_and_repair`
        - `tolls_bridge_fees`
        - `tourist_attractions_and_exhibits`
        - `towing_services`
        - `trailer_parks_campgrounds`
        - `transportation_services`
        - `travel_agencies_tour_operators`
        - `truck_stop_iteration`
        - `truck_utility_trailer_rentals`
        - `typesetting_plate_making_and_related_services`
        - `typewriter_stores`
        - `u_s_federal_government_agencies_or_departments`
        - `uniforms_commercial_clothing`
        - `used_merchandise_and_secondhand_stores`
        - `utilities`
        - `variety_stores`
        - `veterinary_services`
        - `video_amusement_game_supplies`
        - `video_game_arcades`
        - `video_tape_rental_stores`
        - `vocational_trade_schools`
        - `watch_jewelry_repair`
        - `welding_repair`
        - `wholesale_clubs`
        - `wig_and_toupee_stores`
        - `wires_money_orders`
        - `womens_accessory_and_specialty_shops`
        - `womens_ready_to_wear_stores`
        - `wrecking_and_salvage_yards`

      - `cardholder.spending_controls.spending_limits.interval` (enum)
        Interval (or event) to which the amount applies.
Possible enum values:
        - `all_time`
          Limit applies to all transactions.

        - `daily`
          Limit applies to a day, starting at midnight UTC.

        - `monthly`
          Limit applies to a month, starting on the 1st at midnight UTC.

        - `per_authorization`
          Limit applies to each authorization.

        - `weekly`
          Limit applies to a week, starting on Sunday at midnight UTC.

        - `yearly`
          Limit applies to a year, starting on January 1st at midnight UTC.

    - `cardholder.spending_controls.spending_limits_currency` (enum, nullable)
      Currency of the amounts within `spending_limits`.

  - `cardholder.status` (enum)
    Specifies whether to permit authorizations on this cardholder’s cards.
Possible enum values:
    - `active`
      A platform has enabled the cardholder to approve authorizations made with their attached cards. However, if Stripe hasn’t yet verified the cardholder’s identity information, authorizations might still be blocked.

    - `blocked`
      Cards attached to this cardholder will decline all authorizations with the `cardholder_blocked` reason. This status is non-reversible.

    - `inactive`
      Cards attached to this cardholder will decline all authorizations with the `cardholder_inactive` reason.

  - `cardholder.type` (enum)
    One of `individual` or `company`. See [Choose a cardholder type](https://docs.stripe.com/docs/issuing/other/choose-cardholder.md) for more details.
Possible enum values:
    - `company`
      The cardholder is a company or business entity, and additional information includes their tax ID. This option may not be available if your [use case](https://docs.stripe.com/docs/issuing/other/choose-cardholder.md#find-your-use-case) only supports individual cardholders.

    - `individual`
      The cardholder is a person, and additional information includes first and last name, date of birth, etc. If you’re issuing Celtic Spend Cards, then Individual cardholders must accept Authorized User Terms prior to activating their card.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Supported currencies are `usd` in the US, `eur` in the EU, and `gbp` in the UK.

- `cvc` (string, nullable)
  The card’s CVC. For security reasons, this is only available for virtual cards, and will be omitted unless you explicitly request it with [the `expand` parameter](https://docs.stripe.com/docs/api/expanding_objects.md). Additionally, it’s only available via the [“Retrieve a card” endpoint](https://docs.stripe.com/docs/api/issuing/cards/retrieve.md), not via “List all cards” or any other endpoint.

- `exp_month` (integer)
  The expiration month of the card.

- `exp_year` (integer)
  The expiration year of the card.

- `last4` (string)
  The last 4 digits of the card number.

- `latest_fraud_warning` (object, nullable)
  Stripe’s assessment of whether this card’s details have been compromised. If this property isn’t null, cancel and reissue the card to prevent fraudulent activity risk.

  - `latest_fraud_warning.started_at` (timestamp, nullable)
    Timestamp of the most recent fraud warning.

  - `latest_fraud_warning.type` (enum, nullable)
    The type of fraud warning that most recently took place on this card. This field updates with every new fraud warning, so the value changes over time. If populated, cancel and reissue the card.
Possible enum values:
    - `card_testing_exposure`
      The card’s credentials were used successfully in a card testing attempt. Requires [Advanced Fraud Tools](https://docs.stripe.com/docs/issuing/controls/advanced-fraud-tools.md).

    - `fraud_dispute_filed`
      The cardholder filed a fraud dispute for a transaction

    - `third_party_reported`
      The card was reported compromised by a third party

    - `user_indicated_fraud`
      The cardholder indicated that a fraudulent transaction occurred. Requires [Advanced Fraud Tools](https://docs.stripe.com/docs/issuing/controls/advanced-fraud-tools.md).

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `number` (string, nullable)
  The full unredacted card number. For security reasons, this is only available for virtual cards, and will be omitted unless you explicitly request it with [the `expand` parameter](https://docs.stripe.com/docs/api/expanding_objects.md). Additionally, it’s only available via the [“Retrieve a card” endpoint](https://docs.stripe.com/docs/api/issuing/cards/retrieve.md), not via “List all cards” or any other endpoint.

- `personalization_design` (string, nullable)
  The personalization design object belonging to this card.

- `replaced_by` (string, nullable)
  The latest card that replaces this card, if any.

- `replacement_for` (string, nullable)
  The card this card replaces, if any.

- `replacement_reason` (enum, nullable)
  The reason why the previous card needed to be replaced.
Possible enum values:
  - `damaged`
    The physical card has been damaged and cannot be used at terminals. This reason is only valid for cards of type `physical`.

  - `expired`
    The expiration date has passed or is imminent.

  - `lost`
    The card was lost. This status is only valid if the card it replaces is marked as lost.

  - `stolen`
    The card was stolen. This status is only valid if the card it replaces is marked as stolen.

- `second_line` (string, nullable)
  Text separate from cardholder name, printed on the card.

- `shipping` (object, nullable)
  Where and how the card will be shipped.

  - `shipping.address` (object)
    Shipping address.

    - `shipping.address.city` (string, nullable)
      City, district, suburb, town, or village.

    - `shipping.address.country` (string, nullable)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `shipping.address.line1` (string, nullable)
      Address line 1, such as the street, PO Box, or company name.

    - `shipping.address.line2` (string, nullable)
      Address line 2, such as the apartment, suite, unit, or building.

    - `shipping.address.postal_code` (string, nullable)
      ZIP or postal code.

    - `shipping.address.state` (string, nullable)
      State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

  - `shipping.address_validation` (object, nullable)
    Address validation details for the shipment.

    - `shipping.address_validation.mode` (enum)
      The address validation capabilities to use.
Possible enum values:
      - `disabled`
        The card will be shipped without validating or normalizing the shipping address.

      - `normalization_only`
        The card will be shipped with the normalized address without validation. Undeliverable addresses won’t be blocked.

      - `validation_and_normalization`
        The card will be shipped with the normalized, validated address. Undeliverable addresses will be blocked.

    - `shipping.address_validation.normalized_address` (object, nullable)
      The normalized shipping address.

      - `shipping.address_validation.normalized_address.city` (string, nullable)
        City, district, suburb, town, or village.

      - `shipping.address_validation.normalized_address.country` (string, nullable)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `shipping.address_validation.normalized_address.line1` (string, nullable)
        Address line 1, such as the street, PO Box, or company name.

      - `shipping.address_validation.normalized_address.line2` (string, nullable)
        Address line 2, such as the apartment, suite, unit, or building.

      - `shipping.address_validation.normalized_address.postal_code` (string, nullable)
        ZIP or postal code.

      - `shipping.address_validation.normalized_address.state` (string, nullable)
        State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

    - `shipping.address_validation.result` (enum, nullable)
      The validation result for the shipping address.
Possible enum values:
      - `indeterminate`
        The deliverability of the card’s shipping address could not be determined.

      - `likely_deliverable`
        The card’s shipping address is likely deliverable.

      - `likely_undeliverable`
        The card’s shipping address is likely undeliverable as submitted.

  - `shipping.carrier` (enum, nullable)
    The delivery company that shipped a card.
Possible enum values:
    - `dhl`
      DHL

    - `fedex`
      FedEx

    - `royal_mail`
      Royal Mail

    - `usps`
      USPS

  - `shipping.customs` (object, nullable)
    Additional information that may be required for clearing customs.

    - `shipping.customs.eori_number` (string, nullable)
      A registration number used for customs in Europe. See [https://www.gov.uk/eori](https://www.gov.uk/eori) for the UK and [https://ec.europa.eu/taxation_customs/business/customs-procedures-import-and-export/customs-procedures/economic-operators-registration-and-identification-number-eori_en](https://ec.europa.eu/taxation_customs/business/customs-procedures-import-and-export/customs-procedures/economic-operators-registration-and-identification-number-eori_en) for the EU.

  - `shipping.eta` (timestamp, nullable)
    A unix timestamp representing a best estimate of when the card will be delivered.

  - `shipping.name` (string)
    Recipient name.

  - `shipping.phone_number` (string, nullable)
    The phone number of the receiver of the shipment. Our courier partners will use this number to contact you in the event of card delivery issues. For individual shipments to the EU/UK, if this field is empty, we will provide them with the phone number provided when the cardholder was initially created.

  - `shipping.require_signature` (boolean, nullable)
    Whether a signature is required for card delivery. This feature is only supported for US users. Standard shipping service does not support signature on delivery. The default value for standard shipping service is false and for express and priority services is true.

  - `shipping.service` (enum)
    Shipment service, such as `standard` or `express`.
Possible enum values:
    - `express`
      Cards arrive in 4 business days.

    - `priority`
      Cards arrive in 2-3 business days.

    - `standard`
      Cards arrive in 5-8 business days.

  - `shipping.status` (enum, nullable)
    The delivery status of the card.
Possible enum values:
    - `canceled`
      The card was canceled before being shipped.

    - `delivered`
      The card has been delivered to its destination.

    - `failure`
      The card failed to be delivered but was not returned.

    - `pending`
      The card is being prepared and has not yet shipped.

    - `returned`
      The card failed to be delivered and was returned to the sender.

    - `shipped`
      The card has been shipped. If the card’s [shipping carrier](https://docs.stripe.com/docs/issuing/cards/physical.md#shipping-your-cards) does not support tracking, this will be the card’s final status.

    - `submitted`
      The card has been submitted to the printer for shipment.

  - `shipping.tracking_number` (string, nullable)
    A tracking number for a card shipment.

  - `shipping.tracking_url` (string, nullable)
    A link to the shipping carrier’s site where you can view detailed information about a card shipment.

  - `shipping.type` (enum)
    Packaging options.
Possible enum values:
    - `bulk`
      Cards are grouped and mailed together.

    - `individual`
      Cards are sent individually in an envelope.

- `spending_controls` (object)
  Rules that control spending for this card. Refer to our [documentation](https://docs.stripe.com/docs/issuing/controls/spending-controls.md) for more details.

  - `spending_controls.allowed_categories` (array of enums, nullable)
    Array of strings containing [categories](https://docs.stripe.com/docs/api.md#issuing_authorization_object-merchant_data-category) of authorizations to allow. All other categories will be blocked. Cannot be set with `blocked_categories`.
Possible enum values:
    - `ac_refrigeration_repair`
    - `accounting_bookkeeping_services`
    - `advertising_services`
    - `agricultural_cooperative`
    - `airlines_air_carriers`
    - `airports_flying_fields`
    - `ambulance_services`
    - `amusement_parks_carnivals`
    - `antique_reproductions`
    - `antique_shops`
    - `aquariums`
    - `architectural_surveying_services`
    - `art_dealers_and_galleries`
    - `artists_supply_and_craft_shops`
    - `auto_and_home_supply_stores`
    - `auto_body_repair_shops`
    - `auto_paint_shops`
    - `auto_service_shops`
    - `automated_cash_disburse`
    - `automated_fuel_dispensers`
    - `automobile_associations`
    - `automotive_parts_and_accessories_stores`
    - `automotive_tire_stores`
    - `bail_and_bond_payments`
    - `bakeries`
    - `bands_orchestras`
    - `barber_and_beauty_shops`
    - `betting_casino_gambling`
    - `bicycle_shops`
    - `billiard_pool_establishments`
    - `boat_dealers`
    - `boat_rentals_and_leases`
    - `book_stores`
    - `books_periodicals_and_newspapers`
    - `bowling_alleys`
    - `bus_lines`
    - `business_secretarial_schools`
    - `buying_shopping_services`
    - `cable_satellite_and_other_pay_television_and_radio`
    - `camera_and_photographic_supply_stores`
    - `candy_nut_and_confectionery_stores`
    - `car_and_truck_dealers_new_used`
    - `car_and_truck_dealers_used_only`
    - `car_rental_agencies`
    - `car_washes`
    - `carpentry_services`
    - `carpet_upholstery_cleaning`
    - `caterers`
    - `charitable_and_social_service_organizations_fundraising`
    - `chemicals_and_allied_products`
    - `child_care_services`
    - `childrens_and_infants_wear_stores`
    - `chiropodists_podiatrists`
    - `chiropractors`
    - `cigar_stores_and_stands`
    - `civic_social_fraternal_associations`
    - `cleaning_and_maintenance`
    - `clothing_rental`
    - `colleges_universities`
    - `commercial_equipment`
    - `commercial_footwear`
    - `commercial_photography_art_and_graphics`
    - `commuter_transport_and_ferries`
    - `computer_network_services`
    - `computer_programming`
    - `computer_repair`
    - `computer_software_stores`
    - `computers_peripherals_and_software`
    - `concrete_work_services`
    - `construction_materials`
    - `consulting_public_relations`
    - `correspondence_schools`
    - `cosmetic_stores`
    - `counseling_services`
    - `country_clubs`
    - `courier_services`
    - `court_costs`
    - `credit_reporting_agencies`
    - `cruise_lines`
    - `dairy_products_stores`
    - `dance_hall_studios_schools`
    - `dating_escort_services`
    - `dentists_orthodontists`
    - `department_stores`
    - `detective_agencies`
    - `digital_goods_applications`
    - `digital_goods_games`
    - `digital_goods_large_volume`
    - `digital_goods_media`
    - `direct_marketing_catalog_merchant`
    - `direct_marketing_combination_catalog_and_retail_merchant`
    - `direct_marketing_inbound_telemarketing`
    - `direct_marketing_insurance_services`
    - `direct_marketing_other`
    - `direct_marketing_outbound_telemarketing`
    - `direct_marketing_subscription`
    - `direct_marketing_travel`
    - `discount_stores`
    - `doctors`
    - `door_to_door_sales`
    - `drapery_window_covering_and_upholstery_stores`
    - `drinking_places`
    - `drug_stores_and_pharmacies`
    - `drugs_drug_proprietaries_and_druggist_sundries`
    - `dry_cleaners`
    - `durable_goods`
    - `duty_free_stores`
    - `eating_places_restaurants`
    - `educational_services`
    - `electric_razor_stores`
    - `electric_vehicle_charging`
    - `electrical_parts_and_equipment`
    - `electrical_services`
    - `electronics_repair_shops`
    - `electronics_stores`
    - `elementary_secondary_schools`
    - `emergency_services_gcas_visa_use_only`
    - `employment_temp_agencies`
    - `equipment_rental`
    - `exterminating_services`
    - `family_clothing_stores`
    - `fast_food_restaurants`
    - `financial_institutions`
    - `fines_government_administrative_entities`
    - `fireplace_fireplace_screens_and_accessories_stores`
    - `floor_covering_stores`
    - `florists`
    - `florists_supplies_nursery_stock_and_flowers`
    - `freezer_and_locker_meat_provisioners`
    - `fuel_dealers_non_automotive`
    - `funeral_services_crematories`
    - `furniture_home_furnishings_and_equipment_stores_except_appliances`
    - `furniture_repair_refinishing`
    - `furriers_and_fur_shops`
    - `general_services`
    - `gift_card_novelty_and_souvenir_shops`
    - `glass_paint_and_wallpaper_stores`
    - `glassware_crystal_stores`
    - `golf_courses_public`
    - `government_licensed_horse_dog_racing_us_region_only`
    - `government_licensed_online_casions_online_gambling_us_region_only`
    - `government_owned_lotteries_non_us_region`
    - `government_owned_lotteries_us_region_only`
    - `government_services`
    - `grocery_stores_supermarkets`
    - `hardware_equipment_and_supplies`
    - `hardware_stores`
    - `health_and_beauty_spas`
    - `hearing_aids_sales_and_supplies`
    - `heating_plumbing_a_c`
    - `hobby_toy_and_game_shops`
    - `home_supply_warehouse_stores`
    - `hospitals`
    - `hotels_motels_and_resorts`
    - `household_appliance_stores`
    - `industrial_supplies`
    - `information_retrieval_services`
    - `insurance_default`
    - `insurance_underwriting_premiums`
    - `intra_company_purchases`
    - `jewelry_stores_watches_clocks_and_silverware_stores`
    - `landscaping_services`
    - `laundries`
    - `laundry_cleaning_services`
    - `legal_services_attorneys`
    - `luggage_and_leather_goods_stores`
    - `lumber_building_materials_stores`
    - `manual_cash_disburse`
    - `marinas_service_and_supplies`
    - `marketplaces`
    - `masonry_stonework_and_plaster`
    - `massage_parlors`
    - `medical_and_dental_labs`
    - `medical_dental_ophthalmic_and_hospital_equipment_and_supplies`
    - `medical_services`
    - `membership_organizations`
    - `mens_and_boys_clothing_and_accessories_stores`
    - `mens_womens_clothing_stores`
    - `metal_service_centers`
    - `miscellaneous`
    - `miscellaneous_apparel_and_accessory_shops`
    - `miscellaneous_auto_dealers`
    - `miscellaneous_business_services`
    - `miscellaneous_food_stores`
    - `miscellaneous_general_merchandise`
    - `miscellaneous_general_services`
    - `miscellaneous_home_furnishing_specialty_stores`
    - `miscellaneous_publishing_and_printing`
    - `miscellaneous_recreation_services`
    - `miscellaneous_repair_shops`
    - `miscellaneous_specialty_retail`
    - `mobile_home_dealers`
    - `motion_picture_theaters`
    - `motor_freight_carriers_and_trucking`
    - `motor_homes_dealers`
    - `motor_vehicle_supplies_and_new_parts`
    - `motorcycle_shops_and_dealers`
    - `motorcycle_shops_dealers`
    - `music_stores_musical_instruments_pianos_and_sheet_music`
    - `news_dealers_and_newsstands`
    - `non_fi_money_orders`
    - `non_fi_stored_value_card_purchase_load`
    - `nondurable_goods`
    - `nurseries_lawn_and_garden_supply_stores`
    - `nursing_personal_care`
    - `office_and_commercial_furniture`
    - `opticians_eyeglasses`
    - `optometrists_ophthalmologist`
    - `orthopedic_goods_prosthetic_devices`
    - `osteopaths`
    - `package_stores_beer_wine_and_liquor`
    - `paints_varnishes_and_supplies`
    - `parking_lots_garages`
    - `passenger_railways`
    - `pawn_shops`
    - `pet_shops_pet_food_and_supplies`
    - `petroleum_and_petroleum_products`
    - `photo_developing`
    - `photographic_photocopy_microfilm_equipment_and_supplies`
    - `photographic_studios`
    - `picture_video_production`
    - `piece_goods_notions_and_other_dry_goods`
    - `plumbing_heating_equipment_and_supplies`
    - `political_organizations`
    - `postal_services_government_only`
    - `precious_stones_and_metals_watches_and_jewelry`
    - `professional_services`
    - `public_warehousing_and_storage`
    - `quick_copy_repro_and_blueprint`
    - `railroads`
    - `real_estate_agents_and_managers_rentals`
    - `record_stores`
    - `recreational_vehicle_rentals`
    - `religious_goods_stores`
    - `religious_organizations`
    - `roofing_siding_sheet_metal`
    - `secretarial_support_services`
    - `security_brokers_dealers`
    - `service_stations`
    - `sewing_needlework_fabric_and_piece_goods_stores`
    - `shoe_repair_hat_cleaning`
    - `shoe_stores`
    - `small_appliance_repair`
    - `snowmobile_dealers`
    - `special_trade_services`
    - `specialty_cleaning`
    - `sporting_goods_stores`
    - `sporting_recreation_camps`
    - `sports_and_riding_apparel_stores`
    - `sports_clubs_fields`
    - `stamp_and_coin_stores`
    - `stationary_office_supplies_printing_and_writing_paper`
    - `stationery_stores_office_and_school_supply_stores`
    - `swimming_pools_sales`
    - `t_ui_travel_germany`
    - `tailors_alterations`
    - `tax_payments_government_agencies`
    - `tax_preparation_services`
    - `taxicabs_limousines`
    - `telecommunication_equipment_and_telephone_sales`
    - `telecommunication_services`
    - `telegraph_services`
    - `tent_and_awning_shops`
    - `testing_laboratories`
    - `theatrical_ticket_agencies`
    - `timeshares`
    - `tire_retreading_and_repair`
    - `tolls_bridge_fees`
    - `tourist_attractions_and_exhibits`
    - `towing_services`
    - `trailer_parks_campgrounds`
    - `transportation_services`
    - `travel_agencies_tour_operators`
    - `truck_stop_iteration`
    - `truck_utility_trailer_rentals`
    - `typesetting_plate_making_and_related_services`
    - `typewriter_stores`
    - `u_s_federal_government_agencies_or_departments`
    - `uniforms_commercial_clothing`
    - `used_merchandise_and_secondhand_stores`
    - `utilities`
    - `variety_stores`
    - `veterinary_services`
    - `video_amusement_game_supplies`
    - `video_game_arcades`
    - `video_tape_rental_stores`
    - `vocational_trade_schools`
    - `watch_jewelry_repair`
    - `welding_repair`
    - `wholesale_clubs`
    - `wig_and_toupee_stores`
    - `wires_money_orders`
    - `womens_accessory_and_specialty_shops`
    - `womens_ready_to_wear_stores`
    - `wrecking_and_salvage_yards`

  - `spending_controls.allowed_merchant_countries` (array of strings, nullable)
    Array of strings containing representing countries from which authorizations will be allowed. Authorizations from merchants in all other countries will be declined. Country codes should be ISO 3166 alpha-2 country codes (e.g. `US`). Cannot be set with `blocked_merchant_countries`. Provide an empty value to unset this control.

  - `spending_controls.blocked_categories` (array of enums, nullable)
    Array of strings containing [categories](https://docs.stripe.com/docs/api.md#issuing_authorization_object-merchant_data-category) of authorizations to decline. All other categories will be allowed. Cannot be set with `allowed_categories`.
Possible enum values:
    - `ac_refrigeration_repair`
    - `accounting_bookkeeping_services`
    - `advertising_services`
    - `agricultural_cooperative`
    - `airlines_air_carriers`
    - `airports_flying_fields`
    - `ambulance_services`
    - `amusement_parks_carnivals`
    - `antique_reproductions`
    - `antique_shops`
    - `aquariums`
    - `architectural_surveying_services`
    - `art_dealers_and_galleries`
    - `artists_supply_and_craft_shops`
    - `auto_and_home_supply_stores`
    - `auto_body_repair_shops`
    - `auto_paint_shops`
    - `auto_service_shops`
    - `automated_cash_disburse`
    - `automated_fuel_dispensers`
    - `automobile_associations`
    - `automotive_parts_and_accessories_stores`
    - `automotive_tire_stores`
    - `bail_and_bond_payments`
    - `bakeries`
    - `bands_orchestras`
    - `barber_and_beauty_shops`
    - `betting_casino_gambling`
    - `bicycle_shops`
    - `billiard_pool_establishments`
    - `boat_dealers`
    - `boat_rentals_and_leases`
    - `book_stores`
    - `books_periodicals_and_newspapers`
    - `bowling_alleys`
    - `bus_lines`
    - `business_secretarial_schools`
    - `buying_shopping_services`
    - `cable_satellite_and_other_pay_television_and_radio`
    - `camera_and_photographic_supply_stores`
    - `candy_nut_and_confectionery_stores`
    - `car_and_truck_dealers_new_used`
    - `car_and_truck_dealers_used_only`
    - `car_rental_agencies`
    - `car_washes`
    - `carpentry_services`
    - `carpet_upholstery_cleaning`
    - `caterers`
    - `charitable_and_social_service_organizations_fundraising`
    - `chemicals_and_allied_products`
    - `child_care_services`
    - `childrens_and_infants_wear_stores`
    - `chiropodists_podiatrists`
    - `chiropractors`
    - `cigar_stores_and_stands`
    - `civic_social_fraternal_associations`
    - `cleaning_and_maintenance`
    - `clothing_rental`
    - `colleges_universities`
    - `commercial_equipment`
    - `commercial_footwear`
    - `commercial_photography_art_and_graphics`
    - `commuter_transport_and_ferries`
    - `computer_network_services`
    - `computer_programming`
    - `computer_repair`
    - `computer_software_stores`
    - `computers_peripherals_and_software`
    - `concrete_work_services`
    - `construction_materials`
    - `consulting_public_relations`
    - `correspondence_schools`
    - `cosmetic_stores`
    - `counseling_services`
    - `country_clubs`
    - `courier_services`
    - `court_costs`
    - `credit_reporting_agencies`
    - `cruise_lines`
    - `dairy_products_stores`
    - `dance_hall_studios_schools`
    - `dating_escort_services`
    - `dentists_orthodontists`
    - `department_stores`
    - `detective_agencies`
    - `digital_goods_applications`
    - `digital_goods_games`
    - `digital_goods_large_volume`
    - `digital_goods_media`
    - `direct_marketing_catalog_merchant`
    - `direct_marketing_combination_catalog_and_retail_merchant`
    - `direct_marketing_inbound_telemarketing`
    - `direct_marketing_insurance_services`
    - `direct_marketing_other`
    - `direct_marketing_outbound_telemarketing`
    - `direct_marketing_subscription`
    - `direct_marketing_travel`
    - `discount_stores`
    - `doctors`
    - `door_to_door_sales`
    - `drapery_window_covering_and_upholstery_stores`
    - `drinking_places`
    - `drug_stores_and_pharmacies`
    - `drugs_drug_proprietaries_and_druggist_sundries`
    - `dry_cleaners`
    - `durable_goods`
    - `duty_free_stores`
    - `eating_places_restaurants`
    - `educational_services`
    - `electric_razor_stores`
    - `electric_vehicle_charging`
    - `electrical_parts_and_equipment`
    - `electrical_services`
    - `electronics_repair_shops`
    - `electronics_stores`
    - `elementary_secondary_schools`
    - `emergency_services_gcas_visa_use_only`
    - `employment_temp_agencies`
    - `equipment_rental`
    - `exterminating_services`
    - `family_clothing_stores`
    - `fast_food_restaurants`
    - `financial_institutions`
    - `fines_government_administrative_entities`
    - `fireplace_fireplace_screens_and_accessories_stores`
    - `floor_covering_stores`
    - `florists`
    - `florists_supplies_nursery_stock_and_flowers`
    - `freezer_and_locker_meat_provisioners`
    - `fuel_dealers_non_automotive`
    - `funeral_services_crematories`
    - `furniture_home_furnishings_and_equipment_stores_except_appliances`
    - `furniture_repair_refinishing`
    - `furriers_and_fur_shops`
    - `general_services`
    - `gift_card_novelty_and_souvenir_shops`
    - `glass_paint_and_wallpaper_stores`
    - `glassware_crystal_stores`
    - `golf_courses_public`
    - `government_licensed_horse_dog_racing_us_region_only`
    - `government_licensed_online_casions_online_gambling_us_region_only`
    - `government_owned_lotteries_non_us_region`
    - `government_owned_lotteries_us_region_only`
    - `government_services`
    - `grocery_stores_supermarkets`
    - `hardware_equipment_and_supplies`
    - `hardware_stores`
    - `health_and_beauty_spas`
    - `hearing_aids_sales_and_supplies`
    - `heating_plumbing_a_c`
    - `hobby_toy_and_game_shops`
    - `home_supply_warehouse_stores`
    - `hospitals`
    - `hotels_motels_and_resorts`
    - `household_appliance_stores`
    - `industrial_supplies`
    - `information_retrieval_services`
    - `insurance_default`
    - `insurance_underwriting_premiums`
    - `intra_company_purchases`
    - `jewelry_stores_watches_clocks_and_silverware_stores`
    - `landscaping_services`
    - `laundries`
    - `laundry_cleaning_services`
    - `legal_services_attorneys`
    - `luggage_and_leather_goods_stores`
    - `lumber_building_materials_stores`
    - `manual_cash_disburse`
    - `marinas_service_and_supplies`
    - `marketplaces`
    - `masonry_stonework_and_plaster`
    - `massage_parlors`
    - `medical_and_dental_labs`
    - `medical_dental_ophthalmic_and_hospital_equipment_and_supplies`
    - `medical_services`
    - `membership_organizations`
    - `mens_and_boys_clothing_and_accessories_stores`
    - `mens_womens_clothing_stores`
    - `metal_service_centers`
    - `miscellaneous`
    - `miscellaneous_apparel_and_accessory_shops`
    - `miscellaneous_auto_dealers`
    - `miscellaneous_business_services`
    - `miscellaneous_food_stores`
    - `miscellaneous_general_merchandise`
    - `miscellaneous_general_services`
    - `miscellaneous_home_furnishing_specialty_stores`
    - `miscellaneous_publishing_and_printing`
    - `miscellaneous_recreation_services`
    - `miscellaneous_repair_shops`
    - `miscellaneous_specialty_retail`
    - `mobile_home_dealers`
    - `motion_picture_theaters`
    - `motor_freight_carriers_and_trucking`
    - `motor_homes_dealers`
    - `motor_vehicle_supplies_and_new_parts`
    - `motorcycle_shops_and_dealers`
    - `motorcycle_shops_dealers`
    - `music_stores_musical_instruments_pianos_and_sheet_music`
    - `news_dealers_and_newsstands`
    - `non_fi_money_orders`
    - `non_fi_stored_value_card_purchase_load`
    - `nondurable_goods`
    - `nurseries_lawn_and_garden_supply_stores`
    - `nursing_personal_care`
    - `office_and_commercial_furniture`
    - `opticians_eyeglasses`
    - `optometrists_ophthalmologist`
    - `orthopedic_goods_prosthetic_devices`
    - `osteopaths`
    - `package_stores_beer_wine_and_liquor`
    - `paints_varnishes_and_supplies`
    - `parking_lots_garages`
    - `passenger_railways`
    - `pawn_shops`
    - `pet_shops_pet_food_and_supplies`
    - `petroleum_and_petroleum_products`
    - `photo_developing`
    - `photographic_photocopy_microfilm_equipment_and_supplies`
    - `photographic_studios`
    - `picture_video_production`
    - `piece_goods_notions_and_other_dry_goods`
    - `plumbing_heating_equipment_and_supplies`
    - `political_organizations`
    - `postal_services_government_only`
    - `precious_stones_and_metals_watches_and_jewelry`
    - `professional_services`
    - `public_warehousing_and_storage`
    - `quick_copy_repro_and_blueprint`
    - `railroads`
    - `real_estate_agents_and_managers_rentals`
    - `record_stores`
    - `recreational_vehicle_rentals`
    - `religious_goods_stores`
    - `religious_organizations`
    - `roofing_siding_sheet_metal`
    - `secretarial_support_services`
    - `security_brokers_dealers`
    - `service_stations`
    - `sewing_needlework_fabric_and_piece_goods_stores`
    - `shoe_repair_hat_cleaning`
    - `shoe_stores`
    - `small_appliance_repair`
    - `snowmobile_dealers`
    - `special_trade_services`
    - `specialty_cleaning`
    - `sporting_goods_stores`
    - `sporting_recreation_camps`
    - `sports_and_riding_apparel_stores`
    - `sports_clubs_fields`
    - `stamp_and_coin_stores`
    - `stationary_office_supplies_printing_and_writing_paper`
    - `stationery_stores_office_and_school_supply_stores`
    - `swimming_pools_sales`
    - `t_ui_travel_germany`
    - `tailors_alterations`
    - `tax_payments_government_agencies`
    - `tax_preparation_services`
    - `taxicabs_limousines`
    - `telecommunication_equipment_and_telephone_sales`
    - `telecommunication_services`
    - `telegraph_services`
    - `tent_and_awning_shops`
    - `testing_laboratories`
    - `theatrical_ticket_agencies`
    - `timeshares`
    - `tire_retreading_and_repair`
    - `tolls_bridge_fees`
    - `tourist_attractions_and_exhibits`
    - `towing_services`
    - `trailer_parks_campgrounds`
    - `transportation_services`
    - `travel_agencies_tour_operators`
    - `truck_stop_iteration`
    - `truck_utility_trailer_rentals`
    - `typesetting_plate_making_and_related_services`
    - `typewriter_stores`
    - `u_s_federal_government_agencies_or_departments`
    - `uniforms_commercial_clothing`
    - `used_merchandise_and_secondhand_stores`
    - `utilities`
    - `variety_stores`
    - `veterinary_services`
    - `video_amusement_game_supplies`
    - `video_game_arcades`
    - `video_tape_rental_stores`
    - `vocational_trade_schools`
    - `watch_jewelry_repair`
    - `welding_repair`
    - `wholesale_clubs`
    - `wig_and_toupee_stores`
    - `wires_money_orders`
    - `womens_accessory_and_specialty_shops`
    - `womens_ready_to_wear_stores`
    - `wrecking_and_salvage_yards`

  - `spending_controls.blocked_merchant_countries` (array of strings, nullable)
    Array of strings containing representing countries from which authorizations will be declined. Country codes should be ISO 3166 alpha-2 country codes (e.g. `US`). Cannot be set with `allowed_merchant_countries`. Provide an empty value to unset this control.

  - `spending_controls.spending_limits` (array of objects, nullable)
    Limit spending with amount-based rules that apply across any cards this card replaced (i.e., its `replacement_for` card and *that* card’s `replacement_for` card, up the chain).

    - `spending_controls.spending_limits.amount` (integer)
      Maximum amount allowed to spend per interval. This amount is in the card’s currency and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

    - `spending_controls.spending_limits.categories` (array of enums, nullable)
      Array of strings containing [categories](https://docs.stripe.com/docs/api.md#issuing_authorization_object-merchant_data-category) this limit applies to. Omitting this field will apply the limit to all categories.
Possible enum values:
      - `ac_refrigeration_repair`
      - `accounting_bookkeeping_services`
      - `advertising_services`
      - `agricultural_cooperative`
      - `airlines_air_carriers`
      - `airports_flying_fields`
      - `ambulance_services`
      - `amusement_parks_carnivals`
      - `antique_reproductions`
      - `antique_shops`
      - `aquariums`
      - `architectural_surveying_services`
      - `art_dealers_and_galleries`
      - `artists_supply_and_craft_shops`
      - `auto_and_home_supply_stores`
      - `auto_body_repair_shops`
      - `auto_paint_shops`
      - `auto_service_shops`
      - `automated_cash_disburse`
      - `automated_fuel_dispensers`
      - `automobile_associations`
      - `automotive_parts_and_accessories_stores`
      - `automotive_tire_stores`
      - `bail_and_bond_payments`
      - `bakeries`
      - `bands_orchestras`
      - `barber_and_beauty_shops`
      - `betting_casino_gambling`
      - `bicycle_shops`
      - `billiard_pool_establishments`
      - `boat_dealers`
      - `boat_rentals_and_leases`
      - `book_stores`
      - `books_periodicals_and_newspapers`
      - `bowling_alleys`
      - `bus_lines`
      - `business_secretarial_schools`
      - `buying_shopping_services`
      - `cable_satellite_and_other_pay_television_and_radio`
      - `camera_and_photographic_supply_stores`
      - `candy_nut_and_confectionery_stores`
      - `car_and_truck_dealers_new_used`
      - `car_and_truck_dealers_used_only`
      - `car_rental_agencies`
      - `car_washes`
      - `carpentry_services`
      - `carpet_upholstery_cleaning`
      - `caterers`
      - `charitable_and_social_service_organizations_fundraising`
      - `chemicals_and_allied_products`
      - `child_care_services`
      - `childrens_and_infants_wear_stores`
      - `chiropodists_podiatrists`
      - `chiropractors`
      - `cigar_stores_and_stands`
      - `civic_social_fraternal_associations`
      - `cleaning_and_maintenance`
      - `clothing_rental`
      - `colleges_universities`
      - `commercial_equipment`
      - `commercial_footwear`
      - `commercial_photography_art_and_graphics`
      - `commuter_transport_and_ferries`
      - `computer_network_services`
      - `computer_programming`
      - `computer_repair`
      - `computer_software_stores`
      - `computers_peripherals_and_software`
      - `concrete_work_services`
      - `construction_materials`
      - `consulting_public_relations`
      - `correspondence_schools`
      - `cosmetic_stores`
      - `counseling_services`
      - `country_clubs`
      - `courier_services`
      - `court_costs`
      - `credit_reporting_agencies`
      - `cruise_lines`
      - `dairy_products_stores`
      - `dance_hall_studios_schools`
      - `dating_escort_services`
      - `dentists_orthodontists`
      - `department_stores`
      - `detective_agencies`
      - `digital_goods_applications`
      - `digital_goods_games`
      - `digital_goods_large_volume`
      - `digital_goods_media`
      - `direct_marketing_catalog_merchant`
      - `direct_marketing_combination_catalog_and_retail_merchant`
      - `direct_marketing_inbound_telemarketing`
      - `direct_marketing_insurance_services`
      - `direct_marketing_other`
      - `direct_marketing_outbound_telemarketing`
      - `direct_marketing_subscription`
      - `direct_marketing_travel`
      - `discount_stores`
      - `doctors`
      - `door_to_door_sales`
      - `drapery_window_covering_and_upholstery_stores`
      - `drinking_places`
      - `drug_stores_and_pharmacies`
      - `drugs_drug_proprietaries_and_druggist_sundries`
      - `dry_cleaners`
      - `durable_goods`
      - `duty_free_stores`
      - `eating_places_restaurants`
      - `educational_services`
      - `electric_razor_stores`
      - `electric_vehicle_charging`
      - `electrical_parts_and_equipment`
      - `electrical_services`
      - `electronics_repair_shops`
      - `electronics_stores`
      - `elementary_secondary_schools`
      - `emergency_services_gcas_visa_use_only`
      - `employment_temp_agencies`
      - `equipment_rental`
      - `exterminating_services`
      - `family_clothing_stores`
      - `fast_food_restaurants`
      - `financial_institutions`
      - `fines_government_administrative_entities`
      - `fireplace_fireplace_screens_and_accessories_stores`
      - `floor_covering_stores`
      - `florists`
      - `florists_supplies_nursery_stock_and_flowers`
      - `freezer_and_locker_meat_provisioners`
      - `fuel_dealers_non_automotive`
      - `funeral_services_crematories`
      - `furniture_home_furnishings_and_equipment_stores_except_appliances`
      - `furniture_repair_refinishing`
      - `furriers_and_fur_shops`
      - `general_services`
      - `gift_card_novelty_and_souvenir_shops`
      - `glass_paint_and_wallpaper_stores`
      - `glassware_crystal_stores`
      - `golf_courses_public`
      - `government_licensed_horse_dog_racing_us_region_only`
      - `government_licensed_online_casions_online_gambling_us_region_only`
      - `government_owned_lotteries_non_us_region`
      - `government_owned_lotteries_us_region_only`
      - `government_services`
      - `grocery_stores_supermarkets`
      - `hardware_equipment_and_supplies`
      - `hardware_stores`
      - `health_and_beauty_spas`
      - `hearing_aids_sales_and_supplies`
      - `heating_plumbing_a_c`
      - `hobby_toy_and_game_shops`
      - `home_supply_warehouse_stores`
      - `hospitals`
      - `hotels_motels_and_resorts`
      - `household_appliance_stores`
      - `industrial_supplies`
      - `information_retrieval_services`
      - `insurance_default`
      - `insurance_underwriting_premiums`
      - `intra_company_purchases`
      - `jewelry_stores_watches_clocks_and_silverware_stores`
      - `landscaping_services`
      - `laundries`
      - `laundry_cleaning_services`
      - `legal_services_attorneys`
      - `luggage_and_leather_goods_stores`
      - `lumber_building_materials_stores`
      - `manual_cash_disburse`
      - `marinas_service_and_supplies`
      - `marketplaces`
      - `masonry_stonework_and_plaster`
      - `massage_parlors`
      - `medical_and_dental_labs`
      - `medical_dental_ophthalmic_and_hospital_equipment_and_supplies`
      - `medical_services`
      - `membership_organizations`
      - `mens_and_boys_clothing_and_accessories_stores`
      - `mens_womens_clothing_stores`
      - `metal_service_centers`
      - `miscellaneous`
      - `miscellaneous_apparel_and_accessory_shops`
      - `miscellaneous_auto_dealers`
      - `miscellaneous_business_services`
      - `miscellaneous_food_stores`
      - `miscellaneous_general_merchandise`
      - `miscellaneous_general_services`
      - `miscellaneous_home_furnishing_specialty_stores`
      - `miscellaneous_publishing_and_printing`
      - `miscellaneous_recreation_services`
      - `miscellaneous_repair_shops`
      - `miscellaneous_specialty_retail`
      - `mobile_home_dealers`
      - `motion_picture_theaters`
      - `motor_freight_carriers_and_trucking`
      - `motor_homes_dealers`
      - `motor_vehicle_supplies_and_new_parts`
      - `motorcycle_shops_and_dealers`
      - `motorcycle_shops_dealers`
      - `music_stores_musical_instruments_pianos_and_sheet_music`
      - `news_dealers_and_newsstands`
      - `non_fi_money_orders`
      - `non_fi_stored_value_card_purchase_load`
      - `nondurable_goods`
      - `nurseries_lawn_and_garden_supply_stores`
      - `nursing_personal_care`
      - `office_and_commercial_furniture`
      - `opticians_eyeglasses`
      - `optometrists_ophthalmologist`
      - `orthopedic_goods_prosthetic_devices`
      - `osteopaths`
      - `package_stores_beer_wine_and_liquor`
      - `paints_varnishes_and_supplies`
      - `parking_lots_garages`
      - `passenger_railways`
      - `pawn_shops`
      - `pet_shops_pet_food_and_supplies`
      - `petroleum_and_petroleum_products`
      - `photo_developing`
      - `photographic_photocopy_microfilm_equipment_and_supplies`
      - `photographic_studios`
      - `picture_video_production`
      - `piece_goods_notions_and_other_dry_goods`
      - `plumbing_heating_equipment_and_supplies`
      - `political_organizations`
      - `postal_services_government_only`
      - `precious_stones_and_metals_watches_and_jewelry`
      - `professional_services`
      - `public_warehousing_and_storage`
      - `quick_copy_repro_and_blueprint`
      - `railroads`
      - `real_estate_agents_and_managers_rentals`
      - `record_stores`
      - `recreational_vehicle_rentals`
      - `religious_goods_stores`
      - `religious_organizations`
      - `roofing_siding_sheet_metal`
      - `secretarial_support_services`
      - `security_brokers_dealers`
      - `service_stations`
      - `sewing_needlework_fabric_and_piece_goods_stores`
      - `shoe_repair_hat_cleaning`
      - `shoe_stores`
      - `small_appliance_repair`
      - `snowmobile_dealers`
      - `special_trade_services`
      - `specialty_cleaning`
      - `sporting_goods_stores`
      - `sporting_recreation_camps`
      - `sports_and_riding_apparel_stores`
      - `sports_clubs_fields`
      - `stamp_and_coin_stores`
      - `stationary_office_supplies_printing_and_writing_paper`
      - `stationery_stores_office_and_school_supply_stores`
      - `swimming_pools_sales`
      - `t_ui_travel_germany`
      - `tailors_alterations`
      - `tax_payments_government_agencies`
      - `tax_preparation_services`
      - `taxicabs_limousines`
      - `telecommunication_equipment_and_telephone_sales`
      - `telecommunication_services`
      - `telegraph_services`
      - `tent_and_awning_shops`
      - `testing_laboratories`
      - `theatrical_ticket_agencies`
      - `timeshares`
      - `tire_retreading_and_repair`
      - `tolls_bridge_fees`
      - `tourist_attractions_and_exhibits`
      - `towing_services`
      - `trailer_parks_campgrounds`
      - `transportation_services`
      - `travel_agencies_tour_operators`
      - `truck_stop_iteration`
      - `truck_utility_trailer_rentals`
      - `typesetting_plate_making_and_related_services`
      - `typewriter_stores`
      - `u_s_federal_government_agencies_or_departments`
      - `uniforms_commercial_clothing`
      - `used_merchandise_and_secondhand_stores`
      - `utilities`
      - `variety_stores`
      - `veterinary_services`
      - `video_amusement_game_supplies`
      - `video_game_arcades`
      - `video_tape_rental_stores`
      - `vocational_trade_schools`
      - `watch_jewelry_repair`
      - `welding_repair`
      - `wholesale_clubs`
      - `wig_and_toupee_stores`
      - `wires_money_orders`
      - `womens_accessory_and_specialty_shops`
      - `womens_ready_to_wear_stores`
      - `wrecking_and_salvage_yards`

    - `spending_controls.spending_limits.interval` (enum)
      Interval (or event) to which the amount applies.
Possible enum values:
      - `all_time`
        Limit applies to all transactions.

      - `daily`
        Limit applies to a day, starting at midnight UTC.

      - `monthly`
        Limit applies to a month, starting on the 1st at midnight UTC.

      - `per_authorization`
        Limit applies to each authorization.

      - `weekly`
        Limit applies to a week, starting on Sunday at midnight UTC.

      - `yearly`
        Limit applies to a year, starting on January 1st at midnight UTC.

  - `spending_controls.spending_limits_currency` (enum, nullable)
    Currency of the amounts within `spending_limits`. Always the same as the currency of the card.

- `status` (enum)
  Whether authorizations can be approved on this card. May be blocked from activating cards depending on past-due Cardholder requirements. Defaults to `inactive`.
Possible enum values:
  - `active`
    The card can approve authorizations. If the card is linked to a cardholder with past-due requirements, you may be unable to change the card’s status to ‘active’.

  - `canceled`
    The card will decline authorizations with the `card_canceled` reason. This status is permanent.

  - `inactive`
    The card will decline authorizations with the `card_inactive` reason.

- `type` (enum)
  The type of the card.
Possible enum values:
  - `physical`
    A physical card will be printed and shipped. It can be used at physical terminals.

  - `virtual`
    No physical card will be printed. The card can be used online and can be [added to digital wallets](https://stripe.com/docs/issuing/cards/digital-wallets).

- `wallets` (object, nullable)
  Information relating to digital wallets (like Apple Pay and Google Pay).

  - `wallets.apple_pay` (object)
    Apple Pay Details

    - `wallets.apple_pay.eligible` (boolean)
      Apple Pay Eligibility

    - `wallets.apple_pay.ineligible_reason` (enum, nullable)
      Reason the card is ineligible for Apple Pay
Possible enum values:
      - `missing_agreement`
        Apple Pay is not enabled for your account.

      - `missing_cardholder_contact`
        Cardholder phone number or email required.

      - `unsupported_region`
        Apple Pay is not supported in the cardholder’s country.

  - `wallets.google_pay` (object)
    Google Pay Details

    - `wallets.google_pay.eligible` (boolean)
      Google Pay Eligibility

    - `wallets.google_pay.ineligible_reason` (enum, nullable)
      Reason the card is ineligible for Google Pay
Possible enum values:
      - `missing_agreement`
        Google Pay is not enabled for your account.

      - `missing_cardholder_contact`
        Cardholder phone number or email required.

      - `unsupported_region`
        Google Pay is not supported in the cardholder’s country.

  - `wallets.primary_account_identifier` (string, nullable)
    Unique identifier for a card used with digital wallets

#### Virtual

#### Virtual

### The Card object

```json
{
  "id": "ic_1MvSieLkdIwHu7ixn6uuO0Xu",
  "object": "issuing.card",
  "brand": "Visa",
  "cancellation_reason": null,
  "cardholder": {
    "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",
    "object": "issuing.cardholder",
    "billing": {
      "address": {
        "city": "Anytown",
        "country": "US",
        "line1": "123 Main Street",
        "line2": null,
        "postal_code": "12345",
        "state": "CA"
      }
    },
    "company": null,
    "created": 1680415995,
    "email": null,
    "individual": null,
    "livemode": false,
    "metadata": {},
    "name": "John Doe",
    "phone_number": null,
    "requirements": {
      "disabled_reason": "requirements.past_due",
      "past_due": [
        "individual.card_issuing.user_terms_acceptance.ip",
        "individual.card_issuing.user_terms_acceptance.date",
        "individual.first_name",
        "individual.last_name"
      ]
    },
    "spending_controls": {
      "allowed_categories": [],
      "blocked_categories": [],
      "spending_limits": [],
      "spending_limits_currency": null
    },
    "status": "active",
    "type": "individual"
  },
  "created": 1681163868,
  "currency": "usd",
  "exp_month": 8,
  "exp_year": 2024,
  "last4": "4242",
  "livemode": false,
  "metadata": {},
  "replaced_by": null,
  "replacement_for": null,
  "replacement_reason": null,
  "shipping": null,
  "spending_controls": {
    "allowed_categories": null,
    "blocked_categories": null,
    "spending_limits": [],
    "spending_limits_currency": null
  },
  "status": "active",
  "type": "virtual",
  "wallets": {
    "apple_pay": {
      "eligible": false,
      "ineligible_reason": "missing_cardholder_contact"
    },
    "google_pay": {
      "eligible": false,
      "ineligible_reason": "missing_cardholder_contact"
    },
    "primary_account_identifier": null
  }
}
```

#### Physical

#### Physical

### The Card object

```json
{
  "id": "ic_1MvSieLkdIwHu7ixn6uuO0Xu",
  "object": "issuing.card",
  "brand": "Visa",
  "cancellation_reason": null,
  "cardholder": {
    "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",
    "object": "issuing.cardholder",
    "billing": {
      "address": {
        "city": "Anytown",
        "country": "US",
        "line1": "123 Main Street",
        "line2": null,
        "postal_code": "12345",
        "state": "CA"
      }
    },
    "company": null,
    "created": 1680415995,
    "email": null,
    "individual": null,
    "livemode": false,
    "metadata": {},
    "name": "John Doe",
    "phone_number": null,
    "requirements": {
      "disabled_reason": "requirements.past_due",
      "past_due": [
        "individual.card_issuing.user_terms_acceptance.ip",
        "individual.card_issuing.user_terms_acceptance.date",
        "individual.first_name",
        "individual.last_name"
      ]
    },
    "spending_controls": {
      "allowed_categories": [],
      "blocked_categories": [],
      "spending_limits": [],
      "spending_limits_currency": null
    },
    "status": "active",
    "type": "individual"
  },
  "created": 1681163868,
  "currency": "usd",
  "exp_month": 8,
  "exp_year": 2024,
  "last4": "4242",
  "livemode": false,
  "personalization_design": "ipcd_1QhT4vRkL7wZcM8bJqF3gN2Y",
  "metadata": {},
  "replaced_by": null,
  "replacement_for": null,
  "replacement_reason": null,
  "shipping": {
    "address": {
      "city": "Anytown",
      "country": "US",
      "line1": "123 Main Street",
      "line2": null,
      "postal_code": "12345",
      "state": "CA"
    },
    "address_validation": {
      "mode": "validation_and_normalization",
      "normalized_address": {
        "city": "ANYTOWN",
        "country": "US",
        "line1": "123 MAIN ST",
        "line2": null,
        "postal_code": "12345",
        "state": "CA"
      },
      "result": "likely_deliverable"
    },
    "carrier": "usps",
    "customs": {
      "eori_number": null
    },
    "eta": 1680415995,
    "name": "John Doe",
    "phone": null,
    "phone_number": "+12345678910",
    "require_signature": false,
    "service": "standard",
    "status": "pending",
    "tracking_number": null,
    "tracking_url": null,
    "type": "individual"
  },
  "spending_controls": {
    "allowed_categories": null,
    "blocked_categories": null,
    "spending_limits": [],
    "spending_limits_currency": null
  },
  "status": "active",
  "type": "physical",
  "wallets": {
    "apple_pay": {
      "eligible": false,
      "ineligible_reason": "missing_cardholder_contact"
    },
    "google_pay": {
      "eligible": false,
      "ineligible_reason": "missing_cardholder_contact"
    },
    "primary_account_identifier": null
  }
}
```