import cx_Oracle

# Configurações de conexão ao banco de dados
username = 'system'
password = 'kauan'
dsn = cx_Oracle.makedsn('localhost', 
                                1521, 
                                service_name = 'XEPDB1')  # Pode ser um TNS name ou uma string de conexão completa

# Criar a conexão
connection = cx_Oracle.connect(username, password, dsn)

# Criar um cursor
cursor = connection.cursor()

query = "SELECT * FROM tb_login"
cursor.execute(query)

# Puxar os nomes das colunas
column_names = [desc[0] for desc in cursor.description]

# Imprimir os nomes das colunas
print(column_names)

# Fechar cursor e conexão
cursor.close()
connection.close()
