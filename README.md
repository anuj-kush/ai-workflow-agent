markdown
# AI Workflow Automation Agent

An AI-powered workflow automation system that understands natural-language requests, selects the appropriate workflow from an Excel-based configuration, creates an execution plan, calls reusable tools, applies deterministic business rules, and returns a structured result.

The project is designed around a reusable workflow engine rather than separate hard-coded applications for each workflow.

---

## Features

- Natural-language workflow selection using an LLM
- Excel-based workflow configuration
- Reusable workflow planner and executor
- Generic tool registry
- Deterministic business logic for calculations and decisions
- LLM-powered content generation where appropriate
- CSV/XLSX data processing
- Mock data/API-style integrations
- Missing-input handling
- Execution trace for every workflow step
- Decision engine for workflow-specific business rules
- Automated tests with pytest
- Easy extension for additional workflows

---

## Architecture


User Request
     |
     v
LLM Workflow Selector
     |
     v
Workflow Registry
     |
     v
Workflow Planner
     |
     v
Step Parser + Tool Mapper
     |
     v
Workflow Executor
     |
     +--------------------+
     |                    |
     v                    v
Tool Registry        Decision Engine
     |                    |
     +----------+---------+
                |
                v
           Final Output


The workflow definitions are loaded from:


data/workflows.xlsx


This keeps workflow configuration separate from the core orchestration code.

---

## Technology Stack

* Python
* Google Gemini API
* Pandas
* OpenPyXL
* Pydantic
* pytest
* python-dotenv

---

## Project Structure


ai-workflow-agent/
│
├── app/
│   ├── models/
│   │   ├── workflow.py
│   │   ├── execution.py
│   │   └── selection.py
│   │
│   ├── services/
│   │   ├── workflow_loader.py
│   │   ├── workflow_registry.py
│   │   ├── workflow_selector.py
│   │   ├── workflow_planner.py
│   │   ├── workflow_executor.py
│   │   ├── step_parser.py
│   │   ├── step_tool_mapper.py
│   │   ├── tool_registry.py
│   │   ├── decision_engine.py
│   │   ├── llm_client.py
│   │   └── tool_setup.py
│   │
│   ├── tools/
│   │   ├── inventory_tools.py
│   │   ├── price_tools.py
│   │   ├── vendor_tools.py
│   │   ├── product_content_tools.py
│   │   ├── order_tools.py
│   │   ├── duplicate_tools.py
│   │   ├── marketing_tools.py
│   │   ├── seo_tools.py
│   │   ├── employee_tools.py
│   │   └── performance_tools.py
│   │
│   ├── config.py
│   └── main.py
│
├── data/
│   ├── workflows.xlsx
│   ├── inventory.csv
│   ├── product_prices.csv
│   ├── vendor_prices.csv
│   ├── vendor_products.csv
│   ├── orders.csv
│   ├── shipments.csv
│   ├── products.csv
│   ├── keywords.csv
│   ├── employees.csv
│   └── execution_logs.csv
│
├── tests/
│
├── scripts/
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md


---

# Workflows

The system supports the following 10 workflows.

| ID    | Workflow                      | Main Purpose                                 |
| ----- | ----------------------------- | -------------------------------------------- |
| WF001 | Inventory Restock Check       | Identify products below minimum stock        |
| WF002 | Product Price Validation      | Compare internal and vendor prices           |
| WF003 | Vendor File Processing        | Validate and clean vendor data               |
| WF004 | Product Description Generator | Generate product and SEO content             |
| WF005 | Customer Order Status         | Retrieve order and shipment information      |
| WF006 | Duplicate Product Detection   | Identify potential duplicate products        |
| WF007 | Marketing Campaign Brief      | Generate structured campaign briefs          |
| WF008 | SEO Keyword Classification    | Classify keywords and map them to categories |
| WF009 | Employee Task Assignment      | Rank employees and recommend an assignee     |
| WF010 | Workflow Performance Report   | Analyze workflow execution performance       |

---

# How Workflow Selection Works

A user provides a natural-language request such as:


Which products need restocking?


The workflow selector sends the request together with the configured workflow definitions to the LLM.

The LLM returns a structured selection containing:


workflow_id
confidence
extracted_inputs
reason


The selected workflow is then retrieved from the workflow registry.

The LLM is responsible for understanding the request.

The actual calculations, validation, ranking, and business decisions are handled by deterministic Python tools.

This separation helps keep business logic predictable and testable.

---

# Workflow Execution

After selecting a workflow, the planner:

1. Reads the workflow steps from Excel.
2. Parses the step sequence.
3. Maps each step to a registered tool.
4. Creates the execution plan.
5. Executes the tools sequentially.
6. Applies workflow-specific decision logic.
7. Returns the final result.

Example:


User Request
     |
     v
WF001 selected
     |
     v
Load inventory
     |
     v
Check stock
     |
     v
Identify low-stock products
     |
     v
Calculate reorder quantity
     |
     v
Generate restock list
     |
     v
Decision Engine
     |
     v
Final Result


---

