import psycopg2
from os import environ
conn = psycopg2.connect(dbname='Yandex_vinil', user=environ['DB_LOGIN'],
                        password=environ['DB_PASSWORD'], host=environ['DB_HOST'], port=64320)
cursor = conn.cursor()
cursor.execute('select musicians.name, labels.name, albums.name, albums.rating from albums'
               ' join musicians ON (albums.musician_id = musicians.id)'
               ' join labels ON (albums.label_id = labels.id) '
               'where albums.rating between 5 and 9 order by musicians.name ASC')
records = cursor.fetchall()
cursor.close()
conn.close()
print(records)
