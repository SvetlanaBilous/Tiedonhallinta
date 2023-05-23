import mysql.connector

connection = None
cursor = None

try:

    connection = mysql.connector.connect(database='suunnittelutehtava3_svetlana_bilous', user='root')
    cursor = connection.cursor(prepared=True, dictionary=True)

    user_email = input("Anna userin sähköpostiosoite: ")

    query = ('SELECT user.e_mail, title.name FROM user INNER JOIN user_has_title ON user.id = user_has_title.user_id INNER JOIN title ON title.id = user_has_title.title_id WHERE user.e_mail = (%s)')

    cursor.execute(query, (user_email, ))

    ten_most_watched_titles = cursor.fetchall()

    print(f"Käyttäjä {user_email} on katsonut seuraavat nimikeet: ")
    for title in ten_most_watched_titles:
        print(title['name'])

except Exception as e:
    print(e)

finally:

    if cursor is not None:
        cursor.close()

    if connection is not None and connection.is_connected():
        connection.close()
