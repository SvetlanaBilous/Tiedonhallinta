import mysql.connector

connection = None
cursor = None

try:

    connection = mysql.connector.connect(database='suunnittelutehtava3_svetlana_bilous', user='root')
    cursor = connection.cursor(prepared=True, dictionary=True)

    category_name = input("Anna kategorian nimi (crime, drama, comedy): ")

    query = ('SELECT title.* FROM title INNER JOIN category_has_title ON title.id = category_has_title.title_id INNER JOIN category ON category.id = category_has_title.category_id WHERE category.name = (%s)')

    cursor.execute(query, (category_name, ))

    titles_by_category = cursor.fetchall()

    for title in titles_by_category:
        print(title['name'])

except Exception as e:
    print(e)

finally:

    if cursor is not None:
        cursor.close()

    if connection is not None and connection.is_connected():
        connection.close()
