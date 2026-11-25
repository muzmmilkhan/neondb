# NeonDB Employee API

A simple API for adding and viewing employees. It uses [FastAPI](https://fastapi.tiangolo.com/) and a PostgreSQL database, such as [Neon](https://neon.tech/).

## What you'll need

- Python 3.12 or newer
- A PostgreSQL database
- [uv](https://docs.astral.sh/uv/) to install and run the project

## Get started

1. Install the project dependencies:

   ```bash
   uv sync
   ```

2. Create a file named `.env` in the project folder. Add your PostgreSQL connection string:

   ```env
   DATABASE_URL=postgresql://USER:PASSWORD@HOST/DATABASE?sslmode=require
   ```

   Replace the example values with your database details.

3. Create the employees table in your database:

   ```sql
   CREATE TABLE employees (
       id INTEGER PRIMARY KEY,
       name TEXT NOT NULL,
       position TEXT NOT NULL
   );
   ```

4. Start the API:

   ```bash
   uv run fastapi dev main.py
   ```

The API is now available at <http://127.0.0.1:8000>. Visit <http://127.0.0.1:8000/docs> to try it in your browser.

## API examples

### Add an employee

Send a `POST` request to `/employees`:

```bash
curl -X POST http://127.0.0.1:8000/employees \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "name": "Alex Smith", "position": "Developer"}'
```

### View all employees

Send a `GET` request to `/employees`:

```bash
curl http://127.0.0.1:8000/employees
```