#my use lib import
import time
import mysql.connector


#make connection to database
connector=mysql.connector.connect (
    user ='user', 
    password ='passwd', 
    host ='127.0.0.1', 
    database ='Ps4_db'
    #charset="utf8mb3"
    )

#time value
Localtime = time.asctime(time.localtime(time.time()))

#make cursor
cursor = connector.cursor(prepared=True)

#write mysql function
Start_Time_sql = "INSERT INTO Time (Start_Time) VALUE (Localtime)";

cursor.execute(Start_Time_sql)

#ready to finish?!
connector.commit()

#print time
print(Localtime)

#Number of rows added
print(cursor.rowcount, "Record Inserted!")

#ID of the last row added
print("Last ID is: ", cursor.lastrowid)


#*Stop_Time colum*

#The row ID to change
ID = input("Please insert ID:")

#write mysql function
#cursor.execute("UPDATE Time SET END_Time = localtime WHERE id = '%s' ", (int(ID),))

END_Time_sql = "UPDATE Time SET END_Time = localtime WHERE id = %s"

cursor.execute(END_Time_sql, (int(ID),))
#ready to finish?!
connector.commit()

#print time
print(Localtime)

#Number of rows added
print(cursor.rowcount, "Record Inserted!")

#ID of the last row added
print("Last ID is: ", cursor.lastrowid, (int(ID)))

#Done close it!
connector.close()
