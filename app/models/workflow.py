from pydantic import BaseModel, Field


class WorkflowDefinition(BaseModel):
    workflow_id: str = Field(min_length=1)
    workflow_name: str = Field(min_length=1)
    trigger: str = Field(min_length=1)
    inputs: str = Field(min_length=1)
    steps: str = Field(min_length=1)
    decision_logic: str = Field(min_length=1)
    tools_required: str = Field(min_length=1)
    expected_output: str = Field(min_length=1)