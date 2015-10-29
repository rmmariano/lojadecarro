#!/usr/bin/env python
# -*- coding: utf-8 -*-

# importa o TestCase, para a criacao do W2PTestCase
from unittest import TestCase

# importa o Mock, para a criação dos objetos falsos.
from mock import Mock

# importa os imports automáticos do web2py
from imports import *

class W2PTestCase(TestCase):
	PROJECT_PATH=path.sep.join(path.abspath(__file__).split(path.sep)[:-2])
	filename='tests/db_test.sqlite'
	
	def setUp(self,*controllers):
		for c in controllers:
			c.db=None

			c.T=Mock(side_effect=__T__)
			c.URL=Mock(side_effect=__URL__)
			c.IS_URL=Mock(side_effect=__IS_URL__)

			c.request=request # = web2py 2.1.1
			#c.request=Request({}) # > web2py 2.1.1
			c.cache=cache
			c.response=response
			c.session=session
			c.redirect=redirect

			import_classes(c)
			import_gluon_validators(c)
			import_gluon_html(c)

	# def tearDown(self):
	# 	print '\nteardown--------------------------\n'
	# 	self.clearDB()

	# def clearDB(self):
	# 	delete_file(self.PROJECT_PATH+'/sql.log')
	# 	files = glob(self.PROJECT_PATH+'/*.table')
	# 	for f in files:
	# 		delete_file(f)
	# 	files = glob(self.PROJECT_PATH+'/'+self.filename+'*')
	# 	for f in files:
	# 		delete_file(f)

	def inside(self,a,b):
		if str(a) in str(b):
			return True
		return False
	
# objeto fake do T
def __T__(f):
	return f

#URL('detalhes', args=row.id)
# new
# objeto fake do URL
def __URL__(foo,**dfoo):
	foo = 'http://'+str(foo)
	#hu = dict(sorted(dfoo.items(), key=lambda x: x[0]))
	#from operator import itemgetter
	#hu = sorted(dfoo.items(), key=itemgetter(0))
	for f in dfoo:
		foo=foo+'/'+str(dfoo[f])
	return foo

def __IS_URL__(foo,**dfoo):
	foo = str(foo)
	if foo.startswith('http://') or foo.startswith('https://'):
		return True
	return False


def import_classes(mod):
	mod.Request=Request
	mod.Cache=Cache
	mod.Response=Response
	mod.Session=Session

	mod.HTTP=HTTP
	mod.DAL=DAL
	mod.Field=Field
	mod.SQLDB=SQLDB
	mod.SQLFORM=SQLFORM

def import_gluon_validators(mod):
	#mod.IS_URL=IS_URL # criado mock para ele

	mod.CLEANUP=CLEANUP
	mod.CRYPT=CRYPT
	mod.IS_ALPHANUMERIC=IS_ALPHANUMERIC
	mod.IS_DATE=IS_DATE
	mod.IS_DATETIME=IS_DATETIME
	mod.IS_DATETIME_IN_RANGE=IS_DATETIME_IN_RANGE
	mod.IS_DATE_IN_RANGE=IS_DATE_IN_RANGE
	mod.IS_DECIMAL_IN_RANGE=IS_DECIMAL_IN_RANGE
	mod.IS_EMAIL=IS_EMAIL
	mod.IS_EMPTY_OR=IS_EMPTY_OR
	mod.IS_EQUAL_TO=IS_EQUAL_TO
	mod.IS_EXPR=IS_EXPR
	mod.IS_FLOAT_IN_RANGE=IS_FLOAT_IN_RANGE
	mod.IS_IMAGE=IS_IMAGE
	mod.IS_INT_IN_RANGE=IS_INT_IN_RANGE
	mod.IS_IN_DB=IS_IN_DB
	mod.IS_IN_SET=IS_IN_SET	
	mod.IS_IPV4=IS_IPV4
	mod.IS_LENGTH=IS_LENGTH
	mod.IS_LIST_OF=IS_LIST_OF
	mod.IS_LOWER=IS_LOWER
	mod.IS_MATCH=IS_MATCH
	mod.IS_NOT_EMPTY=IS_NOT_EMPTY
	mod.IS_NOT_IN_DB=IS_NOT_IN_DB
	mod.IS_NULL_OR=IS_NULL_OR
	mod.IS_SLUG=IS_SLUG
	mod.IS_STRONG=IS_STRONG
	mod.IS_TIME=IS_TIME
	mod.IS_UPLOAD_FILENAME=IS_UPLOAD_FILENAME
	mod.IS_UPPER=IS_UPPER

	# não funcionam quando usados dentro do virtualenv utilizando o gluon do web2py
	# que foi instalado (pip install web2py)
	# mod.ANY_OF=ANY_OF
	# mod.IS_IPADDRESS=IS_IPADDRESS
	# mod.IS_IPV6=IS_IPV6
	# mod.IS_JSON=IS_JSON
	# mod.IS_LIST_OF_EMAILS=IS_LIST_OF_EMAILS

