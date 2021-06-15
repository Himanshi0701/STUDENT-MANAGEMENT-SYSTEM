import sqlite3
#backend

def studentData():
          con=sqlite3.connect("student.db")
          cur=con.cursor()
          cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY,StdId text,Fristname text,surname text,DoB text,Age text,Gender text,Address text,Mobile text)")
          con.commit()
          con.close()

def addStdRec(StdId,Fristname,surname,DoB,Age,Gender,Address,Mobile ):
          con=sqlite3.connect("student.db")
          cur=con.cursor()
          cur.execute("SELECT StdId FROM student WHERE StdId='{}'".format(StdId))
          rows=cur.fetchall()
          print(rows)
          if rows:
              return("hi")
          else:
              print("hi")
              cur.execute("INSERT INTO student VALUES(NULL,?,?,?,?,?,?,?,?)",(StdId,Fristname,surname,DoB,Age,Gender,Address,Mobile))
              con.commit()
              con.close()

def viewData():
          con=sqlite3.connect("student.db")
          cur=con.cursor()
          cur.execute("SELECT * FROM student")
          rows=cur.fetchall()
          con.close()
          return rows

def deleteRec(id):
          con=sqlite3.connect("student.db")
          cur=con.cursor()
          cur.execute("DELETE FROM student  WHERE id=?",(id,))
          con.commit()
          con.close()

def searchData(StdId="",Fristname="",surname="",DoB="",Age="",Gender="",Address="",Mobile=""):
          con=sqlite3.connect("student.db")
          cur=con.cursor()
          cur.execute("SELECT * FROM student WHERE StdId=? OR Fristname=? OR surname=? OR DoB=? OR Age=? OR Gender=? OR Address=? OR Mobile=? "
                      ,(StdId,Fristname,surname,DoB,Age,Gender,Address,Mobile))
          rows=cur.fetchall()
          con.close()
          return rows

def dataUpdate(id,StdId="",Fristname="",surname="",DoB="",Age="",Gender="",Address="",Mobile=""):
          con=sqlite3.connect("student.db")
          cur=con.cursor()
          cur.execute("UPDATE student SET StdId=? , Fristname=? ,surname=? , DoB=? , Age=? , Gender=? ,\
              Address=? , Mobile=?,WHERE id=?",(StdId,Fristname,surname,DoB,Age,Gender,Address,Mobile,id))
          con.commit()
          con.close()
          

          
studentData()
