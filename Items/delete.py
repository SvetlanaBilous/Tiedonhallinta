import mysql.connector

connection = None
cursor = None

try:
    connection = mysql.connector.connect(database='suunnittelutehtava3_svetlana_bilous', user='root')
    cursor = connection.cursor(prepared=True, dictionary=True)

    print("Nimikkeen poistaminen! ")
    title_id = input("Anna nimikkeen id: ")

    insert_query = ("DELETE FROM title WHERE id = (%s)")

    cursor.execute(insert_query, (title_id, ))
    connection.commit()
    print("Nimike on poistettu!")

except Exception as e:
    print(e)
    connection.rollback()

finally:
    if cursor is not None:
        cursor.close()

    if connection is not None and connection.is_connected():
        connection.close()


