from app.config import EMPLOYEES_FILE

from app.tools.employee_tools import (
    understand_task_requirements,
    compare_employee_skills,
    check_employee_workload,
    rank_employees,
    select_employee,
    generate_assignment_summary,
)


def test_employee_task_assignment():

    context = {
        "employees_path": EMPLOYEES_FILE,
        "extracted_inputs": {
            "task_description": "Python and Django task",
            "required_skills": [
                "python",
                "django",
            ],
            "priority": "high",
            "deadline": "October 15",
        },
    }

    understand_task_requirements(context)

    result = compare_employee_skills(context)

    assert "python" in result["required_skills"]
    assert "django" in result["required_skills"]

    check_employee_workload(context)

    rank_employees(context)

    result = select_employee(context)

    assert result["selected_employee"] == "Aman"

    final_result = generate_assignment_summary(context)

    assert final_result["employee_name"] == "Aman"
    assert final_result["priority"] == "high"
    assert final_result["deadline"] == "October 15"