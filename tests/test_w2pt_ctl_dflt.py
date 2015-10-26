#!/usr/bin/env python
# -*- coding: utf-8 -*-

from w2ptests import W2PTestCase

# Importa o controller a ser testado
import default
# Importa os modelos a serem utilizados
#import _web2py_brasil_utils
import carros
#import vitrine

class TestCtlDefault(W2PTestCase):
	def setUp(self):
		W2PTestCase.setUp(self,default)
		default.db = carros.db

	def test_index(self):
		inicializarDb(default.db)


		self.assertEqual('55','55')


	# def test_carros(self):
	# 	self.assertEqual('Text','Text')
	# def test_detalhes(self):
	# 	self.assertEqual('55','55')
	# def test_pesquisa(self):
	# 	self.assertEqual('Text','Text')
	# def test_admin(self):
	# 	self.assertEqual('55','55')

	# def test_cfib(self):
	# 	self.assertEqual(default.cfib()['message'],'55')
	# def test_text(self):
	# 	self.assertEqual(default.ctext()['text'],'Text')


def inicializarDb(__db__):
	id_marca1 = __db__.marca.insert(nome="marca1")
	id_marca2 = __db__.marca.insert(nome="marca2")

	__db__.carro.insert(marca=id_marca1,modelo="modelo1",ano=1950,
						cor="preto",valor=30.000,descr="um carro preto")



# db.define_table('carro',
#                 Field('marca', db.marca, notnull=True),
#                 Field('modelo', notnull=True),
#                 Field('ano', 'integer', notnull=True),
#                 Field('cor', notnull=True),
#                 Field('valor', 'double'),
#                 Field('itens', 'list:string'),
#                 Field('estado', notnull=True),
#                 Field('descr', 'text')