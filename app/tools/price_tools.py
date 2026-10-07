from pathlib import Path

import pandas as pd


def load_product_prices(context: dict) -> dict:
    file_path = Path(
        context["product_prices_path"]
    )

    if not file_path.exists():
        raise FileNotFoundError(
            f"Product price file not found: {file_path}"
        )

    dataframe = pd.read_csv(file_path)

    required_columns = {
        "sku",
        "product_name",
        "internal_price",
    }

    missing_columns = (
        required_columns
        - set(dataframe.columns)
    )

    if missing_columns:
        raise ValueError(
            "Product price file is missing columns: "
            + ", ".join(sorted(missing_columns))
        )

    context["product_prices"] = dataframe

    return {
        "message": "Product prices loaded successfully.",
        "records": len(dataframe),
    }


def load_vendor_prices(context: dict) -> dict:
    file_path = Path(
        context["vendor_prices_path"]
    )

    if not file_path.exists():
        raise FileNotFoundError(
            f"Vendor price file not found: {file_path}"
        )

    dataframe = pd.read_csv(file_path)

    required_columns = {
        "sku",
        "vendor_price",
    }

    missing_columns = (
        required_columns
        - set(dataframe.columns)
    )

    if missing_columns:
        raise ValueError(
            "Vendor price file is missing columns: "
            + ", ".join(sorted(missing_columns))
        )

    context["vendor_prices"] = dataframe

    return {
        "message": "Vendor prices loaded successfully.",
        "records": len(dataframe),
    }


def match_product_prices(context: dict) -> dict:
    products = context["product_prices"]
    vendors = context["vendor_prices"]

    matched = products.merge(
        vendors,
        on="sku",
        how="inner",
    )

    context["matched_prices"] = matched

    return {
        "message": "Product and vendor prices matched.",
        "matched_records": len(matched),
    }


def calculate_price_difference(context: dict) -> dict:
    dataframe = context["price_comparison"].copy()

    dataframe["difference_percentage"] = (
        dataframe["difference"].abs()
        / dataframe["internal_price"]
        * 100
    )

    context["price_comparison"] = dataframe

    return {
        "message": "Percentage price differences calculated.",
        "records": len(dataframe),
    }


def generate_price_validation_report(
    context: dict,
) -> dict:

    dataframe = context["price_comparison"].copy()

    dataframe["exception"] = (
        dataframe["difference_percentage"] > 10
    )

    report = dataframe[
        [
            "sku",
            "product_name",
            "internal_price",
            "vendor_price",
            "difference",
            "difference_percentage",
            "exception",
        ]
    ]

    result = report.to_dict(
        orient="records"
    )

    context["final_output"] = result

    return {
        "validation_report": result,
    }

def compare_product_prices(context: dict) -> dict:
    dataframe = context["matched_prices"].copy()

    dataframe["difference"] = (
        dataframe["vendor_price"]
        - dataframe["internal_price"]
    )

    context["price_comparison"] = dataframe

    return {
        "message": "Internal and vendor prices compared.",
        "records": len(dataframe),
    }