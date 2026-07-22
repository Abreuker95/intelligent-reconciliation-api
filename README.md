Intelligent FinTech Reconciliation Engine
An enterprise-grade, serverless accounts payable (AP) automation tool designed to simulate intelligent document processing (IDP), financial reconciliation, and human-in-the-loop exception handling.

This project demonstrates a fully decoupled microservice architecture, pairing a responsive modern web UI with a high-performance Python FastAPI backend.

System Architecture
The application is split into two independent tiers:

The Frontend Layer: A 3-panel interactive dashboard built with responsive CSS Grid and vanilla JavaScript. It handles asynchronous data fetching, real-time confidence score rendering, and audit-ready manual overrides.

The Backend Tier: A containerized Python microservice built with FastAPI and Pydantic, hosted via cloud infrastructure with automated CI/CD deployments through GitHub.

How It Works (The Pipeline)


<img width="754" height="370" alt="image" src="https://github.com/user-attachments/assets/2a07a79b-35b1-4e14-a71b-03f7cb5cfea7" />


              
Ingestion & Event Trigger: The user selects a vendor invoice from the 5-item multi-scenario queue. This triggers an asynchronous fetch() POST request containing the raw OCR payload.

AI Extraction & Structuring: The Python backend parses the raw text, extracts key financial fields (Vendor name, PO number, and invoice total), and generates a structured JSON object alongside an AI confidence score.

System of Record Reconciliation: The backend validates the extracted invoice data against a mock internal Purchase Order (PO) database:

Straight-Through Processing (STP): If the invoice amount matches the approved budget perfectly, the system verifies the transaction and enables automated AP routing.

Exception Handling: If a variance, late fee, or missing PO is detected, the engine flags the transaction as an exception, triggering a human-in-the-loop workflow requiring manual audit override.

Tech Stack
Frontend: HTML5, CSS Grid, Vanilla JavaScript (ES6+), Asynchronous Fetch API

Backend: Python 3.11+, FastAPI, Uvicorn, Pydantic, CORS Middleware

Infrastructure & CI/CD: GitHub, Render (Cloud Hosting Platform)

Repository Structure
Plaintext
├── main.py               # FastAPI server, request models, and reconciliation logic
├── requirements.txt      # Project dependencies (fastapi, uvicorn, pydantic)
└── README.md             # Project documentation
 Local Development & Deployment
1. Run Locally
To run the FastAPI backend locally for development:

Bash

# Install dependencies
pip install -r requirements.txt

# Start the development server

uvicorn main:app --reload
2. Cloud Deployment (CI/CD Pipeline)
This repository is linked to a cloud hosting platform via a continuous deployment pipeline.

Every push to the main branch automatically triggers a build test, installs the environment specified in requirements.txt, and redeploys the live production API endpoint.
