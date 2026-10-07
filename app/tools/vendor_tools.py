from pathlib import Path

import pandas as pd


def read_vendor_file(context: dict) -> dict:
    path = Path(
        context.get(
            "vendor_file_path",
            context["vendor_products_path"],
        )
    )

    if not path.exists():
        raise FileNotFoundError(
            f"Vendor file not found: {path}"
        )

    if path.suffix.lower() == ".xlsx":
        dataframe = pd.read_excel(path)
    else:
        dataframe = pd.read_csv(path)

    context["vendor_raw"] = dataframe

    return {
        "message": "Vendor file loaded.",
        "records": len(dataframe),
    }


def detect_vendor_columns(context: dict) -> dict:
    dataframe = context["vendor_raw"]

    columns = list(dataframe.columns)

    context["vendor_columns"] = columns

    return {
        "columns": columns
    }


def normalize_vendor_columns(context: dict) -> dict:
    dataframe = context["vendor_raw"].copy()

    dataframe.columns = [
        str(column)
        .strip()
        .lower()
        .replace(" ", "_")
        for column in dataframe.columns
    ]

    context["vendor_normalized"] = dataframe

    return {
        "message": "Vendor columns normalized.",
        "columns": list(dataframe.columns),
    }


def validate_vendor_fields(context: dict) -> dict:
    dataframe = context["vendor_normalized"]

    required = {
        "sku",
        "product_name",
    }

    missing_columns = (
        required - set(dataframe.columns)
    )

    if missing_columns:
        raise ValueError(
            "Missing required fields: "
            + ", ".join(sorted(missing_columns))
        )

    context["vendor_validated"] = dataframe

    return {
        "message": "Required vendor fields are present."
    }


def identify_invalid_vendor_rows(context: dict) -> dict:
    dataframe = context["vendor_validated"].copy()

    invalid = (
        dataframe["sku"]
        .fillna("")
        .astype(str)
        .str.strip()
        .eq("")
        |
        dataframe["product_name"]
        .fillna("")
        .astype(str)
        .str.strip()
        .eq("")
    )

    dataframe["is_invalid"] = invalid

    context["vendor_processed"] = dataframe
    context["invalid_vendor_rows"] = dataframe[invalid]

    return {
        "invalid_rows": int(invalid.sum())
    }


def create_cleaned_vendor_dataset(context: dict) -> dict:
    dataframe = context["vendor_processed"]

    cleaned = dataframe[
        ~dataframe["is_invalid"]
    ].drop(
        columns=["is_invalid"]
    )

    invalid = context["invalid_vendor_rows"]

    context["cleaned_vendor_data"] = cleaned

    result = {
        "cleaned_records": len(cleaned),
        "invalid_records": len(invalid),
        "invalid_rows": invalid.to_dict(
            orient="records"
        ),
    }

    context["final_output"] = result

    return result