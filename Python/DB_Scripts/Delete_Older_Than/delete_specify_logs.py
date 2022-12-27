import mysql.connector

mydb = mysql.connector.connect(
  host="HOST",
  port='PORT',
  user="USER",
  password="PWD",
  database="myschema" # Schema Name
)

# Temporary memory.
mycursor = mydb.cursor()

# Query.
sql = "DELETE FROM table_name WHERE column1_time < now() - interval 14 DAY AND column2_time IS NOT NULL"

# Execute.
mycursor.execute(sql)

# Used to confirm the changes made by the user to the database.
mydb.commit()

print(mycursor.rowcount, "record(s) deleted")