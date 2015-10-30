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
from gluon.sqlhtml import SQLFORM 
from gluon.validators import * 
from gluon.html import * 
from gluon.globals import current


# função fake/mock do T
def m__T__(f):
	return f

# função fake/mock do URL
def m__URL__(foo,**dfoo):
	foo = 'http://'+str(foo)
	for f in dfoo:
		foo=foo+'/'+str(dfoo[f])
	return foo

# função fake/mock do IS_URL
def m__IS_URL__(foo,**dfoo):
	foo = str(foo)
	if foo.startswith('http://') or foo.startswith('https://'):
		return True
	return False


current.request = request = Request()
current.response = response = Response()
current.session = session = Session()
current.cache = cache = Cache(request)
current.T = T = m__T__

deleteDB()

db = DAL('sqlite://'+DB_PATH)




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