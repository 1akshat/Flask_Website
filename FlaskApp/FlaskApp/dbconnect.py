import MySQLdb


def connection():
    conn = MySQLdb.connect(host="localhost",
                           user="root",
                           passwd="password123",
                           db="pythonprogramming")

    c = conn.cursor()

    return c, conn