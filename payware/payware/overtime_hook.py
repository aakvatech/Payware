from __future__ import unicode_literals
import json
import frappe
from frappe.model.document import Document
from dateutil.relativedelta import relativedelta
from frappe.utils import get_first_day, getdate, flt, add_to_date, rounded, time_diff_in_hours ,get_first_day_of_week
from frappe import _
from erpnext.hr.doctype.employee.employee import is_holiday
from calendar import monthrange
from payware.payware.doctype.payware_settings import payware_settings
from frappe.desk.form.linked_with import get_linked_docs, get_linked_doctypes


def validate_min_overtime(overtime):
    if overtime >= payware_settings.get_min_overtime():
        return overtime
    else:
        return 0

def validate_daily_overtime(overtime):
    if payware_settings.get_max_daily() == 0:
        return overtime
    if overtime <= payware_settings.get_max_daily():
        return overtime
    else:
        return payware_settings.get_max_daily()


def validate_weekly_overtime(emp_name, overtime,date):
    max_weekly = payware_settings.get_max_weekly()
    if max_weekly== 0:
        return overtime
    start_week_date = get_first_day_of_week(date)
    sum_overtime = get_sum_overtime(emp_name,start_week_date,date)
    full_overtime = overtime + sum_overtime
    if full_overtime <= max_weekly:
        return overtime
    elif  sum_overtime <= max_weekly:
        return max_weekly - sum_overtime
    else:
        return 0
        


def validate_monthly_overtime(emp_name, overtime,date):
    max_monthly = payware_settings.get_max_monthly()
    if max_monthly == 0:
        return overtime
    start_month_date = get_first_day(date)
    sum_overtime = get_sum_overtime(emp_name,start_month_date,date)
    full_overtime = overtime + sum_overtime
    if full_overtime <= max_monthly:
        return overtime
    elif  sum_overtime <= max_monthly:
        return max_monthly - sum_overtime
    else:
        return 0


def get_sum_overtime(emp_name,start_date,end_date):
    frappe.msgprint(str(emp_name)+" "+str(start_date)+" "+str(end_date))
    query = """select sum(overtime_normal) as overtime_normal, sum(overtime_holidays) as overtime_holidays
		from `tabAttendance` where
		attendance_date between %(from_date)s and %(to_date)s
		and docstatus < 2 and employee = %(employee)s"""
    overtime_sums = frappe.db.sql(query, {"from_date":start_date, "to_date":end_date, "employee":emp_name}, as_dict=True)

    sum_overtime_normal = overtime_sums[0]["overtime_normal"]
    sum_overtime_holidays = overtime_sums[0]["overtime_holidays"]

    return sum_overtime_normal + sum_overtime_holidays

	
def validate_maximum_overtime_for_employee(emp_name, overtime, date):
    overtime = validate_min_overtime(overtime)
    overtime = validate_daily_overtime(overtime)
    overtime = validate_weekly_overtime(emp_name, overtime, date)
    overtime = validate_monthly_overtime(emp_name, overtime, date)
    return overtime


def time_diff_in_hour(start, end):
	return round((end-start).total_seconds() / 3600, 1)


def get_chekout_time(doctype,docname):
    linkinfo = get_linked_doctypes(doctype)
    linked_doc = get_linked_docs(doctype,docname,linkinfo)
    if linked_doc:
        for key, value in linked_doc.items() :
            if key != "Activity Log" and key == "Employee Checkin":
                for val in value:
                    log_type = frappe.db.get_value("Employee Checkin", val.name, "log_type")
                    if log_type == "OUT":
                        return frappe.db.get_value("Employee Checkin", val.name, "time")


def get_chekin_time(doctype,docname):
    linkinfo = get_linked_doctypes(doctype)
    linked_doc = get_linked_docs(doctype,docname,linkinfo)
    if linked_doc:
        for key, value in linked_doc.items() :
            if key != "Activity Log" and key == "Employee Checkin":
                for val in value:
                    log_type = frappe.db.get_value("Employee Checkin", val.name, "log_type")
                    if log_type == "IN":
                        return frappe.db.get_value("Employee Checkin", val.name, "time")
                    




@frappe.whitelist()
def calculate_overtime(doc, method):
    if not payware_settings.get_enable_overtime() :
        return
    if frappe.db.get_value("Shift Type", doc.shift, "determine_check_in_and_check_out") != 'Strictly based on Log Type in Employee Checkin':
        return
    overtime = 0
    holiday = is_holiday(doc.employee, doc.attendance_date)
    start_time = frappe.db.get_value("Shift Type", doc.shift, "start_time")
    end_time = frappe.db.get_value("Shift Type", doc.shift, "end_time")
    shift_duration = time_diff_in_hour(start_time, end_time)

    if payware_settings.get_overtime_mode() == "Checkout Time":
        frappe.msgprint("Checkout Time")
        employee_checkout_time=get_chekout_time(doc.doctype,doc.name)
        if not employee_checkout_time:
            return
        employee_checkin_time=get_chekin_time(doc.doctype,doc.name)
        if not employee_checkin_time:
            return
        employee_checkin_date=getdate(employee_checkin_time)
        supposed_employee_checkin_time = str(employee_checkin_date)+ " " + str(start_time)
        supposed_employee_checkout_time = add_to_date(date = supposed_employee_checkin_time, hours = shift_duration)

        overtime = flt(time_diff_in_hours(employee_checkout_time, supposed_employee_checkout_time),2)

        if overtime < 0:
            return
        overtime = validate_maximum_overtime_for_employee(doc.employee, overtime, doc.attendance_date)
        if not holiday:
            frappe.msgprint("overtime_normal" +" "+ str(overtime))
            # doc.overtime_normal = overtime
        else:
            frappe.msgprint("overtime_holidays" +" "+ str(overtime))
            # doc.overtime_holidays = overtime

    elif payware_settings.get_overtime_mode() == "Working Hours":
        frappe.msgprint("Working Hours")

        if doc.working_hours and doc.working_hours>=shift_duration:
            overtime = flt(doc.working_hours - shift_duration, 2)
            overtime = validate_maximum_overtime_for_employee(doc.employee, overtime, doc.attendance_date)
            if not holiday:
                frappe.msgprint("overtime_normal" +" "+ str(overtime))
                # doc.overtime_normal = overtime
            else:
                frappe.msgprint("overtime_holidays" +" "+ str(overtime))
                # doc.overtime_holidays = overtime
            






