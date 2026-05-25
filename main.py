from fastapi import FastAPI
from cost_engine import calculate_cost
from alerts import send_alert
from storage import save_data, load_data
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cost_history =[]

 #CostModel
class Service(BaseModel):
    name: str
    usage: float
    price: float

class CostRequest(BaseModel):
    services: list[Service]

@app.post("/calculate")
def calculate(request: CostRequest):

    total = calculate_cost(request.services)

    entry = {
        "total": total,
        "timestamp": datetime.now().isoformat(),
        "services": [s.dict() for s in request.services]
    }

    cost_history.append(entry)

    save_data(cost_history)

    send_alert(total)

    return {
        'total_cost': total,
        'history': cost_history
    }

@app.get('/data')
def get_data():
    return {
        'history': load_data()
    }

@app.delete('/data')
def delete_data():
    global cost_history
    cost_history = []
    save_data(cost_history)
    return {"message": "History deleted"}