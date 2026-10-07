from app.config import EXECUTION_LOGS_FILE

from app.tools.performance_tools import (
    load_execution_logs,
    calculate_workflow_metrics,
    calculate_average_execution_time,
    identify_frequent_errors,
    identify_slow_steps,
    generate_performance_recommendations,
)


def test_workflow_performance_report():

    context = {
        "execution_logs_path": EXECUTION_LOGS_FILE
    }

    result = load_execution_logs(context)

    assert result["records"] == 10

    calculate_workflow_metrics(context)

    calculate_average_execution_time(context)

    errors = identify_frequent_errors(context)

    assert len(errors["errors"]) == 2

    slow_steps = identify_slow_steps(context)

    assert len(slow_steps["slow_steps"]) == 3

    final_result = generate_performance_recommendations(context)

    recommendations = final_result["recommendations"]

    assert any(
        "WF002" in recommendation
        for recommendation in recommendations
    )

    assert any(
        "WF004" in recommendation
        for recommendation in recommendations
    )

    assert any(
        "WF007" in recommendation
        for recommendation in recommendations
    )

    assert any(
        "WF008" in recommendation
        for recommendation in recommendations
    )