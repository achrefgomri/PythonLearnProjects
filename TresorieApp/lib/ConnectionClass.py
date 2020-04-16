# coding: utf-8
#!/usr/bin/env python
import pymysql.cursors
import re
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
			#Closez la connexion (Close connection).
			connection.close()
	def add_line (self, table, list_valeurs={}):
		"""
        add_line
    """
		connection = pymysql.connect(host=str(self.host),
                                user=str(self.user),
                                password=str(self.password),
                                db=str(self.db),
                                charset=str(self.charset),
                                cursorclass=pymysql.cursors.DictCursor)
    
		try:
			with connection.cursor() as cursor:
				# Create a new record
				liste_colones=list()
				list_valeur=list()
				if len(list_valeurs)>1:
					for val in list_valeurs:
						liste_colones.append(val)
						list_valeur.append(list_valeurs[val])
					sql = "INSERT INTO "+str(table)+str(tuple(liste_colones))+" VALUES "+str(tuple(list_valeur))
					sql=re.sub("[\']*", r"", sql)
					print (str(sql))
					cursor.execute(sql)
					connection.commit()
				#print (sql,"    ",list_valeurs)
				else:
					print("erreur")
		finally:
			#Closez la connexion (Close connection).
			connection.close()
        def del_lines (self, table, condition=''):
                """
        add_line
    """
                connection = pymysql.connect(host=str(self.host),
                                user=str(self.user),
                                password=str(self.password),
                                db=str(self.db),
                                charset=str(self.charset),
                                cursorclass=pymysql.cursors.DictCursor)

                try:
                        with connection.cursor() as cursor:
                                if condition=='':
                                	sql = "DELETE FROM "+str(table)
                                else:
                                        sql="DELETE FROM "+str(table)+" WHERE "+condition
				print (str(sql))
				cursor.execute(sql)
				connection.commit()
                finally:
                        #Closez la connexion (Close connection).
                        connection.close()

	def __connect__(self):
        	self.connection = pymysql.connect(host=str(self.host),
                             user=str(self.user),
                             password=str(self.password),
                             db=str(self.db),
                             charset=str(self.charset),
                             cursorclass=pymysql.cursors.DictCursor)

        	#self.cur = self.con.cursor()
		self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
		#cursor.execute("SELECT ...")

	def __disconnect__(self):
		self.connection.close()

	def fetch(self, sql):
		self.__connect__()
		self.cursor.execute(sql)
		result = self.cursor.fetchall()
		self.__disconnect__()
		return result
	
	def request(self, sql):
        	self.__connect__()
        	self.cursor.execute(sql)
        	self.__disconnect__()
	
	def execute(self, sql):
                self.__connect__()
                self.cursor.execute(sql)
		self.connection.commit()
                self.__disconnect__()
