
class DecisionEngine:

    def evaluate(
        self,
        decision_logic: str,
        context: dict,
    ) -> dict:

        logic = decision_logic.lower()

        if (
            "current_stock" in logic
            and "minimum_stock" in logic
        ):
            return self._stock_decision(context)

        if (
            "price difference" in logic
            and "10%" in logic
        ):
            return self._price_decision(context)

        if (
            "missing sku" in logic
            or "product name" in logic
        ):
            return self._vendor_decision(context)

        if "do not invent" in logic:
            return self._content_decision(context)

        if "no order is found" in logic:
            return self._order_decision(context)

        if "exact sku" in logic:
            return self._duplicate_decision(context)

        if (
            "campaign goal" in logic
            or "campaign dates" in logic
        ):
            return self._campaign_decision(context)

        if "informational" in logic:
            return self._keyword_decision(context)

        if "available capacity" in logic:
            return self._employee_decision(context)

        if (
            "failure rate" in logic
            or "execution time" in logic
        ):
            return self._performance_decision(context)

        return {
            "decision": "not_evaluated",
            "message": "No supported decision rule matched.",
        }

    def _stock_decision(self, context):
        dataframe = context.get(
            "inventory_checked"
        )

        if dataframe is None:
            raise ValueError(
                "Inventory data unavailable."
            )

        count = int(
            dataframe["needs_restock"].sum()
        )

        return {
            "decision": (
                "restock_required"
                if count > 0
                else "no_restock"
            ),
            "count": count,
        }

    def _price_decision(self, context):
        dataframe = context.get(
            "price_comparison"
        )

        if dataframe is None:
            raise ValueError(
                "Price comparison data unavailable."
            )

        exceptions = dataframe[
            dataframe["difference_percentage"] > 10
        ]

        return {
            "decision": (
                "exceptions_found"
                if not exceptions.empty
                else "no_exceptions"
            ),
            "exception_count": len(exceptions),
        }

    def _vendor_decision(self, context):
        invalid = context.get(
            "invalid_vendor_rows"
        )

        return {
            "decision": (
                "invalid_rows_found"
                if invalid is not None
                and not invalid.empty
                else "all_rows_valid"
            ),
            "invalid_count": (
                len(invalid)
                if invalid is not None
                else 0
            ),
        }

    def _content_decision(self, context):
        missing = context.get(
            "missing_product_attributes",
            [],
        )

        return {
            "decision": (
                "missing_information"
                if missing
                else "attributes_complete"
            ),
            "missing_attributes": missing,
        }

    def _order_decision(self, context):
        order = context.get("order")

        return {
            "decision": (
                "order_found"
                if order
                else "order_not_found"
            )
        }

    def _duplicate_decision(self, context):
        groups = context.get(
            "duplicate_groups",
            [],
        )

        return {
            "decision": (
                "duplicates_found"
                if groups
                else "no_duplicates"
            ),
            "count": len(groups),
        }

    def _campaign_decision(self, context):
        missing = context.get(
            "campaign_missing",
            [],
        )

        return {
            "decision": (
                "request_missing_inputs"
                if missing
                else "inputs_valid"
            ),
            "missing_inputs": missing,
        }

    def _keyword_decision(self, context):
        dataframe = context.get(
            "classified_keywords"
        )

        return {
            "decision": "classification_completed",
            "classified_count": (
                len(dataframe)
                if dataframe is not None
                else 0
            ),
            "allowed_intents": [
                "informational",
                "commercial",
                "transactional",
                "navigational",
            ],
        }

    def _employee_decision(self, context):
        selected = context.get(
            "selected_employee"
        )

        return {
            "decision": (
                "employee_selected"
                if selected
                else "escalate"
            ),
            "employee": (
                selected["employee_name"]
                if selected
                else None
            ),
        }

    def _performance_decision(self, context):
        flagged = []

        # workflow_metrics is stored as a Pandas DataFrame
        metrics = context.get(
            "workflow_metrics"
        )

        # execution_averages is also stored as a DataFrame
        averages = context.get(
            "execution_averages"
        )

        if metrics is None:
            raise ValueError(
                "Workflow performance metrics unavailable."
            )

        if averages is None:
            raise ValueError(
                "Average execution times unavailable."
            )

        # Convert average execution times into a simple lookup dictionary.
        average_lookup = dict(
            zip(
                averages["workflow_id"],
                averages["average_execution_time"],
            )
        )

        for _, metric in metrics.iterrows():

            workflow_id = metric["workflow_id"]

            failure_rate = float(
                metric["failure_rate"]
            )

            average_execution_time = float(
                average_lookup.get(
                    workflow_id,
                    0,
                )
            )

            if (
                failure_rate > 10
                or average_execution_time > 5
            ):
                flagged.append(workflow_id)

        return {
            "decision": (
                "performance_issues_found"
                if flagged
                else "performance_acceptable"
            ),
            "flagged_workflows": flagged,
        }

