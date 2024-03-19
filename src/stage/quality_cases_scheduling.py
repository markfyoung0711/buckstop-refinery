data_structures = {
    "production_schedule_report": {
        "order_details": {
            "order_number": "string",
            "customer_name": "string",
            "order_quantity": "integer",
            "specifications": "string",
        },
        "production_schedule": {
            "planned_start_date": "date",
            "planned_end_date": "date",
            "scheduled_tasks": ["string"],
        },
        "resource_allocation": {
            "equipment_assigned": ["string"],
            "production_line": "string",
            "labor_assigned": ["string"],
        },
    },
    "wip_status_report": {
        "work_order_details": {
            "work_order_number": "string",
            "customer_order": "string",
            "product_details": "string",
        },
        "wip_inventory": {
            "production_stage": "string",
            "quantity": "integer",
            "percentage_completion": "float",
            "estimated_completion_date": "date",
        },
    },
    "quality_control_metrics_dashboard": {
        "inspection_results": {"defects": ["string"], "inspection_date": "date"},
        "rework_data": {
            "rework_order_number": "string",
            "reasons_for_rework": "string",
            "rework_completion_date": "date",
        },
        "first_pass_yield": {"pass_count": "integer", "total_count": "integer"},
    },
    "resource_utilization_efficiency_report": {
        "equipment_utilization": {
            "machine": "string",
            "uptime": "float",
            "downtime": "float",
            "idle_time": "float",
            "setup_time": "float",
        },
        "labor_productivity": {
            "labor_hours_worked": "float",
            "labor_hours_per_case": "float",
        },
        "material_usage": {
            "material": "string",
            "quantity_used": "float",
            "scrap_rate": "float",
            "material_waste": "float",
        },
    },
    "customer_order_fulfillment_report": {
        "order_details": {
            "order_number": "string",
            "customer_name": "string",
            "order_date": "date",
            "requested_delivery_date": "date",
        },
        "order_status": "string",
        "delivery_performance": {
            "actual_delivery_date": "date",
            "on_time_delivery": "boolean",
        },
    },
    "material_inventory_procurement_report": {
        "inventory_levels": {"material": "string", "inventory_level": "integer"},
        "stockouts": {"material": "string", "stockout_date": "date"},
        "procurement_data": {
            "supplier": "string",
            "purchase_order_number": "string",
            "lead_time": "integer",
            "order_quantity": "integer",
        },
    },
    "sales_revenue_analysis": {
        "sales_data": {"order_number": "string", "revenue_generated": "float"},
        "order_trends": {
            "period": "date",
            "order_volume": "integer",
            "order_value": "float",
        },
        "customer_segmentation": {"segment": "string", "sales": "float"},
    },
    "custom_case_design_engineering_report": {
        "design_parameters": {
            "case_specifications": "string",
            "dimensions": "string",
            "materials": "string",
        },
        "design_revisions": {
            "revision_number": "integer",
            "reason_for_change": "string",
            "approval_status": "string",
        },
        "engineering_data": {
            "cad_cam_files": ["string"],
            "bom": ["string"],
            "design_feedback": "string",
        },
    },
    "customer_feedback_satisfaction_survey_results": {
        "customer_feedback": {
            "survey_date": "date",
            "ratings": "integer",
            "comments": "string",
        },
        "satisfaction_scores": {"nps_score": "integer", "csi_score": "integer"},
        "improvement_suggestions": "string",
    },
    "operational_kpis_dashboard": {
        "kpi_metrics": {
            "oee": "float",
            "cycle_time": "float",
            "lead_time": "float",
            "production_yield": "float",
            "scrap_rates": "float",
            "rework_rates": "float",
            "customer_complaints": "integer",
        }
    },
    "continuous_improvement_initiatives_tracking_report": {
        "improvement_initiatives": {
            "project_details": "string",
            "objectives": "string",
            "milestones": ["string"],
            "timeline": "string",
        },
        "progress_updates": {
            "status": "string",
            "progress": "float",
            "completion_status": "string",
        },
        "impact_assessment": {"metrics": "string", "impact": "string"},
    },
}
