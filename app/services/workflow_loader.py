from pathlib import Path

import pandas as pd

from app.models.workflow import WorkflowDefinition


REQUIRED_COLUMNS = {
    "Workflow_ID",
    "Workflow_Name",
    "Trigger",
    "Inputs",
    "Steps",
    "Decision_Logic",
    "Tools_Required",
    "Expected_Output",
}


class WorkflowLoader:
    """Loads workflow definitions from the Excel source file."""

    def __init__(self, excel_path: str | Path):
        self.excel_path = Path(excel_path)

    def load(self) -> list[WorkflowDefinition]:
        """Read Excel and convert each row into a WorkflowDefinition."""

        if not self.excel_path.exists():
            raise FileNotFoundError(
                f"Workflow Excel file not found: {self.excel_path}"
            )

        dataframe = pd.read_excel(self.excel_path)

        self._validate_columns(dataframe)

        workflows = []

        for _, row in dataframe.iterrows():
            workflow = WorkflowDefinition(
                workflow_id=self._clean_value(row["Workflow_ID"]),
                workflow_name=self._clean_value(row["Workflow_Name"]),
                trigger=self._clean_value(row["Trigger"]),
                inputs=self._clean_value(row["Inputs"]),
                steps=self._clean_value(row["Steps"]),
                decision_logic=self._clean_value(row["Decision_Logic"]),
                tools_required=self._clean_value(row["Tools_Required"]),
                expected_output=self._clean_value(row["Expected_Output"]),
            )

            workflows.append(workflow)

        return workflows

    @staticmethod
    def _clean_value(value) -> str:
        """Convert Excel cell values into clean strings."""

        if pd.isna(value):
            return ""

        return str(value).strip()

    @staticmethod
    def _validate_columns(dataframe: pd.DataFrame) -> None:
        """Ensure the Excel contains all required columns."""

        actual_columns = set(dataframe.columns)

        missing_columns = REQUIRED_COLUMNS - actual_columns

        if missing_columns:
            raise ValueError(
                "Missing required Excel columns: "
                + ", ".join(sorted(missing_columns))
            )