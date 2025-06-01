import frappe

@frappe.whitelist()
def fetch_custom_payroll_working_days(employee):
    employee_doc = frappe.get_doc("Employee", employee)
    return employee_doc.custom_payroll_working_days
    
