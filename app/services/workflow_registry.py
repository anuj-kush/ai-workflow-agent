from app.models.workflow import WorkflowDefinition


class WorkflowRegistry:
    """
    Stores workflows by workflow ID.

    The registry provides fast lookup after workflows
    have been loaded from Excel.
    """

    def __init__(self, workflows: list[WorkflowDefinition]):
        self._workflows = {
            workflow.workflow_id: workflow
            for workflow in workflows
        }

    def get(self, workflow_id: str) -> WorkflowDefinition | None:
        """Return a workflow by ID."""

        return self._workflows.get(workflow_id)

    def get_all(self) -> list[WorkflowDefinition]:
        """Return all registered workflows."""

        return list(self._workflows.values())

    def count(self) -> int:
        """Return number of registered workflows."""

        return len(self._workflows)