from pathlib import Path

import pandas as pd


def validate_order_identifier(context: dict) -> dict:
    inputs = context.get("extracted_inputs", {})

    order_id = inputs.get("order_id")
    customer_email = inputs.get("customer_email")

    if not order_id and not customer_email:
        raise ValueError(
            "Please provide an order ID or customer email."
        )

    context["order_id"] = order_id
    context["customer_email"] = customer_email

    return {
        "message": "Order identifier validated.",
        "order_id": order_id,
        "customer_email": customer_email,
    }


def search_order(context: dict) -> dict:
    path = Path(context["orders_path"])

    if not path.exists():
        raise FileNotFoundError(
            f"Orders file not found: {path}"
        )

    dataframe = pd.read_csv(path)

    order_id = context.get("order_id")
    customer_email = context.get("customer_email")

    if order_id:
        matches = dataframe[
            dataframe["order_id"].astype(str).str.lower()
            == str(order_id).lower()
        ]
    else:
        matches = dataframe[
            dataframe["customer_email"].astype(str).str.lower()
            == str(customer_email).lower()
        ]

    if matches.empty:
        raise ValueError(
            "No order found. Please provide another order ID "
            "or customer email."
        )

    context["order"] = matches.iloc[0].to_dict()

    return {
        "message": "Order found.",
        "order": context["order"],
    }


def get_order_status(context: dict) -> dict:
    order = context["order"]

    context["order_status"] = order.get("status")

    return {
        "status": order.get("status")
    }


def get_shipment_information(context: dict) -> dict:
    path = Path(context["shipments_path"])

    if not path.exists():
        raise FileNotFoundError(
            f"Shipment file not found: {path}"
        )

    dataframe = pd.read_csv(path)

    order_id = context["order"]["order_id"]

    matches = dataframe[
        dataframe["order_id"].astype(str).str.lower()
        == str(order_id).lower()
    ]

    if matches.empty:
        context["shipment"] = None

        return {
            "message": "Shipment information not available."
        }

    context["shipment"] = matches.iloc[0].to_dict()

    return {
        "shipment": context["shipment"]
    }


def summarize_order_status(context: dict) -> dict:
    order = context["order"]
    shipment = context.get("shipment")

    result = {
        "order_id": order.get("order_id"),
        "customer": order.get("customer_name"),
        "items": order.get("items"),
        "order_status": order.get("status"),
        "shipment_status": (
            shipment.get("shipment_status")
            if shipment
            else None
        ),
        "tracking_number": (
            shipment.get("tracking_number")
            if shipment
            else None
        ),
        "carrier": (
            shipment.get("carrier")
            if shipment
            else None
        ),
    }

    context["final_output"] = result

    return result