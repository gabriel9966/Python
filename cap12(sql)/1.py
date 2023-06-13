import sqlite3 as sql

#print(sql.version)

#print(pd.__version__)

#conectar no banco de dados
con = sql.connect("python/cap12(sql)/cap12_dsa.db")


#abre um cursor para percorrer os dados do banco de dados
cursor = con.cursor()
#query para extrair os nomes das colunas no banco de dados
sql_query = """SELECT name FROM sqlite_master WHERE type = 'table';"""
#executa a query
cursor.execute(sql_query)
#visualiza o resultado
print(cursor.fetchall())

#metadado = dado sobre o dado , nome de coluna , nome de tabela