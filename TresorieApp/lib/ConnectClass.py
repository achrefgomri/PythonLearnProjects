#!/usr/bin/env python
import pymysql.cursors
class ConnectSQL 


	def __init__(self,host=localhost,user=root,password='Azerty22',db='TresorieDB',charset='utf8mb4'):
		self.host=host
		self.user=user
		self.password=password
		self.db=db
		self.charset=charset
		self.cursorclass=pymysql.cursors.DictCursor
		
	def connect(sql_commande)
# Connectez- vous à la base de données.
		connection = pymysql.connect(host=str(self.host),
                             user=str(self.user),
                             password=str(self.password),                             
                             db=str(self.db),
                             charset=str(self.charset),
                             cursorclass=pymysql.cursors.DictCursor)
 
		print ("connect successful!!")
 
		try:
  
 
			with connection.cursor() as cursor:
       
			# SQL 
			sql = str(sql_commande)
         
			# Exécutez la requête (Execute Query).
			cursor.execute(sql)
	
         
			print ("cursor.description: ", cursor.description)
 
			print()
 
			for row in cursor:
            print(row)
             
	finally:
		# Closez la connexion (Close connection).      
		connection.close()
