import sqlite3
import pandas as pd

conexion = sqlite3.connect('_databases/nba_salary.sqlite')
cursor = conexion.cursor()
cursor.execute('SELECT * FROM NBA_season1718_salary LIMIT 5')
rows = cursor.fetchall()
print(rows)
conexion.close

df = pd.read_sql('SELECT * FROM NBA_season1718_salary LIMIT 10', conexion)
print(df.head())