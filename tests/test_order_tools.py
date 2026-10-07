import pytest

from app.config import (
    ORDERS_FILE,
    SHIPMENTS_FILE,
)

from app.tools.order_tools import (
    validate_order_identifier,
    search_order,
    get_order_status,
    get_shipment_information,
    summarize_order_status,
)


def test_order_status_workflow():

    context = {
        "orders_path": ORDERS_FILE,
        "shipments_path": SHIPMENTS_FILE,
        "extracted_inputs": {
            "order_id": "ORD-1001"
        },
    }

    validate_order_identifier(context)
    search_order(context)
    status = get_order_status(context)

    assert status["status"] == "Shipped"

    shipment = get_shipment_information(context)

    assert shipment["shipment"]["shipment_status"] == "In Transit"
    assert shipment["shipment"]["tracking_number"] == "TRK10001"

    result = summarize_order_status(context)

    assert result["order_id"] == "ORD-1001"
    assert result["order_status"] == "Shipped"
    assert result["shipment_status"] == "In Transit"
    assert result["tracking_number"] == "TRK10001"


def test_unknown_order_fails():

    context = {
        "orders_path": ORDERS_FILE,
        "shipments_path": SHIPMENTS_FILE,
        "extracted_inputs": {
            "order_id": "ORD999"
        },
    }

    validate_order_identifier(context)

    with pytest.raises(ValueError, match="No order found"):
        search_order(context)