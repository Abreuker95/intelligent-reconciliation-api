from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging

app = FastAPI()

# Allow your portfolio website to talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can lock this down to "https://austinbreuker.com" later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InvoiceRequest(BaseModel):
    invoice_text: str

PO_DATABASE = {
    "PO-9941": {"approved_amount": 4500.00, "vendor": "TechCorp"},
    "PO-9942": {"approved_amount": 3200.00, "vendor": "Global Office"}
}

@app.post("/extract-and-reconcile")
def process_invoice(request: InvoiceRequest):
    text = request.invoice_text
    
    # 1. Extraction
    if "INV-2026-089" in text:
        extraction = {"vendor": "TechCorp", "po_number": "PO-9941", "amount": 4500.00, "confidence": 0.98}
    else:
        extraction = {"vendor": "Global Office Supplies", "po_number": "PO-9942", "amount": 3500.00, "confidence": 0.82}
        
    # 2. Reconciliation
    po_record = PO_DATABASE.get(extraction['po_number'])
    if not po_record:
        reconciliation = {"status": "FLAGGED", "reason": "PO Not Found", "st_processing": False}
    elif extraction['amount'] == po_record['approved_amount']:
        reconciliation = {"status": "VERIFIED", "reason": "Amounts Match", "st_processing": True}
    else:
        variance = abs(extraction['amount'] - po_record['approved_amount'])
        reconciliation = {"status": "EXCEPTION", "reason": f"Variance of ${variance:.2f} detected.", "st_processing": False}
        
    return {
        "extraction": extraction,
        "reconciliation": reconciliation
    }
