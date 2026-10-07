def _get_inputs(context: dict) -> dict:
    inputs = context.get("extracted_inputs", {}).copy()

    if not inputs:
        inputs = context.get("campaign_context", {}).copy()

    if not inputs:
        raise ValueError("Campaign information is required.")

    return inputs


def validate_campaign_inputs(context: dict) -> dict:
    inputs = _get_inputs(context)

    missing = []

    if not inputs.get("campaign_goal"):
        missing.append("campaign goal")

    if not inputs.get("dates"):
        missing.append("campaign dates")

    if missing:
        context["campaign_missing"] = missing

        return {
            "status": "missing_information",
            "message": (
                "Before I can create the campaign brief, "
                "please provide: " + ", ".join(missing) + "."
            ),
            "missing_inputs": missing,
        }

    context["campaign_inputs"] = inputs

    return {
        "status": "validated",
        "message": "Campaign inputs validated."
    }


def identify_campaign_objective(context: dict) -> dict:
    inputs = context["campaign_inputs"]

    goal = inputs.get("campaign_goal")

    context["campaign_objective"] = goal

    return {
        "objective": goal
    }


def summarize_campaign_products(context: dict) -> dict:
    inputs = context["campaign_inputs"]

    products = inputs.get(
        "product_list",
        inputs.get("products", [])
    )

    context["campaign_products"] = products

    return {
        "products": products
    }


def _generate_campaign_content(context: dict) -> str:
    llm_client = context.get("llm_client")

    if llm_client is None:
        raise ValueError("LLM client is not available.")

    prompt = f"""
Create a structured marketing campaign brief.

Campaign information:
{context["campaign_inputs"]}

Objective:
{context["campaign_objective"]}

Products:
{context["campaign_products"]}

Rules:
1. Do not invent missing information.
2. Use only the provided campaign information.
3. Keep the recommendations practical and suitable for an e-commerce campaign.
"""

    return llm_client.generate(prompt)


def generate_campaign_messaging(context: dict) -> dict:
    content = _generate_campaign_content(context)

    context["campaign_messaging"] = content

    return {
        "message": "Campaign messaging generated."
    }


def generate_channel_recommendations(context: dict) -> dict:
    channels = [
        "Email",
        "Social Media",
        "Website"
    ]

    context["campaign_channels"] = channels

    return {
        "recommended_channels": channels
    }


def generate_campaign_checklist(context: dict) -> dict:
    checklist = [
        "Confirm campaign objective",
        "Confirm target audience",
        "Prepare campaign messaging",
        "Prepare creative assets",
        "Schedule campaign",
        "Monitor campaign performance",
    ]

    result = {
        "objective": context["campaign_objective"],
        "products": context["campaign_products"],
        "messaging": context.get("campaign_messaging"),
        "channels": context.get("campaign_channels"),
        "timeline": context["campaign_inputs"].get("dates"),
        "checklist": checklist,
    }

    context["final_output"] = result

    return result