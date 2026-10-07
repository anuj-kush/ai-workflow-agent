from app.config import VENDOR_PRODUCTS_FILE

from app.tools.vendor_tools import (
    read_vendor_file,
    detect_vendor_columns,
    normalize_vendor_columns,
    validate_vendor_fields,
    identify_invalid_vendor_rows,
    create_cleaned_vendor_dataset,
)


def test_vendor_file_processing():

    context = {
        "vendor_products_path": VENDOR_PRODUCTS_FILE
    }

    result = read_vendor_file(context)

    assert result["records"] == 5

    detect_vendor_columns(context)

    normalize_vendor_columns(context)

    validate_result = validate_vendor_fields(context)

    assert "required vendor fields are present" in validate_result["message"].lower()

    invalid_result = identify_invalid_vendor_rows(context)

    assert invalid_result["invalid_rows"] == 2

    final_result = create_cleaned_vendor_dataset(context)

    assert final_result["cleaned_records"] == 3
    assert final_result["invalid_records"] == 2