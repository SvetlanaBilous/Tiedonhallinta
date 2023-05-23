import mysql.connector

connection = None
cursor = None

try:
    connection = mysql.connector.connect(database='suunnittelutehtava3_svetlana_bilous', user='root')
    cursor = connection.cursor(prepared=True, dictionary=True)

    title_id = input("Anna nimikkeen id: ")
    actor_id = input("Anna näyttelijän id: ")

    insert_query = ("DELETE FROM title_has_actor WHERE title_id = (%s) AND actor_id = (%s)")

    cursor.execute(insert_query, (title_id, actor_id))
    connection.commit()
    print("Näyttelijä on poistettu nimikkeestä!")

except Exception as e:
    print(e)
    connection.rollback()

finally:
    if cursor is not None:
        cursor.close()

    if connection is not None and connection.is_connected():
        connection.close()


