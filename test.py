import mysql.connector
from mysql.connector import Error
from datetime import datetime
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'danil',
    database = "testdatabase"
    )

# mycursor = mydb.cursor()

# # mycursor.execute("CREATE TABLE test (name varchar(50), created datetime, gender ENUM('M', 'F', 'O') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
# # mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s,%s,%s)", ('Joey', datetime.now(), "F"))
# # mycursor.execute("SELECT id,name, gender FROM Test WHERE id > 0 ORDER BY id DESC")

# # mycursor.execute("ALTER TABLE test ADD COLUMN food VARCHAR(50) NOT NULL")

# mycursor.execute("ALTER TABLE test CHANGE created when_created varchar(50)")

# mycursor.execute("DESCRIBE TEST")

# for i in mycursor:
#     print(i)


users = [("danil", "volobuyev"),
         ("danil1", "volobuyev1"),
         ("danil12", "volobuyev12")]

users_score = [(45,100),
               (12,312),
               (42,123)]

mycursor = mydb.cursor()

Q1 = "CREATE TABLE IF NOT EXISTED Users (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), passwd VARCHAR(50))"

Q2 = "CREATE TABLE IF NOT EXISTED Scores (userId int PRIMARY KEY, FOREIGN KEY(userId) REFERENCES Users(id), game1 int DEFAULT 0, game2 int DEFAULT 0)"

Q3 = "INSERT INTO Users (name, passwd) VALUES (%s,%s)"

Q4 = "INSERT INTO Scores (userId, game1, game2) VALUES (%s,%s,%s)"

for x,user in enumerate(users):
    mycursor.execute(Q3,user)
    last_id = mycursor.lastrowid
    mycursor.execute(Q4,(last_id,) + users_score[x])

mydb.commit()

mycursor.execute('SHOW DATABASES')
for i in mycursor:
    print(i)
    
# mycursor.execute("SELECT * FROM Users")
# for i in mycursor:
#     print(i)
    