import mysql.connector

def get_airports (area_code):
    sql = "select name, type from airport where iso_country = '"+ area_code + "' order by type asc, name asc;"
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    print(response)

connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    database = "flight_game",
    user = "****",
    password = "****",
    autocommit = True
)

area_code = input("To fetch the list of airports, enter the area code: ")
get_airports(area_code)
