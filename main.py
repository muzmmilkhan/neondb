import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from psycopg import connect

load_dotenv()

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")


class Employee(BaseModel):
    id: int
    name: str
    position: str

@app.post("/employees")
def create_employee(employee: Employee):
    with connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO employees (id, name, position) VALUES (%s, %s, %s)",
                (employee.id, employee.name, employee.position)
            )
    return employee

@app.get("/employees")
def get_employee():
    with connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, name, position FROM employees"
            )
            rows = cur.fetchall()
            employees = []
            for row in rows:
                employees.append(Employee(id=row[0], name=row[1], position=row[2]))
            return employees

