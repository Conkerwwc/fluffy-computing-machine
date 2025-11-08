# Geeks (2025). Do loop in Postgresql Using Psycopg2 Python
# https://www.geeksforgeeks.org/python/do-loop-in-postgresql-using-psycopg2-python/
#  Vuyisile Ndlovu (January 21, 2019).
#  Working With Files in Python
#  https://realpython.com/working-with-files-in-python/



# --- Main execution block ---
# The __name__ == '__main__' idiom prevents code from running when imported.
# (Downey (Pg.122, 2015). 

import psycopg2
# Geeks (2025). Do loop in Postgresql Using Psycopg2 Python
# https://www.geeksforgeeks.org/python/do-loop-in-postgresql-using-psycopg2-python/
# Connect to the database
conn = psycopg2.connect(
    database="postgres",  
    user='postgres',  
    password='0451',  
    host='localhost',  
    port='5432' 
)

# Create a cursor
cur = conn.cursor()

# Defining data but id key error like 37 times already. I must change this.
data = [(8, 'John Doe'), (9, 'Jane Doe'), (10, 'Jim Doe')]

# Use a for loop to insert each row of data into the table
for row in data:
    sql = "INSERT INTO employees (id,name) VALUES (%s,%s) ON CONFLICT (id) DO NOTHING"
    cur.execute(sql, row) # mistakes increases to 70

# Commit the changes to the database, use f-string but remove it to see if the id error goes away. 
conn.commit()
print("Data is successfully inserted")

# Close the cursor and the connection
cur.close()
conn.close()










import psycopg2
from psycopg2 import OperationalError, ProgrammingError

# --- Connection Parameters ---
# I started coding Here
# ||||||||||||||||||||
# Port 5432 is the default for PostgreSQL. Where was the site? Connect (2025). 
# https://dbcode.io/docs/get-started/connect
DB_PARAMS = {
    'dbname': 'postgres', # Use 'postgres' or your specific db
    'user': 'postgres',
    'password': '0451', # <-- CHANGE THIS to your password or my password AI Flash (2025). Highlights the issue I spent 2 hours here.
    'host': 'localhost',
    'port': '5432'
}

def setup_database(conn):
    """A helper function to create tables and insert data."""
    # 'ON CONFLICT (id) DO NOTHING' to make this script
    # runnable multiple times without erroring on duplicate keys.
    create_tables_sql = """
    CREATE TABLE IF NOT EXISTS departments (
        id SERIAL PRIMARY KEY,
        department_name VARCHAR(100) NOT NULL UNIQUE
    );
    CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        department_id INT,
        FOREIGN KEY (department_id) REFERENCES departments (id)
    );
    """
    insert_sql = """
    INSERT INTO departments (id, department_name) 
    VALUES (1, 'Data Analysts'), (2, 'Actors'), (3, 'HR')
    ON CONFLICT (id) DO NOTHING;
    
    INSERT INTO employees (id, name, department_id)
    VALUES 
        (1, 'Jose Perez', 1),
        (2, 'Tech Champion', 2),
        (3, 'Nimish Arvind', 3),
        (4, 'Jennifer Hale', 2)
    ON CONFLICT (id) DO NOTHING;
    """
    try:
        with conn.cursor() as cur:
            cur.execute(create_tables_sql)
            cur.execute(insert_sql)
        conn.commit()
        print("Database tables created and populated successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error during setup: {e}") # mistakes 89

# Geeks (2025). Perform Insert Operations with psycopg2 in Python
# https://www.geeksforgeeks.org/python/perform-insert-operations-with-psycopg2-in-python/
def get_sales_employees():
    """Main function to connect, query, and print results."""
    conn = None # Must define conn outside try for finally to access it
    
    try:
        # ||| Q1. Connect 1.42 MB speed Bad|||
        conn = psycopg2.connect(**DB_PARAMS)
        
        # Run setup (optional, for demo)
        setup_database(conn)

        # ||| Q2. Create a Cursor |||
        # Using 'with' is a great way to manage cursors
        with conn.cursor() as cur:
            
            # ||| Q3. Use the Query (SELECT, FROM, JOIN, WHERE) |||
            # We use '%s' as a placeholder for our variable.
            # This is the *correct* way to prevent SQL injection (Tech Champion, 2021).
            sql_query = """
            SELECT e.name, d.department_name
            FROM employees AS e
            JOIN departments AS d ON e.department_id = d.id
            WHERE d.department_name = %s;
            """
      

            # The value to pass for the placeholder.
            # Must be in a tuple or list.Spent 4 hours trying to make sense of this. Error 120
            # Geeks (2025). Tuple within a Tuple in Python.
            # https://www.geeksforgeeks.org/python/tuple-within-a-tuple-in-python/
            query_value = ('Actors',) 
            
            # ||| Q4. Run the Query ||| 
            # Psycopg2 9.11 Documentation (2021). Cursor CLass. https://www.psycopg.org/docs/cursor.html
            cur.execute(sql_query, query_value)
            
            print("\n--- Query Results (Employees in 'Sales') ---")


            # ||| Q5. Fetch and Display Results |||
            results = cur.fetchall()
            
            if not results:
                print("No employees found in that department.")
            else:
                for row in results:
                    # row[0] is e.name, row[1] is d.department_name
                    print(f"Name: {row[0]}, Department: {row[1]}")

    except OperationalError as e:
        print(f"CRITICAL: Connection Error. Check credentials/host/port.")
        print(f"Details: {e}")
    except ProgrammingError as e:
        print(f"CRITICAL: SQL Syntax Error.")
        print(f"Details: {e}")
    except (Exception, psycopg2.DatabaseError) as e:
        # Catch any other database errors (GeeksforGeeks, 2025)
        print(f"An unexpected database error occurred: {e}")
        if conn:
            # If an error happens *during* a transaction, roll it back
            conn.rollback() # (Tech Champion, 2021)
    finally:
        # ||| Q6. Cleaning |||
        # This *always* runs to close the connection (Tech Champion, 2021).
        if conn:
            conn.close()
            print("\nDatabase connection closed.")

# --- Run the main function ---
if __name__ == "__main__":
    get_sales_employees()

    
    
def insert_sales_list(sales_list):
    """ insert multiple vendors into the vendors table  """
    sql = "INSERT INTO employees (name) VALUES(%s) ON CONFLICT DO NOTHING"
    conn = None
    try:
        # read database configuration params = config()????? WHat's this for anyway, out of my program
    
        # connect to the PostgreSQL database ** this is not the right connection it should be DB
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**DB_PARAMS)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql,sales_list)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
# To test the insert_vendor() and insert_vendor_list() functions, you use the following code snippet:
# Redrock Postgres (July 31, 2023).
# PostgreSQL Python Tutorial: Insert Data Into a Table https://www.rockdata.net/tutorial/python-insert/

if __name__ == '__main__':
    # insert one vendor made mistake 269 here. Python docs. Data structures.
    # https://docs.python.org/3/tutorial/datastructures.html
    insert_sales_list([("William Brown",)]) 
    # insert multiple vendors
    insert_sales_list([
        ('Naoya Atsumi',),
        ('Shradha Suri',),
        ('Masanori Togawa',),
        ('Alex Carnevale',),
        ('Michael Wheeler.',),
        ('Norio Nakajima',)
    ])