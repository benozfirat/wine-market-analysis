import sqlite3
import csv

conn = sqlite3.connect('db/vivino.db')
cursor = conn.cursor()

req = ('''
       select vintages.name, vintages.year, vintages.price_euros, vintages.ratings_average, countries.name as country
       from vintages
       join wines on vintages.wine_id = wines.id
       join regions on wines.region_id = regions.id
       join countries on regions.country_code = countries.code
       where vintages.ratings_count > 500
       order by vintages.ratings_average desc
       limit 1
''')

cursor.execute(req)

rows = cursor.fetchall()
csv_file_name = 'wines_data.csv'

with open(csv_file_name, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    headers = [i[0] for i in cursor.description]
    csv_writer.writerow(headers)
    
    csv_writer.writerows(rows)

conn.close()
