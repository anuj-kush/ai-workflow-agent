from app.config import WORKFLOW_FILE
from app.services.workflow_loader import WorkflowLoader
from app.services.workflow_registry import WorkflowRegistry


def test_workflow_file_exists():
    assert WORKFLOW_FILE.exists()


def test_load_all_workflows():
    loader = WorkflowLoader(WORKFLOW_FILE)

    workflows = loader.load()

    assert len(workflows) == 10


def test_workflow_ids():
    loader = WorkflowLoader(WORKFLOW_FILE)

    workflows = loader.load()

    workflow_ids = {
        workflow.workflow_id
        for workflow in workflows
    }

    expected_ids = {
        "WF001",
        "WF002",
        "WF003",
        "WF004",
        "WF005",
        "WF006",
        "WF007",
        "WF008",
        "WF009",
        "WF010",
    }

    assert workflow_ids == expected_ids


def test_registry_lookup():
    loader = WorkflowLoader(WORKFLOW_FILE)

    workflows = loader.load()

    registry = WorkflowRegistry(workflows)

    workflow = registry.get("WF001")

    assert workflow is not None
    assert workflow.workflow_name == "Inventory Restock Check"


def test_unknown_workflow():
    loader = WorkflowLoader(WORKFLOW_FILE)

    workflows = loader.load()

    registry = WorkflowRegistry(workflows)

    workflow = registry.get("WF999")

    assert workflow is None