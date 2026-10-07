from pathlib import Path

import pandas as pd


def load_product_catalog(context: dict) -> dict:
    path = Path(context["products_path"])

    if not path.exists():
        raise FileNotFoundError(
            f"Products file not found: {path}"
        )

    dataframe = pd.read_csv(path)

    required = {
        "sku",
        "product_name",
        "category",
        "material",
        "color",
    }

    missing = required - set(dataframe.columns)

    if missing:
        raise ValueError(
            "Products file is missing columns: "
            + ", ".join(sorted(missing))
        )

    context["products"] = dataframe

    return {
        "message": "Product catalog loaded.",
        "records": len(dataframe),
    }


def normalize_product_identifiers(context: dict) -> dict:
    dataframe = context["products"].copy()

    dataframe["normalized_sku"] = (
        dataframe["sku"]
        .fillna("")
        .astype(str)
        .str.strip()
        .str.lower()
    )

    dataframe["normalized_name"] = (
        dataframe["product_name"]
        .fillna("")
        .astype(str)
        .str.strip()
        .str.lower()
    )

    context["normalized_products"] = dataframe

    return {
        "message": "Product identifiers normalized."
    }


def compare_product_identifiers(context: dict) -> dict:
    dataframe = context["normalized_products"]

    duplicate_skus = dataframe[
        dataframe["normalized_sku"].duplicated(
            keep=False
        )
        & dataframe["normalized_sku"].ne("")
    ]

    context["duplicate_skus"] = duplicate_skus

    return {
        "duplicate_sku_records": len(duplicate_skus)
    }


def compare_product_attributes(context: dict) -> dict:
    dataframe = context["normalized_products"]

    groups = []

    grouped = dataframe.groupby(
        ["normalized_name", "category", "material", "color"],
        dropna=False,
    )

    for _, group in grouped:
        if len(group) > 1:
            groups.append(group)

    context["attribute_duplicate_groups"] = groups

    return {
        "possible_duplicate_groups": len(groups)
    }


def group_duplicate_products(context: dict) -> dict:
    groups = []

    duplicate_skus = context["duplicate_skus"]

    if not duplicate_skus.empty:
        groups.append(
            {
                "type": "exact_sku",
                "confidence": "definite",
                "products": duplicate_skus[
                    [
                        "sku",
                        "product_name",
                    ]
                ].to_dict(orient="records"),
            }
        )

    for group in context["attribute_duplicate_groups"]:
        groups.append(
            {
                "type": "attribute_similarity",
                "confidence": "possible",
                "products": group[
                    [
                        "sku",
                        "product_name",
                        "category",
                        "material",
                        "color",
                    ]
                ].to_dict(orient="records"),
            }
        )

    context["duplicate_groups"] = groups

    return {
        "duplicate_groups": groups
    }


def assign_duplicate_confidence(context: dict) -> dict:
    groups = context.get(
        "duplicate_groups",
        [],
    )

    result = {
        "duplicate_groups": groups,
        "total_groups": len(groups),
    }

    context["final_output"] = result

    return result