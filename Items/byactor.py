import mysql.connector

connection = None
cursor = None

try:

    connection = mysql.connector.connect(database='suunnittelutehtava3_svetlana_bilous', user='root')
    cursor = connection.cursor(prepared=True, dictionary=True)

    title_name = input("Anna nimike: ")
    query = ('SELECT actor.full_name FROM actor INNER JOIN title_has_actor ON actor.id = title_has_actor.actor_id INNER JOIN title ON title.id = title_has_actor.title_id WHERE title.name = (%s)')

    cursor.execute(query, (title_name, ))

    actors = cursor.fetchall()

    print(f"Nimikkeen {title_name} näyttelijöitä ovat: ")
    for actor in actors:
        print(actor['full_name'])

except Exception as e:
    print(e)

finally:

    if cursor is not None:
        cursor.close()

    if connection is not None and connection.is_connected():
        connection.close()
