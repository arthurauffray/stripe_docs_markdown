# The Authorization object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount` (integer)
  The total amount that was authorized or rejected. This amount is in `currency` and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). `amount` should be the same as `merchant_amount`, unless `currency` and `merchant_currency` are different.

- `amount_details` (object, nullable)
  Detailed breakdown of amount components. These amounts are denominated in `currency` and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

  - `amount_details.atm_fee` (integer, nullable)
    The fee charged by the ATM for the cash withdrawal.

  - `amount_details.cashback_amount` (integer, nullable)
    The amount of cash requested by the cardholder.

- `approved` (boolean)
  Whether the authorization has been approved.

- `authorization_method` (enum)
  How the card details were provided.
Possible enum values:
  - `chip`
    The card was physically present and inserted into a chip-enabled terminal. The transaction is cryptographically secured.

  - `contactless`
    The card was tapped on a contactless-enabled terminal. If a digital wallet copy of the card was used, the `wallet` field will be present.

  - `keyed_in`
    The card number was manually entered into a terminal.

  - `online`
    The card was used in a card-not-present scenario, such as a transaction initiated at an online e-commerce checkout.

  - `swipe`
    The card was physically swiped in a terminal.

- `balance_transactions` (array of objects)
  List of balance transactions associated with this authorization.

  - `balance_transactions.id` (string)
    Unique identifier for the object.

  - `balance_transactions.object` (string)
    String representing the object’s type. Objects of the same type share the same value.

  - `balance_transactions.amount` (integer)
    Gross amount of this transaction (in cents). A positive value represents funds charged to another party, and a negative value represents funds sent to another party.

  - `balance_transactions.available_on` (timestamp)
    The date that the transaction’s net funds become available in the Stripe balance.

  - `balance_transactions.balance_type` (enum)
    The balance that this transaction impacts.
