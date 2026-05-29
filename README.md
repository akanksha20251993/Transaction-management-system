# Transaction-management-system
FastAPI + PostgreSQL transaction backend system

Ever needed a simple way to track transactions in a database?
That is exactly what this project does.
It is a backend API built with Python that lets you create and retrieve transaction records. Nothing overcomplicated — just a clean, functional system that does the job.

**Tools used:**
FastAPI — for building fast and simple APIs
PostgreSQL — for storing transaction data
SQLAlchemy — to interact with the database without writing raw SQL
Python — the core language behind everything

**Functionality:**
Add new transaction records to the database
Retrieve existing transactions
Handle database operations cleanly in the background

**To run:**
Make sure Python is installed, then run:
pip install -r requirements.txt
Start the server:
uvicorn app:app --reload

Then open your browser and go to: http://127.0.0.1:8000/docs

This project helped me understand how backend systems work end-to-end — from API request handling to database storage and retrieval.It is a simple but solid foundation for building real-world systems like payment or transaction platforms.
