import sqlite3 as sql
from matplotlib.backend_bases import cursors
#print(sql.version)
import pandas as pd
#print(pd.__version__)

#conectar no banco de dados
con = sql.connect("cap12_dsa.db")

#abre um cursor para percorrer os dados do banco de dados
cursor = con.cursor()