Possible enum values:
    - `issuing`
      Balance Transactions that affect your Issuing balance

    - `payments`
      Balance Transactions that affect your Payments balance

    - `refund_and_dispute_prefunding`
      Balance Transactions that affect your Refund and Dispute Prefunding balance

  - `balance_transactions.created` (timestamp)
    Time at which the object was created. Measured in seconds since the Unix epoch.

  - `balance_transactions.currency` (enum)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `balance_transactions.description` (string, nullable)
    An arbitrary string attached to the object. Often useful for displaying to users.

  - `balance_transactions.exchange_rate` (float, nullable)
    If applicable, this transaction uses an exchange rate. If money converts from currency A to currency B, then the `amount` in currency A, multipled by the `exchange_rate`, equals the `amount` in currency B. For example, if you charge a customer 10.00 EUR, the PaymentIntent’s `amount` is `1000` and `currency` is `eur`. If this converts to 12.34 USD in your Stripe account, the BalanceTransaction’s `amount` is `1234`, its `currency` is `usd`, and the `exchange_rate` is `1.234`.

  - `balance_transactions.fee` (integer)
    Fees (in cents) paid for this transaction. Represented as a positive integer when assessed.

  - `balance_transactions.fee_details` (array of objects)
    Detailed breakdown of fees (in cents) paid for this transaction.

    - `balance_transactions.fee_details.amount` (integer)
      Amount of the fee, in cents.

    - `balance_transactions.fee_details.application` (string, nullable)
      ID of the Connect application that earned the fee.

    - `balance_transactions.fee_details.currency` (enum)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `balance_transactions.fee_details.description` (string, nullable)
      An arbitrary string attached to the object. Often useful for displaying to users.

    - `balance_transactions.fee_details.type` (string)
      Type of the fee, one of: `application_fee`, `payment_method_passthrough_fee`, `stripe_fee` or `tax`.

  - `balance_transactions.net` (integer)
    Net impact to a Stripe balance (in cents). A positive value represents incrementing a Stripe balance, and a negative value decrementing a Stripe balance. You can calculate the net impact of a transaction on a balance by `amount` - `fee`

  - `balance_transactions.reporting_category` (string)
    Learn more about how [reporting categories](https://stripe.com/docs/reports/reporting-categories) can help you understand balance transactions from an accounting perspective.

  - `balance_transactions.source` (string, nullable)
    This transaction relates to the Stripe object.

  - `balance_transactions.status` (string)
    The transaction’s net funds status in the Stripe balance, which are either `available` or `pending`.

  - `balance_transactions.type` (enum)
    Transaction type: `adjustment`, `advance`, `advance_funding`, `anticipation_repayment`, `application_fee`, `application_fee_refund`, `charge`, `climate_order_purchase`, `climate_order_refund`, `connect_collection_transfer`, `contribution`, `issuing_authorization_hold`, `issuing_authorization_release`, `issuing_dispute`, `issuing_transaction`, `obligation_outbound`, `obligation_reversal_inbound`, `payment`, `payment_failure_refund`, `payment_network_reserve_hold`, `payment_network_reserve_release`, `payment_refund`, `payment_reversal`, `payment_unreconciled`, `payout`, `payout_cancel`, `payout_failure`, `payout_minimum_balance_hold`, `payout_minimum_balance_release`, `refund`, `refund_failure`, `reserve_transaction`, `reserved_funds`, `stripe_fee`, `stripe_fx_fee`, `stripe_balance_payment_debit`, `stripe_balance_payment_debit_reversal`, `tax_fee`, `topup`, `topup_reversal`, `transfer`, `transfer_cancel`, `transfer_failure`, or `transfer_refund`. Learn more about [balance transaction types and what they represent](https://stripe.com/docs/reports/balance-transaction-types). To classify transactions for accounting purposes, consider `reporting_category` instead.
Possible enum values:
    - `adjustment`
    - `advance`
    - `advance_funding`
    - `anticipation_repayment`
    - `application_fee`
    - `application_fee_refund`
    - `charge`
    - `climate_order_purchase`
    - `climate_order_refund`
    - `connect_collection_transfer`
    - `contribution`
    - `issuing_authorization_hold`
    - `issuing_authorization_release`
    - `issuing_dispute`
    - `issuing_transaction`
    - `obligation_outbound`
    - `obligation_reversal_inbound`
    - `payment`
    - `payment_failure_refund`
    - `payment_network_reserve_hold`
    - `payment_network_reserve_release`
    - `payment_refund`
    - `payment_reversal`
    - `payment_unreconciled`
    - `payout`
    - `payout_cancel`
    - `payout_failure`
    - `payout_minimum_balance_hold`
    - `payout_minimum_balance_release`
    - `refund`
    - `refund_failure`
    - `reserve_transaction`
    - `reserved_funds`
    - `stripe_balance_payment_debit`
    - `stripe_balance_payment_debit_reversal`
    - `stripe_fee`
    - `stripe_fx_fee`
    - `tax_fee`
    - `topup`
    - `topup_reversal`
    - `transfer`
    - `transfer_cancel`
    - `transfer_failure`
    - `transfer_refund`

- `card` (object)
  Card associated with this authorization.

  - `card.id` (string)
    Unique identifier for the object.

  - `card.object` (string)
    String representing the object’s type. Objects of the same type share the same value.

  - `card.brand` (string)
    The brand of the card.

  - `card.cancellation_reason` (enum, nullable)
    The reason why the card was canceled.
Possible enum values:
    - `design_rejected`
      The design of this card was rejected by Stripe for violating our [partner guidelines](https://docs.stripe.com/docs/issuing/cards/physical.md#design-review).

    - `lost`
      The card was lost.

    - `stolen`
      The card was stolen.

  - `card.cardholder` (object)
    The [Cardholder](https://docs.stripe.com/docs/api.md#issuing_cardholder_object) object to which the card belongs.

    - `card.cardholder.id` (string)
      Unique identifier for the object.

    - `card.cardholder.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `card.cardholder.billing` (object)
      The cardholder’s billing information.

      - `card.cardholder.billing.address` (object)
        The cardholder’s billing address.

        - `card.cardholder.billing.address.city` (string, nullable)
          City, district, suburb, town, or village.

        - `card.cardholder.billing.address.country` (string, nullable)
          Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

        - `card.cardholder.billing.address.line1` (string, nullable)
          Address line 1, such as the street, PO Box, or company name.

        - `card.cardholder.billing.address.line2` (string, nullable)
          Address line 2, such as the apartment, suite, unit, or building.

        - `card.cardholder.billing.address.postal_code` (string, nullable)
          ZIP or postal code.

        - `card.cardholder.billing.address.state` (string, nullable)
          State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

    - `card.cardholder.company` (object, nullable)
      Additional information about a `company` cardholder.

      - `card.cardholder.company.tax_id_provided` (boolean)
        Whether the company’s business ID number was provided.

    - `card.cardholder.created` (timestamp)
      Time at which the object was created. Measured in seconds since the Unix epoch.

    - `card.cardholder.email` (string, nullable)
      The cardholder’s email address.

    - `card.cardholder.individual` (object, nullable)
      Additional information about an `individual` cardholder.

      - `card.cardholder.individual.card_issuing` (object, nullable)
        Information related to the card_issuing program for this cardholder.

        - `card.cardholder.individual.card_issuing.user_terms_acceptance` (object, nullable)
          Information about cardholder acceptance of Celtic [Authorized User Terms](https://stripe.com/docs/issuing/cards#accept-authorized-user-terms). Required for cards backed by a Celtic program.

          - `card.cardholder.individual.card_issuing.user_terms_acceptance.date` (timestamp, nullable)
            The Unix timestamp marking when the cardholder accepted the Authorized User Terms.

          - `card.cardholder.individual.card_issuing.user_terms_acceptance.ip` (string, nullable)
            The IP address from which the cardholder accepted the Authorized User Terms.

          - `card.cardholder.individual.card_issuing.user_terms_acceptance.user_agent` (string, nullable)
            The user agent of the browser from which the cardholder accepted the Authorized User Terms.

      - `card.cardholder.individual.dob` (object, nullable)
        The date of birth of this cardholder.

        - `card.cardholder.individual.dob.day` (integer, nullable)
          The day of birth, between 1 and 31.

        - `card.cardholder.individual.dob.month` (integer, nullable)
          The month of birth, between 1 and 12.

        - `card.cardholder.individual.dob.year` (integer, nullable)
          The four-digit year of birth.

      - `card.cardholder.individual.first_name` (string, nullable)
        The first name of this cardholder. Required before activating Cards. This field cannot contain any numbers, special characters (except periods, commas, hyphens, spaces and apostrophes) or non-latin letters.

      - `card.cardholder.individual.last_name` (string, nullable)
        The last name of this cardholder.  Required before activating Cards. This field cannot contain any numbers, special characters (except periods, commas, hyphens, spaces and apostrophes) or non-latin letters.

      - `card.cardholder.individual.verification` (object, nullable)
        Government-issued ID document for this cardholder.

        - `card.cardholder.individual.verification.document` (object, nullable)
          An identifying document, either a passport or local ID card.

          - `card.cardholder.individual.verification.document.back` (string, nullable)
            The back of a document returned by a [file upload](https://docs.stripe.com/api/issuing/authorizations/object.md#create_file) with a `purpose` value of `identity_document`.

          - `card.cardholder.individual.verification.document.front` (string, nullable)
            The front of a document returned by a [file upload](https://docs.stripe.com/api/issuing/authorizations/object.md#create_file) with a `purpose` value of `identity_document`.

    - `card.cardholder.livemode` (boolean)
      Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

    - `card.cardholder.metadata` (object)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

    - `card.cardholder.name` (string)
      The cardholder’s name. This will be printed on cards issued to them.

    - `card.cardholder.phone_number` (string, nullable)
      The cardholder’s phone number. This is required for all cardholders who will be creating EU cards. See the [3D Secure documentation](https://docs.stripe.com/docs/issuing/3d-secure.md#when-is-3d-secure-applied) for more details.

    - `card.cardholder.preferred_locales` (array of enums, nullable)
      The cardholder’s preferred locales (languages), ordered by preference. Locales can be `de`, `en`, `es`, `fr`, or `it`. This changes the language of the [3D Secure flow](https://docs.stripe.com/docs/issuing/3d-secure.md) and one-time password messages sent to the cardholder.

    - `card.cardholder.requirements` (object)
      Information about verification requirements for the cardholder.

      - `card.cardholder.requirements.disabled_reason` (enum, nullable)
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

      - `card.cardholder.requirements.past_due` (array of enums, nullable)
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

    - `card.cardholder.spending_controls` (object, nullable)
      Rules that control spending across this cardholder’s cards. Refer to our [documentation](https://docs.stripe.com/docs/issuing/controls/spending-controls.md) for more details.

      - `card.cardholder.spending_controls.allowed_categories` (array of enums, nullable)
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

      - `card.cardholder.spending_controls.allowed_merchant_countries` (array of strings, nullable)
        Array of strings containing representing countries from which authorizations will be allowed. Authorizations from merchants in all other countries will be declined. Country codes should be ISO 3166 alpha-2 country codes (e.g. `US`). Cannot be set with `blocked_merchant_countries`. Provide an empty value to unset this control.

      - `card.cardholder.spending_controls.blocked_categories` (array of enums, nullable)
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

      - `card.cardholder.spending_controls.blocked_merchant_countries` (array of strings, nullable)
        Array of strings containing representing countries from which authorizations will be declined. Country codes should be ISO 3166 alpha-2 country codes (e.g. `US`). Cannot be set with `allowed_merchant_countries`. Provide an empty value to unset this control.

      - `card.cardholder.spending_controls.spending_limits` (array of objects, nullable)
        Limit spending with amount-based rules that apply across this cardholder’s cards.

        - `card.cardholder.spending_controls.spending_limits.amount` (integer)
          Maximum amount allowed to spend per interval. This amount is in the card’s currency and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

        - `card.cardholder.spending_controls.spending_limits.categories` (array of enums, nullable)
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

        - `card.cardholder.spending_controls.spending_limits.interval` (enum)
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

      - `card.cardholder.spending_controls.spending_limits_currency` (enum, nullable)
        Currency of the amounts within `spending_limits`.

    - `card.cardholder.status` (enum)
      Specifies whether to permit authorizations on this cardholder’s cards.
Possible enum values:
      - `active`
        A platform has enabled the cardholder to approve authorizations made with their attached cards. However, if Stripe hasn’t yet verified the cardholder’s identity information, authorizations might still be blocked.

      - `blocked`
        Cards attached to this cardholder will decline all authorizations with the `cardholder_blocked` reason. This status is non-reversible.

      - `inactive`
        Cards attached to this cardholder will decline all authorizations with the `cardholder_inactive` reason.

    - `card.cardholder.type` (enum)
      One of `individual` or `company`. See [Choose a cardholder type](https://docs.stripe.com/docs/issuing/other/choose-cardholder.md) for more details.
Possible enum values:
      - `company`
        The cardholder is a company or business entity, and additional information includes their tax ID. This option may not be available if your [use case](https://docs.stripe.com/docs/issuing/other/choose-cardholder.md#find-your-use-case) only supports individual cardholders.

      - `individual`
        The cardholder is a person, and additional information includes first and last name, date of birth, etc. If you’re issuing Celtic Spend Cards, then Individual cardholders must accept Authorized User Terms prior to activating their card.

  - `card.created` (timestamp)
    Time at which the object was created. Measured in seconds since the Unix epoch.

  - `card.currency` (enum)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Supported currencies are `usd` in the US, `eur` in the EU, and `gbp` in the UK.

  - `card.cvc` (string, nullable)
    The card’s CVC. For security reasons, this is only available for virtual cards, and will be omitted unless you explicitly request it with [the `expand` parameter](https://docs.stripe.com/docs/api/expanding_objects.md). Additionally, it’s only available via the [“Retrieve a card” endpoint](https://docs.stripe.com/docs/api/issuing/cards/retrieve.md), not via “List all cards” or any other endpoint.

  - `card.exp_month` (integer)
    The expiration month of the card.

  - `card.exp_year` (integer)
    The expiration year of the card.

  - `card.last4` (string)
    The last 4 digits of the card number.

  - `card.latest_fraud_warning` (object, nullable)
    Stripe’s assessment of whether this card’s details have been compromised. If this property isn’t null, cancel and reissue the card to prevent fraudulent activity risk.

    - `card.latest_fraud_warning.started_at` (timestamp, nullable)
      Timestamp of the most recent fraud warning.

    - `card.latest_fraud_warning.type` (enum, nullable)
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

  - `card.livemode` (boolean)
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

  - `card.metadata` (object)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

  - `card.number` (string, nullable)
    The full unredacted card number. For security reasons, this is only available for virtual cards, and will be omitted unless you explicitly request it with [the `expand` parameter](https://docs.stripe.com/docs/api/expanding_objects.md). Additionally, it’s only available via the [“Retrieve a card” endpoint](https://docs.stripe.com/docs/api/issuing/cards/retrieve.md), not via “List all cards” or any other endpoint.

  - `card.personalization_design` (string, nullable)
    The personalization design object belonging to this card.

  - `card.replaced_by` (string, nullable)
    The latest card that replaces this card, if any.

  - `card.replacement_for` (string, nullable)
    The card this card replaces, if any.

  - `card.replacement_reason` (enum, nullable)
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

  - `card.second_line` (string, nullable)
    Text separate from cardholder name, printed on the card.

  - `card.shipping` (object, nullable)
    Where and how the card will be shipped.

    - `card.shipping.address` (object)
      Shipping address.

      - `card.shipping.address.city` (string, nullable)
        City, district, suburb, town, or village.

      - `card.shipping.address.country` (string, nullable)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `card.shipping.address.line1` (string, nullable)
        Address line 1, such as the street, PO Box, or company name.

      - `card.shipping.address.line2` (string, nullable)
        Address line 2, such as the apartment, suite, unit, or building.

      - `card.shipping.address.postal_code` (string, nullable)
        ZIP or postal code.

      - `card.shipping.address.state` (string, nullable)
        State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

    - `card.shipping.address_validation` (object, nullable)
      Address validation details for the shipment.

      - `card.shipping.address_validation.mode` (enum)
        The address validation capabilities to use.
Possible enum values:
        - `disabled`
          The card will be shipped without validating or normalizing the shipping address.

        - `normalization_only`
          The card will be shipped with the normalized address without validation. Undeliverable addresses won’t be blocked.

        - `validation_and_normalization`
          The card will be shipped with the normalized, validated address. Undeliverable addresses will be blocked.

      - `card.shipping.address_validation.normalized_address` (object, nullable)
        The normalized shipping address.

        - `card.shipping.address_validation.normalized_address.city` (string, nullable)
          City, district, suburb, town, or village.

        - `card.shipping.address_validation.normalized_address.country` (string, nullable)
          Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

        - `card.shipping.address_validation.normalized_address.line1` (string, nullable)
          Address line 1, such as the street, PO Box, or company name.

        - `card.shipping.address_validation.normalized_address.line2` (string, nullable)
          Address line 2, such as the apartment, suite, unit, or building.

        - `card.shipping.address_validation.normalized_address.postal_code` (string, nullable)
          ZIP or postal code.

        - `card.shipping.address_validation.normalized_address.state` (string, nullable)
          State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

      - `card.shipping.address_validation.result` (enum, nullable)
        The validation result for the shipping address.
Possible enum values:
        - `indeterminate`
          The deliverability of the card’s shipping address could not be determined.

        - `likely_deliverable`
          The card’s shipping address is likely deliverable.

        - `likely_undeliverable`
          The card’s shipping address is likely undeliverable as submitted.

    - `card.shipping.carrier` (enum, nullable)
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

    - `card.shipping.customs` (object, nullable)
      Additional information that may be required for clearing customs.

      - `card.shipping.customs.eori_number` (string, nullable)
        A registration number used for customs in Europe. See [https://www.gov.uk/eori](https://www.gov.uk/eori) for the UK and [https://ec.europa.eu/taxation_customs/business/customs-procedures-import-and-export/customs-procedures/economic-operators-registration-and-identification-number-eori_en](https://ec.europa.eu/taxation_customs/business/customs-procedures-import-and-export/customs-procedures/economic-operators-registration-and-identification-number-eori_en) for the EU.

    - `card.shipping.eta` (timestamp, nullable)
      A unix timestamp representing a best estimate of when the card will be delivered.

    - `card.shipping.name` (string)
      Recipient name.

    - `card.shipping.phone_number` (string, nullable)
      The phone number of the receiver of the shipment. Our courier partners will use this number to contact you in the event of card delivery issues. For individual shipments to the EU/UK, if this field is empty, we will provide them with the phone number provided when the cardholder was initially created.

    - `card.shipping.require_signature` (boolean, nullable)
      Whether a signature is required for card delivery. This feature is only supported for US users. Standard shipping service does not support signature on delivery. The default value for standard shipping service is false and for express and priority services is true.

    - `card.shipping.service` (enum)
      Shipment service, such as `standard` or `express`.
Possible enum values:
      - `express`
        Cards arrive in 4 business days.

      - `priority`
        Cards arrive in 2-3 business days.

      - `standard`
        Cards arrive in 5-8 business days.

    - `card.shipping.status` (enum, nullable)
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

    - `card.shipping.tracking_number` (string, nullable)
      A tracking number for a card shipment.

    - `card.shipping.tracking_url` (string, nullable)
      A link to the shipping carrier’s site where you can view detailed information about a card shipment.

    - `card.shipping.type` (enum)
      Packaging options.
Possible enum values:
      - `bulk`
        Cards are grouped and mailed together.

      - `individual`
        Cards are sent individually in an envelope.

  - `card.spending_controls` (object)
    Rules that control spending for this card. Refer to our [documentation](https://docs.stripe.com/docs/issuing/controls/spending-controls.md) for more details.

    - `card.spending_controls.allowed_categories` (array of enums, nullable)
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

    - `card.spending_controls.allowed_merchant_countries` (array of strings, nullable)
      Array of strings containing representing countries from which authorizations will be allowed. Authorizations from merchants in all other countries will be declined. Country codes should be ISO 3166 alpha-2 country codes (e.g. `US`). Cannot be set with `blocked_merchant_countries`. Provide an empty value to unset this control.

    - `card.spending_controls.blocked_categories` (array of enums, nullable)
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

    - `card.spending_controls.blocked_merchant_countries` (array of strings, nullable)
      Array of strings containing representing countries from which authorizations will be declined. Country codes should be ISO 3166 alpha-2 country codes (e.g. `US`). Cannot be set with `allowed_merchant_countries`. Provide an empty value to unset this control.

    - `card.spending_controls.spending_limits` (array of objects, nullable)
      Limit spending with amount-based rules that apply across any cards this card replaced (i.e., its `replacement_for` card and *that* card’s `replacement_for` card, up the chain).

      - `card.spending_controls.spending_limits.amount` (integer)
        Maximum amount allowed to spend per interval. This amount is in the card’s currency and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

      - `card.spending_controls.spending_limits.categories` (array of enums, nullable)
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

      - `card.spending_controls.spending_limits.interval` (enum)
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

    - `card.spending_controls.spending_limits_currency` (enum, nullable)
      Currency of the amounts within `spending_limits`. Always the same as the currency of the card.

  - `card.status` (enum)
    Whether authorizations can be approved on this card. May be blocked from activating cards depending on past-due Cardholder requirements. Defaults to `inactive`.
Possible enum values:
    - `active`
      The card can approve authorizations. If the card is linked to a cardholder with past-due requirements, you may be unable to change the card’s status to ‘active’.

    - `canceled`
      The card will decline authorizations with the `card_canceled` reason. This status is permanent.

    - `inactive`
      The card will decline authorizations with the `card_inactive` reason.

  - `card.type` (enum)
    The type of the card.
Possible enum values:
    - `physical`
      A physical card will be printed and shipped. It can be used at physical terminals.

    - `virtual`
      No physical card will be printed. The card can be used online and can be [added to digital wallets](https://stripe.com/docs/issuing/cards/digital-wallets).

  - `card.wallets` (object, nullable)
    Information relating to digital wallets (like Apple Pay and Google Pay).

    - `card.wallets.apple_pay` (object)
      Apple Pay Details

      - `card.wallets.apple_pay.eligible` (boolean)
        Apple Pay Eligibility

      - `card.wallets.apple_pay.ineligible_reason` (enum, nullable)
        Reason the card is ineligible for Apple Pay
Possible enum values:
        - `missing_agreement`
          Apple Pay is not enabled for your account.

        - `missing_cardholder_contact`
          Cardholder phone number or email required.

        - `unsupported_region`
          Apple Pay is not supported in the cardholder’s country.

    - `card.wallets.google_pay` (object)
      Google Pay Details

      - `card.wallets.google_pay.eligible` (boolean)
        Google Pay Eligibility

      - `card.wallets.google_pay.ineligible_reason` (enum, nullable)
        Reason the card is ineligible for Google Pay
Possible enum values:
        - `missing_agreement`
          Google Pay is not enabled for your account.

        - `missing_cardholder_contact`
          Cardholder phone number or email required.

        - `unsupported_region`
          Google Pay is not supported in the cardholder’s country.

    - `card.wallets.primary_account_identifier` (string, nullable)
      Unique identifier for a card used with digital wallets

- `cardholder` (string, nullable)
  The cardholder to whom this authorization belongs.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (enum)
  The currency of the cardholder. This currency can be different from the currency presented at authorization and the `merchant_currency` field on this authorization. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `fleet` (object, nullable)
  Fleet-specific information for authorizations using Fleet cards.

  - `fleet.cardholder_prompt_data` (object, nullable)
    Answers to prompts presented to the cardholder at the point of sale. Prompted fields vary depending on the configuration of your physical fleet cards. Typical points of sale support only numeric entry.

    - `fleet.cardholder_prompt_data.alphanumeric_id` (string, nullable)
      [Deprecated] An alphanumeric ID, though typical point of sales only support numeric entry. The card program can be configured to prompt for a vehicle ID, driver ID, or generic ID.

    - `fleet.cardholder_prompt_data.driver_id` (string, nullable)
      Driver ID.

    - `fleet.cardholder_prompt_data.odometer` (integer, nullable)
      Odometer reading.

    - `fleet.cardholder_prompt_data.unspecified_id` (string, nullable)
      An alphanumeric ID. This field is used when a vehicle ID, driver ID, or generic ID is entered by the cardholder, but the merchant or card network did not specify the prompt type.

    - `fleet.cardholder_prompt_data.user_id` (string, nullable)
      User ID.

    - `fleet.cardholder_prompt_data.vehicle_number` (string, nullable)
      Vehicle number.

  - `fleet.purchase_type` (enum, nullable)
    The type of purchase.
Possible enum values:
    - `fuel_and_non_fuel_purchase`
      Fuel and non-fuel purchase.

    - `fuel_purchase`
      Fuel-only purchase.

    - `non_fuel_purchase`
      Non-fuel purchase.

  - `fleet.reported_breakdown` (object, nullable)
    More information about the total amount. Typically this information is received from the merchant after the authorization has been approved and the fuel dispensed. This information is not guaranteed to be accurate as some merchants may provide unreliable data.

    - `fleet.reported_breakdown.fuel` (object, nullable)
      Breakdown of fuel portion of the purchase.

      - `fleet.reported_breakdown.fuel.gross_amount_decimal` (decimal string, nullable)
        Gross fuel amount that should equal Fuel Quantity multiplied by Fuel Unit Cost, inclusive of taxes.

    - `fleet.reported_breakdown.non_fuel` (object, nullable)
      Breakdown of non-fuel portion of the purchase.

      - `fleet.reported_breakdown.non_fuel.gross_amount_decimal` (decimal string, nullable)
        Gross non-fuel amount that should equal the sum of the line items, inclusive of taxes.

    - `fleet.reported_breakdown.tax` (object, nullable)
      Information about tax included in this transaction.

      - `fleet.reported_breakdown.tax.local_amount_decimal` (decimal string, nullable)
        Amount of state or provincial Sales Tax included in the transaction amount. `null` if not reported by merchant or not subject to tax.

      - `fleet.reported_breakdown.tax.national_amount_decimal` (decimal string, nullable)
        Amount of national Sales Tax or VAT included in the transaction amount. `null` if not reported by merchant or not subject to tax.

  - `fleet.service_type` (enum, nullable)
    The type of fuel service.
Possible enum values:
    - `full_service`
      Full-service fuel station purchase.

    - `non_fuel_transaction`
      Non-fuel transaction.

    - `self_service`
      Self-service fuel station purchase.

- `fraud_challenges` (array of objects, nullable)
  Fraud challenges sent to the cardholder, if this authorization was declined for fraud risk reasons.

  - `fraud_challenges.channel` (enum)
    The method by which the fraud challenge was delivered to the cardholder.
Possible enum values:
    - `sms`
      SMS sent to the cardholder’s phone number.

  - `fraud_challenges.status` (enum)
    The status of the fraud challenge.
Possible enum values:
    - `expired`
      The cardholder did not respond to the challenge within 12 hours of it being sent, and it has expired. Any further response to the challenge will be ignored.

    - `pending`
      The challenge has been sent to the cardholder or is about to be sent.

    - `rejected`
      The cardholder responded to the challenge indicating that the authorization was fraudulent, and that similar authorizations should continue to be declined.

    - `undeliverable`
      A challenge has been requested to be sent, but the cardholder is unable to receive it.

    - `verified`
      The cardholder responded to the challenge indicating that the authorization was not fraudulent, and that similar authorizations should be approved.

  - `fraud_challenges.undeliverable_reason` (enum, nullable)
    If the challenge is not deliverable, the reason why.
Possible enum values:
    - `no_phone_number`
      SMS fraud challenges cannot be delivered to this cardholder because they have no `phone_number`.

    - `unsupported_phone_number`
      SMS fraud challenges cannot be delivered to this cardholder because their `phone_number` is not supported

- `fuel` (object, nullable)
  Information about fuel that was purchased with this transaction. Typically this information is received from the merchant after the authorization has been approved and the fuel dispensed.

  - `fuel.industry_product_code` (string, nullable)
    [Conexxus Payment System Product Code](https://www.conexxus.org/conexxus-payment-system-product-codes) identifying the primary fuel product purchased.

  - `fuel.quantity_decimal` (decimal string, nullable)
    The quantity of `unit`s of fuel that was dispensed, represented as a decimal string with at most 12 decimal places.

  - `fuel.type` (enum, nullable)
    The type of fuel that was purchased.
Possible enum values:
    - `diesel`
      Diesel.

    - `other`
      Other.

    - `unleaded_plus`
      Unleaded plus.

    - `unleaded_regular`
      Unleaded regular.

    - `unleaded_super`
      Unleaded super.

  - `fuel.unit` (enum, nullable)
    The units for `quantity_decimal`.
Possible enum values:
    - `charging_minute`
      Charging minute.

    - `imperial_gallon`
      Imperial gallon.

    - `kilogram`
      Kilogram.

    - `kilowatt_hour`
      Kilowatt-hour.

    - `liter`
      Liter.

    - `other`
      Other.

    - `pound`
      Pound.

    - `us_gallon`
      US gallon.

  - `fuel.unit_cost_decimal` (decimal string, nullable)
    The cost in cents per each unit of fuel, represented as a decimal string with at most 12 decimal places.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `merchant_amount` (integer)
  The total amount that was authorized or rejected. This amount is in the `merchant_currency` and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). `merchant_amount` should be the same as `amount`, unless `merchant_currency` and `currency` are different.

- `merchant_currency` (enum)
  The local currency that was presented to the cardholder for the authorization. This currency can be different from the cardholder currency and the `currency` field on this authorization. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `merchant_data` (object)
  Details about the seller (grocery store, e-commerce website, etc.) where the card authorization happened.

  - `merchant_data.category` (string)
    A categorization of the seller’s type of business. See our [merchant categories guide](https://docs.stripe.com/docs/issuing/merchant-categories.md) for a list of possible values.

  - `merchant_data.category_code` (string)
    The merchant category code for the seller’s business

  - `merchant_data.city` (string, nullable)
    City where the seller is located

  - `merchant_data.country` (string, nullable)
    Country where the seller is located

  - `merchant_data.name` (string, nullable)
    Name of the seller

  - `merchant_data.network_id` (string)
    Identifier assigned to the seller by the card network. Different card networks may assign different network_id fields to the same merchant.

  - `merchant_data.postal_code` (string, nullable)
    Postal code where the seller is located

  - `merchant_data.state` (string, nullable)
    State where the seller is located

  - `merchant_data.tax_id` (string, nullable)
    The seller’s tax identification number. Currently populated for French merchants only.

  - `merchant_data.terminal_id` (string, nullable)
    An ID assigned by the seller to the location of the sale.

  - `merchant_data.url` (string, nullable)
    URL provided by the merchant on a 3DS request

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `network_data` (object, nullable)
  Details about the authorization, such as identifiers, set by the card network.

  - `network_data.acquiring_institution_id` (string, nullable)
    Identifier assigned to the acquirer by the card network. Sometimes this value is not provided by the network; in this case, the value will be `null`.

  - `network_data.system_trace_audit_number` (string, nullable)
    The System Trace Audit Number (STAN) is a 6-digit identifier assigned by the acquirer. Prefer `network_data.transaction_id` if present, unless you have special requirements.

  - `network_data.transaction_id` (string, nullable)
    Unique identifier for the authorization assigned by the card network used to match subsequent messages, disputes, and transactions.

- `pending_request` (object, nullable)
  The pending authorization request. This field will only be non-null during an `issuing_authorization.request` webhook.

  - `pending_request.amount` (integer)
    The additional amount Stripe will hold if the authorization is approved, in the card’s [currency](https://docs.stripe.com/docs/api.md#issuing_authorization_object-pending-request-currency) and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

  - `pending_request.amount_details` (object, nullable)
    Detailed breakdown of amount components. These amounts are denominated in `currency` and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

    - `pending_request.amount_details.atm_fee` (integer, nullable)
      The fee charged by the ATM for the cash withdrawal.

    - `pending_request.amount_details.cashback_amount` (integer, nullable)
      The amount of cash requested by the cardholder.

  - `pending_request.currency` (enum)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `pending_request.is_amount_controllable` (boolean)
    If set `true`, you may provide [amount](https://docs.stripe.com/docs/api/issuing/authorizations/approve.md#approve_issuing_authorization-amount) to control how much to hold for the authorization.

  - `pending_request.merchant_amount` (integer)
    The amount the merchant is requesting to be authorized in the `merchant_currency`. The amount is in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

  - `pending_request.merchant_currency` (enum)
    The local currency the merchant is requesting to authorize.

  - `pending_request.network_risk_score` (integer, nullable)
    The card network’s estimate of the likelihood that an authorization is fraudulent. Takes on values between 1 and 99.

- `request_history` (array of objects)
  History of every time a `pending_request` authorization was approved/declined, either by you directly or by Stripe (e.g. based on your spending_controls). If the merchant changes the authorization by performing an incremental authorization, you can look at this field to see the previous requests for the authorization. This field can be helpful in determining why a given authorization was approved/declined.

  - `request_history.amount` (integer)
    The `pending_request.amount` at the time of the request, presented in your card’s currency and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal). Stripe held this amount from your account to fund the authorization if the request was approved.

  - `request_history.amount_details` (object, nullable)
    Detailed breakdown of amount components. These amounts are denominated in `currency` and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

    - `request_history.amount_details.atm_fee` (integer, nullable)
      The fee charged by the ATM for the cash withdrawal.

    - `request_history.amount_details.cashback_amount` (integer, nullable)
      The amount of cash requested by the cardholder.

  - `request_history.approved` (boolean)
    Whether this request was approved.

  - `request_history.authorization_code` (string, nullable)
    A code created by Stripe which is shared with the merchant to validate the authorization. This field will be populated if the authorization message was approved. The code typically starts with the letter “S”, followed by a six-digit number. For example, “S498162”. Please note that the code is not guaranteed to be unique across authorizations.

  - `request_history.created` (timestamp)
    Time at which the object was created. Measured in seconds since the Unix epoch.

  - `request_history.currency` (string)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `request_history.merchant_amount` (integer)
    The `pending_request.merchant_amount` at the time of the request, presented in the `merchant_currency` and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

  - `request_history.merchant_currency` (string)
    The currency that was collected by the merchant and presented to the cardholder for the authorization. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `request_history.network_risk_score` (integer, nullable)
    The card network’s estimate of the likelihood that an authorization is fraudulent. Takes on values between 1 and 99.

  - `request_history.reason` (enum)
    When an authorization is approved or declined by you or by Stripe, this field provides additional detail on the reason for the outcome.
Possible enum values:
    - `account_disabled`
      The authorization request was declined because your account is disabled. For more information, please contact us at support-issuing@stripe.com. Replaces the deprecated account_inactive and account_compliance_disabled enums.

    - `card_active`
      The authorization was approved according to your Issuing default settings. Authorization outcome was not driven by real-time auth webhook or spending controls as neither were configured.

    - `card_canceled`
      The authorization request was declined because the card was canceled.

    - `card_expired`
      The authorization request was declined because the card has expired. Documentation for replacing an expired card can be found [here](https://docs.stripe.com/docs/issuing/cards/replacements.md).

    - `card_inactive`
      The authorization request was declined because the card was inactive. To activate the card, refer to our documentation.

    - `cardholder_blocked`
      The authorization request was declined because the cardholder is blocked.

    - `cardholder_inactive`
      The authorization request was declined because the cardholder was inactive. You can activate the cardholder in the dashboard or via the API update endpoint.

    - `cardholder_verification_required`
      The authorization was not approved because the cardholder still required verification. More details can be found by querying the API and obtaining the requirements field of the Cardholder object.

    - `insecure_authorization_method`
      The authorization request was declined because an insecure authorization method was used. The authorization may be retried by inserting the chip into the terminal and/or entering the PIN at the point of sale.

    - `insufficient_funds`
      The authorization request was declined because your account had insufficient funds. Documentation for topping up your Issuing Balance can be found [here](https://docs.stripe.com/docs/issuing/funding/balance.md#top-up-your-issuing-balance).

    - `network_fallback`
      Stripe timed out or encountered an error when responding to the card network. If you have a dedicated BIN and have configured Autopilot, the card network approved or declined the authorization based on your STIP configuration.

    - `not_allowed`
      The charge is not allowed on the Stripe network, possibly because it is an ATM withdrawal or cash advance.

    - `pin_blocked`
      The authorization request was declined because the card’s PIN is blocked. Documentation on managing PINs can be found [here](https://docs.stripe.com/docs/issuing/cards/pin-management.md).

    - `spending_controls`
      The authorization was declined because of your spending controls. Documentation for updating your spending controls can be found [here](https://docs.stripe.com/docs/issuing/controls/spending-controls.md). Replaces the deprecated authorization_controls enum.

    - `suspected_fraud`
      The authorization was suspected to be fraud based on Stripe’s risk controls.

    - `verification_failed`
      The authorization failed required verification checks. See [authorization.verification_data](https://stripe.com/docs/api/issuing/authorizations/object#issuing_authorization_object-verification_data) for more information. Replaces the deprecated authentication_failed, incorrect_cvc, and incorrect_expiry enums.

    - `webhook_approved`
      The authorization was approved via the real-time auth webhook. More details on this can be found [here](https://stripe.com/docs/issuing/controls/real-time-authorizations).

    - `webhook_declined`
      The authorization was declined via the real-time auth webhook. More details on this can be found [here](https://stripe.com/docs/issuing/controls/real-time-authorizations).

    - `webhook_error`
      The response sent through the [real-time auth webhook](https://stripe.com/docs/issuing/controls/real-time-authorizations) is invalid.

    - `webhook_timeout`
      If you are using the [real-time auth webhook](https://stripe.com/docs/issuing/controls/real-time-authorizations), the webhook timed out before we received your authorization decision. Stripe approved or declined the authorization based on what you’ve configured in your Issuing default or [Autopilot](https://stripe.com/docs/issuing/controls/real-time-authorizations#autopilot) settings.

  - `request_history.reason_message` (string, nullable)
    If the `request_history.reason` is `webhook_error` because the direct webhook response is invalid (for example, parsing errors or missing parameters), we surface a more detailed error message via this field.

  - `request_history.requested_at` (timestamp, nullable)
    Time when the card network received an authorization request from the acquirer in UTC. Referred to by networks as transmission time.

- `status` (enum)
  The current status of the authorization in its lifecycle.
Possible enum values:
  - `closed`
    The authorization was declined or [captured](https://docs.stripe.com/docs/issuing/purchases/transactions.md) through one or more [transactions](https://docs.stripe.com/docs/api/issuing/authorizations/object.md#issuing_authorization_object-transactions).

  - `expired`
    The authorization was expired without capture.

  - `pending`
    The authorization was created and is awaiting approval or was approved and is awaiting [capture](https://docs.stripe.com/docs/issuing/purchases/transactions.md).

  - `reversed`
    The authorization was reversed by the merchant.

- `token` (string, nullable)
  [Token](https://docs.stripe.com/docs/api/issuing/tokens/object.md) object used for this authorization. If a network token was not used for this authorization, this field will be null.

- `transactions` (array of objects)
  List of [transactions](https://docs.stripe.com/docs/api/issuing/transactions.md) associated with this authorization.

  - `transactions.id` (string)
    Unique identifier for the object.

  - `transactions.object` (string)
    String representing the object’s type. Objects of the same type share the same value.

  - `transactions.amount` (integer)
    The transaction amount, which will be reflected in your balance. This amount is in your currency and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

  - `transactions.amount_details` (object, nullable)
    Detailed breakdown of amount components. These amounts are denominated in `currency` and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

    - `transactions.amount_details.atm_fee` (integer, nullable)
      The fee charged by the ATM for the cash withdrawal.

    - `transactions.amount_details.cashback_amount` (integer, nullable)
      The amount of cash requested by the cardholder.

  - `transactions.authorization` (string, nullable)
    The `Authorization` object that led to this transaction.

  - `transactions.balance_transaction` (string, nullable)
    ID of the [balance transaction](https://docs.stripe.com/docs/api/balance_transactions.md) associated with this transaction.

  - `transactions.card` (string)
    The card used to make this transaction.

  - `transactions.cardholder` (string, nullable)
    The cardholder to whom this transaction belongs.

  - `transactions.created` (timestamp)
    Time at which the object was created. Measured in seconds since the Unix epoch.

  - `transactions.currency` (enum)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `transactions.dispute` (string, nullable)
    If you’ve disputed the transaction, the ID of the dispute.

  - `transactions.livemode` (boolean)
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

  - `transactions.merchant_amount` (integer)
    The amount that the merchant will receive, denominated in `merchant_currency` and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal). It will be different from `amount` if the merchant is taking payment in a different currency.

  - `transactions.merchant_currency` (enum)
    The currency with which the merchant is taking payment.

  - `transactions.merchant_data` (object)
    Details about the seller (grocery store, e-commerce website, etc.) involved in this transaction.

    - `transactions.merchant_data.category` (string)
      A categorization of the seller’s type of business. See our [merchant categories guide](https://docs.stripe.com/docs/issuing/merchant-categories.md) for a list of possible values.

    - `transactions.merchant_data.category_code` (string)
      The merchant category code for the seller’s business

    - `transactions.merchant_data.city` (string, nullable)
      City where the seller is located

    - `transactions.merchant_data.country` (string, nullable)
      Country where the seller is located

    - `transactions.merchant_data.name` (string, nullable)
      Name of the seller

    - `transactions.merchant_data.network_id` (string)
      Identifier assigned to the seller by the card network. Different card networks may assign different network_id fields to the same merchant.

    - `transactions.merchant_data.postal_code` (string, nullable)
      Postal code where the seller is located

    - `transactions.merchant_data.state` (string, nullable)
      State where the seller is located

    - `transactions.merchant_data.tax_id` (string, nullable)
      The seller’s tax identification number. Currently populated for French merchants only.

    - `transactions.merchant_data.terminal_id` (string, nullable)
      An ID assigned by the seller to the location of the sale.

    - `transactions.merchant_data.url` (string, nullable)
      URL provided by the merchant on a 3DS request

  - `transactions.metadata` (object)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

  - `transactions.network_data` (object, nullable)
    Details about the transaction, such as processing dates, set by the card network.

    - `transactions.network_data.authorization_code` (string, nullable)
      A code created by Stripe which is shared with the merchant to validate the authorization. This field will be populated if the authorization message was approved. The code typically starts with the letter “S”, followed by a six-digit number. For example, “S498162”. Please note that the code is not guaranteed to be unique across authorizations.

    - `transactions.network_data.processing_date` (string, nullable)
      The date the transaction was processed by the card network. This can be different from the date the seller recorded the transaction depending on when the acquirer submits the transaction to the network.

    - `transactions.network_data.transaction_id` (string, nullable)
      Unique identifier for the authorization assigned by the card network used to match subsequent messages, disputes, and transactions.

  - `transactions.purchase_details` (object, nullable)
    Additional purchase information that is optionally provided by the merchant.

    - `transactions.purchase_details.fleet` (object, nullable)
      Fleet-specific information for transactions using Fleet cards.

      - `transactions.purchase_details.fleet.cardholder_prompt_data` (object, nullable)
        Answers to prompts presented to cardholder at point of sale.

        - `transactions.purchase_details.fleet.cardholder_prompt_data.driver_id` (string, nullable)
          Driver ID.

        - `transactions.purchase_details.fleet.cardholder_prompt_data.odometer` (integer, nullable)
          Odometer reading.

        - `transactions.purchase_details.fleet.cardholder_prompt_data.unspecified_id` (string, nullable)
          An alphanumeric ID. This field is used when a vehicle ID, driver ID, or generic ID is entered by the cardholder, but the merchant or card network did not specify the prompt type.

        - `transactions.purchase_details.fleet.cardholder_prompt_data.user_id` (string, nullable)
          User ID.

        - `transactions.purchase_details.fleet.cardholder_prompt_data.vehicle_number` (string, nullable)
          Vehicle number.

      - `transactions.purchase_details.fleet.purchase_type` (string, nullable)
        The type of purchase. One of `fuel_purchase`, `non_fuel_purchase`, or `fuel_and_non_fuel_purchase`.

      - `transactions.purchase_details.fleet.reported_breakdown` (object, nullable)
        More information about the total amount. This information is not guaranteed to be accurate as some merchants may provide unreliable data.

        - `transactions.purchase_details.fleet.reported_breakdown.fuel` (object, nullable)
          Breakdown of fuel portion of the purchase.

          - `transactions.purchase_details.fleet.reported_breakdown.fuel.gross_amount_decimal` (decimal string, nullable)
            Gross fuel amount that should equal Fuel Volume multipled by Fuel Unit Cost, inclusive of taxes.

        - `transactions.purchase_details.fleet.reported_breakdown.non_fuel` (object, nullable)
          Breakdown of non-fuel portion of the purchase.

          - `transactions.purchase_details.fleet.reported_breakdown.non_fuel.gross_amount_decimal` (decimal string, nullable)
            Gross non-fuel amount that should equal the sum of the line items, inclusive of taxes.

        - `transactions.purchase_details.fleet.reported_breakdown.tax` (object, nullable)
          Information about tax included in this transaction.

          - `transactions.purchase_details.fleet.reported_breakdown.tax.local_amount_decimal` (decimal string, nullable)
            Amount of state or provincial Sales Tax included in the transaction amount. Null if not reported by merchant or not subject to tax.

          - `transactions.purchase_details.fleet.reported_breakdown.tax.national_amount_decimal` (decimal string, nullable)
            Amount of national Sales Tax or VAT included in the transaction amount. Null if not reported by merchant or not subject to tax.

      - `transactions.purchase_details.fleet.service_type` (string, nullable)
        The type of fuel service. One of `non_fuel_transaction`, `full_service`, or `self_service`.

    - `transactions.purchase_details.flight` (object, nullable)
      Information about the flight that was purchased with this transaction.

      - `transactions.purchase_details.flight.departure_at` (integer, nullable)
        The time that the flight departed.

      - `transactions.purchase_details.flight.passenger_name` (string, nullable)
        The name of the passenger.

      - `transactions.purchase_details.flight.refundable` (boolean, nullable)
        Whether the ticket is refundable.

      - `transactions.purchase_details.flight.segments` (array of objects, nullable)
        The legs of the trip.

        - `transactions.purchase_details.flight.segments.arrival_airport_code` (string, nullable)
          The three-letter IATA airport code of the flight’s destination.

        - `transactions.purchase_details.flight.segments.carrier` (string, nullable)
          The airline carrier code.

        - `transactions.purchase_details.flight.segments.departure_airport_code` (string, nullable)
          The three-letter IATA airport code that the flight departed from.

        - `transactions.purchase_details.flight.segments.flight_number` (string, nullable)
          The flight number.

        - `transactions.purchase_details.flight.segments.service_class` (string, nullable)
          The flight’s service class.

        - `transactions.purchase_details.flight.segments.stopover_allowed` (boolean, nullable)
          Whether a stopover is allowed on this flight.

      - `transactions.purchase_details.flight.travel_agency` (string, nullable)
        The travel agency that issued the ticket.

    - `transactions.purchase_details.fuel` (object, nullable)
      Information about fuel that was purchased with this transaction.

      - `transactions.purchase_details.fuel.industry_product_code` (string, nullable)
        [Conexxus Payment System Product Code](https://www.conexxus.org/conexxus-payment-system-product-codes) identifying the primary fuel product purchased.

      - `transactions.purchase_details.fuel.quantity_decimal` (decimal string, nullable)
        The quantity of `unit`s of fuel that was dispensed, represented as a decimal string with at most 12 decimal places.

      - `transactions.purchase_details.fuel.type` (string)
        The type of fuel that was purchased. One of `diesel`, `unleaded_plus`, `unleaded_regular`, `unleaded_super`, or `other`.

      - `transactions.purchase_details.fuel.unit` (string)
        The units for `quantity_decimal`. One of `charging_minute`, `imperial_gallon`, `kilogram`, `kilowatt_hour`, `liter`, `pound`, `us_gallon`, or `other`.

      - `transactions.purchase_details.fuel.unit_cost_decimal` (decimal string)
        The cost in cents per each unit of fuel, represented as a decimal string with at most 12 decimal places.

    - `transactions.purchase_details.lodging` (object, nullable)
      Information about lodging that was purchased with this transaction.

      - `transactions.purchase_details.lodging.check_in_at` (integer, nullable)
        The time of checking into the lodging.

      - `transactions.purchase_details.lodging.nights` (integer, nullable)
        The number of nights stayed at the lodging.

    - `transactions.purchase_details.receipt` (array of objects, nullable)
      The line items in the purchase.

      - `transactions.purchase_details.receipt.description` (string, nullable)
        The description of the item. The maximum length of this field is 26 characters.

      - `transactions.purchase_details.receipt.quantity` (float, nullable)
        The quantity of the item.

      - `transactions.purchase_details.receipt.total` (integer, nullable)
        The total for this line item in cents.

      - `transactions.purchase_details.receipt.unit_cost` (integer, nullable)
        The unit cost of the item in cents.

    - `transactions.purchase_details.reference` (string, nullable)
      A merchant-specific order number.

  - `transactions.token` (string, nullable)
    [Token](https://docs.stripe.com/docs/api/issuing/tokens/object.md) object used for this transaction. If a network token was not used for this transaction, this field will be null.

  - `transactions.type` (enum)
    The nature of the transaction.
Possible enum values:
    - `capture`
      Funds were captured by the acquirer. `amount` will be negative because funds are moving out of your balance. Not all captures will be linked to an authorization, as acquirers [can force capture in some cases](https://stripe.com/docs/issuing/purchases/transactions).

    - `refund`
      An acquirer initiated a refund. This transaction might not be linked to an original capture, for example credits are original transactions. `amount` will be positive for refunds and negative for refund reversals (very rare).

  - `transactions.wallet` (enum, nullable)
    The digital wallet used for this transaction. One of `apple_pay`, `google_pay`, or `samsung_pay`.

- `verification_data` (object)
  Verifications that Stripe performed on information that the cardholder provided to the merchant.

  - `verification_data.address_line1_check` (enum)
    Whether the cardholder provided an address first line and if it matched the cardholder’s `billing.address.line1`.
Possible enum values:
    - `match`
      Verification succeeded, values matched.

    - `mismatch`
      Verification failed, values didn’t match.

    - `not_provided`
      Verification was not performed because no value was provided.

  - `verification_data.address_postal_code_check` (enum)
    Whether the cardholder provided a postal code and if it matched the cardholder’s `billing.address.postal_code`.
Possible enum values:
    - `match`
      Verification succeeded, values matched.

    - `mismatch`
      Verification failed, values didn’t match.

    - `not_provided`
      Verification was not performed because no value was provided.

  - `verification_data.authentication_exemption` (object, nullable)
    The exemption applied to this authorization.

    - `verification_data.authentication_exemption.claimed_by` (enum)
      The entity that requested the exemption, either the acquiring merchant or the Issuing user.
Possible enum values:
      - `acquirer`
        Acquiring merchant.

      - `issuer`
        Issuing user.

    - `verification_data.authentication_exemption.type` (enum)
      The specific exemption claimed for this authorization.
Possible enum values:
      - `low_value_transaction`
        Specifies an exemption for some low-value authorizations.

      - `transaction_risk_analysis`
        Specifies an exemption for low-risk authorizations, determined using real-time risk analysis.

      - `unknown`
        Specifies an unknown exemption type.

  - `verification_data.cvc_check` (enum)
    Whether the cardholder provided a CVC and if it matched Stripe’s record.
Possible enum values:
    - `match`
      Verification succeeded, values matched.

    - `mismatch`
      Verification failed, values didn’t match.

    - `not_provided`
      Verification was not performed because no value was provided.

  - `verification_data.expiry_check` (enum)
    Whether the cardholder provided an expiry date and if it matched Stripe’s record.
Possible enum values:
    - `match`
      Verification succeeded, values matched.

    - `mismatch`
      Verification failed, values didn’t match.

    - `not_provided`
      Verification was not performed because no value was provided.

  - `verification_data.postal_code` (string, nullable)
    The postal code submitted as part of the authorization used for postal code verification.

  - `verification_data.three_d_secure` (object, nullable)
    3D Secure details.

    - `verification_data.three_d_secure.result` (enum)
      The outcome of the 3D Secure authentication request.
Possible enum values:
      - `attempt_acknowledged`
        The merchant attempted to authenticate the authorization, but the cardholder is not enrolled or was unable to reach Stripe.

      - `authenticated`
        Authentication successful.

      - `failed`
        Authentication failed.

      - `required`
        The authorization was declined because regulatory requirements mandated an authentication for this transaction but it wasn’t submitted correctly by the merchant, and they didn’t claim an applicable exemption. Check out our [3DS documentation](https://stripe.com/docs/issuing/3d-secure#prevent-fraud) if you want to learn more.

- `verified_by_fraud_challenge` (boolean, nullable)
  Whether the authorization bypassed fraud risk checks because the cardholder has previously completed a fraud challenge on a similar high-risk authorization from the same merchant.

- `wallet` (string, nullable)
  The digital wallet used for this transaction. One of `apple_pay`, `google_pay`, or `samsung_pay`. Will populate as `null` when no digital wallet was utilized.

### The Authorization object

```json
{
  "id": "iauth_1JVXl82eZvKYlo2CPIiWlzrn",
  "object": "issuing.authorization",
  "amount": 382,
  "amount_details": {
    "atm_fee": null
  },
  "approved": false,
  "authorization_method": "online",
  "balance_transactions": [],
  "card": {
    "id": "ic_1JDmgz2eZvKYlo2CRXlTsXj6",
    "object": "issuing.card",
    "brand": "Visa",
    "cancellation_reason": null,
    "cardholder": {
      "id": "ich_1JDmfb2eZvKYlo2CwHUgaAxU",
      "object": "issuing.cardholder",
      "billing": {
        "address": {
          "city": "San Francisco",
          "country": "US",
          "line1": "123 Main Street",
          "line2": null,
          "postal_code": "94111",
          "state": "CA"
        }
      },
      "company": null,
      "created": 1626425119,
      "email": "jenny.rosen@example.com",
      "individual": null,
      "livemode": false,
      "metadata": {},
      "name": "Jenny Rosen",
      "phone_number": "+18008675309",
      "redaction": null,
      "requirements": {
        "disabled_reason": null,
        "past_due": []
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
    "created": 1626425206,
    "currency": "usd",
    "exp_month": 6,
    "exp_year": 2024,
    "last4": "8693",
    "livemode": false,
    "metadata": {},
    "redaction": null,
    "replaced_by": null,
    "replacement_for": null,
    "replacement_reason": null,
    "shipping": null,
    "spending_controls": {
      "allowed_categories": null,
      "blocked_categories": null,
      "spending_limits": [
        {
          "amount": 50000,
          "categories": [],
          "interval": "daily"
        }
      ],
      "spending_limits_currency": "usd"
    },
    "status": "active",
    "type": "virtual",
    "wallets": {
      "apple_pay": {
        "eligible": true,
        "ineligible_reason": null
      },
      "google_pay": {
        "eligible": true,
        "ineligible_reason": null
      },
      "primary_account_identifier": null
    }
  },
  "cardholder": "ich_1JDmfb2eZvKYlo2CwHUgaAxU",
  "created": 1630657706,
  "currency": "usd",
  "livemode": false,
  "merchant_amount": 382,
  "merchant_currency": "usd",
  "merchant_data": {
    "category": "computer_software_stores",
    "category_code": "5734",
    "city": "SAN FRANCISCO",
    "country": "US",
    "name": "STRIPE",
    "network_id": "1234567890",
    "postal_code": "94103",
    "state": "CA"
  },
  "metadata": {
    "order_id": "6735"
  },
  "network_data": null,
  "pending_request": null,
  "redaction": null,
  "request_history": [
    {
      "amount": 382,
      "amount_details": {
        "atm_fee": null
      },
      "approved": false,
      "created": 1630657706,
      "currency": "usd",
      "merchant_amount": 382,
      "merchant_currency": "usd",
      "reason": "verification_failed",
      "reason_message": null
    }
  ],
  "status": "closed",
  "transactions": [],
  "verification_data": {
    "address_line1_check": "not_provided",
    "address_postal_code_check": "not_provided",
    "cvc_check": "mismatch",
    "expiry_check": "match"
  },
  "wallet": null
}
```