import mysql.connector

connection = None
cursor = None

try:
    connection = mysql.connector.connect(database='suunnittelutehtava3_svetlana_bilous', user='root')
    cursor = connection.cursor(prepared=True, dictionary=True)

    actor_firs_name = input("Anna näyttelijän etunimi: ")
    actor_last_name = input("Anna näyttelijän sukunimi: ")
    actor_date_of_birth = input("Anna näyttelijän syntymäpäivä (vv:kk:pp): ")
    actor_full_name = input("Anna näyttelijän etunumi ja sukunimi: ")

    insert_query = ("INSERT INTO actor(first_name, last_name, date_of_birth, full_name) VALUES((%s),(%s),(%s),(%s))")

    cursor.execute(insert_query, (actor_firs_name, actor_last_name, actor_date_of_birth, actor_full_name))
    connection.commit()
    print("Näyttelijä on tallennettu!")

except Exception as e:
    print(e)
    connection.rollback()

finally:
    if cursor is not None:
        cursor.close()

    if connection is not None and connection.is_connected():
        connection.close()


