import sqlite3
from utils import printTable

def print_tables(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # GET THE LIST OF TABLES IN DATABASE
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for table in tables:
        print(f"Contents of table: {table[0]}")
        cursor.execute(f"SELECT * FROM {table[0]};")
        rows = cursor.fetchall()
        cursor.execute(f"PRAGMA table_info({table[0]});")
        columns = cursor.fetchall()
        headers = [column[1] for column in columns]
        printTable([headers] + rows)
        print("\n")

    conn.close()

print_tables('ams.db')