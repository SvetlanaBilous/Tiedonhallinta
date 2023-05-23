import mysql.connector

connection = None
cursor = None

try:

    connection = mysql.connector.connect(database='suunnittelutehtava3_svetlana_bilous', user='root')
    cursor = connection.cursor(prepared=True, dictionary=True)

    actor_id = input("Anna näyttelijän id: ")

    query = ('SELECT actor.* FROM actor WHERE id = (%s)')

    cursor.execute(query, (actor_id, ))
    actor = cursor.fetchone()

    print("Nimi:", actor['full_name'])
    print("Syntymäpäivä:", actor['date_of_birth'])

except Exception as e:
    print(e)

finally:

    if cursor is not None:
        cursor.close()

    if connection is not None and connection.is_connected():
        connection.close()
