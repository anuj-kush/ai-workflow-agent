############# 1. the First workflow


(venv) C:\Users\Anuj Kushwaha\ai-workflow-agent>python -m app.main 
============================================================
AI Workflow Automation System
============================================================

Loaded 10 workflows.

Enter your request: "Which products need restocking?"
Direct use of automatic function calling (AFC) in Models.generate_content is not recommended. Instead, we recommend to use AFC in Chat.send_message. Similarly, direct use of AFC in Models.generate_content_stream is not recommended. Instead, we recommend to use AFC in Chat.send_message_stream.

============================================================
WORKFLOW SELECTION
============================================================

Workflow ID: WF001
Confidence: 1.00
Reason: The user is asking which products need restocking, which directly matches the Inventory Restock Check workflow.
Extracted Inputs: {}

Selected Workflow:
WF001 - Inventory Restock Check

============================================================
EXECUTION PLAN
============================================================

Step 1: Load inventory
Tool: load_inventory

Step 2: compare current stock with minimum threshold
Tool: check_stock

Step 3: identify low-stock products
Tool: identify_low_stock_products

Step 4: calculate reorder quantity
Tool: calculate_reorder_quantity

Step 5: generate restock list
Tool: generate_restock_list

============================================================
EXECUTION RESULT
============================================================

Status: success

Step 1
Name: Load inventory
Tool: load_inventory
Status: success
Output: {'message': 'Inventory loaded successfully.', 'records': 5}

Step 2
Name: compare current stock with minimum threshold
Tool: check_stock
Status: success
Output: {'message': 'Stock levels checked.', 'low_stock_count': 3}

Step 3
Name: identify low-stock products
Tool: identify_low_stock_products
Status: success
Output: {'message': 'Low-stock products identified.', 'products': [{'sku': 'P001', 'product_name': 'Blue Cotton Shirt', 'current_stock': 8, 'minimum_stock': 20}, {'sku': 'P003', 'product_name': 'Running Shoes', 'current_stock': 5, 'minimum_stock': 15}, {'sku': 'P005', 'product_name': 'Cotton Hoodie', 'current_stock': 10, 'minimum_stock': 25}]}

Step 4
Name: calculate reorder quantity
Tool: calculate_reorder_quantity
Status: success
Output: {'message': 'Reorder quantities calculated.', 'products': [{'sku': 'P001', 'product_name': 'Blue Cotton Shirt', 'current_stock': 8, 'minimum_stock': 20, 'reorder_quantity': 12}, {'sku': 'P003', 'product_name': 'Running Shoes', 'current_stock': 5, 'minimum_stock': 15, 'reorder_quantity': 10}, {'sku': 'P005', 'product_name': 'Cotton Hoodie', 'current_stock': 10, 'minimum_stock': 25, 'reorder_quantity': 15}]}

Step 5
Name: generate restock list
Tool: generate_restock_list
Status: success
Output: {'restock_list': [{'sku': 'P001', 'product_name': 'Blue Cotton Shirt', 'current_stock': 8, 'minimum_stock': 20, 'reorder_quantity': 12}, {'sku': 'P003', 'product_name': 'Running Shoes', 'current_stock': 5, 'minimum_stock': 15, 'reorder_quantity': 10}, {'sku': 'P005', 'product_name': 'Cotton Hoodie', 'current_stock': 10, 'minimum_stock': 25, 'reorder_quantity': 15}]}

============================================================
DECISION RESULT
============================================================
{'decision': 'restock_required', 'count': 3}

