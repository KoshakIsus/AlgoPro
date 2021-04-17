import pymysql.cursors

conn = pymysql.connect(
	host = 'localhost',
	user = 'soft0028',
	password = 'iPjXAp8m',
	db = 'soft0028_labrab_8',
	port = 3306,
	cursorclass = pymysql.cursors.DictCursor)

cur = conn.cursor()

sql = ("SELECT `nameStud`, `rating`, `city` FROM `Students` ORDER BY `city`) ORDER BY `rating` DESC")
cur.execute(sql)
rows = cur.fetchall()

for row in rows:
    print(f'name = {row["nameStud"]}, rating = {row["rating"]}, city = {row["city"]}')

conn.close()
