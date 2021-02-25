import mysql.connector


def reservation_delete(id):

    conn = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='Li009294',
        database='tokyo_hotels'
    )

    cur = conn.cursor()

    sql_format = """

        DELETE FROM reservations 
        WHERE id={id}

    """

    sql = sql_format.format(
        id=id
    )

    cur.execute(sql)
    conn.commit()

    cur.close()
    conn.close()

print(reservation_delete(id=6))

