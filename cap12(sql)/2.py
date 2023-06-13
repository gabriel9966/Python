import sqlite3 as sql

# Conectar ao banco de dados
con = sql.connect("cap12_dsa.db")

# Abrir um cursor para percorrer os dados do banco de dados
cursor = con.cursor()

# Query para extrair os nomes das tabelas no banco de dados
sql_query = "SELECT name FROM sqlite_master WHERE type = 'table';"

# Executar a query
cursor.execute(sql_query)

# Recuperar os resultados da consulta
tables = cursor.fetchall()

# Imprimir os nomes das tabelas
for table in tables:
    print(table[0])

# Fechar o cursor e a conexão com o banco de dados
cursor.close()
con.close()
