from app.models.execution import WorkflowStep


class StepToolMapper:

    WORKFLOW_TOOL_RULES = {
        # WF001 - Inventory Restock Check
        "WF001": [
            (["load", "inventory"], "load_inventory"),
            (["compare", "stock"], "check_stock"),
            (["identify", "low-stock"], "identify_low_stock_products"),
            (["calculate", "reorder"], "calculate_reorder_quantity"),
            (["generate", "restock"], "generate_restock_list"),
        ],

        # WF002 - Product Price Validation
        "WF002": [
            (["load", "product", "prices"], "load_product_prices"),
            (["load", "vendor", "prices"], "load_vendor_prices"),
            (["match", "products", "sku"], "match_product_prices"),
            (
                ["compare", "internal", "vendor", "prices"],
                "compare_product_prices",
            ),
            (
                ["calculate", "percentage", "difference"],
                "calculate_price_difference",
            ),
            (["flag", "exceptions"], "generate_price_validation_report"),
        ],

        # WF003 - Vendor File Processing
        "WF003": [
            (["read", "vendor", "file"], "read_vendor_file"),
            (["detect", "columns"], "detect_vendor_columns"),
            (
                ["normalize", "column", "names"],
                "normalize_vendor_columns",
            ),
            (
                ["validate", "required", "fields"],
                "validate_vendor_fields",
            ),
            (
                ["identify", "invalid", "rows"],
                "identify_invalid_vendor_rows",
            ),
            (
                ["produce", "cleaned", "dataset"],
                "create_cleaned_vendor_dataset",
            ),
        ],

        # WF004 - Product Description Generator
        "WF004": [
            (
                ["validate", "required", "attributes"],
                "validate_product_attributes",
            ),
            (
                ["create", "product", "description"],
                "generate_product_description",
            ),
            (
                ["generate", "short", "description"],
                "generate_short_description",
            ),
            (
                ["generate", "seo", "title"],
                "generate_seo_title",
            ),
            (
                ["generate", "meta", "description"],
                "generate_meta_description",
            ),
        ],

        # WF005 - Customer Order Status
        "WF005": [
            (["validate", "identifier"], "validate_order_identifier"),
            (["search", "order", "data"], "search_order"),
            (["retrieve", "order", "status"], "get_order_status"),
            (
                ["retrieve", "shipment", "information"],
                "get_shipment_information",
            ),
            (
                ["summarize", "current", "status"],
                "summarize_order_status",
            ),
        ],

        # WF006 - Duplicate Product Detection
        "WF006": [
            (
                ["load", "product", "catalog"],
                "load_product_catalog",
            ),
            (
                ["normalize", "names", "skus"],
                "normalize_product_identifiers",
            ),
            (
                ["compare", "identifiers"],
                "compare_product_identifiers",
            ),
            (
                ["compare", "product", "attributes"],
                "compare_product_attributes",
            ),
            (
                ["group", "likely", "duplicates"],
                "group_duplicate_products",
            ),
            (
                ["assign", "confidence"],
                "assign_duplicate_confidence",
            ),
        ],

        # WF007 - Marketing Campaign Brief
        "WF007": [
            (["validate", "inputs"], "validate_campaign_inputs"),
            (
                ["identify", "campaign", "objective"],
                "identify_campaign_objective",
            ),
            (
                ["summarize", "products"],
                "summarize_campaign_products",
            ),
            (
                ["create", "messaging"],
                "generate_campaign_messaging",
            ),
            (
                ["create", "channel", "recommendations"],
                "generate_channel_recommendations",
            ),
            (
                ["create", "campaign", "checklist"],
                "generate_campaign_checklist",
            ),
        ],

        # WF008 - SEO Keyword Classification
        "WF008": [
            (["read", "keywords"], "load_keywords"),
            (
                ["remove", "duplicates"],
                "remove_duplicate_keywords",
            ),
            (
                ["classify", "search", "intent"],
                "classify_keyword_intent",
            ),
            (
                ["map", "keywords", "categories"],
                "map_keywords_to_categories",
            ),
            (
                ["identify", "high-priority", "keywords"],
                "identify_priority_keywords",
            ),
            (["export", "results"], "export_keyword_report"),
        ],

        # WF009 - Employee Task Assignment
        "WF009": [
            (
                ["understand", "task", "requirements"],
                "understand_task_requirements",
            ),
            (
                ["compare", "employee", "skills"],
                "compare_employee_skills",
            ),
            (
                ["check", "current", "workload"],
                "check_employee_workload",
            ),
            (["rank", "candidates"], "rank_employees"),
            (["select", "employee"], "select_employee"),
            (
                ["generate", "assignment", "summary"],
                "generate_assignment_summary",
            ),
        ],

        # WF010 - Workflow Performance Report
        "WF010": [
            (
                ["load", "execution", "logs"],
                "load_execution_logs",
            ),
            (
                ["calculate", "success/failure", "rate"],
                "calculate_workflow_metrics",
            ),
            (
                ["calculate", "average", "execution", "time"],
                "calculate_average_execution_time",
            ),
            (
                ["identify", "frequent", "errors"],
                "identify_frequent_errors",
            ),
            (
                ["identify", "slow", "steps"],
                "identify_slow_steps",
            ),
            (
                ["generate", "recommendations"],
                "generate_performance_recommendations",
            ),
        ],
    }

    def map_step(
        self,
        step: WorkflowStep,
        workflow_id: str,
    ) -> WorkflowStep:

        rules = self.WORKFLOW_TOOL_RULES.get(workflow_id)

        if not rules:
            raise ValueError(
                f"No tool mapping rules found for {workflow_id}"
            )

        description = step.description.lower()

        for keywords, tool_name in rules:

            if all(
                keyword in description
                for keyword in keywords
            ):
                step.tool_name = tool_name
                return step

        raise ValueError(
            f"No tool mapping found for {workflow_id} step: "
            f"{step.description}"
        )

    def map_steps(
        self,
        steps: list[WorkflowStep],
        workflow_id: str,
    ) -> list[WorkflowStep]:

        if not workflow_id:
            raise ValueError(
                "workflow_id is required for tool mapping."
            )

        return [
            self.map_step(
                step,
                workflow_id,
            )
            for step in steps
        ]