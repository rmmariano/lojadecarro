#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports automáticos

from os import path
from os import remove
from glob import glob
#from sys import exit

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

# Pasta anterior a pasta atual (raiz projeto)
PROJECT_PATH=path.sep.join(path.abspath(__file__).split(path.sep)[:-2])

FILENAME='tests/db_test.sqlite'

def delete_file(filepath):
    try:
        remove(filepath)
    except:
    	print '\nWARNING: Not found the file: '+filepath+'\n'

# # Exclui todos os arquivos da base de dados de teste que são temporários
delete_file(PROJECT_PATH+'/sql.log')
files = glob(PROJECT_PATH+'/*.table')
for f in files:
	delete_file(f)
files = glob(PROJECT_PATH+'/'+FILENAME+'*')
for f in files:
	delete_file(f)


db = DAL('sqlite://'+FILENAME)