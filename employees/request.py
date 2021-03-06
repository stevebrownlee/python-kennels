import sqlite3
import json
from models import Employee


def get_all_employees():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            e.id,
            e.name
        from employee e
        """)

        # Initialize an empty list to hold all employee representations
        employees = []
        dataset = db_cursor.fetchall()

        # Iterate all rows of data returned from database
        for row in dataset:

            # Create an employee instance from the current row
            employee = Employee(row['id'], row['name'])
            employees.append(employee.__dict__)

    return json.dumps(employees)


def create_employee(employee):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Employee
            ( name )
        VALUES
            ( ? );
        """, (employee['name'])
        )

        id = db_cursor.lastrowid
        employee['id'] = id


    return json.dumps(employee)

def get_single_employee(id):
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            e.id,
            e.name
        from employee e
        WHERE e.id = ?
        """, (id,))

        data = db_cursor.fetchone()
        employee = Employee(data['id'], data['name'])
        return json.dumps(employee.__dict__)


def update_employee(id, new_employee):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Employee
            SET name = ?
        WHERE id = ?
        """, (new_employee['name'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True


def delete_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Employee WHERE id = ?
        """, (id, ))
