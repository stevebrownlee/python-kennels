import sqlite3
import json
from models import Location


def get_all_locations():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address,
            COUNT(a.id) animals
        FROM location l
        JOIN animal a ON a.location_id = l.id
        GROUP BY a.location_id
        """)

        # Initialize an empty list to hold all location representations
        locations = []
        dataset = db_cursor.fetchall()

        # Iterate all rows of data returned from database
        for row in dataset:

            # Create an location instance from the current row
            location = Location(row['name'], row['address'], row['animals'])
            location.id = row['id']

            locations.append(location.__dict__)

    return json.dumps(locations)

