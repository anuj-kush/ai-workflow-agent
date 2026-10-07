from app.models.execution import WorkflowStep
from app.services.step_tool_mapper import StepToolMapper


def test_wf001_step_mapping():
    mapper = StepToolMapper()

    steps = [
        WorkflowStep(
            step_number=1,
            description="Load inventory",
        ),
        WorkflowStep(
            step_number=2,
            description="compare current stock with minimum threshold",
        ),
        WorkflowStep(
            step_number=3,
            description="identify low-stock products",
        ),
        WorkflowStep(
            step_number=4,
            description="calculate reorder quantity",
        ),
        WorkflowStep(
            step_number=5,
            description="generate restock list",
        ),
    ]

    mapped = mapper.map_steps(
        steps,
        workflow_id="WF001",
    )

    assert mapped[0].tool_name == "load_inventory"
    assert mapped[1].tool_name == "check_stock"
    assert mapped[2].tool_name == "identify_low_stock_products"
    assert mapped[3].tool_name == "calculate_reorder_quantity"
    assert mapped[4].tool_name == "generate_restock_list"


def test_wf002_compare_step_maps_correctly():
    mapper = StepToolMapper()

    step = WorkflowStep(
        step_number=1,
        description="compare internal and vendor prices",
    )

    mapped = mapper.map_step(
        step,
        workflow_id="WF002",
    )

    assert mapped.tool_name == "compare_product_prices"


def test_unknown_workflow_fails():
    mapper = StepToolMapper()

    steps = [
        WorkflowStep(
            step_number=1,
            description="Load inventory",
        )
    ]

    try:
        mapper.map_steps(
            steps,
            workflow_id="UNKNOWN",
        )
        assert False
    except ValueError as exc:
        assert "No tool mapping rules" in str(exc)