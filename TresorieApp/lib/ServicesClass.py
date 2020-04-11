# coding: utf-8
#!/usr/bin/env python
import ConnectionClass
import TresorieClass
class ServiceMouvement:
	"""
	c'est la classe :D
	"""
	def get_all(cls):
		mouvement=TresorieClass.Mouvement()
		Tresorie=ConnectionClass.ConnectSQL()
		print(Tresorie.connect('select * from mouvement'))
