from app.config import INVENTORY_FILE, WORKFLOW_FILE
from app.services.step_parser import StepParser
from app.services.step_tool_mapper import StepToolMapper
from app.services.tool_setup import create_tool_registry
from app.services.workflow_executor import WorkflowExecutor
from app.services.workflow_loader import WorkflowLoader
from app.services.workflow_planner import WorkflowPlanner


def test_inventory_workflow_execution():

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

    registry = create_tool_registry()

    executor = WorkflowExecutor(
        tool_registry=registry
    )

    context = {
        "inventory_path": INVENTORY_FILE,
        "user_request": "Which products are running low?",
        "extracted_inputs": {},
    }

    result = executor.execute(
        workflow=workflow,
        steps=steps,
        context=context,
    )

    assert result.status == "success"

    assert len(result.steps) == 5

    assert "Blue Cotton Shirt" in result.final_output

    assert "Running Shoes" in result.final_output

    assert "Cotton Hoodie" in result.final_output