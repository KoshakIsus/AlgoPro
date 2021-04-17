import pymysql.cursors

conn = pymysql.connect(
	host = 'pgsha.ru',
	user = 'soft0028',
	password = 'iPjXAp8m',
	db = 'soft0028_labrab_8',
	port = 35080,
	cursorclass = pymysql.cursors.DictCursor)

cur = conn.cursor()

sql = "SELECT * FROM `Students` WHERE `city` != 'Пермь' ORDER BY `date` ASC"
cur.execute(sql)
rows = cur.fetchall()

for row in rows:
    print(f'name = {row["nameStud"]}, rating = {row["rating"]}, gender = {row["gender"]}, date = {row["rating"]}, city = {row["city"]}')
  #В задании надо было вывести ВСЕХ студентов, а не их имена, так что я просто вывел всю информацию о них.

conn.close()