import mysql.connector

connection = None
cursor = None

try:
    connection = mysql.connector.connect(database='suunnittelutehtava3_svetlana_bilous', user='root')
    cursor = connection.cursor(prepared=True, dictionary=True)

    title_id = input("Anna nimikkeen id, jonka arvostelu haluat poistaa: ")

    insert_query = ("DELETE FROM review WHERE id = (%s)")

    cursor.execute(insert_query, (title_id, ))
    connection.commit()
    print("Arvostelu on poistettu!")

except Exception as e:
    print(e)
    connection.rollback()

finally:
    if cursor is not None:
        cursor.close()

    if connection is not None and connection.is_connected():
        connection.close()


