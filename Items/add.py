import mysql.connector

connection = None
cursor = None

try:
    connection = mysql.connector.connect(database='suunnittelutehtava3_svetlana_bilous', user='root')
    cursor = connection.cursor(prepared=True, dictionary=True)

    title_name = input("Anna nimikkeen nimi: ")
    title_year_of_production = input("Anna nimikkeen valmistusvuosi: ")
    title_running_time = input("Anna nimikkeen kesto (tt:mm:ss): ")
    title_type = input("Anna nimikkeen tyyppi (1 - elokuva, 2 - kirja): ")
    title_recommended_age_limit = input("Anna ikäraja: ")
    title_description = input("Anna nimikkeen kuvaus: ")

    insert_query = ("INSERT INTO title(name, year_of_production, running_time, title_type_id, recommended_age_limit, description) VALUES((%s),(%s),(%s),(%s),(%s),(%s))")

    cursor.execute(insert_query, (title_name, title_year_of_production, title_running_time, title_type, title_recommended_age_limit, title_description))
    connection.commit()
    print("Nimike on tallennettu!")

except Exception as e:
    print(e)
    connection.rollback()

finally:
    if cursor is not None:
        cursor.close()

    if connection is not None and connection.is_connected():
        connection.close()


