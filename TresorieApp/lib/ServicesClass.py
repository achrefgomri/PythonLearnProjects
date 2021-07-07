# coding: utf-8
#!/usr/bin/env python
from . import ConnectionClass
from . import TresorieClass
class ServiceMouvement:
	"""
	c'est la classe :D
	"""
	def get_all(cls):
		#mouvement=TresorieClass.Mouvement()
		Tresorie=ConnectionClass.ConnectSQL()
		list_row=list()
		Tresorie.execute('select * from mouvement')
		#print(a)
		#print(Tresorie.cursor.__dict__)
		for row in Tresorie.cursor:
			mouvement=TresorieClass.Mouvement()
			mouvement.id=row['id']
			mouvement.type=row['type']
			mouvement.nature=row['nature']
			mouvement.id_caisse=row['id_caisse']
			mouvement.valeur=row['valeur']
			mouvement.motif=row['motif']
			mouvement.date_valeur=row['date_valeur']
			list_row.append(mouvement)
		return list_row

	def get_by (cls,colonne,valeur):
		#mouvement=TresorieClass.Mouvement()
		Tresorie=ConnectionClass.ConnectSQL()
		list_row=list()
		Tresorie.execute('select * from mouvement where {}={}'.format(colonne,valeur))
		#Tresorie.cursor:
		for row in Tresorie.cursor:
			#print('00000000000000000000000000000000000000')
			#print(row)
			mouvement=TresorieClass.Mouvement()
			mouvement.id=row['id']
			mouvement.type=row['type']
			mouvement.nature=row['nature']
			mouvement.id_caisse=row['id_caisse']
			mouvement.valeur=row['valeur']
			mouvement.motif=row['motif']
			mouvement.date_valeur=row['date_valeur']
			list_row.append(mouvement)
		if len(list_row)==1:
			list_row=list_row[0]
		return list_row
	def insert (cls,m_object):
		Tresorie=ConnectionClass.ConnectSQL()
		Tresorie.execute('INSERT INTO mouvement ({0},{1},{2},{3},{4}) VALUES ({5},{6},{7},{8},{9})'.format('nature','id_caisse','valeur','motif','date_valeur',m_object.nature,m_object.id_caisse,m_object.valeur,m_object.motif,m_object.date_valeur))
	


	def delete_by (cls,colonne='',valeur=''):
		Tresorie=ConnectionClass.ConnectSQL()
		if (colonne==''):
			Tresorie.execute('DELETE FROM mouvement')
		else:
			Tresorie.execute('DELETE FROM mouvement WHERE {}={}'.format(colonne,valeur))
	def update (cls,m_object,colonne,valeur):
		Tresorie=ConnectionClass.ConnectSQL()
		del m_object.__dict__[colonne]
		list_i=list()
		list_values=list()
		for i in m_object.__dict__:
			list_i.append(i)
			list_values.append(m_object.__dict__[i])

		Tresorie.execute('UPDATE mouvement SET {}={},{}={},{}={},{}={},{}={},{}={} WHERE {}={}'.format(list_i[0],list_values[0],list_i[1],list_values[1],list_i[2],list_values[2],list_i[3],list_values[3],list_i[4],list_values[4],list_i[5],list_values[5],colonne,valeur))
		m_object.colonne=valeur

class ServiceCaisse:
	"""
	C'est aussi la classe :D :D
	"""
	def get_all(cls):
		#caisse=TresorieClass.Caisse()
		Tresorie=ConnectionClass.ConnectSQL()
		list_row=list()
		Tresorie.execute('select * from caisse')
		#print(Tresorie.cursor)
		for row in Tresorie.cursor:
			caisse=TresorieClass.Caisse()
			caisse.id=row['id']
			caisse.nom=row['nom']
			caisse.valeur=row['valeur']
			caisse.date_creation=row['date_creation']
			caisse.commentaire=row['commentaire']
			list_row.append(caisse)
		return list_row

	def get_by (cls,table,valeur):
		#caisse=TresorieClass.Caisse()
		Tresorie=ConnectionClass.ConnectSQL()
		list_row=list()
		Tresorie.execute('select * from caisse where {}={}'.format(table,valeur))
		#Tresorie.cursor:
		for row in Tresorie.cursor:
			caisse=TresorieClass.Caisse()
			caisse.id=row['id']
			caisse.nom=row['nom']
			caisse.valeur=row['valeur']
			caisse.date_creation=row['date_creation']
			caisse.commentaire=row['commentaire']
			list_row.append(caisse)
		if len(list_row)==1:
			list_row=list_row[0]
		return list_row
	def insert (cls,c_object):
		Tresorie=ConnectionClass.ConnectSQL()
		Tresorie.execute('INSERT INTO caisse ({0},{1},{2},{3}) VALUES ({4},{5},{6},{7})'.format('nom','valeur','date_creation','commentaire',c_object.nom,c_object.valeur,c_object.date_creation,c_object.commentaire))
                




