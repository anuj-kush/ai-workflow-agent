from app.config import (
    WORKFLOW_FILE,
    INVENTORY_FILE,
    PRODUCT_PRICES_FILE,
    VENDOR_PRICES_FILE,
    VENDOR_PRODUCTS_FILE,
    ORDERS_FILE,
    SHIPMENTS_FILE,
    PRODUCTS_FILE,
    KEYWORDS_FILE,
    EMPLOYEES_FILE,
    EXECUTION_LOGS_FILE,
)

from app.services.decision_engine import DecisionEngine
from app.services.llm_client import GeminiClient
from app.services.step_parser import StepParser
from app.services.step_tool_mapper import StepToolMapper
from app.services.tool_setup import create_tool_registry
from app.services.workflow_executor import WorkflowExecutor
from app.services.workflow_loader import WorkflowLoader
from app.services.workflow_planner import WorkflowPlanner
from app.services.workflow_registry import WorkflowRegistry
from app.services.workflow_selector import WorkflowSelector


def main():

    print("=" * 60)
    print("AI Workflow Automation System")
    print("=" * 60)

    # --------------------------------------------------
    # 1. Load workflows from Excel
    # --------------------------------------------------

    loader = WorkflowLoader(WORKFLOW_FILE)

    workflows = loader.load()

    print(f"\nLoaded {len(workflows)} workflows.")

    workflow_registry = WorkflowRegistry(workflows)

    # --------------------------------------------------
    # 2. Initialize LLM workflow selector
    # --------------------------------------------------

    llm_client = GeminiClient()

    selector = WorkflowSelector(
        llm_client=llm_client,
        workflow_registry=workflow_registry,
    )

    # --------------------------------------------------
    # 3. Get user request
    # --------------------------------------------------

    user_request = input("\nEnter your request: ")

    # --------------------------------------------------
    # 4. Select workflow using LLM
    # --------------------------------------------------

    selection = selector.select(user_request)

    print("\n" + "=" * 60)
    print("WORKFLOW SELECTION")
    print("=" * 60)

    print(f"\nWorkflow ID: {selection.workflow_id}")
    print(f"Confidence: {selection.confidence:.2f}")
    print(f"Reason: {selection.reason}")
    print(f"Extracted Inputs: {selection.extracted_inputs}")

    if selection.workflow_id == "NONE":

        print("\nNo suitable workflow was found.")

        return

    selected_workflow = workflow_registry.get(
        selection.workflow_id
    )

    if selected_workflow is None:

        print("\nWorkflow could not be found.")

        return

    print("\nSelected Workflow:")

    print(
        f"{selected_workflow.workflow_id} - "
        f"{selected_workflow.workflow_name}"
    )

    # --------------------------------------------------
    # 5. Create executable workflow plan
    # --------------------------------------------------

    planner = WorkflowPlanner(
        step_parser=StepParser(),
        step_tool_mapper=StepToolMapper(),
    )

    steps = planner.create_plan(
        selected_workflow
    )

    print("\n" + "=" * 60)
    print("EXECUTION PLAN")
    print("=" * 60)

    for step in steps:

        print(
            f"\nStep {step.step_number}: "
            f"{step.description}"
        )

        print(
            f"Tool: {step.tool_name}"
        )

    # --------------------------------------------------
    # 6. Create tool registry
    # --------------------------------------------------

    tool_registry = create_tool_registry()

    # --------------------------------------------------
    # 7. Create generic executor
    # --------------------------------------------------

    executor = WorkflowExecutor(
        tool_registry=tool_registry
    )

    # --------------------------------------------------
    # 8. Runtime context
    # --------------------------------------------------

    context = {
        "user_request": user_request,
        "extracted_inputs": selection.extracted_inputs,

        # ----------------------------------------------
        # Data files
        # ----------------------------------------------

        "inventory_path": INVENTORY_FILE,

        "product_prices_path": PRODUCT_PRICES_FILE,
        "vendor_prices_path": VENDOR_PRICES_FILE,

        "vendor_products_path": VENDOR_PRODUCTS_FILE,
        "vendor_file_path": VENDOR_PRODUCTS_FILE,

        "orders_path": ORDERS_FILE,
        "shipments_path": SHIPMENTS_FILE,

        "products_path": PRODUCTS_FILE,

        "keywords_path": KEYWORDS_FILE,
        "keyword_file_path": KEYWORDS_FILE,

        "employees_path": EMPLOYEES_FILE,

        "execution_logs_path": EXECUTION_LOGS_FILE,

        # ----------------------------------------------
        # LLM
        # ----------------------------------------------

        "llm_client": llm_client,

        # ----------------------------------------------
        # Demo context for assignment test requests
        # ----------------------------------------------

        "product_context": {
            "product_name": "Blue Cotton Shirt",
            "category": "Shirts",
            "material": "Cotton",
            "color": "Blue",
            "target_audience": "Young professionals",
        },

        "task_context": {
            "task_description": (
                "Python and Django backend development task"
            ),
            "required_skills": [
                "python",
                "django",
            ],
            "priority": "urgent",
            "deadline": "October 15",
        },
        "campaign_context": {
    "product_list": [
        "Blue Cotton Shirt",
        "Black Jeans",
        "Running Shoes",
    ],
    "target_audience": "Online shoppers",
    "promotion": "New collection launch",
},
    }

    # --------------------------------------------------
    # 9. Execute workflow
    # --------------------------------------------------

    result = executor.execute(
        workflow=selected_workflow,
        steps=steps,
        context=context,
    )

    # --------------------------------------------------
    # 10. Display execution trace
    # --------------------------------------------------

    print("\n" + "=" * 60)
    print("EXECUTION RESULT")
    print("=" * 60)

    print(f"\nStatus: {result.status}")

    for step_result in result.steps:

        print(
            f"\nStep {step_result.step_number}"
        )

        print(
            f"Name: "
            f"{step_result.step_name}"
        )

        print(
            f"Tool: "
            f"{step_result.tool_name}"
        )

        print(
            f"Status: "
            f"{step_result.status}"
        )

        print(
            f"Output: "
            f"{step_result.output}"
        )

    # --------------------------------------------------
    # 11. Evaluate workflow decision logic
    # --------------------------------------------------

    if result.status == "success":
        decision_engine = DecisionEngine()

        try:
            decision_result = decision_engine.evaluate(
                selected_workflow.decision_logic,
                context,
            )
            print("\n" + "=" * 60)
            print("DECISION RESULT")
            print("=" * 60)

            print(decision_result)

        except Exception as exc:
            print("\n" + "=" * 60)
            print("DECISION ERROR")
            print("=" * 60)

            print(str(exc))

        print("\n" + "=" * 60)
        print("FINAL OUTPUT")
        print("=" * 60)

        print(result.final_output)


    elif result.status == "needs_input":

        print("\n" + "=" * 60)
        print("ADDITIONAL INFORMATION REQUIRED")
        print("=" * 60)

        print(result.final_output)


    else:
        print("\n" + "=" * 60)
        print("ERROR")
        print("=" * 60)

        print(result.error)




if __name__ == "__main__":
    main()