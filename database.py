
import sqlite3
from config import DB_PATH
def init_db():
    con=sqlite3.connect(DB_PATH)
    con.execute("CREATE TABLE IF NOT EXISTS history(id INTEGER PRIMARY KEY,user_id INTEGER,role TEXT,text TEXT)")
    con.commit();con.close()
def save(uid,role,text):
    con=sqlite3.connect(DB_PATH)
    con.execute("INSERT INTO history(user_id,role,text) VALUES(?,?,?)",(uid,role,text))
    con.commit();con.close()