============================================================
FINAL OUTPUT
============================================================
[{'sku': 'P001', 'product_name': 'Blue Cotton Shirt', 'current_stock': 8, 'minimum_stock': 20, 'reorder_quantity': 12}, {'sku': 'P003', 'product_name': 'Running Shoes', 'current_stock': 5, 'minimum_stock': 15, 'reorder_quantity'############# 1. the First workflow: 10}, {'sku': 'P005', 'product_name': 'Cotton Hoodie', 'current_stock': 10, 'minimum_stock': 25, 'reorder_quantity': 15}] (venv) C:\Users\Anuj Kushwaha\ai-workflow-agent>python -m app.main 
============================================================
AI Workflow Automation System
============================================================

Loaded 10 workflows.

Enter your request: "Find products where vendor price differs by more than 10%."
Direct use of automatic function calling (AFC) in Models.generate_content is not recommended. Instead, we recommend to use AFC in Chat.send_message. Similarly, direct use of AFC in Models.generate_content_stream is not recommended. Instead, we recommend to use AFC in Chat.send_message_stream.

============================================================
WORKFLOW SELECTION
============================================================

Workflow ID: WF002
Confidence: 0.95
Reason: User asks to validate product prices against vendor price list.
Extracted Inputs: {}

Selected Workflow:
WF002 - Product Price Validation

============================================================
EXECUTION PLAN
============================================================

Step 1: Load product prices
Tool: load_product_prices

Step 2: load vendor prices
Tool: load_vendor_prices

Step 3: match products by SKU
Tool: match_product_prices

Step 4: compare internal and vendor prices
Tool: compare_product_prices

Step 5: calculate percentage difference
Tool: calculate_price_difference

Step 6: flag exceptions
Tool: generate_price_validation_report

============================================================
EXECUTION RESULT
============================================================

Status: success

Step 1
Name: Load product prices
Tool: load_product_prices
Status: success
Output: {'message': 'Product prices loaded successfully.', 'records': 5}

Step 2
Name: load vendor prices
Tool: load_vendor_prices
Status: success
Output: {'message': 'Vendor prices loaded successfully.', 'records': 5}

Step 3
Name: match products by SKU
Tool: match_product_prices
Status: success
Output: {'message': 'Product and vendor prices matched.', 'matched_records': 5}

Step 4
Name: compare internal and vendor prices
Tool: compare_product_prices
Status: success
Output: {'message': 'Internal and vendor prices compared.', 'records': 5}

Step 5
Name: calculate percentage difference
Tool: calculate_price_difference
Status: success
Output: {'message': 'Percentage price differences calculated.', 'records': 5}

Step 6
Name: flag exceptions
Tool: generate_price_validation_report
Status: success
Output: {'validation_report': [{'sku': 'P001', 'product_name': 'Blue Cotton Shirt', 'internal_price': 25, 'vendor_price': 27, 'difference': 2, 'difference_percentage': 8.0, 'exception': False}, {'sku': 'P002', 'product_name': 'Black Jeans', 'internal_price': 40, 'vendor_price': 44, 'difference': 4, 'difference_percentage': 10.0, 'exception': False}, {'sku': 'P003', 'product_name': 'Running Shoes', 'internal_price': 60, 'vendor_price': 58, 'difference': -2, 'difference_percentage': 3.3333333333333335, 'exception': False}, {'sku': 'P004', 'product_name': 'White T Shirt', 'internal_price': 18, 'vendor_price': 20, 'difference': 2, 'difference_percentage': 11.11111111111111, 'exception': True}, {'sku': 'P005', 'product_name': 'Cotton Hoodie', 'internal_price': 35, 'vendor_price': 40, 'difference': 5, 'difference_percentage': 14.285714285714285, 'exception': True}]}

============================================================
DECISION RESULT
============================================================
{'decision': 'exceptions_found', 'exception_count': 2}

============================================================
FINAL OUTPUT
============================================================
[{'sku': 'P001', 'product_name': 'Blue Cotton Shirt', 'internal_price': 25, 'vendor_price': 27, 'difference': 2, 'difference_percentage': 8.0, 'exception': False}, {'sku': 'P002', 'product_name': 'Black Jeans', 'internal_price': 40, 'vendor_price': 44, 'difference': 4, 'difference_percentage': 10.0, 'exception': False}, {'sku': 'P003', 'product_name': 'Running Shoes', 'internal_price': 60, 'vendor_price': 58, 'difference': -2, 'difference_percentage': 3.3333333333333335, 'exception': False}, {'sku': 'P004', 'product_name': 'White T Shirt', 'internal_price': 18, 'vendor_price': 20, 'difference': 2, 'difference_percentage': 11.11111111111111, 'exception': True}, {'sku': 'P005', 'product_name': 'Cotton Hoodie', 'internal_price': 35, 'vendor_price': 40, 'difference': 5, 'difference_percentage': 14.285714285714285, 'exception': True}]



############# 2. the Second workflow


(venv) C:\Users\Anuj Kushwaha\ai-workflow-agent>python -m app.main 
============================================================
AI Workflow Automation System
============================================================

Loaded 10 workflows.

Enter your request: "Process this vendor spreadsheet and show invalid rows."
Direct use of automatic function calling (AFC) in Models.generate_content is not recommended. Instead, we recommend to use AFC in Chat.send_message. Similarly, direct use of AFC in Models.generate_content_stream is not recommended. Instead, we recommend to use AFC in Chat.send_message_stream.

============================================================
WORKFLOW SELECTION
============================================================

Workflow ID: WF003
Confidence: 0.95
Reason: User provided a vendor spreadsheet for processing and wants to see invalid rows.
Extracted Inputs: {}

Selected Workflow:
WF003 - Vendor File Processing

============================================================
EXECUTION PLAN
============================================================

Step 1: Read vendor file
Tool: read_vendor_file

Step 2: detect columns
Tool: detect_vendor_columns

Step 3: normalize column names
Tool: normalize_vendor_columns

Step 4: validate required fields
Tool: validate_vendor_fields

Step 5: identify invalid rows
Tool: identify_invalid_vendor_rows

Step 6: produce cleaned dataset
Tool: create_cleaned_vendor_dataset

============================================================
EXECUTION RESULT
============================================================

Status: success

Step 1
Name: Read vendor file
Tool: read_vendor_file
Status: success
Output: {'message': 'Vendor file loaded.', 'records': 5}

Step 2
Name: detect columns
Tool: detect_vendor_columns
Status: success
Output: {'columns': ['SKU', 'Product Name', 'Category', 'Price', 'Material']}

Step 3
Name: normalize column names
Tool: normalize_vendor_columns
Status: success
Output: {'message': 'Vendor columns normalized.', 'columns': ['sku', 'product_name', 'category', 'price', 'material']}

Step 4
Name: validate required fields
Tool: validate_vendor_fields
Status: success
Output: {'message': 'Required vendor fields are present.'}

Step 5
Name: identify invalid rows
Tool: identify_invalid_vendor_rows
Status: success
Output: {'invalid_rows': 2}

Step 6
Name: produce cleaned dataset
Tool: create_cleaned_vendor_dataset
Status: success
Output: {'cleaned_records': 3, 'invalid_records': 2, 'invalid_rows': [{'sku': nan, 'product_name': 'Running Shoes', 'category': 'Footwear', 'price': 60, 'material': 'Mesh', 'is_invalid': True}, {'sku': 'V004', 'product_name': nan, 'category': 'T-Shirts', 'price': 18, 'material': 'Cotton', 'is_invalid': True}]}

============================================================
DECISION RESULT
============================================================
{'decision': 'invalid_rows_found', 'invalid_count': 2}

============================================================
FINAL OUTPUT
============================================================
{'cleaned_records': 3, 'invalid_records': 2, 'invalid_rows': [{'sku': nan, 'product_name': 'Running Shoes', 'category': 'Footwear', 'price': 60, 'material': 'Mesh', 'is_invalid': True}, {'sku': 'V004', 'product_name': nan, 'category': 'T-Shirts', 'price': 18, 'material': 'Cotton', 'is_invalid': True}]}



############# 3. the Third workflow


(venv) C:\Users\Anuj Kushwaha\ai-workflow-agent>python -m app.main 
============================================================
AI Workflow Automation System
============================================================

Loaded 10 workflows.

Enter your request: "Generate SEO content for this product."
Direct use of automatic function calling (AFC) in Models.generate_content is not recommended. Instead, we recommend to use AFC in Chat.send_message. Similarly, direct use of AFC in Models.generate_content_stream is not recommended. Instead, we recommend to use AFC in Chat.send_message_stream.

============================================================
WORKFLOW SELECTION
============================================================

Workflow ID: WF004
Confidence: 0.95
Reason: User asked to generate SEO content for a product, matching the Product Description Generator workflow.
Extracted Inputs: {}

Selected Workflow:
WF004 - Product Description Generator

============================================================
EXECUTION PLAN
============================================================

Step 1: Validate required attributes
Tool: validate_product_attributes

Step 2: create product description
Tool: generate_product_description

Step 3: generate short description
Tool: generate_short_description

Step 4: generate SEO title
Tool: generate_seo_title

Step 5: generate meta description
Tool: generate_meta_description

============================================================
EXECUTION RESULT
============================================================

Status: success

Step 1
Name: Validate required attributes
Tool: validate_product_attributes
Status: success
Output: {'message': 'Product attributes validated.', 'product_name': 'Blue Cotton Shirt'}

Step 2
Name: create product description
Tool: generate_product_description
Status: success
Output: {'description_generated': True}

Step 3
Name: generate short description
Tool: generate_short_description
Status: success
Output: {'short_description_generated': True}

Step 4
Name: generate SEO title
Tool: generate_seo_title
Status: success
Output: {'seo_title_generated': True}

Step 5
Name: generate meta description
Tool: generate_meta_description
Status: success
Output: {'product_content': '{\n    "description": "Upgrade your work wardrobe with the Blue Cotton Shirt, designed specifically for young professionals. Crafted from high-quality cotton, this blue shirt offers both style and comfort for your daily office needs. Additional product features and specifications are not provided.",\n    "short_description": "A stylish blue cotton shirt for young professionals. Material and color details are provided; other information is not provided.",\n    "seo_title": "Blue Cotton Shirt for Young Professionals",\n    "meta_description": "Shop the Blue Cotton Shirt made for young professionals. Comfortable cotton material in a stylish blue color. Other details are not provided.",\n    "category": "Shirts",\n    "material": "Cotton",\n    "color": "Blue",\n    "target_audience": "Young professionals"\n}'}

============================================================
DECISION RESULT
============================================================
{'decision': 'attributes_complete', 'missing_attributes': []}

============================================================
FINAL OUTPUT
============================================================
{'product_content': '{\n    "description": "Upgrade your work wardrobe with the Blue Cotton Shirt, designed specifically for young professionals. Crafted from high-quality cotton, this blue shirt offers both style and comfort for your daily office needs. Additional product features and specifications are not provided.",\n    "short_description": "A stylish blue cotton shirt for young professionals. Material and color details are provided; other information is not provided.",\n    "seo_title": "Blue Cotton Shirt for Young Professionals",\n    "meta_description": "Shop the Blue Cotton Shirt made for young professionals. Comfortable cotton material in a stylish blue color. Other details are not provided.",\n    "category": "Shirts",\n    "material": "Cotton",\n    "color": "Blue",\n    "target_audience": "Young professionals"\n}'}



############# 4. the Fourth workflow


(venv) C:\Users\Anuj Kushwaha\ai-workflow-agent>python -m app.main 
============================================================
AI Workflow Automation System
============================================================

Loaded 10 workflows.

Enter your request: "Where is order ORD-1001?"
Direct use of automatic function calling (AFC) in Models.generate_content is not recommended. Instead, we recommend to use AFC in Chat.send_message. Similarly, direct use of AFC in Models.generate_content_stream is not recommended. Instead, we recommend to use AFC in Chat.send_message_stream.

============================================================
WORKFLOW SELECTION
============================================================

Workflow ID: WF005
Confidence: 0.99
Reason: The user is asking for the location/status of a specific order ID.
Extracted Inputs: {'order_id': 'ORD-1001'}

Selected Workflow:
WF005 - Customer Order Status

============================================================
EXECUTION PLAN
============================================================

Step 1: Validate identifier
Tool: validate_order_identifier

Step 2: search order data
Tool: search_order

Step 3: retrieve order status
Tool: get_order_status

Step 4: retrieve shipment information
Tool: get_shipment_information

Step 5: summarize current status
Tool: summarize_order_status

============================================================
EXECUTION RESULT
============================================================

Status: success

Step 1
Name: Validate identifier
Tool: validate_order_identifier
Status: success
Output: {'message': 'Order identifier validated.', 'order_id': 'ORD-1001', 'customer_email': None}

Step 2
Name: search order data
Tool: search_order
Status: success
Output: {'message': 'Order found.', 'order': {'order_id': 'ORD-1001', 'customer_email': 'customer1@example.com', 'customer_name': 'Rahul', 'items': 'Blue Cotton Shirt, Black Jeans', 'status': 'Shipped'}}

Step 3
Name: retrieve order status
Tool: get_order_status
Status: success
Output: {'status': 'Shipped'}

Step 4
Name: retrieve shipment information
Tool: get_shipment_information
Status: success
Output: {'shipment': {'order_id': 'ORD-1001', 'shipment_status': 'In Transit', 'tracking_number': 'TRK10001', 'carrier': 'DemoExpress'}}

Step 5
Name: summarize current status
Tool: summarize_order_status
Status: success
Output: {'order_id': 'ORD-1001', 'customer': 'Rahul', 'items': 'Blue Cotton Shirt, Black Jeans', 'order_status': 'Shipped', 'shipment_status': 'In Transit', 'tracking_number': 'TRK10001', 'carrier': 'DemoExpress'}

============================================================
DECISION RESULT
============================================================
{'decision': 'order_found'}

============================================================
FINAL OUTPUT
============================================================
{'order_id': 'ORD-1001', 'customer': 'Rahul', 'items': 'Blue Cotton Shirt, Black Jeans', 'order_status': 'Shipped', 'shipment_status': 'In Transit', 'tracking_number': 'TRK10001', 'carrier': 'DemoExpress'}



############# 5. the Fifth workflow
(venv) C:\Users\Anuj Kushwaha\ai-workflow-agent>python -m app.main 
============================================================
AI Workflow Automation System
============================================================

Loaded 10 workflows.

Enter your request: "Find likely duplicate products in the catalog."
Direct use of automatic function calling (AFC) in Models.generate_content is not recommended. Instead, we recommend to use AFC in Chat.send_message. Similarly, direct use of AFC in Models.generate_content_stream is not recommended. Instead, we recommend to use AFC in Chat.send_message_stream.

============================================================
WORKFLOW SELECTION
============================================================

Workflow ID: WF006
Confidence: 0.95
Reason: The user is asking to find duplicate products in the catalog.
Extracted Inputs: {}

Selected Workflow:
WF006 - Duplicate Product Detection

============================================================
EXECUTION PLAN
============================================================

Step 1: Load product catalog
Tool: load_product_catalog

Step 2: normalize names and SKUs
Tool: normalize_product_identifiers

Step 3: compare identifiers
Tool: compare_product_identifiers

Step 4: compare product attributes
Tool: compare_product_attributes

Step 5: group likely duplicates
Tool: group_duplicate_products

Step 6: assign confidence
Tool: assign_duplicate_confidence

============================================================
EXECUTION RESULT
============================================================

Status: success

Step 1
Name: Load product catalog
Tool: load_product_catalog
Status: success
Output: {'message': 'Product catalog loaded.', 'records': 5}

Step 2
Name: normalize names and SKUs
Tool: normalize_product_identifiers
Status: success
Output: {'message': 'Product identifiers normalized.'}

Step 3
Name: compare identifiers
Tool: compare_product_identifiers
Status: success
Output: {'duplicate_sku_records': 0}

Step 4
Name: compare product attributes
Tool: compare_product_attributes
Status: success
Output: {'possible_duplicate_groups': 1}

Step 5
Name: group likely duplicates
Tool: group_duplicate_products
Status: success
Output: {'duplicate_groups': [{'type': 'attribute_similarity', 'confidence': 'possible', 'products': [{'sku': 'P001', 'product_name': 'Blue Cotton Shirt', 'category': 'Shirts', 'material': 'Cotton', 'color': 'Blue'}, {'sku': 'P002', 'product_name': 'Blue Cotton Shirt', 'category': 'Shirts', 'material': 'Cotton', 'color': 'Blue'}]}]}

Step 6
Name: assign confidence
Tool: assign_duplicate_confidence
Status: success
Output: {'duplicate_groups': [{'type': 'attribute_similarity', 'confidence': 'possible', 'products': [{'sku': 'P001', 'product_name': 'Blue Cotton Shirt', 'category': 'Shirts', 'material': 'Cotton', 'color': 'Blue'}, {'sku': 'P002', 'product_name': 'Blue Cotton Shirt', 'category': 'Shirts', 'material': 'Cotton', 'color': 'Blue'}]}], 'total_groups': 1}

============================================================
DECISION RESULT
============================================================
{'decision': 'duplicates_found', 'count': 1}

============================================================
FINAL OUTPUT
============================================================
{'duplicate_groups': [{'type': 'attribute_similarity', 'confidence': 'possible', 'products': [{'sku': 'P001', 'product_name': 'Blue Cotton Shirt', 'category': 'Shirts', 'material': 'Cotton', 'color': 'Blue'}, {'sku': 'P002', 'product_name': 'Blue Cotton Shirt', 'category': 'Shirts', 'material': 'Cotton', 'color': 'Blue'}]}], 'total_groups': 1}



############# 6. the sixth workflow
(venv) C:\Users\Anuj Kushwaha\ai-workflow-agent>python -m app.main 
============================================================
AI Workflow Automation System
============================================================

Loaded 10 workflows.

Enter your request: "Create a campaign brief for the new collection."
Direct use of automatic function calling (AFC) in Models.generate_content is not recommended. Instead, we recommend to use AFC in Chat.send_message. Similarly, direct use of AFC in Models.generate_content_stream is not recommended. Instead, we recommend to use AFC in Chat.send_message_stream.

============================================================
WORKFLOW SELECTION
============================================================

Workflow ID: WF007
Confidence: 0.95
Reason: The user is asking to create a campaign brief for a new collection.
Extracted Inputs: {'campaign_goal': 'new collection'}

Selected Workflow:
WF007 - Marketing Campaign Brief

============================================================
EXECUTION PLAN
============================================================

Step 1: Validate inputs
Tool: validate_campaign_inputs

Step 2: identify campaign objective
Tool: identify_campaign_objective

Step 3: summarize products
Tool: summarize_campaign_products

Step 4: create messaging
Tool: generate_campaign_messaging

Step 5: create channel recommendations
Tool: generate_channel_recommendations

Step 6: create campaign checklist
Tool: generate_campaign_checklist

============================================================
EXECUTION RESULT
============================================================

Status: needs_input

Step 1
Name: Validate inputs
Tool: validate_campaign_inputs
Status: needs_input
Output: {'status': 'missing_information', 'message': 'Before I can create the campaign brief, please provide: campaign dates.', 'missing_inputs': ['campaign dates']}

============================================================
ADDITIONAL INFORMATION REQUIRED
============================================================
Before I can create the campaign brief, please provide: campaign dates.



############# 7. the seventh workflow


(venv) C:\Users\Anuj Kushwaha\ai-workflow-agent>python -m app.main "Create a campaign brief for the new collection. The campaign goal is to launch our new collection and increase sales. The campaign dates are October 15 to October 31. Target audience is online shoppers. Promotion is 20% off."
============================================================
AI Workflow Automation System
============================================================

Loaded 10 workflows.

Enter your request: "Create a campaign brief for the new collection. The campaign goal is to launch our new collection and increase sales. The campaign dates are October 15 to October 31. Target audience is online shoppers. Promotion is 20% off."
Direct use of automatic function calling (AFC) in Models.generate_content is not recommended. Instead, we recommend to use AFC in Chat.send_message. Similarly, direct use of AFC in Models.generate_content_stream is not recommended. Instead, we recommend to use AFC in Chat.send_message_stream.

============================================================
WORKFLOW SELECTION
============================================================

Workflow ID: WF007
Confidence: 0.98
Reason: User requested to create a campaign brief with explicit goal, audience, promotion, and dates.
Extracted Inputs: {'campaign_goal': 'launch our new collection and increase sales', 'target_audience': 'online shoppers', 'promotion': '20% off', 'dates': 'October 15 to October 31'}

Selected Workflow:
WF007 - Marketing Campaign Brief

============================================================
EXECUTION PLAN
============================================================

Step 1: Validate inputs
Tool: validate_campaign_inputs

Step 2: identify campaign objective
Tool: identify_campaign_objective

Step 3: summarize products
Tool: summarize_campaign_products

Step 4: create messaging
Tool: generate_campaign_messaging

Step 5: create channel recommendations
Tool: generate_channel_recommendations

Step 6: create campaign checklist
Tool: generate_campaign_checklist

============================================================
EXECUTION RESULT
============================================================

Status: success

Step 1
Name: Validate inputs
Tool: validate_campaign_inputs
Status: success
Output: {'status': 'validated', 'message': 'Campaign inputs validated.'}

Step 2
Name: identify campaign objective
Tool: identify_campaign_objective
Status: success
Output: {'objective': 'launch our new collection and increase sales'}

Step 3
Name: summarize products
Tool: summarize_campaign_products
Status: success
Output: {'products': []}

Step 4
Name: create messaging
Tool: generate_campaign_messaging
Status: success
Output: {'message': 'Campaign messaging generated.'}

Step 5
Name: create channel recommendations
Tool: generate_channel_recommendations
Status: success
Output: {'recommended_channels': ['Email', 'Social Media', 'Website']}

Step 6
Name: create campaign checklist
Tool: generate_campaign_checklist
Status: success
Output: {'objective': 'launch our new collection and increase sales', 'products': [], 'messaging': '# Marketing Campaign Brief\n\n## 1. Campaign Overview\n* **Campaign Goal:** Launch our new collection and increase sales\n* **Dates:** October 15 to October 31\n* **Promotion:** 20% off\n\n## 2. Target Audience\n* **Audience:** Online shoppers\n\n## 3. Campaign Channels & Execution\n* **Online/E-commerce Promotion:** Highlight the 20% off promotion across digital touchpoints to incentivize online shoppers between October 15 and October 31.\n* **Collection Launch:** Feature the new collection prominently for online shoppers during the campaign window.', 'channels': ['Email', 'Social Media', 'Website'], 'timeline': 'October 15 to October 31', 'checklist': ['Confirm campaign objective', 'Confirm target audience', 'Prepare campaign messaging', 'Prepare creative assets', 'Schedule campaign', 'Monitor campaign performance']}

============================================================
DECISION RESULT
============================================================
{'decision': 'inputs_valid', 'missing_inputs': []}

============================================================
FINAL OUTPUT
============================================================
{'objective': 'launch our new collection and increase sales', 'products': [], 'messaging': '# Marketing Campaign Brief\n\n## 1. Campaign Overview\n* **Campaign Goal:** Launch our new collection and increase sales\n* **Dates:** October 15 to October 31\n* **Promotion:** 20% off\n\n## 2. Target Audience\n* **Audience:** Online shoppers\n\n## 3. Campaign Channels & Execution\n* **Online/E-commerce Promotion:** Highlight the 20% off promotion across digital touchpoints to incentivize online shoppers between October 15 and October 31.\n* **Collection Launch:** Feature the new collection prominently for online shoppers during the campaign window.', 'channels': ['Email', 'Social Media', 'Website'], 'timeline': 'October 15 to October 31', 'checklist': ['Confirm campaign objective', 'Confirm target audience', 'Prepare campaign messaging', 'Prepare creative assets', 'Schedule campaign', 'Monitor campaign performance']}



############# 8. the Eight workflow



(venv) C:\Users\Anuj Kushwaha\ai-workflow-agent>python -m app.main 
============================================================
AI Workflow Automation System
============================================================

Loaded 10 workflows.

Enter your request: "Classify these keywords and map them to pages."
Direct use of automatic function calling (AFC) in Models.generate_content is not recommended. Instead, we recommend to use AFC in Chat.send_message. Similarly, direct use of AFC in Models.generate_content_stream is not recommended. Instead, we recommend to use AFC in Chat.send_message_stream.

============================================================
WORKFLOW SELECTION
============================================================

Workflow ID: WF008
Confidence: 0.95
Reason: The user is asking to classify keywords and map them to pages, which matches SEO Keyword Classification.
Extracted Inputs: {}

Selected Workflow:
WF008 - SEO Keyword Classification

============================================================
EXECUTION PLAN
============================================================

Step 1: Read keywords
Tool: load_keywords

Step 2: remove duplicates
Tool: remove_duplicate_keywords

Step 3: classify search intent
Tool: classify_keyword_intent

Step 4: map keywords to categories
Tool: map_keywords_to_categories

Step 5: identify high-priority keywords
Tool: identify_priority_keywords

Step 6: export results
Tool: export_keyword_report

============================================================
EXECUTION RESULT
============================================================

Status: success

Step 1
Name: Read keywords
Tool: load_keywords
Status: success
Output: {'message': 'Keywords loaded.', 'records': 10}

Step 2
Name: remove duplicates
Tool: remove_duplicate_keywords
Status: success
Output: {'unique_keywords': 10}

Step 3
Name: classify search intent
Tool: classify_keyword_intent
Status: success
Output: {'classified_keywords': 10}

Step 4
Name: map keywords to categories
Tool: map_keywords_to_categories
Status: success
Output: {'categories_mapped': True}

Step 5
Name: identify high-priority keywords
Tool: identify_priority_keywords
Status: success
Output: {'high_priority_count': 2}

Step 6
Name: export results
Tool: export_keyword_report
Status: success
Output: {'keyword_report': [{'keyword': 'how to wash cotton shirt', 'intent': 'informational', 'category': 'Shirts', 'priority': 'medium'}, {'keyword': 'buy blue cotton shirt', 'intent': 'transactional', 'category': 'Shirts', 'priority': 'high'}, {'keyword': 'blue cotton shirt price', 'intent': 'commercial', 'category': 'Shirts', 'priority': 'medium'}, {'keyword': 'running shoes', 'intent': 'commercial', 'category': 'Footwear', 'priority': 'medium'}, {'keyword': 'best running shoes for beginners', 'intent': 'informational', 'category': 'Footwear', 'priority': 'medium'}, {'keyword': 'black jeans buy online', 'intent': 'transactional', 'category': 'Jeans', 'priority': 'high'}, {'keyword': 'company about us', 'intent': 'navigational', 'category': 'General', 'priority': 'medium'}, {'keyword': 'cotton hoodie', 'intent': 'commercial', 'category': 'Hoodies', 'priority': 'medium'}, {'keyword': 'cotton hoodie price', 'intent': 'commercial', 'category': 'Hoodies', 'priority': 'medium'}, {'keyword': 'how to style jeans', 'intent': 'informational', 'category': 'Jeans', 'priority': 'medium'}]}

============================================================
DECISION RESULT
============================================================
{'decision': 'classification_completed', 'classified_count': 10, 'allowed_intents': ['informational', 'commercial', 'transactional', 'navigational']}

============================================================
FINAL OUTPUT
============================================================
[{'keyword': 'how to wash cotton shirt', 'intent': 'informational', 'category': 'Shirts', 'priority': 'medium'}, {'keyword': 'buy blue cotton shirt', 'intent': 'transactional', 'category': 'Shirts', 'priority': 'high'}, {'keyword': 'blue cotton shirt price', 'intent': 'commercial', 'category': 'Shirts', 'priority': 'medium'}, {'keyword': 'running shoes', 'intent': 'commercial', 'category': 'Footwear', 'priority': 'medium'}, {'keyword': 'best running shoes for beginners', 'intent': 'informational', 'category': 'Footwear', 'priority': 'medium'}, {'keyword': 'black jeans buy online', 'intent': 'transactional', 'category': 'Jeans', 'priority': 'high'}, {'keyword': 'company about us', 'intent': 'navigational', 'category': 'General', 'priority': 'medium'}, {'keyword': 'cotton hoodie', 'intent': 'commercial', 'category': 'Hoodies', 'priority': 'medium'}, {'keyword': 'cotton hoodie price', 'intent': 'commercial', 'category': 'Hoodies', 'priority': 'medium'}, {'keyword': 'how to style jeans', 'intent': 'informational', 'category': 'Jeans', 'priority': 'medium'}]



############# 9. the Nineth workflow





(venv) C:\Users\Anuj Kushwaha\ai-workflow-agent>python -m app.main 
============================================================
AI Workflow Automation System
============================================================

Loaded 10 workflows.

Enter your request: "Assign this urgent task to the best available developer."
Direct use of automatic function calling (AFC) in Models.generate_content is not recommended. Instead, we recommend to use AFC in Chat.send_message. Similarly, direct use of AFC in Models.generate_content_stream is not recommended. Instead, we recommend to use AFC in Chat.send_message_stream.

============================================================
WORKFLOW SELECTION
============================================================

Workflow ID: WF009
Confidence: 0.95
Reason: The user is asking a manager/agent to assign a task with a specified priority.
Extracted Inputs: {'task_description': 'Assign this urgent task to the best available developer.', 'priority': 'urgent'}

Selected Workflow:
WF009 - Employee Task Assignment

============================================================
EXECUTION PLAN
============================================================

Step 1: Understand task requirements
Tool: understand_task_requirements

Step 2: compare employee skills
Tool: compare_employee_skills

Step 3: check current workload
Tool: check_employee_workload

Step 4: rank candidates
Tool: rank_employees

Step 5: select employee
Tool: select_employee

Step 6: generate assignment summary
Tool: generate_assignment_summary

============================================================
EXECUTION RESULT
============================================================

Status: success

Step 1
Name: Understand task requirements
Tool: understand_task_requirements
Status: success
Output: {'task_description': 'Assign this urgent task to the best available developer.'}

Step 2
Name: compare employee skills
Tool: compare_employee_skills
Status: success
Output: {'required_skills': []}

Step 3
Name: check current workload
Tool: check_employee_workload
Status: success
Output: {'message': 'Employee workload checked.'}

Step 4
Name: rank candidates
Tool: rank_employees
Status: success
Output: {'ranked_employees': [{'employee_id': 'E004', 'employee_name': 'Sneha', 'skill_match': 0, 'workload': 15, 'available_capacity': 85}, {'employee_id': 'E002', 'employee_name': 'Neha', 'skill_match': 0, 'workload': 20, 'available_capacity': 80}, {'employee_id': 'E003', 'employee_name': 'Rohit', 'skill_match': 0, 'workload': 35, 'available_capacity': 65}, {'employee_id': 'E001', 'employee_name': 'Aman', 'skill_match': 0, 'workload': 40, 'available_capacity': 60}]}

Step 5
Name: select employee
Tool: select_employee
Status: success
Output: {'selected_employee': 'Sneha'}

Step 6
Name: generate assignment summary
Tool: generate_assignment_summary
Status: success
Output: {'employee_id': 'E004', 'employee_name': 'Sneha', 'task': 'Assign this urgent task to the best available developer.', 'reason': 'Selected based on skill match and available workload capacity.', 'priority': 'urgent', 'deadline': None}

============================================================
DECISION RESULT
============================================================
{'decision': 'employee_selected', 'employee': 'Sneha'}

============================================================
FINAL OUTPUT
============================================================
{'employee_id': 'E004', 'employee_name': 'Sneha', 'task': 'Assign this urgent task to the best available developer.', 'reason': 'Selected based on skill match and available workload capacity.', 'priority': 'urgent', 'deadline': None}



############# 10. the Tenth workflow


(venv) C:\Users\Anuj Kushwaha\ai-workflow-agent>python -m app.main 
============================================================
AI Workflow Automation System
============================================================

Loaded 10 workflows.

Enter your request: "Which workflows are failing most often?"
Direct use of automatic function calling (AFC) in Models.generate_content is not recommended. Instead, we recommend to use AFC in Chat.send_message. Similarly, direct use of AFC in Models.generate_content_stream is not recommended. Instead, we recommend to use AFC in Chat.send_message_stream.

============================================================
WORKFLOW SELECTION
============================================================

Workflow ID: WF010
Confidence: 0.95
Reason: User is asking for a performance report on workflows failing most often.
Extracted Inputs: {}

Selected Workflow:
WF010 - Workflow Performance Report

============================================================
EXECUTION PLAN
============================================================

Step 1: Load execution logs
Tool: load_execution_logs

Step 2: calculate success/failure rate
Tool: calculate_workflow_metrics

Step 3: calculate average execution time
Tool: calculate_average_execution_time

Step 4: identify frequent errors
Tool: identify_frequent_errors

Step 5: identify slow steps
Tool: identify_slow_steps

Step 6: generate recommendations
Tool: generate_performance_recommendations

============================================================
EXECUTION RESULT
============================================================

Status: success

Step 1
Name: Load execution logs
Tool: load_execution_logs
Status: success
Output: {'message': 'Execution logs loaded.', 'records': 10}

Step 2
Name: calculate success/failure rate
Tool: calculate_workflow_metrics
Status: success
Output: {'metrics': [{'workflow_id': 'WF001', 'total_steps': 2, 'successful_steps': np.int64(2), 'failed_steps': 0, 'failure_rate': np.float64(0.0)}, {'workflow_id': 'WF002', 'total_steps': 2, 'successful_steps': np.int64(1), 'failed_steps': 1, 'failure_rate': np.float64(50.0)}, {'workflow_id': 'WF003', 'total_steps': 1, 'successful_steps': np.int64(1), 'failed_steps': 0, 'failure_rate': np.float64(0.0)}, {'workflow_id': 'WF004', 'total_steps': 1, 'successful_steps': np.int64(1), 'failed_steps': 0, 'failure_rate': np.float64(0.0)}, {'workflow_id': 'WF005', 'total_steps': 1, 'successful_steps': np.int64(1), 'failed_steps': 0, 'failure_rate': np.float64(0.0)}, {'workflow_id': 'WF006', 'total_steps': 1, 'successful_steps': np.int64(1), 'failed_steps': 0, 'failure_rate': np.float64(0.0)}, {'workflow_id': 'WF007', 'total_steps': 1, 'successful_steps': np.int64(1), 'failed_steps': 0, 'failure_rate': np.float64(0.0)}, {'workflow_id': 'WF008', 'total_steps': 1, 'successful_steps': np.int64(0), 'failed_steps': 1, 'failure_rate': np.float64(100.0)}]}

Step 3
Name: calculate average execution time
Tool: calculate_average_execution_time
Status: success
Output: {'average_execution_times': [{'workflow_id': 'WF001', 'average_execution_time': 1.35}, {'workflow_id': 'WF002', 'average_execution_time': 3.8}, {'workflow_id': 'WF003', 'average_execution_time': 1.8}, {'workflow_id': 'WF004', 'average_execution_time': 8.5}, {'workflow_id': 'WF005', 'average_execution_time': 1.1}, {'workflow_id': 'WF006', 'average_execution_time': 3.4}, {'workflow_id': 'WF007', 'average_execution_time': 7.2}, {'workflow_id': 'WF008', 'average_execution_time': 4.2}]}

Step 4
Name: identify frequent errors
Tool: identify_frequent_errors
Status: success
Output: {'errors': [{'error': 'Vendor data mismatch', 'count': 1}, {'error': 'Invalid keyword row', 'count': 1}]}

Step 5
Name: identify slow steps
Tool: identify_slow_steps
Status: success
Output: {'slow_steps': [{'workflow_id': 'WF002', 'step_name': 'Generate report', 'status': 'failed', 'execution_time': 5.5, 'error': 'Vendor data mismatch'}, {'workflow_id': 'WF004', 'step_name': 'Generate description', 'status': 'success', 'execution_time': 8.5, 'error': nan}, {'workflow_id': 'WF007', 'step_name': 'Generate brief', 'status': 'success', 'execution_time': 7.2, 'error': nan}]}

Step 6
Name: generate recommendations
Tool: generate_performance_recommendations
Status: success
Output: {'performance_summary': [{'workflow_id': 'WF001', 'total_steps': 2, 'successful_steps': 2, 'failed_steps': 0, 'failure_rate': 0.0, 'average_execution_time': 1.35}, {'workflow_id': 'WF002', 'total_steps': 2, 'successful_steps': 1, 'failed_steps': 1, 'failure_rate': 50.0, 'average_execution_time': 3.8}, {'workflow_id': 'WF003', 'total_steps': 1, 'successful_steps': 1, 'failed_steps': 0, 'failure_rate': 0.0, 'average_execution_time': 1.8}, {'workflow_id': 'WF004', 'total_steps': 1, 'successful_steps': 1, 'failed_steps': 0, 'failure_rate': 0.0, 'average_execution_time': 8.5}, {'workflow_id': 'WF005', 'total_steps': 1, 'successful_steps': 1, 'failed_steps': 0, 'failure_rate': 0.0, 'average_execution_time': 1.1}, {'workflow_id': 'WF006', 'total_steps': 1, 'successful_steps': 1, 'failed_steps': 0, 'failure_rate': 0.0, 'average_execution_time': 3.4}, {'workflow_id': 'WF007', 'total_steps': 1, 'successful_steps': 1, 'failed_steps': 0, 'failure_rate': 0.0, 'average_execution_time': 7.2}, {'workflow_id': 'WF008', 'total_steps': 1, 'successful_steps': 0, 'failed_steps': 1, 'failure_rate': 100.0, 'average_execution_time': 4.2}], 'recommendations': ['WF002: investigate failures because failure rate is 50.0%.', 'WF004: optimize slow steps because average execution time is 8.5 seconds.', 'WF007: optimize slow steps because average execution time is 7.2 seconds.', 'WF008: investigate failures because failure rate is 100.0%.']}

============================================================
DECISION RESULT
============================================================
{'decision': 'performance_issues_found', 'flagged_workflows': ['WF002', 'WF004', 'WF007', 'WF008']}

============================================================
FINAL OUTPUT
============================================================
{'performance_summary': [{'workflow_id': 'WF001', 'total_steps': 2, 'successful_steps': 2, 'failed_steps': 0, 'failure_rate': 0.0, 'average_execution_time': 1.35}, {'workflow_id': 'WF002', 'total_steps': 2, 'successful_steps': 1, 'failed_steps': 1, 'failure_rate': 50.0, 'average_execution_time': 3.8}, {'workflow_id': 'WF003', 'total_steps': 1, 'successful_steps': 1, 'failed_steps': 0, 'failure_rate': 0.0, 'average_execution_time': 1.8}, {'workflow_id': 'WF004', 'total_steps': 1, 'successful_steps': 1, 'failed_steps': 0, 'failure_rate': 0.0, 'average_execution_time': 8.5}, {'workflow_id': 'WF005', 'total_steps': 1, 'successful_steps': 1, 'failed_steps': 0, 'failure_rate': 0.0, 'average_execution_time': 1.1}, {'workflow_id': 'WF006', 'total_steps': 1, 'successful_steps': 1, 'failed_steps': 0, 'failure_rate': 0.0, 'average_execution_time': 3.4}, {'workflow_id': 'WF007', 'total_steps': 1, 'successful_steps': 1, 'failed_steps': 0, 'failure_rate': 0.0, 'average_execution_time': 7.2}, {'workflow_id': 'WF008', 'total_steps': 1, 'successful_steps': 0, 'failed_steps': 1, 'failure_rate': 100.0, 'average_execution_time': 4.2}], 'recommendations': ['WF002: investigate failures because failure rate is 50.0%.', 'WF004: optimize slow steps because average execution time is 8.5 seconds.', 'WF007: optimize slow steps because average execution time is 7.2 seconds.', 'WF008: investigate failures because failure rate is 100.0%.']}
