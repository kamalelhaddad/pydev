name = input('conn_name: ')
db_name = input('db_name: ')
user_name = input('user_name: ')
password = input('password: ')
conn = f'<add name="{name}" connectionString="data source=jobrock-prod.database.windows.net;initial catalog={db_name};user id={user_name};password={password};MultipleActiveResultSets=True;PersistSecurityInfo=True;App=EntityFramework" providerName="System.Data.SqlClient" />'
print(conn)
