# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "payware"
app_title = "Payware"
app_publisher = "Aakvatech"
app_description = "Payware Payroll System"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@aakvatech.com"
app_license = "GNU General Public License (v3)"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/payware/css/payware.css"
# app_include_js = "/assets/payware/js/payware.js"

# include js, css files in header of web template
# web_include_css = "/assets/payware/css/payware.css"
# web_include_js = "/assets/payware/js/payware.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Loan": "payware/loan.js",
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "payware.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "payware.install.before_install"
# after_install = "payware.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "payware.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                (
                    "Additional Salary-auto_created_based_on",
                    "Additional Salary-auto_repeat_details",
                    "Additional Salary-auto_repeat_end_date",
                    "Additional Salary-auto_repeat_frequency",
                    "Additional Salary-based_on_hourly_rate",
                    "Additional Salary-column_break_15",
                    "Additional Salary-column_break_19",
                    "Additional Salary-hourly_rate",
                    "Additional Salary-last_transaction_amount",
                    "Additional Salary-last_transaction_date",
                    "Additional Salary-last_transaction_details",
                    "Additional Salary-no_of_hours",
                    "Additional Salary-section_break_17",
                    "Employee-area",
                    "Employee-attachments",
                    "Employee-bank_code",
                    "Employee-biometric_code",
                    "Employee-biometric_id",
                    "Employee-column_break_49",
                    "Employee-column_break_50",
                    "Employee-column_break_54",
                    "Employee-employee_ot_component",
                    "Employee-enable_biometric",
                    "Employee-files",
                    "Employee-national_identity",
                    "Employee-other_allowance",
                    "Employee-overtime_components",
                    "Employee-pension_fund_number",
                    "Employee-pension_fund",
                    "Employee-statutory_details",
                    "Employee-tin_number",
                    "Employee-wcf_number",
                    "Employee-worker_subsistence",
                    "Loan-loan_repayments_not_from_salary",
                    "Loan-not_from_salary_loan_repayments",
                    "Loan-total_nsf_repayments",
                    "Payroll Entry-bank_account_for_transfer",
                    "Payroll Entry-bank_payment_details",
                    "Payroll Entry-cheque_date",
                    "Payroll Entry-cheque_number",
                    "Payroll Entry-column_break_34",
                    "Payroll Entry-section_break_35",
                    "Repayment Schedule-change_amount",
                    "Repayment Schedule-changed_interest_amount",
                    "Repayment Schedule-changed_principal_amount",
                    "Salary Component-based_on_hourly_rate",
                    "Salary Component-column_break_16",
                    "Salary Component-create_cash_journal",
                    "Salary Component-hourly_rate",
                    "Salary Component-payware_specifics",
                    "Salary Component-sdl_emolument_category",
                    "Salary Slip-overtime_components",
                    "Salary Slip-salary_slip_ot_component",
                ),
            ]
        ],
    },
    {
        "doctype": "Property Setter",
        "filters": [
            [
                "name",
                "in",
                (
                    "Additional Salary-naming_series-options",
                    "Additional Salary-overwrite_salary_structure_amount-default",
                    "Attendance-leave_type-allow_on_submit",
                    "Attendance-main-track_changes",
                    "Attendance-status-allow_on_submit",
                    "Employee-company-in_list_view",
                    "Employee-department-permlevel",
                    "Employee-image-hidden",
                    "Employee-job_profile-permlevel",
                    "Employee-main-track_changes",
                    "Leave Application-naming_series-options",
                    "Loan-applicant_name-in_list_view",
                    "Loan-applicant_name-in_standard_filter",
                    "Loan-loan_amount-in_list_view",
                    "Loan-loan_type-in_list_view",
                    "Loan-loan_type-in_standard_filter",
                    "Loan-posting_date-in_list_view",
                    "Loan-repay_from_salary-allow_on_submit",
                    "Loan-repayment_method-options",
                    "Loan-search_fields",
                    "Loan-status-in_list_view",
                    "Loan-status-in_standard_filter",
                    "Payroll Entry-branch-in_list_view",
                    "Payroll Entry-company-in_standard_filter",
                    "Payroll Entry-company-print_width",
                    "Payroll Entry-end_date-in_list_view",
                    "Payroll Entry-posting_date-in_list_view",
                    "Salary Structure Assignment-base-in_list_view",
                    "Salary Structure Assignment-company-in_standard_filter",
                    "Salary Structure Assignment-employee-in_list_view",
                    "Salary Structure-deductions-allow_on_submit",
                    "Salary Structure-earnings-allow_on_submit",
                    "Repayment Schedule-payment_date-read_only",
                ),
            ]
        ],
    },
]

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Loan": {"validate": "payware.payware.utils.validate_loan"},
    "Salary Slip": {
        "on_submit": "payware.payware.utils.set_loan_paid",
        "on_cancel": "payware.payware.utils.set_loan_paid",
        "before_insert": "payware.payware.salary_slip_hook.generate_component_in_salary_slip_insert",
        "before_save": "payware.payware.salary_slip_hook.generate_component_in_salary_slip_update",
    },
    "Loan Repayment Not From Salary": {
        "on_submit": "payware.payware.utils.create_loan_repayment_jv",
        "validate": "payware.payware.utils.validate_loan_repayment_nfs",
        "on_cancel": "payware.payware.utils.create_loan_repayment_jv",
    },
    "Additional Salary": {
        "on_submit": "payware.payware.utils.create_additional_salary_journal",
        "on_cancel": "payware.payware.utils.create_additional_salary_journal",
        "before_validate": "payware.payware.utils.set_employee_base_salary_in_hours",
    },
    "Employee": {
        "validate": "payware.payware.doctype.biometric_settings.biometric_settings.check_employee_bio_info"
    },
}

# Scheduled Tasks
# ---------------

scheduler_events = {
    # 	"all": [
    # 		"payware.tasks.all"
    # 	],
    "daily": [
        "payware.payware.utils.generate_additional_salary_records",
        "payware.payware.doctype.biometric_settings.biometric_settings.auto_shift_assignment_for_active_today",
    ],
    "hourly": [
        "payware.payware.doctype.biometric_settings.biometric_settings.auto_get_transactions",
        "payware.payware.doctype.biometric_settings.biometric_settings.auto_make_employee_checkin",
    ]
    # 	"weekly": [
    # 		"payware.tasks.weekly"
    # 	]
    # 	"monthly": [
    # 		"payware.tasks.monthly"
    # 	]
}

# Testing
# -------

# before_tests = "payware.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "payware.event.get_events"
# }
