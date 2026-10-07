from pathlib import Path

import pandas as pd


SLOW_EXECUTION_THRESHOLD = 5.0
FAILURE_RATE_THRESHOLD = 10.0


def load_execution_logs(context: dict) -> dict:
    path = Path(context["execution_logs_path"])

    if not path.exists():
        raise FileNotFoundError(
            f"Execution log file not found: {path}"
        )

    dataframe = pd.read_csv(path)

    required = {
        "workflow_id",
        "step_name",
        "status",
        "execution_time",
        "error",
    }

    missing = required - set(dataframe.columns)

    if missing:
        raise ValueError(
            "Execution log is missing columns: "
            + ", ".join(sorted(missing))
        )

    context["execution_logs"] = dataframe

    return {
        "message": "Execution logs loaded.",
        "records": len(dataframe),
    }


def calculate_workflow_metrics(context: dict) -> dict:
    dataframe = context["execution_logs"]

    metrics = []

    for workflow_id, group in dataframe.groupby(
        "workflow_id"
    ):
        total = len(group)

        failures = (
            group["status"]
            .astype(str)
            .str.lower()
            .eq("failed")
            .sum()
        )

        success = total - failures

        failure_rate = (
            failures / total * 100
            if total
            else 0
        )

        metrics.append(
            {
                "workflow_id": workflow_id,
                "total_steps": total,
                "successful_steps": success,
                "failed_steps": int(failures),
                "failure_rate": round(
                    failure_rate,
                    2,
                ),
            }
        )

    context["workflow_metrics"] = pd.DataFrame(
        metrics
    )

    return {
        "metrics": metrics
    }


def calculate_average_execution_time(
    context: dict,
) -> dict:

    dataframe = context["execution_logs"]

    averages = (
        dataframe.groupby("workflow_id")[
            "execution_time"
        ]
        .mean()
        .reset_index()
    )

    averages = averages.rename(
        columns={
            "execution_time":
            "average_execution_time"
        }
    )

    context["execution_averages"] = averages

    return {
        "average_execution_times":
        averages.to_dict(orient="records")
    }


def identify_frequent_errors(context: dict) -> dict:
    dataframe = context["execution_logs"]

    errors = dataframe[
        dataframe["error"]
        .fillna("")
        .astype(str)
        .str.strip()
        .ne("")
    ]

    counts = (
        errors["error"]
        .value_counts()
        .reset_index()
    )

    counts.columns = [
        "error",
        "count",
    ]

    context["frequent_errors"] = counts

    return {
        "errors": counts.to_dict(
            orient="records"
        )
    }


def identify_slow_steps(context: dict) -> dict:
    dataframe = context["execution_logs"]

    slow = dataframe[
        dataframe["execution_time"]
        > SLOW_EXECUTION_THRESHOLD
    ].copy()

    context["slow_steps"] = slow

    return {
        "slow_steps": slow.to_dict(
            orient="records"
        )
    }


def generate_performance_recommendations(
    context: dict,
) -> dict:

    metrics = context["workflow_metrics"]
    averages = context["execution_averages"]

    merged = metrics.merge(
        averages,
        on="workflow_id",
    )

    recommendations = []

    for _, row in merged.iterrows():

        workflow_id = row["workflow_id"]

        if row["failure_rate"] > FAILURE_RATE_THRESHOLD:
            recommendations.append(
                f"{workflow_id}: investigate failures "
                f"because failure rate is "
                f"{row['failure_rate']}%."
            )

        if (
            row["average_execution_time"]
            > SLOW_EXECUTION_THRESHOLD
        ):
            recommendations.append(
                f"{workflow_id}: optimize slow steps "
                f"because average execution time is "
                f"{round(row['average_execution_time'], 2)} seconds."
            )

    result = {
        "performance_summary":
            merged.to_dict(orient="records"),
        "recommendations":
            recommendations,
    }

    context["final_output"] = result

    return result