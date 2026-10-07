from pathlib import Path

import pandas as pd


def load_keywords(context: dict) -> dict:
    path = Path(context["keywords_path"])

    if not path.exists():
        raise FileNotFoundError(
            f"Keyword file not found: {path}"
        )

    dataframe = pd.read_csv(path)

    if "keyword" not in dataframe.columns:
        raise ValueError(
            "Keyword file must contain a 'keyword' column."
        )

    context["keywords"] = dataframe

    return {
        "message": "Keywords loaded.",
        "records": len(dataframe),
    }


def remove_duplicate_keywords(context: dict) -> dict:
    dataframe = context["keywords"].copy()

    dataframe["keyword"] = (
        dataframe["keyword"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    dataframe = dataframe[
        dataframe["keyword"].ne("")
    ]

    dataframe = dataframe.drop_duplicates(
        subset=["keyword"]
    )

    context["unique_keywords"] = dataframe

    return {
        "unique_keywords": len(dataframe)
    }


def classify_keyword_intent(context: dict) -> dict:
    dataframe = context["unique_keywords"].copy()

    def classify(keyword: str) -> str:
        text = keyword.lower()

        if any(
            word in text
            for word in [
                "how",
                "what",
                "guide",
                "best",
            ]
        ):
            return "informational"

        if any(
            word in text
            for word in [
                "buy",
                "purchase",
                "order",
            ]
        ):
            return "transactional"

        if any(
            word in text
            for word in [
                "price",
                "pricing",
                "compare",
            ]
        ):
            return "commercial"

        if any(
            word in text
            for word in [
                "about",
                "login",
                "official",
            ]
        ):
            return "navigational"

        return "commercial"

    dataframe["intent"] = dataframe[
        "keyword"
    ].apply(classify)

    context["classified_keywords"] = dataframe

    return {
        "classified_keywords": len(dataframe)
    }


def map_keywords_to_categories(context: dict) -> dict:
    dataframe = context["classified_keywords"].copy()

    def category(keyword: str) -> str:
        text = keyword.lower()

        if "shirt" in text:
            return "Shirts"

        if "jeans" in text:
            return "Jeans"

        if "shoe" in text:
            return "Footwear"

        if "hoodie" in text:
            return "Hoodies"

        return "General"

    dataframe["category"] = dataframe[
        "keyword"
    ].apply(category)

    context["categorized_keywords"] = dataframe

    return {
        "categories_mapped": True
    }


def identify_priority_keywords(context: dict) -> dict:
    dataframe = context["categorized_keywords"].copy()

    dataframe["priority"] = dataframe[
        "intent"
    ].apply(
        lambda intent:
        "high"
        if intent == "transactional"
        else "medium"
    )

    context["priority_keywords"] = dataframe

    return {
        "high_priority_count": int(
            (
                dataframe["priority"]
                == "high"
            ).sum()
        )
    }


def export_keyword_report(context: dict) -> dict:
    dataframe = context["priority_keywords"]

    result = dataframe[
        [
            "keyword",
            "intent",
            "category",
            "priority",
        ]
    ].to_dict(orient="records")

    context["final_output"] = result

    return {
        "keyword_report": result
    }