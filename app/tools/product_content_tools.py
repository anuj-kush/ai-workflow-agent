def _get_inputs(context: dict) -> dict:
    inputs = context.get("extracted_inputs", {}).copy()

    # If the LLM did not extract product details,
    # use the provided runtime product context.
    if not inputs:
        inputs = context.get("product_context", {}).copy()

    if not inputs:
        raise ValueError(
            "Product information is required. "
            "Please provide product name and available attributes."
        )

    # Normalize possible alternative field names
    if not inputs.get("product_name"):
        for key in ["product", "name", "item"]:
            if inputs.get(key):
                inputs["product_name"] = inputs[key]
                break

    if not inputs.get("product_name"):
        raise ValueError(
            "Product name is required. "
            "Please provide the product name."
        )

    return inputs


def validate_product_attributes(context: dict) -> dict:
    inputs = _get_inputs(context)

    product_name = inputs.get("product_name")

    context["product_inputs"] = inputs

    return {
        "message": "Product attributes validated.",
        "product_name": product_name,
    }


def _generate_content(context: dict) -> dict:
    inputs = context["product_inputs"]
    llm_client = context.get("llm_client")

    if llm_client is None:
        raise ValueError("LLM client is not available.")

    prompt = f"""
Create product SEO content using ONLY the information provided below.

Product information:
{inputs}

Rules:
1. Do not invent missing product attributes.
2. Use only the provided information.
3. If an attribute is missing, explicitly mention that the information is not provided.
4. Keep the content suitable for an e-commerce product page.
5. Make the SEO title concise.
6. Make the meta description suitable for search engines.

Return ONLY valid JSON with these fields:

{{
    "description": "...",
    "short_description": "...",
    "seo_title": "...",
    "meta_description": "..."
}}
"""

    response = llm_client.generate(prompt)

    context["product_content"] = response

    return {
        "message": "Product content generated.",
        "content": response,
    }


def generate_product_description(context: dict) -> dict:
    if "product_content" not in context:
        _generate_content(context)

    return {
        "description_generated": True
    }


def generate_short_description(context: dict) -> dict:
    if "product_content" not in context:
        _generate_content(context)

    return {
        "short_description_generated": True
    }


def generate_seo_title(context: dict) -> dict:
    if "product_content" not in context:
        _generate_content(context)

    return {
        "seo_title_generated": True
    }


def generate_meta_description(context: dict) -> dict:
    if "product_content" not in context:
        _generate_content(context)

    result = {
        "product_content": context["product_content"]
    }

    context["final_output"] = result

    return result