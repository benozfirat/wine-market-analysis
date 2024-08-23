import sqlite3
import csv

conn = sqlite3.connect('db/vivino.db')
cursor = conn.cursor()

req = ('''
    select distinct wines.name as name, wines.ratings_average as ratings_average, countries.name as country
    from wines
    join regions on wines.region_id = regions.id
    join countries on regions.country_code = countries.code
    join keywords_wine on wines.id = keywords_wine.wine_id
    join keywords on keywords.id = keywords_wine.keyword_id
    where keywords.name in ('coffee', 'toast', 'green apple', 'cream', 'citrus')
    and keywords_wine.count >= 10
    order by keywords_wine.count desc
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
