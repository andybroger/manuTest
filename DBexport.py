import mysql.connector

# setup mysql connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testing",
    # auth_plugin='mysql_native_password'
)

# craete dictionary cursor
cursor = db.cursor(dictionary=True)
# execute query against table
cursor.execute("SELECT * FROM Properties")

# fetch results
result_set = cursor.fetchall()

# define file output
file = open("unload.txt", "w")

# write each row to file
for row in result_set:
    file.write("#{id}#{name}#{title}#{description}#\n".format(**row))
