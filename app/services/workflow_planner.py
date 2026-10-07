from app.models.execution import WorkflowStep
from app.models.workflow import WorkflowDefinition
from app.services.step_parser import StepParser
from app.services.step_tool_mapper import StepToolMapper


class WorkflowPlanner:

    def __init__(
        self,
        step_parser: StepParser,
        step_tool_mapper: StepToolMapper,
    ):
        self.step_parser = step_parser
        self.step_tool_mapper = step_tool_mapper

    def create_plan(
        self,
        workflow: WorkflowDefinition,
    ) -> list[WorkflowStep]:

        steps = self.step_parser.parse(workflow.steps)

        if not steps:
            raise ValueError(
                f"Workflow {workflow.workflow_id} "
                "does not contain executable steps."
            )

        mapped_steps = self.step_tool_mapper.map_steps(
            steps,
            workflow_id=workflow.workflow_id,
        )

        return mapped_steps