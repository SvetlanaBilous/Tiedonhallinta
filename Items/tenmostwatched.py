import mysql.connector

connection = None
cursor = None

try:

    connection = mysql.connector.connect(database='suunnittelutehtava3_svetlana_bilous', user='root')
    cursor = connection.cursor(prepared=True, dictionary=True)

    query = ('SELECT title.name, user_has_title.title_id, SUM(user_has_title.watch_times) as total_watch_times FROM user_has_title INNER JOIN title ON user_has_title.title_id = title.id GROUP BY title_id ASC LIMIT 10')

    cursor.execute(query)

    ten_most_watched_titles = cursor.fetchall()

    for title in ten_most_watched_titles:
        print(title['name'], title['total_watch_times'])

except Exception as e:
    print(e)

finally:

    if cursor is not None:
        cursor.close()

    if connection is not None and connection.is_connected():
        connection.close()
