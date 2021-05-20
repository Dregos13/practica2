import mysql.connector

def function(arg):

    cnx = mysql.connector.connect(user='root',password='',host='127.0.0.1',database='employees')

    cursor = cnx.cursor()

    query = (arg)

    cursor.execute(query)

    resul = cursor.fetchall()

    cursor.close

    return resul

def function2(arg):

    cnx = mysql.connector.connect(user='root',password='',host='127.0.0.1',database='employees')

    cursor = cnx.cursor()

    query = (arg)

    cursor.execute(query)

    cnx.commit()

    cursor.close