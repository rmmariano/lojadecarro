#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path as os_path
from os import remove as os_remove
from glob import glob

# Pasta anterior a pasta atual (raiz projeto)
PROJECT_PATH=os_path.sep.join(os_path.abspath(__file__).split(os_path.sep)[:-2])
# Pasta atual, onde o run_tests.py está
ROOT_PATH=os_path.dirname(__file__)
# Pasta onde está o banco de dados de teste
FILENAME='tests/db_test.sqlite'

def delete_file(filepath):
    try:
        os_remove(filepath)
    except:
    	print '\nWARNING: Not found the file: '+filepath+'\n'

def clearTemp():
    # Exclui todos os arquivos da base de dados de teste que são temporários
    delete_file(PROJECT_PATH+'/sql.log')
    files = glob(PROJECT_PATH+'/*.table')
    for f in files:
        delete_file(f)
    files = glob(PROJECT_PATH+'/'+FILENAME+'*')
    for f in files:
        delete_file(f)