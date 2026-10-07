from pydantic import BaseModel, Field


class WorkflowSelection(BaseModel):
    """
    Structured result returned by the workflow-selection LLM.
    """

    workflow_id: str = Field(
        description="ID of the selected workflow, such as WF001."
    )

    confidence: float = Field(
        ge=0.0,
        le=1.0,
        description="Confidence that the selected workflow is correct."
    )

    extracted_inputs: dict = Field(
        default_factory=dict,
        description="Inputs extracted from the user's request."
    )

    reason: str = Field(
        description="Short explanation for the workflow selection."
    )