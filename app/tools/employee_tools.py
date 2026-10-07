from pathlib import Path

import pandas as pd


def understand_task_requirements(context: dict) -> dict:
    inputs = context.get("extracted_inputs", {})

    task_description = inputs.get(
        "task_description",
        context.get("user_request", ""),
    )

    if not task_description:
        raise ValueError(
            "Task description is required."
        )

    context["task_description"] = task_description

    return {
        "task_description": task_description
    }


def compare_employee_skills(context: dict) -> dict:
    path = Path(context["employees_path"])

    if not path.exists():
        raise FileNotFoundError(
            f"Employees file not found: {path}"
        )

    dataframe = pd.read_csv(path)

    required = {
        "employee_id",
        "employee_name",
        "skills",
        "workload",
    }

    missing = required - set(dataframe.columns)

    if missing:
        raise ValueError(
            "Employee file is missing columns: "
            + ", ".join(sorted(missing))
        )

    task = context["task_description"].lower()

    known_skills = [
        "python",
        "django",
        "fastapi",
        "sql",
        "rest api",
        "react",
        "javascript",
        "html",
        "css",
        "machine learning",
    ]

    required_skills = [
        skill
        for skill in known_skills
        if skill in task
    ]

    def skill_match(skills: str) -> int:
        employee_skills = [
            item.strip().lower()
            for item in str(skills).split(",")
        ]

        return sum(
            skill in employee_skills
            for skill in required_skills
        )

    dataframe["skill_match"] = dataframe[
        "skills"
    ].apply(skill_match)

    context["employees"] = dataframe

    return {
        "required_skills": required_skills
    }


def check_employee_workload(context: dict) -> dict:
    dataframe = context["employees"].copy()

    dataframe["available_capacity"] = (
        100 - dataframe["workload"]
    )

    context["employees"] = dataframe

    return {
        "message": "Employee workload checked."
    }


def rank_employees(context: dict) -> dict:
    dataframe = context["employees"].copy()

    dataframe = dataframe.sort_values(
        by=[
            "skill_match",
            "available_capacity",
        ],
        ascending=[
            False,
            False,
        ],
    )

    context["ranked_employees"] = dataframe

    return {
        "ranked_employees": dataframe[
            [
                "employee_id",
                "employee_name",
                "skill_match",
                "workload",
                "available_capacity",
            ]
        ].to_dict(orient="records")
    }


def select_employee(context: dict) -> dict:
    dataframe = context["ranked_employees"]

    suitable = dataframe[
        dataframe["available_capacity"] > 0
    ]

    if suitable.empty:
        raise ValueError(
            "No suitable employee has available capacity."
        )

    selected = suitable.iloc[0].to_dict()

    context["selected_employee"] = selected

    return {
        "selected_employee": selected[
            "employee_name"
        ]
    }


def generate_assignment_summary(context: dict) -> dict:
    employee = context["selected_employee"]

    inputs = context.get(
        "extracted_inputs",
        {},
    )

    result = {
        "employee_id": employee["employee_id"],
        "employee_name": employee["employee_name"],
        "task": context["task_description"],
        "reason": (
            "Selected based on skill match "
            "and available workload capacity."
        ),
        "priority": inputs.get("priority"),
        "deadline": inputs.get("deadline"),
    }

    context["final_output"] = result

    return result