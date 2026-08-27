import sqlite3 as ss
con = ss.connect(r"database.db")
cur = con.cursor()
cur.execute("create table if not exists person(uname text, pswrd text);")
con.commit()
data = ("ali" ,"123")
cur.execute("INSERT INTO person VALUES(?, ?);", data)
con.commit()
def login(u,p):
 cur.execute(f"select * from person where uname ='{u}' and pswrd = '{p}' ")
 data = cur.fetchall()
 if len(data )==1 :
  return True
 else :
  return False