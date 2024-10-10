# Automated Sales Invoice Creation for Lab Tests, Medications, and Procedures in Frappe

This repository provides scripts to automate the creation of sales invoices for lab tests, medications, and clinical procedures within the Frappe framework. It dynamically fetches the relevant item details (e.g., item code, rate) and appends them to an existing draft Sales Invoice for the patient.

## Features

- Automates the process of adding services (lab tests, medications, procedures) to a patient’s Sales Invoice.
- Supports adding multiple items to the same Sales Invoice.
- Ensures that patient information is available before attempting to add a service.
- Throws an error if no draft Sales Invoice is found for the patient.

## Installation

To use these scripts, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/sales-invoice-automation.git
   ```

2. Add the cloned scripts to your custom app in the Frappe framework.

3. Ensure the `service_item_details.py` file contains the appropriate functions to fetch item details for lab tests, medications, and procedures.

## Usage

These functions are designed to be called during specific document events in the Frappe framework (e.g., on_submit, validate). They automatically append services to an existing Sales Invoice based on the patient.

### Lab Test Sales Invoice

```python
create_sales_invoice_for_lab_test(doc, method)
```

- This function adds a lab test service to the patient's draft Sales Invoice.
- Parameters: 
  - `doc`: The lab test document object.
  - `method`: The triggered method (event).

### Medication Sales Invoice

```python
create_sales_invoice_for_medication(doc, method)
```

- This function adds a medication service to the patient's draft Sales Invoice.
- Parameters: 
  - `doc`: The medication document object.
  - `method`: The triggered method (event).

### Procedure Sales Invoice

```python
create_sales_invoice_for_procedure(doc, method)
```

- This function adds a clinical procedure service to the patient's draft Sales Invoice.
- Parameters: 
  - `doc`: The procedure document object.
  - `method`: The triggered method (event).

## Helper Functions

### `get_lab_test_item_details`

```python
def get_lab_test_item_details(doc):
    lab_test_template = frappe.get_doc("Lab Test Template", doc.template)
    return doc.lab_test_name, doc.lab_test_name, lab_test_template.lab_test_rate
```

- Fetches the lab test service name, item code, and rate from the lab test template.

### `get_medication_item_details`

```python
def get_medication_item_details(doc):
    item = frappe.get_doc("Item", doc.medication_item)
    return doc.medication, doc.medication_item, item.valuation_rate
```

- Fetches the medication service name, item code, and rate from the item document.

### `get_procedure_item_details`

```python
def get_procedure_item_details(doc):
    return doc.procedure_name, doc.item_code, doc.rate
```

- Fetches the procedure service name, item code, and rate from the procedure document.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This documentation outlines the repository’s functionality and explains how to use each function and helper function in your code.
