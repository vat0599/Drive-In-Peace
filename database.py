import sqlite3
conn = sqlite3.connect('Test.db')
cursor = conn.execute("SELECT ID, NAME, ADDRESS, SLEPT from DATA")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SLEPT = ", row[3],"\n")
conn.close()
