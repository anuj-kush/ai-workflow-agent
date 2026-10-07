from app.config import PRODUCTS_FILE

from app.tools.duplicate_tools import (
    load_product_catalog,
    normalize_product_identifiers,
    compare_product_identifiers,
    compare_product_attributes,
    group_duplicate_products,
    assign_duplicate_confidence,
)


def test_duplicate_product_detection():

    context = {
        "products_path": PRODUCTS_FILE
    }

    result = load_product_catalog(context)

    assert result["records"] == 5

    normalize_product_identifiers(context)

    compare_product_identifiers(context)

    compare_product_attributes(context)

    result = group_duplicate_products(context)

    assert len(result["duplicate_groups"]) >= 1

    final_result = assign_duplicate_confidence(context)

    groups = final_result["duplicate_groups"]

    assert len(groups) >= 1

    attribute_group = next(
        (
            group
            for group in groups
            if group["type"] == "attribute_similarity"
        ),
        None,
    )

    assert attribute_group is not None
    assert attribute_group["confidence"] == "possible"