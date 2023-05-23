import mysql.connector

connection = None
cursor = None

try:
    connection = mysql.connector.connect(database='suunnittelutehtava3_svetlana_bilous', user='root')
    cursor = connection.cursor(prepared=True, dictionary=True)

    print("Näyttelijän poistaminen! ")
    actor_id = input("Anna näyttelijän id: ")

    insert_query = ("DELETE FROM actor WHERE id = (%s)")

    cursor.execute(insert_query, (actor_id, ))
    connection.commit()
    print("Näyttelijä on poistettu!")

except Exception as e:
    print(e)
    connection.rollback()

finally:
    if cursor is not None:
        cursor.close()

    if connection is not None and connection.is_connected():
        connection.close()