def import_gluon_html(mod):
	#mod.URL=URL # criado mock para ele

	mod.A=A
	mod.B=B
	mod.BEAUTIFY=BEAUTIFY
	mod.BODY=BODY
	mod.BR=BR
	mod.BUTTON=BUTTON
	mod.CAT=CAT
	mod.CENTER=CENTER
	mod.CODE=CODE
	mod.COL=COL
	mod.COLGROUP=COLGROUP
	mod.DIV=DIV
	mod.EM=EM
	mod.EMBED=EMBED
	mod.FIELDSET=FIELDSET
	mod.FORM=FORM
	mod.H1=H1
	mod.H2=H2
	mod.H3=H3
	mod.H4=H4
	mod.H5=H5
	mod.H6=H6
	mod.HEAD=HEAD
	mod.HR=HR
	mod.HTML=HTML
	mod.I=I
	mod.IFRAME=IFRAME
	mod.IMG=IMG
	mod.INPUT=INPUT
	mod.LABEL=LABEL
	mod.LEGEND=LEGEND
	mod.LI=LI
	mod.LINK=LINK
	mod.MARKMIN=MARKMIN
	mod.MENU=MENU
	mod.META=META
	mod.OBJECT=OBJECT
	mod.OL=OL
	mod.ON=ON
	mod.OPTGROUP=OPTGROUP
	mod.OPTION=OPTION
	mod.P=P
	mod.PRE=PRE
	mod.SCRIPT=SCRIPT
	mod.SELECT=SELECT
	mod.SPAN=SPAN
	mod.STRONG=STRONG
	mod.STYLE=STYLE
	mod.TABLE=TABLE
	mod.TAG=TAG
	mod.TBODY=TBODY
	mod.TD=TD
	mod.TEXTAREA=TEXTAREA
	mod.TFOOT=TFOOT
	mod.TH=TH
	mod.THEAD=THEAD
	mod.TITLE=TITLE
	mod.TR=TR
	mod.TT=TT
	mod.UL=UL
	mod.XHTML=XHTML
	mod.XML=XML
	mod.embed64=embed64
	mod.xmlescape=xmlescape

	# não funcionam quando usados dentro do virtualenv utilizando o gluon do web2py
	# que foi instalado (pip install web2py)
	#mod.ASSIGNJS=ASSIGNJS


# W2PTestCase herda da TestCase
# class W2PTestCase(TestCase):
# 	# Inicia os atributos do W2PTestCase, criando os mocks necessarios para os
# 	# imports automaticos do web2py
# 	def setUp(self,*controllers):
# 		for c in controllers:
# 			# Quando T() for chamado, será retornado o valor que entrar, porque não é necessário
# 			# testar a funcionalidade do T(), pois é uma função do sistema, não do desenvolvedor.
# 			c.T=Mock(side_effect=__T__)
# 			# objeto fake do cache
# 			c.cache=Mock()
# 			# objeto fake do request
# 			c.request=Mock()
# 			# objeto fake do response
# 			c.response=Mock()
# 			# objeto fake do session
# 			c.session=Mock()


# d = dir()
# for i in d:
# 	print 'mod.'+i+'='+i

# # Alguns imports globais do web2py

# # Ja feitos
# from gluon.cache import Cache 
# from gluon.globals import Request 
# from gluon.globals import Response 
# from gluon.globals import Session  
# request = Request() #request = Request({})
# cache = Cache() #cache = Cache(request)
# response = Response() #funciona sem parametro
# session = Session()  #funciona sem parametro
# from gluon.html import * 
# from gluon.http import HTTP 
# from gluon.http import redirect 
# from gluon.sql import DAL 
# from gluon.sql import Field 
# from gluon.sql import SQLDB 
# from gluon.sqlhtml import SQLFORM 
# from gluon.validators import * 

# # Dão erro
# import gluon.languages.translator as T #error
# from gluon.contrib.gql import GQLDB #error