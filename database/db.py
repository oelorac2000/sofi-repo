import pymysql

db_host = "sofidb.cb4c4o04wh0o.us-east-1.rds.amazonaws.com"
db_user = "admin"
db_password = "Sofi1022*"
db_database = "db_sofi"

try:
    pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_database
    )
    print("Bien")
except Exception as err:
    print("Mal", err)