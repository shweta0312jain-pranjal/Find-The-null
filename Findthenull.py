import sqlite3
import pandas as pd

conn = sqlite3.connect("students.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS Students (
    id INTEGER,
    name TEXT,
    city TEXT,
    marks INTEGER
)
""")

conn.execute("DELETE FROM Students")

conn.executemany(
    "INSERT INTO Students VALUES (?, ?, ?, ?)",
    [
        (1, "Aarav", "Delhi", 85),
        (2, "Riya", None, 78),
        (3, "Kabir", "Mumbai", None),
        (4, "Ananya", None, None)
    ]
)

conn.commit()

df = pd.read_sql_query("SELECT * FROM Students", conn)
print(df)

null_data = pd.read_sql_query(
    "SELECT * FROM Students WHERE city IS NULL OR marks IS NULL",
    conn
)
print(null_data)

conn.close()
