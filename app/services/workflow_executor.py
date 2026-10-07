
from app.models.execution import ExecutionResult, StepResult
from app.models.workflow import WorkflowDefinition
from app.services.tool_registry import ToolRegistry


class WorkflowExecutor:
    def __init__(self, tool_registry: ToolRegistry):
        self.tool_registry = tool_registry

    def execute(
        self,
        workflow: WorkflowDefinition,
        steps: list,
        context: dict,
    ) -> ExecutionResult:

        execution_steps = []

        try:
            for step in steps:

                if not step.tool_name:
                    raise ValueError(
                        f"No tool assigned to step {step.step_number}: "
                        f"{step.description}"
                    )

                tool = self.tool_registry.get(step.tool_name)

                output = tool(context)

                # Handle workflows that require additional information.
                if (
                    isinstance(output, dict)
                    and output.get("status") == "missing_information"
                ):
                    execution_steps.append(
                        StepResult(
                            step_number=step.step_number,
                            step_name=step.description,
                            tool_name=step.tool_name,
                            status="needs_input",
                            output=str(output),
                        )
                    )

                    return ExecutionResult(
                        workflow_id=workflow.workflow_id,
                        workflow_name=workflow.workflow_name,
                        status="needs_input",
                        steps=execution_steps,
                        final_output=output.get(
                            "message",
                            "Additional information is required.",
                        ),
                    )

                execution_steps.append(
                    StepResult(
                        step_number=step.step_number,
                        step_name=step.description,
                        tool_name=step.tool_name,
                        status="success",
                        output=str(output),
                    )
                )

            final_output = context.get(
                "final_output",
                "Workflow completed successfully.",
            )

            return ExecutionResult(
                workflow_id=workflow.workflow_id,
                workflow_name=workflow.workflow_name,
                status="success",
                steps=execution_steps,
                final_output=str(final_output),
            )

        except Exception as exc:
            execution_steps.append(
                StepResult(
                    step_number=len(execution_steps) + 1,
                    step_name="Execution failed",
                    tool_name=None,
                    status="failed",
                    output=str(exc),
                )
            )

            return ExecutionResult(
                workflow_id=workflow.workflow_id,
                workflow_name=workflow.workflow_name,
                status="failed",
                steps=execution_steps,
                error=str(exc),
            )

