from app.config import INVENTORY_FILE
from app.tools.inventory_tools import (
    load_inventory,
    check_stock,
    identify_low_stock_products,
    calculate_reorder_quantity,
    generate_restock_list,
)


def test_inventory_restock_workflow():

    context = {
        "inventory_path": INVENTORY_FILE
    }

    load_result = load_inventory(context)

    assert load_result["records"] == 5

    check_result = check_stock(context)

    assert check_result["low_stock_count"] == 3

    identify_low_stock_products(context)

    calculate_reorder_quantity(context)

    result = generate_restock_list(context)

    restock_list = result["restock_list"]

    assert len(restock_list) == 3

    quantities = {
        item["sku"]: item["reorder_quantity"]
        for item in restock_list
    }

    assert quantities["P001"] == 12
    assert quantities["P003"] == 10
    assert quantities["P005"] == 15