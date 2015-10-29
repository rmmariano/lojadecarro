#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common import *

# Imports automáticos

from os import path
from os import remove
from glob import glob

from gluon.cache import Cache 
from gluon.globals import Request, Response, Session
from gluon.http import HTTP, redirect
from gluon.sql import DAL, Field, SQLDB
from gluon.sqlhtml import SQLFORM 
from gluon.validators import * 
from gluon.html import * 

request = Request()
response = Response()
session = Session()
cache = Cache(request)

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