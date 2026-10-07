from pydantic import BaseModel, Field


class WorkflowStep(BaseModel):
    step_number: int
    description: str
    tool_name: str | None = None


class StepResult(BaseModel):
    step_number: int
    step_name: str
    tool_name: str | None = None
    status: str
    output: str = ""


class ExecutionResult(BaseModel):
    workflow_id: str
    workflow_name: str
    status: str
    steps: list[StepResult] = Field(default_factory=list)
    final_output: str = ""
    error: str | None = None