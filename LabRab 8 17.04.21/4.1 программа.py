import pymysql.cursors

conn = pymysql.connect(
	host = 'pgsha.ru',
	user = 'soft0028',
	password = 'iPjXAp8m',
	db = 'soft0028_labrab_8',
	port = 35080,
	cursorclass = pymysql.cursors.DictCursor)

cur = conn.cursor()

sql = "SELECT `nameStud` FROM `Students` WHERE `city` = 'Кунгур'"
cur.execute(sql)
rows = cur.fetchall()

for row in rows:
    print(f'name = {row["nameStud"]}')

conn.close()
