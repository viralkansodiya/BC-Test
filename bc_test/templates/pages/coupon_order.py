import frappe
from frappe import _



def get_context(context):   
    sales_order = frappe.form_dict.sales_order
    context["doc"] = frappe.get_doc("Sales Order", sales_order)