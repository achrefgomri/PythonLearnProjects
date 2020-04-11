#!/usr/bin/env python
import pymysql.cursors
class ConnectSQL :


	def __init__(self,host='ubuntuakrem.magsecurity.tn',user='root',password='Azerty22',db='TresorieDB',charset='utf8mb4'):
		
		self.host=str(host)
		self.user=str(user)
		self.password=str(password)                             
		self.db=str(db)
		self.charset=str(charset)
		
		connection = pymysql.connect(host=str(self.host),
                             user=str(self.user),
                             password=str(self.password),                             
                             db=str(self.db),
                             charset=str(self.charset),
                             cursorclass=pymysql.cursors.DictCursor)
		print ("connect successful!!")
		
		connection.close()
	def connect(self,sql_commande):
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
 
				print("\n")
 
				for row in cursor:
					print(row)
             
		finally:
			# Closez la connexion (Close connection).      
			connection.close()
	
	def add_line(self,sql_commande="INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)",*list_valeurs):
		connection = pymysql.connect(host=str(self.host),
                             user=str(self.user),
                             password=str(self.password),                             
                             db=str(self.db),
                             charset=str(self.charset),
                             cursorclass=pymysql.cursors.DictCursor)

		try:
			with connection.cursor() as cursor:
				# Create a new record
				sql = str(sql_commande)
				cursor.execute(sql, list_valeurs)

			print (sql,"    ",list_valeurs)
		finally:
			# Closez la connexion (Close connection).      
			connection.close()
	
	
