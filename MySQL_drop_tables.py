import pymysql
dbname="playlists"
host="localhost"
user="root"
passwd=""
db=pymysql.connect(db=dbname, host=host, user=user,passwd=passwd, charset='utf8')

cur = db.cursor()
drop_tables = '''drop table playlists, songs;'''
cur.execute(drop_tables)

db.commit()