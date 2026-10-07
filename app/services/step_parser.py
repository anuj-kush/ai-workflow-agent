from app.models.execution import WorkflowStep


class StepParser:

    def parse(self, steps_text: str) -> list[WorkflowStep]:
        if not steps_text:
            return []

        raw_steps = steps_text.split("→")

        steps = []

        for index, step in enumerate(raw_steps, start=1):
            description = step.strip()

            if not description:
                continue

            steps.append(
                WorkflowStep(
                    step_number=index,
                    description=description,
                )
            )

        return steps