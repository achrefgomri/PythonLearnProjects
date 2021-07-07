import pymysql.cursors

class ConnectionMysql:
    def __init__(self,host='ubuntuakrem.magsecurity.tn',user='root',password='Azerty22',db='TiersDB',charset='utf8mb4'):
        self.host=str(host)
        self.user=str(user)
        self.password=str(password)                             
        self.db=str(db)
        self.charset=str(charset)
		
        self.connection = pymysql.connect(host=str(self.host),
            user=str(self.user),
            password=str(self.password),                             
            db=str(self.db),
            charset=str(self.charset),
            cursorclass=pymysql.cursors.DictCursor)
        print ("connect successful!!")
		
        self.connection.close()
    def __connect(self):
        self.connection = pymysql.connect(host=str(self.host),
            user=str(self.user),
            password=str(self.password),                             
            db=str(self.db),
            charset=str(self.charset),
            cursorclass=pymysql.cursors.DictCursor)
            
        self.cursor=self.connection.cursor(pymysql.cursors.DictCursor)
            
    def __disconnect(self):
        self.connection.close()
    
    def execute(self,sql):
        self.__connect()
        self.cursor.execute(sql)
        self.connection.commit()
        self.__disconnect()