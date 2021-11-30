# insert data to an existing table in postgres:
# table was created in django's models.py file
import psycopg2
import csv

conn = psycopg2.connect("host=localhost dbname=meteo user=postgres password=557878ars!!")
cur = conn.cursor()
with open('stations.csv', 'r') as file_stations:
    reader = csv.reader(file_stations, dialect='excel', delimiter=';')
    next(reader)  # Skip the header row.
    for row in reader:
        cur.execute(
            "INSERT INTO arkeo_meteostation VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            row
        )
conn.commit()
file_stations.close()

# see more: ds_projects/ml-weather/postgres_csv.ipynb
