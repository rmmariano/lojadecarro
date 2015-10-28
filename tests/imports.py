#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports automáticos

from os import path
from os import remove
from glob import glob
#from sys import exit

# Pasta anterior a pasta atual (raiz projeto)
PROJECT_PATH=path.sep.join(path.abspath(__file__).split(path.sep)[:-2])

def delete_file(filepath):
    try:
        remove(filepath)
    except:
    	print '\nWARNING: Not found the file: '+filepath+'\n'


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

filename='tests/db_test.sqlite'

# Exclui todos os arquivos da base de dados de teste que são temporários
delete_file(PROJECT_PATH+'/sql.log')
files = glob(PROJECT_PATH+'/*.table')
for f in files:
	delete_file(f)
files = glob(PROJECT_PATH+'/'+filename+'*')
for f in files:
	delete_file(f)

db = DAL('sqlite://'+filename)