from app.services.step_parser import StepParser


def test_parse_workflow_steps():

    parser = StepParser()

    steps = parser.parse(
        "Load inventory → "
        "compare current stock with minimum threshold → "
        "identify low-stock products → "
        "calculate reorder quantity → "
        "generate restock list"
    )

    assert len(steps) == 5

    assert steps[0].step_number == 1
    assert steps[0].description == "Load inventory"

    assert steps[4].step_number == 5
    assert steps[4].description == "generate restock list"