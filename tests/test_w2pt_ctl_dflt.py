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

DB = carros.db

class TestCtlDefault(W2PTestCase):
	def setUp(self):
		W2PTestCase.setUp(self,default,carros,vitrine)
		#inicializarDb(carros)
		construirDependencias()

	def tearDown(self):
		# truncate apaga todos os registros e começa a contar os ids a partir do 1 novamente
		for table_name in carros.db.tables():
			carros.db[table_name].truncate()
		carros.db.commit()

	def test_index(self):	
		# verificarRegistros(self)

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
		# verificarRegistros(self)

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
		# verificarRegistros(self)

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


		# for row in rows:
		# 	self.assertEqual(True,self.inside(default.URL('detalhes', args=row.id),result['vitrine']))
		# 	self.assertEqual(True,self.inside(row.marca,result['vitrine']))
		# 	self.assertEqual(True,self.inside(row.modelo,result['vitrine']))
		# 	self.assertEqual(True,self.inside(row.ano,result['vitrine']))
		# 	self.assertEqual(True,self.inside(row.estado,result['vitrine']))
		# 	self.assertEqual(True,self.inside(row.cor,result['vitrine']))
		# 	for item in row.itens:
		# 		self.assertEqual(True,self.inside(item,result['vitrine']))	
		# 	self.assertEqual(True,self.inside(row.descr,result['vitrine']))
		# 	self.assertEqual(True,self.inside(_web2py_brasil_utils.Moeda(row.valor),result['vitrine']))

		# self.assertEqual('55','55')




  
    
 #    #cria um objeto de retorno
 #    vitrine = VITRINE(rows)
    
 #    # caso existam dados cria outros objetos    
 #    if rows:
                
 #        #Configurações para o formulário            
 #        db.comprador.id_carro.default = id
 #        db.comprador.id_carro.readable = False
 #        db.comprador.id_carro.writable = False 
        
 #        #criação do formulário       
 #        form = SQLFORM(db.comprador,formstyle='divs',submit_button='Enviar')
        
 #        #validação do formulário    
 #        if form.accepts(request.vars, session):
 #            response.flash = 'formulário aceito'
            
 #            #alteração do formulário em caso de sucesso
 #            form = DIV(H3('Sua mensagem foi enviada, em breve entraremos em contato'))
                
 #        elif form.errors:
 #            response.flash = 'formulário contém erros'
                                        
 #        return dict(vitrine=vitrine,titulo=titulo,form=form)
        
 #    else:
 #        return dict(vitrine=H1('Veículo não encontrado'))  





	# def test_pesquisa(self):
	# 	self.assertEqual('Text','Text')

	# def test_admin(self):
	# 	self.assertEqual('55','55')


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
	default.db = carros.db = DB
	default.request = carros.request
	default.response = carros.response
	default.session = carros.session
	default.cache = carros.cache
	vitrine.Moeda=_web2py_brasil_utils.Moeda
	default.VITRINE=vitrine.VITRINE

# serve somente para verificar os registros existentes no inicializarDB
def verificarRegistros(self):
	inicializarDb(carros)
	query=default.db.carro.id>0
	rows=default.db(query).select(orderby=default.db.carro.id) 
	for r in rows:
		print r
		print '\n'
	self.assertEqual('55','55')