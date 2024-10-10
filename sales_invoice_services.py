import frappe
from frappe.utils import nowdate
from .service_item_details import *

def create_sales_invoice_for_lab_test(doc, method):
    if not doc.patient:
        frappe.throw("Patient information is required to add to the Sales Invoice.")

    service_name, item_code, rate = get_lab_test_item_details(doc)

    sales_invoices = frappe.get_all("Sales Invoice", filters={"customer": doc.patient, "docstatus": 0})
    if sales_invoices:
        sales_invoice = frappe.get_doc("Sales Invoice", sales_invoices[0].name)
    else:
        frappe.throw("No draft Sales Invoice found for this patient.")

    sales_invoice.append("items", {
        "item_code": item_code,
        "qty": 1,
        "rate": rate,
        "description": service_name
    })

    sales_invoice.save()
    frappe.msgprint(f"Service {service_name} added to Sales Invoice {sales_invoice.name} (Service ID: {doc.name})")



def create_sales_invoice_for_medication(doc, method):
    if not doc.patient:
        frappe.throw("Patient information is required to add to the Sales Invoice.")

    service_name, item_code, rate = get_medication_item_details(doc)

    sales_invoices = frappe.get_all("Sales Invoice", filters={"customer": doc.patient, "docstatus": 0})
    if sales_invoices:
        sales_invoice = frappe.get_doc("Sales Invoice", sales_invoices[0].name)
    else:
        frappe.throw("No draft Sales Invoice found for this patient.")

    sales_invoice.append("items", {
        "item_code": item_code,
        "qty": 1,
        "rate": rate,
        "description": service_name
    })

    sales_invoice.save()
    frappe.msgprint(f"Service {service_name} added to Sales Invoice {sales_invoice.name} (Service ID: {doc.name})")


def create_sales_invoice_for_procedure(doc, method):
    if not doc.patient:
        frappe.throw("Patient information is required to add to the Sales Invoice.")

    service_name, item_code, rate = get_procedure_item_details(doc)

    sales_invoices = frappe.get_all("Sales Invoice", filters={"customer": doc.patient, "docstatus": 0})
    if sales_invoices:
        sales_invoice = frappe.get_doc("Sales Invoice", sales_invoices[0].name)
    else:
        frappe.throw("No draft Sales Invoice found for this patient.")

    sales_invoice.append("items", {
        "item_code": item_code,
        "qty": 1,
        "rate": rate,
        "description": service_name
    })

    sales_invoice.save()
    frappe.msgprint(f"Service {service_name} added to Sales Invoice {sales_invoice.name} (Service ID: {doc.name})")