#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path as os_path
from os import remove as os_remove
from glob import glob

# Pasta anterior a pasta atual (raiz projeto)
PROJECT_PATH=os_path.sep.join(os_path.abspath(__file__).split(os_path.sep)[:-2])
# Pasta atual, onde o run_tests.py está
ROOT_PATH=os_path.dirname(__file__)
# Nome do banco de teste
DB_NAME='db_test.sqlite'
# Path do banco de testes (sem contar a raiz)
DB_PATH='tests/'+DB_NAME
#DB_PATH=ROOT_PATH+'/'+DB_NAME

def deleteFile(filepath):
    try:
        os_remove(filepath)
    except:
    	print '\nWARNING: Not found the file: '+filepath+'\n'

def deleteDB():
    # Exclui todos os arquivos da base de dados de teste que são temporários
    deleteFile(PROJECT_PATH+'/sql.log')
    files = glob(PROJECT_PATH+'/*.table')
    for f in files:
        deleteFile(f)
    files = glob(PROJECT_PATH+'/'+DB_PATH+'*')
    for f in files:
        deleteFile(f)




# raise HTTP(404, "Object not found")