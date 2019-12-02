import sqlite3
def commit_after_execute(cursor,f,*args):
  cursor.execute("""INSERT INTO func (funcname) values (?)""", str(f(*args)))
  conn.commit()
  
def f(a,b):
   return a+b

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS func (funcname)""")



commit_after_execute(cursor,f,1,2)
cursor.execute("SELECT funcname FROM func")
print(cursor.fetchall())
