from pathlib import Path

import pandas as pd


def load_inventory(context: dict) -> dict:
    inventory_path = context["inventory_path"]

    path = Path(inventory_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Inventory file not found: {inventory_path}"
        )

    dataframe = pd.read_csv(path)

    required_columns = {
        "sku",
        "product_name",
        "current_stock",
        "minimum_stock",
    }

    missing_columns = required_columns - set(dataframe.columns)

    if missing_columns:
        raise ValueError(
            "Inventory file is missing columns: "
            + ", ".join(sorted(missing_columns))
        )

    context["inventory"] = dataframe

    return {
        "message": "Inventory loaded successfully.",
        "records": len(dataframe),
    }


def check_stock(context: dict) -> dict:
    dataframe = context["inventory"].copy()

    dataframe["needs_restock"] = (
        dataframe["current_stock"] < dataframe["minimum_stock"]
    )

    context["inventory_checked"] = dataframe

    return {
        "message": "Stock levels checked.",
        "low_stock_count": int(
            dataframe["needs_restock"].sum()
        ),
    }


def identify_low_stock_products(context: dict) -> dict:
    dataframe = context["inventory_checked"]

    low_stock = dataframe[
        dataframe["needs_restock"]
    ].copy()

    context["low_stock_products"] = low_stock

    return {
        "message": "Low-stock products identified.",
        "products": low_stock[
            ["sku", "product_name", "current_stock", "minimum_stock"]
        ].to_dict(orient="records"),
    }


def calculate_reorder_quantity(context: dict) -> dict:
    dataframe = context["low_stock_products"].copy()

    dataframe["reorder_quantity"] = (
        dataframe["minimum_stock"]
        - dataframe["current_stock"]
    )

    context["reorder_list"] = dataframe

    return {
        "message": "Reorder quantities calculated.",
        "products": dataframe[
            [
                "sku",
                "product_name",
                "current_stock",
                "minimum_stock",
                "reorder_quantity",
            ]
        ].to_dict(orient="records"),
    }


def generate_restock_list(context: dict) -> dict:
    dataframe = context["reorder_list"]

    restock_list = dataframe[
        [
            "sku",
            "product_name",
            "current_stock",
            "minimum_stock",
            "reorder_quantity",
        ]
    ]

    result = restock_list.to_dict(orient="records")

    context["final_output"] = result

    return {
        "restock_list": result,
    }