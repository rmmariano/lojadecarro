#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importa a classe de teste W2PTestCase do pacote w2ptests
from w2ptests import W2PTestCase
# Importa o controller a ser testado
import default
# Importa os modelos a serem utilizados
import _web2py_brasil_utils
import vitrine
import carros

DB_CARROS = carros.db

class TestCtlDefault(W2PTestCase):
	def setUp(self):
		W2PTestCase.setUp(self,default,carros,vitrine)
		construirDependencias()

	def tearDown(self):
		# truncate apaga todos os registros e começa a contar os ids a partir do 1 novamente
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
			row_with_result_test(self,row,result)

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
			row_with_result_test(self,row,result)

	def test_detalhes01(self):
		inicializarDb(carros)
		default.request.args.append('1')
		id = default.request.args(0)
		query=default.db.carro.id==int(id) 
		rows=default.db(query).select()
		row = rows[0]                  
		titulo = "%(marca)s - %(modelo)s - %(ano)s - %(estado)s" % \
		    dict(marca=row.marca.nome,modelo=row.modelo,ano=row.ano,estado=row.estado)
		result=default.detalhes()
		self.assertEqual(result['titulo'],titulo)
		row_with_result_test(self,row,result)

	def test_detalhes02(self):
		# Como o banco não foi inicializado, então não há registro 1
		default.request.args.append('1')
		result=default.detalhes()
		not_found=str(default.H1('Veículo não encontrado'))
		self.assertEqual(str(result['vitrine']),not_found)

	def test_pesquisa01(self):
		inicializarDb(carros)
		default.request.vars.busca = 'ummodeloquenaoexisteaqui'
		result=str(default.pesquisa())
		# Como foi passado um modelo que não existe, deve retornar '<ul></ul>'
		self.assertEqual(result,'<ul></ul>')

	def test_pesquisa02(self):
		inicializarDb(carros)
		# A busca é feita pelo modelo do carro, então passa um modelo existente
		default.request.vars.busca = 'modelo2'
		result=str(default.pesquisa())
		# Como só existe 1 carro com o modelo2, deve retornar 1 <li> com o modelo e ano do carro 
		foo = '<ul><li><a href="http://detalhes/2/">modelo2 - 1950</a></li></ul>'
		self.assertEqual(result,foo)

	def test_pesquisa03(self):
		# Como não identificou o tipo de busca, a função pesquisa() deve retornar ''
		result=default.pesquisa()
		self.assertEqual(result,'')

	def test_admin01(self):
		inicializarDb(carros)
		result=default.admin()
		# O result['items'] deve retornar um <li> com uma URL para cada tabela no DB
		urls_dbs='<ul><li><a href="http://marca/">marca</a></li><li><a href="http://carro/">carro</a></li><li><a href="http://comprador/">comprador</a></li></ul>'
		self.assertEqual(result['titulo'],'administração')
		self.assertEqual(str(result['items']),urls_dbs)

	def test_admin02(self):
		inicializarDb(carros)
		table='marca'
		titulo = 'Inserir %s' % table
		query=default.db.marca.id>0
		rows=default.db(query).select()
		default.request.args.append(table)
		result=default.admin()
		self.assertEqual(result['titulo'],titulo)
		# Verifica se todos os registros de marca estão em result['items']
		for row in rows:
			self.assertEqual(True,self.inside(row.nome,result['items']))


def inicializarDb(foo):
	# o id dos registros começam do 1
	id_marca1 = foo.db.marca.insert(nome="marca1")
	id_marca2 = foo.db.marca.insert(nome="marca2")
	foo.db.carro.insert(marca=id_marca1,modelo="modelo1",ano=1950,estado="Novo",
						cor="Preto",valor=30000,descr="um carro preto novo",
						itens=['item1','item2'])
	foo.db.carro.insert(marca=id_marca2,modelo="modelo2",ano=1950,estado="Usado",
						cor="Azul",valor=20000,descr="um carro azul usado",
						itens=['item3'])

def construirDependencias():
	default.db = carros.db = DB_CARROS
	default.request = carros.request
	default.response = carros.response
	default.session = carros.session
	default.cache = carros.cache
	vitrine.Moeda=_web2py_brasil_utils.Moeda
	default.VITRINE=vitrine.VITRINE

def row_with_result_test(self,row,result):
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

# serve somente para verificar os registros existentes no inicializarDB
def verificarRegistros(self):
	inicializarDb(carros)
	query=default.db.carro.id>0
	rows=default.db(query).select(orderby=default.db.carro.id) 
	for r in rows:
		print r
		print '\n'
	self.assertEqual('55','55')

