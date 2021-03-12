import sqlite3


database = input()
condition_one = input()
condition_two = input()
sort_by = input()

conn = sqlite3.connect(database)
c = conn.cursor()
c.execute("SELECT condition FROM Talks WHERE "+condition_one+" AND "+condition_two+" ORDER BY "+sort_by+" ASC")
conditions_list = c.fetchall()
c.close()

for e in conditions_list:
    print(*e)
