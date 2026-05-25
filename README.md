Cloud Cost Project

A full-stack cloud cost calculator that simulates AWS service pricing.
Built with Python/FastAPI on the backend and vanilla HTML/JS on the frontend.

## Features
- Calculate costs across multiple AWS services (S3, Lambda, SNS, CloudWatch)
- Persistent cost history saved to disk
- Interactive dashboard with service breakdown table
- REST API with full CRUD — calculate, retrieve, and delete history
- Threshold alerts when costs exceed a set limit

## Tech Stack
| Layer | Technology |
|---|---|
| Backend | Python, FastAPI, Uvicorn |
| Frontend | HTML, JavaScript (vanilla) |
| Storage | Local JSON |

## Setup
git clone https://github.com/iquinones2/Cloud-Cost-Project.git
cd cloud-cost-project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Running the app
# Start backend
uvicorn main:app --reload

# Open frontend
open frontend/index.html

## API Endpoints
| Method | Endpoint | Description |
|---|---|---|
| POST | /calculate | Submit services and calculate cost |
| GET | /data | Retrieve full cost history |
| DELETE | /data | Clear all history |

## Planned Features
- Chart.js cost visualization
- Dynamic service input from the UI
- Configurable alert threshold
- Additional AWS services (SNS, CloudWatch, DynamoDB)