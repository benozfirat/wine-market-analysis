import sqlite3
import csv

conn = sqlite3.connect('db/vivino.db')
cursor = conn.cursor()

req = ('''
    select wines.name as name, wines.ratings_average as  "rating avg",  wines.ratings_count as "rating count", countries.name as country
    from wines 
    join regions on wines.region_id = regions.id
    join countries on regions.country_code = countries.code
    where countries.name = 'Italie'
    order by wines.ratings_average desc
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
