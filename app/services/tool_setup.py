from app.services.tool_registry import ToolRegistry

from app.tools.inventory_tools import (
    load_inventory,
    check_stock,
    identify_low_stock_products,
    calculate_reorder_quantity,
    generate_restock_list,
)

from app.tools.price_tools import (
    load_product_prices,
    load_vendor_prices,
    match_product_prices,
    compare_product_prices,
    calculate_price_difference,
    generate_price_validation_report,
)

from app.tools.vendor_tools import (
    read_vendor_file,
    detect_vendor_columns,
    normalize_vendor_columns,
    validate_vendor_fields,
    identify_invalid_vendor_rows,
    create_cleaned_vendor_dataset,
)

from app.tools.product_content_tools import (
    validate_product_attributes,
    generate_product_description,
    generate_short_description,
    generate_seo_title,
    generate_meta_description,
)

from app.tools.order_tools import (
    validate_order_identifier,
    search_order,
    get_order_status,
    get_shipment_information,
    summarize_order_status,
)

from app.tools.duplicate_tools import (
    load_product_catalog,
    normalize_product_identifiers,
    compare_product_identifiers,
    compare_product_attributes,
    group_duplicate_products,
    assign_duplicate_confidence,
)

from app.tools.marketing_tools import (
    validate_campaign_inputs,
    identify_campaign_objective,
    summarize_campaign_products,
    generate_campaign_messaging,
    generate_channel_recommendations,
    generate_campaign_checklist,
)

from app.tools.seo_tools import (
    load_keywords,
    remove_duplicate_keywords,
    classify_keyword_intent,
    map_keywords_to_categories,
    identify_priority_keywords,
    export_keyword_report,
)

from app.tools.employee_tools import (
    understand_task_requirements,
    compare_employee_skills,
    check_employee_workload,
    rank_employees,
    select_employee,
    generate_assignment_summary,
)

from app.tools.performance_tools import (
    load_execution_logs,
    calculate_workflow_metrics,
    calculate_average_execution_time,
    identify_frequent_errors,
    identify_slow_steps,
    generate_performance_recommendations,
)


def create_tool_registry() -> ToolRegistry:

    registry = ToolRegistry()

    # WF001
    registry.register("load_inventory", load_inventory)
    registry.register("check_stock", check_stock)
    registry.register(
        "identify_low_stock_products",
        identify_low_stock_products,
    )
    registry.register(
        "calculate_reorder_quantity",
        calculate_reorder_quantity,
    )
    registry.register(
        "generate_restock_list",
        generate_restock_list,
    )

    # WF002
    registry.register("load_product_prices", load_product_prices)
    registry.register("load_vendor_prices", load_vendor_prices)
    registry.register(
        "match_product_prices",
        match_product_prices,
    )
    registry.register(
        "compare_product_prices",
        compare_product_prices,
    )
    registry.register(
        "calculate_price_difference",
        calculate_price_difference,
    )
    registry.register(
        "generate_price_validation_report",
        generate_price_validation_report,
    )

    # WF003
    registry.register(
        "read_vendor_file",
        read_vendor_file,
    )
    registry.register(
        "detect_vendor_columns",
        detect_vendor_columns,
    )
    registry.register(
        "normalize_vendor_columns",
        normalize_vendor_columns,
    )
    registry.register(
        "validate_vendor_fields",
        validate_vendor_fields,
    )
    registry.register(
        "identify_invalid_vendor_rows",
        identify_invalid_vendor_rows,
    )
    registry.register(
        "create_cleaned_vendor_dataset",
        create_cleaned_vendor_dataset,
    )

    # WF004
    registry.register(
        "validate_product_attributes",
        validate_product_attributes,
    )
    registry.register(
        "generate_product_description",
        generate_product_description,
    )
    registry.register(
        "generate_short_description",
        generate_short_description,
    )
    registry.register(
        "generate_seo_title",
        generate_seo_title,
    )
    registry.register(
        "generate_meta_description",
        generate_meta_description,
    )

    # WF005
    registry.register(
        "validate_order_identifier",
        validate_order_identifier,
    )
    registry.register("search_order", search_order)
    registry.register("get_order_status", get_order_status)
    registry.register(
        "get_shipment_information",
        get_shipment_information,
    )
    registry.register(
        "summarize_order_status",
        summarize_order_status,
    )

    # WF006
    registry.register(
        "load_product_catalog",
        load_product_catalog,
    )
    registry.register(
        "normalize_product_identifiers",
        normalize_product_identifiers,
    )
    registry.register(
        "compare_product_identifiers",
        compare_product_identifiers,
    )
    registry.register(
        "compare_product_attributes",
        compare_product_attributes,
    )
    registry.register(
        "group_duplicate_products",
        group_duplicate_products,
    )
    registry.register(
        "assign_duplicate_confidence",
        assign_duplicate_confidence,
    )

    # WF007
    registry.register(
        "validate_campaign_inputs",
        validate_campaign_inputs,
    )
    registry.register(
        "identify_campaign_objective",
        identify_campaign_objective,
    )
    registry.register(
        "summarize_campaign_products",
        summarize_campaign_products,
    )
    registry.register(
        "generate_campaign_messaging",
        generate_campaign_messaging,
    )
    registry.register(
        "generate_channel_recommendations",
        generate_channel_recommendations,
    )
    registry.register(
        "generate_campaign_checklist",
        generate_campaign_checklist,
    )

    # WF008
    registry.register("load_keywords", load_keywords)
    registry.register(
        "remove_duplicate_keywords",
        remove_duplicate_keywords,
    )
    registry.register(
        "classify_keyword_intent",
        classify_keyword_intent,
    )
    registry.register(
        "map_keywords_to_categories",
        map_keywords_to_categories,
    )
    registry.register(
        "identify_priority_keywords",
        identify_priority_keywords,
    )
    registry.register(
        "export_keyword_report",
        export_keyword_report,
    )

    # WF009
    registry.register(
        "understand_task_requirements",
        understand_task_requirements,
    )
    registry.register(
        "compare_employee_skills",
        compare_employee_skills,
    )
    registry.register(
        "check_employee_workload",
        check_employee_workload,
    )
    registry.register("rank_employees", rank_employees)
    registry.register("select_employee", select_employee)
    registry.register(
        "generate_assignment_summary",
        generate_assignment_summary,
    )

    # WF010
    registry.register(
        "load_execution_logs",
        load_execution_logs,
    )
    registry.register(
        "calculate_workflow_metrics",
        calculate_workflow_metrics,
    )
    registry.register(
        "calculate_average_execution_time",
        calculate_average_execution_time,
    )
    registry.register(
        "identify_frequent_errors",
        identify_frequent_errors,
    )
    registry.register(
        "identify_slow_steps",
        identify_slow_steps,
    )
    registry.register(
        "generate_performance_recommendations",
        generate_performance_recommendations,
    )

    return registry