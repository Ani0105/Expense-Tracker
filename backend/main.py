from fastapi import FastAPI
from backend.models import Expense
from backend.database import add_expense, get_expenses
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable Streamlit access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

@app.get("/expenses")
def read_expenses():
    return get_expenses()

@app.post("/expenses")
def create_expense(expense: Expense):
    return add_expense(expense.name, expense.amount, expense.category)

@app.get("/")
def root():
    return {"message": "FastAPI is working!"}

