import mysql.connector as m
conn=m.connect(user='root',passwd='root',database='bookstore')
cursor=conn.cursor()

def create_table():
    cursor.execute("CREATE TABLE BOOKS(ID MEDIUMINT NOT NULL AUTO_INCREMENT PRIMARY KEY, TITLE TEXT, AUTHOR TEXT, YEAR INTEGER, ISBN INTEGER);")
    conn.commit()


def insert(title,author,year,isbn):
    cursor.execute("INSERT INTO BOOKS(ID,TITLE,AUTHOR,YEAR,ISBN) VALUES (NULL,%s,%s,%s,%s);",(title,author,year,isbn))
    conn.commit()

def view():
    s="SELECT * FROM BOOKS"
    cursor.execute(s)
    data=cursor.fetchall()
    return data

def search(title="",author="",year="",isbn=""):
    q="SELECT * FROM BOOKS WHERE TITLE = (%s)  OR AUTHOR = (%s) OR YEAR = (%s) OR ISBN = (%s) "
    cursor.execute(q,(title,author,year,isbn))
    data=cursor.fetchall()
    return data

def delete(id):
    q="DELETE FROM BOOKS WHERE ID =(%s);"
    cursor.execute(q,(id,))
    conn.commit()

def update(id,title,author,year,isbn):
    q="UPDATE BOOKS SET TITLE=(%s),AUTHOR=(%s),YEAR=(%s),ISBN=(%s) WHERE ID = (%s)"
    cursor.execute(q,(title,author,year,isbn,id))
    conn.commit()


