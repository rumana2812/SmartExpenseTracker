# Smart Expense Tracker API

## Project Description

Smart Expense Tracker is a REST API built using FastAPI that helps users manage their daily expenses.

## Features

- Add Expense
- View All Expenses
- Filter Expenses by Category
- Calculate Total Expenses
- Calculate Total Expenses by Category
- Delete Expense
- JSON File Storage
- Swagger API Documentation

## Technologies Used

- Python 3.10
- FastAPI
- Uvicorn
- Pytest

## Installation

Clone the repository

```bash
git clone <repository_url>
```

Go to project folder

```bash
cd SmartExpenseTracker
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
uvicorn src.main:app --reload
```

Open Swagger

```
http://127.0.0.1:8000/docs
```

## Project Structure

```
SmartExpenseTracker/
│
├── src/
│   ├── main.py
│   ├── models.py
│   ├── storage.py
│
├── tests/
│   └── test_main.py
│
├── expenses.json
├── requirements.txt
├── README.md
├── AI_NOTES.md
└── .gitignore
```

## Author

Rumana Farheen Yusuf