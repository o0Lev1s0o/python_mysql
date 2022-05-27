import pymysql

conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'test',
    password = 'password',
    database = 'school',
    charset = 'utf8')

cursor = conn.cursor()

sql = 'select * from Students;'

cursor.execute(sql)
res = cursor.fetchone()
print(res)

