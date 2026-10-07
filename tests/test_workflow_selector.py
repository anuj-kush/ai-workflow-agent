from app.services.mock_llm_client import MockLLMClient
from app.services.workflow_loader import WorkflowLoader
from app.services.workflow_registry import WorkflowRegistry
from app.services.workflow_selector import WorkflowSelector
from app.config import WORKFLOW_FILE


def create_registry():
    loader = WorkflowLoader(WORKFLOW_FILE)

    workflows = loader.load()

    return WorkflowRegistry(workflows)


def test_select_inventory_workflow():

    mock_response = """
    {
        "workflow_id": "WF001",
        "confidence": 0.96,
        "extracted_inputs": {},
        "reason": "The user is asking which products need restocking."
    }
    """

    llm_client = MockLLMClient(mock_response)

    registry = create_registry()

    selector = WorkflowSelector(
        llm_client=llm_client,
        workflow_registry=registry,
    )

    result = selector.select(
        "Which products need restocking?"
    )

    assert result.workflow_id == "WF001"
    assert result.confidence == 0.96


def test_select_price_validation_workflow():

    mock_response = """
    {
        "workflow_id": "WF002",
        "confidence": 0.94,
        "extracted_inputs": {},
        "reason": "The user wants product prices validated."
    }
    """

    llm_client = MockLLMClient(mock_response)

    registry = create_registry()

    selector = WorkflowSelector(
        llm_client=llm_client,
        workflow_registry=registry,
    )

    result = selector.select(
        "Validate our product prices against the vendor prices."
    )

    assert result.workflow_id == "WF002"


def test_unknown_workflow_is_rejected():

    mock_response = """
    {
        "workflow_id": "WF999",
        "confidence": 0.99,
        "extracted_inputs": {},
        "reason": "Test unknown workflow."
    }
    """

    llm_client = MockLLMClient(mock_response)

    registry = create_registry()

    selector = WorkflowSelector(
        llm_client=llm_client,
        workflow_registry=registry,
    )

    try:
        selector.select("Some request")

        assert False, "Expected unknown workflow error"

    except ValueError as exc:

        assert "unknown workflow" in str(exc)