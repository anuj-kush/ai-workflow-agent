from app.config import WORKFLOW_FILE
from app.services.step_parser import StepParser
from app.services.step_tool_mapper import StepToolMapper
from app.services.workflow_loader import WorkflowLoader
from app.services.workflow_planner import WorkflowPlanner


def test_inventory_workflow_plan():

    loader = WorkflowLoader(
        WORKFLOW_FILE
    )

    workflows = loader.load()

    workflow = next(
        workflow
        for workflow in workflows
        if workflow.workflow_id == "WF001"
    )

    planner = WorkflowPlanner(
        step_parser=StepParser(),
        step_tool_mapper=StepToolMapper(),
    )

    steps = planner.create_plan(
        workflow
    )

    assert len(steps) == 5

    assert steps[0].tool_name == "load_inventory"

    assert steps[1].tool_name == "check_stock"

    assert (
        steps[2].tool_name
        == "identify_low_stock_products"
    )

    assert (
        steps[3].tool_name
        == "calculate_reorder_quantity"
    )

    assert (
        steps[4].tool_name
        == "generate_restock_list"
    )