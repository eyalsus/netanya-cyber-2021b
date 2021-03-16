import sqlite3

con = sqlite3.connect('users.db')
cur = con.cursor()


# user_database = [
#     {'username': 'alice', 'password': '1234'},
#     {'username': 'bob', 'password': '2345'}
# ]

# Create table
cur.execute('''CREATE TABLE users
               (username text, password text)''')

# Insert a row of data
cur.execute("INSERT INTO users (username, password) VALUES ('alice', '1234'), ('bob', '2345')")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()