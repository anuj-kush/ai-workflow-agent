from app.config import (
    PRODUCT_PRICES_FILE,
    VENDOR_PRICES_FILE,
)

from app.tools.price_tools import (
    load_product_prices,
    load_vendor_prices,
    match_product_prices,
    compare_product_prices,
    calculate_price_difference,
    generate_price_validation_report,
)


def test_price_validation_workflow():

    context = {
        "product_prices_path": PRODUCT_PRICES_FILE,
        "vendor_prices_path": VENDOR_PRICES_FILE,
    }

    product_result = load_product_prices(context)

    assert product_result["records"] == 5

    vendor_result = load_vendor_prices(context)

    assert vendor_result["records"] == 5

    match_result = match_product_prices(context)

    assert match_result["matched_records"] == 5

    compare_product_prices(context)

    calculate_price_difference(context)

    result = generate_price_validation_report(context)

    report = result["validation_report"]

    assert len(report) == 5

    exceptions = {
        item["sku"]: item["exception"]
        for item in report
    }

    assert exceptions["P001"] is False
    assert exceptions["P002"] is False
    assert exceptions["P003"] is False
    assert exceptions["P004"] is True
    assert exceptions["P005"] is True


def test_exactly_ten_percent_is_not_exception():

    context = {
        "product_prices_path": PRODUCT_PRICES_FILE,
        "vendor_prices_path": VENDOR_PRICES_FILE,
    }

    load_product_prices(context)
    load_vendor_prices(context)
    match_product_prices(context)
    compare_product_prices(context)
    calculate_price_difference(context)

    result = generate_price_validation_report(context)

    report = result["validation_report"]

    p002 = next(
        item for item in report
        if item["sku"] == "P002"
    )

    assert round(
        p002["difference_percentage"],
        2,
    ) == 10.00

    assert p002["exception"] is False