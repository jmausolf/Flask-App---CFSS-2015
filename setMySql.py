import pymysql
dbname="white_house_data"
host="localhost"
user="root"
passwd=""
db=pymysql.connect(db=dbname, host=host, user=user,passwd=passwd, charset='utf8')

#Create Blank Tables
cur = db.cursor()
CREATE_TABLE_speech_urls = '''CREATE TABLE IF NOT EXISTS speech_urls (id INTEGER PRIMARY KEY AUTO_INCREMENT, speech_urls VARCHAR(260));'''
#CREATE_TABLE_songs = '''CREATE TABLE IF NOT EXISTS songs (id INTEGER PRIMARY KEY AUTO_INCREMENT, playlistId INTEGER, songOrder INTEGER, artistName VARCHAR(260), albumName VARCHAR(260), trackName VARCHAR(260));'''
cur.execute(CREATE_TABLE_speech_urls)
#cur.execute(CREATE_TABLE_songs)
db.commit()


#Other Commands
"""
#Enter into BASH
mysql -h localhost -u root 


#Enter into MYSQL

create database white_house_data;
use white_house_data;

#Create Blank Tables


#Show Entries

SELECT * FROM speech_urls;

"""