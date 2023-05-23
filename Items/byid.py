import mysql.connector

connection = None
cursor = None

try:

    connection = mysql.connector.connect(database='suunnittelutehtava3_svetlana_bilous', user='root')
    cursor = connection.cursor(prepared=True, dictionary=True)

    title_id = input("Anna nimikeen id: ")

    query = ('SELECT title.*, review.points FROM title INNER JOIN review ON review.title_id = title.id WHERE title.id = (%s)')

    cursor.execute(query, (title_id, ))

    title_info_by_id = cursor.fetchone()

    print("Nimi:", title_info_by_id['name'])
    print("Valmistusvuosi:", title_info_by_id['year_of_production'])
    print("Kesto:", title_info_by_id['running_time'])
    print("Ikäraja:", title_info_by_id['recommended_age_limit'])
    print("Kuvaus:", title_info_by_id['description'])
    print("Arvostelu:", title_info_by_id['points'])

except Exception as e:
    print(e)

finally:

    if cursor is not None:
        cursor.close()

    if connection is not None and connection.is_connected():
        connection.close()
