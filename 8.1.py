import mysql.connector

def get_airport_and_city (icao):
    sql = "select airport.name, country.name from airport,country"
    sql += " where airport.iso_country = country.iso_country and airport.ident = '" + icao + "'";
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    print(response)


connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    database = "flight_game",
    user = "*****",
    password = "****",
    autocommit = True
)

icao = input("Enter ICAO airport code: ")
get_airport_and_city (icao.title())
