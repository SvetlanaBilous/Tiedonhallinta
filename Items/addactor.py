import mysql.connector

connection = None
cursor = None

try:
    connection = mysql.connector.connect(database='suunnittelutehtava3_svetlana_bilous', user='root')
    cursor = connection.cursor(prepared=True, dictionary=True)

    title_id = input("Anna nimikkeen id: ")
    actor_id = input("Anna näyttelijän id: ")

    insert_query = ("INSERT INTO title_has_actor(title_id, actor_id) VALUES((%s), (%s))")

    cursor.execute(insert_query, (title_id, actor_id))
    connection.commit()
    print("Näyttelijä on tallennettu nimikkeelle!")

except Exception as e:
    print(e)
    connection.rollback()

finally:
    if cursor is not None:
        cursor.close()

    if connection is not None and connection.is_connected():
        connection.close()


