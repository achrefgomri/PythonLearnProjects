#!/usr/bin/env python
import pymysql.cursors
 
# Connectez- vous à la base de données.
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Azerty22',                             
                             db='TresorieDB',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
 
print ("connect successful!!")
 
try:
  
 
    with connection.cursor() as cursor:
       
        # SQL 
        sql = "SELECT * from mouvement "
         
        # Exécutez la requête (Execute Query).
        cursor.execute(sql)
	
         
        print ("cursor.description: ", cursor.description)
 
        print()
 
        for row in cursor:
            print(row)
             
finally:
    # Closez la connexion (Close connection).      
    connection.close()
