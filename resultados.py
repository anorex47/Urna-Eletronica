import os
import sqlite3
import pandas

dirpath = os.path.dirname(os.path.abspath(__file__))
database = os.path.join(dirpath, 'dados.db')

con = sqlite3.connect(database)
read = pandas.read_sql_query("SELECT * FROM candidatos", con)
con.close()

print(read)