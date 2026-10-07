
import json

from app.models.selection import WorkflowSelection
from app.models.workflow import WorkflowDefinition
from app.services.llm_client import GeminiClient
from app.services.workflow_registry import WorkflowRegistry


class WorkflowSelector:
    """
    Uses an LLM to identify which registered workflow
    best matches the user's request and extract inputs.
    """

    def __init__(
        self,
        llm_client: GeminiClient,
        workflow_registry: WorkflowRegistry,
    ):
        self.llm_client = llm_client
        self.workflow_registry = workflow_registry

    def select(
        self,
        user_request: str,
    ) -> WorkflowSelection:

        if not user_request.strip():
            raise ValueError(
                "User request cannot be empty."
            )

        prompt = self._build_prompt(user_request)

        response_text = self.llm_client.generate(prompt)

        selection = self._parse_response(response_text)

        self._validate_selection(selection)

        return selection

    def _build_prompt(
        self,
        user_request: str,
    ) -> str:

        workflows = self.workflow_registry.get_all()

        workflow_context = self._format_workflows(
            workflows
        )

        return f"""
You are the workflow-selection component of an
AI business workflow automation system.

Your ONLY responsibility is to:

1. Select the most appropriate registered workflow.
2. Extract information explicitly provided by the user.

Do NOT execute any workflow.
Do NOT invent a workflow.
Do NOT invent tools.
Do NOT make business decisions that belong to the workflow.
Do NOT invent missing input values.

Registered workflows:

{workflow_context}

User request:

{user_request}

Return ONLY valid JSON.

The JSON must have exactly these fields:

{{
    "workflow_id": "WF001",
    "confidence": 0.95,
    "extracted_inputs": {{}},
    "reason": "Short explanation"
}}

GENERAL RULES:

1. workflow_id MUST be one of the registered workflow IDs.
2. If the request does not clearly match a workflow, return:
   "workflow_id": "NONE"
3. confidence must be between 0 and 1.
4. Extract ONLY information explicitly available in the user request.
5. Never invent missing values.
6. Use the exact input field names defined below.
7. Do not use alternative field names.
8. Keep the reason short.
9. Return valid JSON only. Do not use Markdown.

INPUT EXTRACTION RULES:

WF001 - Inventory Restock Check:
Use these fields when available:
- minimum_stock
- product_name
- sku

WF002 - Product Price Validation:
Use these fields when available:
- sku
- product_name

WF003 - Vendor File Processing:
Use these fields when available:
- vendor_file_path
- file_name

WF004 - Product Description Generator:
Use these exact field names when available:
- product_name
- category
- attributes
- material
- color
- target_audience

Example:
User:
"Generate product content for a blue cotton shirt for young professionals."

Return:
"extracted_inputs": {{
    "product_name": "blue cotton shirt",
    "material": "cotton",
    "color": "blue",
    "target_audience": "young professionals"
}}

Do NOT return:
"product": "blue cotton shirt"

Do NOT return:
"name": "blue cotton shirt"

Use "product_name".

WF005 - Customer Order Status:
Use these exact field names when available:
- order_id
- customer_email

Example:
User:
"What is the status of order ORD001?"

Return:
"extracted_inputs": {{
    "order_id": "ORD-1001"
}}

WF006 - Duplicate Product Detection:
Use these fields when available:
- product_name
- sku
- category

WF007 - Marketing Campaign Brief:
Use these exact field names when available:
- campaign_goal
- product_list
- target_audience
- promotion
- dates

Example:
User:
"Create a campaign for Blue Cotton Shirt. The goal is to
increase sales for young professionals. The promotion is
20% off from October 15 to October 30."

Return:
"extracted_inputs": {{
    "campaign_goal": "increase sales",
    "product_list": ["Blue Cotton Shirt"],
    "target_audience": "young professionals",
    "promotion": "20% off",
    "dates": "October 15 to October 30"
}}

WF008 - SEO Keyword Classification:
Use these fields when available:
- keyword_file_path
- keywords
- product
- category

WF009 - Employee Task Assignment:
Use these exact field names when available:
- task_description
- required_skills
- priority
- deadline

Example:
User:
"Assign a Python and Django task to the best available
employee. Priority is high and the deadline is October 15."

Return:
"extracted_inputs": {{
    "task_description": "Python and Django task",
    "required_skills": ["python", "django"],
    "priority": "high",
    "deadline": "October 15"
}}

WF010 - Workflow Performance Report:
Use these fields when available:
- workflow_id
- threshold
- date_range

IMPORTANT:

Only extract values that actually appear in the user request.

For example, if the user says:

"Generate content for a blue cotton shirt"

return:

"extracted_inputs": {{
    "product_name": "blue cotton shirt",
    "material": "cotton",
    "color": "blue"
}}

Do NOT invent:
- category
- target audience
- price
- size
- other attributes

If an input is not provided, simply leave it out of
extracted_inputs.

Return ONLY the JSON object.
"""

    @staticmethod
    def _format_workflows(
        workflows: list[WorkflowDefinition],
    ) -> str:

        formatted = []

        for workflow in workflows:

            formatted.append(
                f"""
Workflow ID: {workflow.workflow_id}
Name: {workflow.workflow_name}
Trigger: {workflow.trigger}
Inputs: {workflow.inputs}
Expected Output: {workflow.expected_output}
"""
            )

        return "\n".join(formatted)

    @staticmethod
    def _parse_response(
        response_text: str,
    ) -> WorkflowSelection:

        cleaned = response_text.strip()

        # Handle accidental Markdown JSON fences.
        if cleaned.startswith("```"):

            cleaned = cleaned.replace(
                "```json",
                "",
                1,
            )

            cleaned = cleaned.replace(
                "```",
                "",
            ).strip()

        try:
            data = json.loads(cleaned)

        except json.JSONDecodeError as exc:

            raise ValueError(
                "LLM returned invalid JSON."
            ) from exc

        return WorkflowSelection.model_validate(data)

    def _validate_selection(
        self,
        selection: WorkflowSelection,
    ) -> None:

        if selection.workflow_id == "NONE":
            return

        workflow = self.workflow_registry.get(
            selection.workflow_id
        )

        if workflow is None:

            raise ValueError(
                f"LLM selected unknown workflow: "
                f"{selection.workflow_id}"
            )

