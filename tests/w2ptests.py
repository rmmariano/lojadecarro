#!/usr/bin/env python
# -*- coding: utf-8 -*-

# importa o TestCase, para a criacao do W2PTestCase
from unittest import TestCase

# importa o Mock, para a criação dos objetos falsos.
from mock import Mock

# importa os imports automáticos do web2py
from global_imports import *

class W2PTestCase(TestCase):	
	def setUp(self,*controllers):
		#initVars()
		for c in controllers:
			c.db=None

			c.T=Mock(side_effect=m__T__)
			c.URL=Mock(side_effect=m__URL__)
			c.IS_URL=Mock(side_effect=m__IS_URL__)

			c.crud=crud

			c.request=Request() # = web2py 2.1.1
			#c.request=Request({}) # > web2py 2.1.1
			c.cache=Cache(request)
			c.response=Response()
			c.session=Session()

			# c.request=request
			# c.cache=cache
			# c.response=response
			# c.session=session

			c.redirect=redirect

			import_classes(c)
			import_gluon_validators(c)
			import_gluon_html(c)

	def inside(self,a,b):
		if str(a) in str(b):
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
	mod.SQLTABLE=SQLTABLE

def import_gluon_validators(mod):
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
