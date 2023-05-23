import mysql.connector

connection = None
cursor = None

try:

    connection = mysql.connector.connect(database='suunnittelutehtava3_svetlana_bilous', user='root')
    cursor = connection.cursor(prepared=True, dictionary=True)

    query = ('SELECT review.points, title.name FROM review INNER JOIN title ON review.title_id = title.id ORDER BY points DESC LIMIT 10')

    cursor.execute(query)

    ten_most_liked_titles = cursor.fetchall()

    for title in ten_most_liked_titles:
        print(title['name'], title['points'])

except Exception as e:
    print(e)

finally:

    if cursor is not None:
        cursor.close()

    if connection is not None and connection.is_connected():
        connection.close()
