import sqlite3
import pandas as pd

conn = sqlite3.connect("_databases/nba_salary.sqlite")

try:
    df = pd.read_sql_query("SELECT * FROM transactions", conn)
    print(df.head())
except Exception as e:
    print(f"Error ejecutando la consulta: {e}")
finally:
    conn.close()