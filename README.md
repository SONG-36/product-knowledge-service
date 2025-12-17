# Product Knowledge Service

A structured product knowledge backend service designed for AWS AI customer support systems.

## Features
- Canonicalized product parameters
- Deterministic fact querying
- REST API for product attributes

## Run locally

```bash
pip install -r requirements.txt
uvicorn src.api:app --reload
