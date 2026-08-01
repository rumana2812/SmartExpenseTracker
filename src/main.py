from fastapi import FastAPI, HTTPException
from src.models import Expense
from src.storage import load_expenses, save_expenses

app = FastAPI(
    title="Smart Expense Tracker API",
    description="REST API to manage personal expenses",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Smart Expense Tracker API"
    }


# Add Expense
@app.post("/expenses")
def add_expense(expense: Expense):
    expenses = load_expenses()

    for item in expenses:
        if item["id"] == expense.id:
            raise HTTPException(
                status_code=400,
                detail="Expense ID already exists."
            )

    expenses.append(expense.model_dump())
    save_expenses(expenses)

    return {
        "message": "Expense added successfully."
    }


# View All Expenses
@app.get("/expenses")
def get_expenses():
    return load_expenses()


# Filter Expenses by Category
@app.get("/expenses/category/{category}")
def get_expenses_by_category(category: str):
    expenses = load_expenses()

    filtered = [
        expense
        for expense in expenses
        if expense["category"].lower() == category.lower()
    ]

    return filtered


# Calculate Total Expenses
@app.get("/expenses/total")
def total_expenses():
    expenses = load_expenses()

    total = sum(expense["amount"] for expense in expenses)

    return {
        "total_expense": total
    }


# Calculate Total by Category
@app.get("/expenses/total/{category}")
def total_by_category(category: str):
    expenses = load_expenses()

    total = sum(
        expense["amount"]
        for expense in expenses
        if expense["category"].lower() == category.lower()
    )

    return {
        "category": category,
        "total": total
    }


# Delete Expense
@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    expenses = load_expenses()

    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            save_expenses(expenses)

            return {
                "message": "Expense deleted successfully."
            }

    raise HTTPException(
        status_code=404,
        detail="Expense not found."
    )