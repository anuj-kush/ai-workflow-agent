
import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent


# Workflow configuration
WORKFLOW_FILE = BASE_DIR / "data" / "workflows.xlsx"


# Workflow data files
INVENTORY_FILE = BASE_DIR / "data" / "inventory.csv"

PRODUCT_PRICES_FILE = BASE_DIR / "data" / "product_prices.csv"

VENDOR_PRICES_FILE = BASE_DIR / "data" / "vendor_prices.csv"

VENDOR_PRODUCTS_FILE = BASE_DIR / "data" / "vendor_products.csv"

ORDERS_FILE = BASE_DIR / "data" / "orders.csv"

SHIPMENTS_FILE = BASE_DIR / "data" / "shipments.csv"

PRODUCTS_FILE = BASE_DIR / "data" / "products.csv"

KEYWORDS_FILE = BASE_DIR / "data" / "keywords.csv"

EMPLOYEES_FILE = BASE_DIR / "data" / "employees.csv"

EXECUTION_LOGS_FILE = BASE_DIR / "data" / "execution_logs.csv"


# Environment variables
load_dotenv(BASE_DIR / ".env")


LLM_PROVIDER = os.getenv(
    "LLM_PROVIDER",
    "gemini",
)

LLM_MODEL = os.getenv(
    "LLM_MODEL",
    "gemini-2.5-flash",
)

GOOGLE_API_KEY = os.getenv(
    "GOOGLE_API_KEY",
)

