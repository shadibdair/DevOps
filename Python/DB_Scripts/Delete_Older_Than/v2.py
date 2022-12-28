import mysql.connector
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('Host' , type=str, help='Host')
parser.add_argument('Port' , type=str, help='Port')
parser.add_argument('User' , type=str, help='User')
parser.add_argument('Password' , type=str, help='Password')
parser.add_argument('Database' , type=str, help='Database')

args = parser.parse_args()

# Environment Variables
HOST = args.Host
PORT = args.Port
USER = args.User
PASSWORD = args.Password
DATABASE = args.Database

mydb = mysql.connector.connect(
  host=HOST,
  port=PORT,
  user=USER,
  password=PASSWORD,
  database=DATABASE, # Schema Name
  connection_timeout=30
)

# global connection timeout argument
global_connect_timeout = 'SET GLOBAL connect_timeout=30'

# Temporary memory.
mycursor = mydb.cursor()

# Query.
sql = "DELETE FROM table_name WHERE column1_time < now() - interval 14 DAY AND column2_time IS NOT NULL"

# Execute.
mycursor.execute(sql, global_connect_timeout)

# Used to confirm the changes made by the user to the database.
mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
