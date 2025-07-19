from sqlalchemy import create_engine, MetaData, Table, text
import pandas as pd

engine = create_engine('sqlite:///_databases/nba_salary.sqlite')
connection = engine.connect()

result = connection.execute(text('SELECT * FROM NBA_season1718_salary LIMIT 5'))
for row in result:
    print(row)

df = pd.read_sql('SELECT * FROM NBA_season1718_salary LIMIT 10', engine)
print(df.head())

'''
ATENCIÓN: para que sqlAlchemy entienda la consulta esta debe ser pasada a texto con text() 
y en la ruta para que entienda el tipo de base de datos debe empezar con sqlite:///
'''