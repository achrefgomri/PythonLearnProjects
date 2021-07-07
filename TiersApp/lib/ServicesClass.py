from . import ConnectionClass
from . import TiersClass

class ServicesTiers:
    def get_all(cls):
        connect=ConnectionClass.ConnectionMysql()
        connect.execute('SELECT * FROM tier')
        liste=list()
        for row in connect.cursor:
            object_t=TiersClass.Tiers()
            object_t.ID=row['id']
            object_t.Type=row['type']
            object_t.nom=rom['nom']
            object_t.adresse=row['adresse']
            object_t.note=row['note']
            liste.append(object_t)
        return liste
    
    
        
    def get_by_id(cls,ID):
        connect=ConnectionClass.ConnectionMysql()
        connect.execute('SELECT * FROM tier WHERE id={}'.format(ID))
        row=connect.cursor[0]
        object_t=TiersClass.Tiers()
        object_t.ID=row['id']
        object_t.Type=row['type']
        object_t.nom=row['nom']
        object_t.adresse=row['adresse']
        object_t.note=row['note']
        return object_t
    
    def insert(cls,object_t):
        connect=ConnectionClass.ConnectionMysql()
        connect.execute('INSERT INTO tier (nom,type,adresse,note) VALUES({},{},{},{})'.format(str(object_t.nom),str(object_t.Type),str(object_t.adresse),str(object_t.note)))
    def update(cls,ID,object_t):
        connect=ConnectionClass.ConnectionMysql()
        connect.execute('UPDATE tier SET type={},nom={},adresse={},note={} WHERE id={}'.format(object_t.Type,object_t.nom,object_t.adresse,object_t.note,ID))
        
        
    def delete_by_id(cls,ID=''):
        connect=ConnectionClass.ConnectionMysql()
        if ID=='':
            connect.execute('DELETE FROM tier')
        else:
            connect.execute('DELETE FROM tier WHERE id={}'.format(ID))