from models.customer import Customer
from models.location import Location
import sqlite3
import json
from models import Animal


def get_all_animals(query_params):
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        conn.set_trace_callback(print)
        db_cursor = conn.cursor()

        sort_by = ""
        where_clause = ""

        if len(query_params) != 0:
            param = query_params[0]
            [qs_key, qs_value] = param.split("=")


            if qs_key == "_sortBy":

                if qs_value == 'location':
                    sort_by = " ORDER BY location_id"
                elif qs_value == 'customer':
                    sort_by = " ORDER BY customer_id"
                elif qs_value == 'name':
                    sort_by = " ORDER BY a.name"
                else:
                    sort_by = qs_value
            else:

                if qs_key == "locationId":
                    where_clause = f"WHERE a.location_id = {qs_value}"
                elif qs_key == "customerId":
                    where_clause = f"WHERE a.customer_id = {qs_value}"
                else:
                    where_clause = f"WHERE a.{qs_key} = '{qs_value}'"




        # Write the SQL query to get the information you want
        sql_to_execute = f"""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id,
            l.name location_name,
            l.address location_address
        FROM Animal a
        JOIN `Location` l
            ON l.id = a.location_id
        {where_clause}
        {sort_by}
        """

        db_cursor.execute(sql_to_execute)

        # Initialize an empty list to hold all animal representations
        animals = []
        dataset = db_cursor.fetchall()

        # Iterate all rows of data returned from database
        for row in dataset:

            # Create an animal instance from the current row
            animal = Animal(row['name'], row['breed'], row['status'],
                            row['location_id'], row['customer_id'], row['id'])

            location = Location(row['location_name'], row['location_address'])
            animal.location = location.__dict__

            animals.append(animal.__dict__)

    return json.dumps(animals)


def get_single_animal(id):
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name animal_name,
            a.breed,
            a.status,
            a.customer_id,
            a.location_id,
            l.name location_name,
            c.name customer_name,
            c.id customer_id,
            c.address
        FROM animal a
        JOIN location l
            ON l.id = a.location_id
        JOIN customer c
            ON c.id = a.customer_id
        WHERE a.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        animal = Animal(data['animal_name'], data['breed'], data['status'],
                        data['location_id'], data['customer_id'], data['id'])

        location = Location(data['location_name'])
        animal.location = location.__dict__

        customer = Customer(data['customer_id'], data['customer_name'], data['address'])
        animal.customer = customer.__dict__

        return json.dumps(animal.__dict__)


def create_animal(new_animal):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Animal
            ( name, breed, status, location_id, customer_id )
        VALUES
            ( ?, ?, ?, ?, ?);
        """, (
            new_animal['name'],
            new_animal['breed'],
            new_animal['status'],
            new_animal['locationId'],
            new_animal['customerId'], )
        )

        id = db_cursor.lastrowid
        new_animal['id'] = id


    return json.dumps(new_animal)


def update_animal(id, new_animal):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Animal
            SET
                name = ?,
                breed = ?,
                status = ?,
                location_id = ?,
                customer_id = ?
        WHERE id = ?
        """, (
                new_animal['name'],
                new_animal['breed'],
                new_animal['status'],
                new_animal['locationId'],
                new_animal['customerId'],
                id,
             )
        )

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True


def delete_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM animal
        WHERE id = ?
        """, (id, ))

        rows_affected = db_cursor.rowcount  # 0 or 1

        if rows_affected == 0:
            return False
        else:
            return True

