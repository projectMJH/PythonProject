import oracledb

conn=oracledb.connect('hr/happy@localhost:1521/XE') # Connection
cursor=conn.cursor() # PreparedStatement
sql=f"SELECT * FROM emp"
cursor.execute(sql)
for row in cursor:
  print(row)
cursor.close()
conn.close()
