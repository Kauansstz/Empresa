from rh.database import banco

result = banco.sql_query(f"""SELECT COUNT(*) FROM TB_RH""")

print(result)
