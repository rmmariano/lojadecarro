#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common import *

from os import path
from os import remove
from glob import glob

# Imports automáticos
from gluon.cache import Cache 
from gluon.globals import Request, Response, Session
from gluon.http import HTTP, redirect
from gluon.sql import DAL, Field, SQLDB
from gluon.sqlhtml import SQLFORM,SQLTABLE
from gluon.validators import * 
from gluon.html import * 
from gluon.globals import current


# função fake/mock do T
def m__T__(f):
	return f

# função fake/mock do URL
def m__URL__(a='', c='', f='', r='', args='', vars='', 
	anchor='', extension='', env='', hmac_key='', hash_vars='', 
	salt='', user_signature='', scheme='', host='', port='', 
	encode_embedded_slash='', url_encode='', language=''):
	
	lfoo=[a,c,f,r,args,vars,anchor,extension,env,hmac_key,hash_vars,
		salt,user_signature,scheme,host,port,encode_embedded_slash,url_encode,language]

	foo = 'http://'
	for f in lfoo:
		if f != '':
			foo=foo+str(f)+'/'

	return foo


# def IS_URL(error_message='Enter a valid URL', mode='http', allowed_schemes=None, 
# 	prepend_scheme='http', allowed_tlds=None):
# 	pass

# função fake/mock do IS_URL
def m__IS_URL__(foo,**dfoo):
	foo = str(foo)
	if foo.startswith('http://') or foo.startswith('https://'):
		return True
	return False


current.request = request = None
current.response = response = None
current.session = session = None
current.cache = cache = None
current.T = T = None

def initVars():
	global current, request, response, session, cache, T
	current.request = request = Request()
	current.response = response = Response()
	current.session = session = Session()
	current.cache = cache = Cache(request)
	current.T = T = m__T__

initVars()

deleteDB()

db = DAL('sqlite://'+DB_PATH)




import gluon.tools as gt
from mock import Mock

gt.URL=Mock(side_effect=m__URL__)

crud = gt.Crud(db)


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