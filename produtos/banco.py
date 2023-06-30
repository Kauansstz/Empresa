import cx_Oracle
def sql_query():
    # create the connection
    dsn     = cx_Oracle.makedsn('', 
                                1521, 
                                service_name = '')

    conn    = cx_Oracle.connect(user     = '', 
                                password = '',  
                                dsn      = dsn)

    cursor  = conn.cursor()
    cursor.execute('select * from consincomonitor.tb_statusconexaopdv where nroempresa = 19')
    result  = cursor.fetchall()
    
    # Close the connection
    cursor.close()
    conn.close()

    for i in result:
        dict = {}
        dict['nroempresa'] = i[0]
        dict['nrocheckout'] = i[1]
        dict['ultimaconexao'] = i[3]
        print(dict)
        
    # return result

sql_query()