# Decision Logic

Business decisions are implemented using deterministic rules.

For example, WF001 uses:


current_stock < minimum_stock


WF002 uses:


price difference > 10%


WF010 flags workflows when:


failure rate > 10%
OR
average execution time > configured threshold


This prevents the LLM from making numerical or business-critical decisions that can be handled deterministically.

---

# Missing Input Handling

The system distinguishes between technical failures and missing business information.

For example, the request:


Create a campaign brief for the new collection.


does not provide a campaign goal or dates.

Instead of treating this as a system failure, WF007 returns:


Status: needs_input


and asks for the missing information.

The execution system therefore supports states such as:


success
needs_input
failed


---

# Example Requests

The following assignment acceptance requests are supported:

### WF001


Which products need restocking?


### WF002


Find products where vendor price differs by more than 10%.


### WF003


Process this vendor spreadsheet and show invalid rows.


### WF004


Generate SEO content for this product.


### WF005


Where is order ORD-1001?


### WF006


Find likely duplicate products in the catalog.


### WF007


Create a campaign brief for the new collection.


If required campaign information is missing, the system requests it.

### WF008


Classify these keywords and map them to pages.


### WF009


Assign this urgent task to the best available developer.


### WF010


Which workflows are failing most often?


---

# Sample WF001 Result

For the inventory data provided with the project, the system identifies:


P001 - Blue Cotton Shirt
Current Stock: 8
Minimum Stock: 20
Reorder Quantity: 12

P003 - Running Shoes
Current Stock: 5
Minimum Stock: 15
Reorder Quantity: 10

P005 - Cotton Hoodie
Current Stock: 10
Minimum Stock: 25
Reorder Quantity: 15


Decision:


restock_required


---

# Data and API Simulation

The assignment requires workflow integrations such as order lookup, shipment lookup, employee data, and execution logs.

For this implementation, these integrations are represented using local CSV data and reusable Python tools.

For example:


orders.csv
shipments.csv
employees.csv
execution_logs.csv


The tool interfaces are designed so that these implementations can later be replaced with real REST APIs or databases without changing the core workflow orchestration layer.

---

# Testing

The project uses pytest for automated testing.

Run:

bash
pytest -q


The test suite covers:

* Workflow loading
* Workflow registry
* Workflow selection
* Step parsing
* Tool mapping
* Workflow planning
* Workflow execution
* Inventory logic
* Price validation
* Vendor validation
* Order lookup
* Duplicate detection
* Employee assignment
* Performance reporting
* Missing/invalid scenarios

Expected result:


23 passed


---

# Setup

## 1. Clone the repository

bash
git clone <repository-url>
cd ai-workflow-agent


## 2. Create a virtual environment

Windows:

powershell
python -m venv venv
venv\Scripts\activate


## 3. Install dependencies

powershell
pip install -r requirements.txt


## 4. Configure Gemini

Create a .env file:


LLM_PROVIDER=gemini
LLM_MODEL=gemini-2.5-flash
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY


Do not commit .env to GitHub.

Use .env.example as the template.

---

# Run the Application

From the project root:

powershell
python -m app.main


Then enter a natural-language request.

Example:


Which products need restocking?


---

# Adding an 11th Workflow

The architecture is designed to make workflow configuration extensible.

A new workflow can be added to:


data/workflows.xlsx


using the existing workflow columns:


Workflow_ID
Workflow_Name
Trigger
Inputs
Steps
Decision_Logic
Tools_Required
Expected_Output


The core workflow loader and registry do not need to be rewritten.

If the new workflow requires a genuinely new capability, a corresponding tool can be implemented and registered in the tool registry.

The existing orchestration flow remains unchanged:


Excel
  ↓
Workflow Loader
  ↓
Workflow Registry
  ↓
Workflow Selector
  ↓
Planner
  ↓
Executor
  ↓
Tools
  ↓
Decision Engine


This keeps the architecture reusable as additional workflows are introduced.

---

# AI Usage

AI was used as a development and implementation assistant during the project.

The application itself uses an LLM for:

* Natural-language workflow selection
* Input extraction
* Product content generation
* Marketing content generation

Deterministic Python code is used for:

* Data processing
* Calculations
* Validation
* Ranking
* Threshold checks
* Business decisions

This separation was intentional so that LLM output does not directly control deterministic business rules.

---

# Limitations and Future Improvements

Possible production improvements include:

* Replace CSV files with PostgreSQL or another production database
* Replace simulated integrations with real REST APIs
* Add authentication and authorization
* Add persistent workflow execution history
* Add structured observability and tracing
* Add retry and timeout policies for external APIs
* Add asynchronous execution for long-running workflows
* Add a web UI/API layer for production deployment
* Add stronger semantic similarity for duplicate detection
* Add human approval steps for sensitive workflows

---

# Project Goal

The goal of this project is to demonstrate a reusable AI workflow automation architecture where an LLM handles natural-language understanding while deterministic tools execute reliable business operations.

The system is intentionally designed as a workflow engine rather than ten independent chatbot implementations.




