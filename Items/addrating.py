import mysql.connector

connection = None
cursor = None

try:
    connection = mysql.connector.connect(database='suunnittelutehtava3_svetlana_bilous', user='root')
    cursor = connection.cursor(prepared=True, dictionary=True)

    points = input("Anna arvostelu nimikkeelle: ")
    title_id = input("Anna nimikkeen id, jolle ainnat pisteitä: ")

    insert_query = ("INSERT INTO review(points, title_id) VALUES((%s), (%s))")

    cursor.execute(insert_query, (points, title_id))
    connection.commit()
    print("Arvostelu on tallennettu!")

except Exception as e:
    print(e)
    connection.rollback()

finally:
    if cursor is not None:
        cursor.close()

    if connection is not None and connection.is_connected():
        connection.close()


