#!/usr/bin/env python
# -*- coding: utf-8 -*-

from w2ptests import W2PTestCase

# Importa o controller a ser testado
import default
# Importa os modelos a serem utilizados
import _web2py_brasil_utils
import vitrine
import carros

class TestCtlDefault(W2PTestCase):
	def setUp(self):
		W2PTestCase.setUp(self,default,vitrine)
		#inicializarDb(carros)
		construirDependencias()

	def tearDown(self):
		for table_name in carros.db.tables():
			carros.db[table_name].truncate()
		carros.db.commit()

	def test_index(self):	
		inicializarDb(carros)

		query=default.db.carro.id>0
		rows=default.db(query).select(orderby=default.db.carro.id) 
		result=default.index()
		self.assertEqual(result['titulo'],'Ofertas')
		for row in rows:
			self.assertEqual(True,self.inside(default.URL('detalhes', args=row.id),result['vitrine']))
			self.assertEqual(True,self.inside(row.marca,result['vitrine']))
			self.assertEqual(True,self.inside(row.modelo,result['vitrine']))
			self.assertEqual(True,self.inside(row.ano,result['vitrine']))
			self.assertEqual(True,self.inside(row.estado,result['vitrine']))
			self.assertEqual(True,self.inside(row.cor,result['vitrine']))
			for item in row.itens:
				self.assertEqual(True,self.inside(item,result['vitrine']))	
			self.assertEqual(True,self.inside(row.descr,result['vitrine']))
			self.assertEqual(True,self.inside(_web2py_brasil_utils.Moeda(row.valor),result['vitrine']))

	def test_carros(self):
		inicializarDb(carros)

		default.request.args.append('Novos')
		estado = default.request.args(0)
		query=default.db.carro.estado==estado[:-1].capitalize()  
		rows=default.db(query).select(orderby=default.db.carro.id)
		titulo='Carros %s' % estado.capitalize()
		result=default.carros()
		self.assertEqual(result['titulo'],titulo)
		for row in rows:
			self.assertEqual(True,self.inside(default.URL('detalhes', args=row.id),result['vitrine']))
			self.assertEqual(True,self.inside(row.marca,result['vitrine']))
			self.assertEqual(True,self.inside(row.modelo,result['vitrine']))
			self.assertEqual(True,self.inside(row.ano,result['vitrine']))
			self.assertEqual(True,self.inside(row.estado,result['vitrine']))
			self.assertEqual(True,self.inside(row.cor,result['vitrine']))
			for item in row.itens:
				self.assertEqual(True,self.inside(item,result['vitrine']))	
			self.assertEqual(True,self.inside(row.descr,result['vitrine']))
			self.assertEqual(True,self.inside(_web2py_brasil_utils.Moeda(row.valor),result['vitrine']))

	def test_detalhes(self):
		self.assertEqual('55','55')


	# def test_pesquisa(self):
	# 	self.assertEqual('Text','Text')
	# def test_admin(self):
	# 	self.assertEqual('55','55')


def inicializarDb(foo):
	id_marca1 = foo.db.marca.insert(nome="marca1")
	id_marca2 = foo.db.marca.insert(nome="marca2")

	foo.db.carro.insert(marca=id_marca1,modelo="modelo1",ano=1950,estado="Novo",
						cor="Preto",valor=30000,descr="um carro preto novo",
						itens=['item1','item2'])
	foo.db.carro.insert(marca=id_marca2,modelo="modelo2",ano=1950,estado="Usado",
						cor="Azul",valor=20000,descr="um carro azul usado",
						itens=['item3'])

def construirDependencias():
	default.db = carros.db
	vitrine.Moeda=_web2py_brasil_utils.Moeda
	default.VITRINE=vitrine.VITRINE
