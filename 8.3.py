import mysql.connector
from geopy.distance import geodesic as GD

def get_airport_name (icao):
    sql = "select airport.name from airport where ident = '" + icao +"'"
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    if cursor.rowcount >= 0:
        for row in response:
            airport = row[0]
            print(f"Airport name is {row[0]}")
    return airport

def get_country_name (icao):
    sql = "select country.name from country, airport where airport.iso_country = country.iso_country and ident = '" + icao +"'"
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    if cursor.rowcount >= 0:
        for row in response:
            country = row[0]
            print(f"Country name is {row[0]}")
    return country

def get_latitude (icao):
    sql = "select latitude_deg from airport where ident = '" + icao +"'"
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    if cursor.rowcount >= 0:
        for row in response:
            latitude = row[0]
            print(f"Latitude is {row[0]}")
    return latitude

def get_longitude (icao):
    sql = "select longitude_deg from airport where ident = '" + icao +"'"
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    if cursor.rowcount >= 0:
        for row in response:
            longitude = row[0]
            print(f"Longitude is {row[0]}")
    return longitude

def calculate_distance (lat1,long1, lat2, long2):
    air1 = (lat1,long1)
    air2 = (lat2,long2)
    distance = GD(air1, air2).km
    #print(distance)
    return distance

connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    database = "flight_game",
    user = "****",
    password = "****",
    autocommit = True
)

icao1 = input("Enter icao code of the first airport: ")
airport1_name = get_airport_name(icao1)
airport1_country = get_country_name(icao1)
airport1_laitude = get_latitude(icao1)
airport1_longitude = get_longitude(icao1)

icao2 = input("Enter icao code of the second airport: ")
airport2_name = get_airport_name(icao2)
airport2_country = get_country_name(icao2)
airport2_laitude = get_latitude(icao2)
airport2_longitude = get_longitude(icao2)

distance = round(calculate_distance(airport1_laitude,airport1_longitude,airport2_laitude,airport2_longitude),3)

print(f"The distance between {airport1_name} in {airport1_country} and {airport2_name} in {airport2_country} is {distance} km")
