#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Para rodar os testes: 
# - no shell entre na pasta: tests/
# - execute: python run_tests.py
# Assim este arquivo de encarregará de rodar os testes na pasta tests/
#

from sys import path as sys_path
from sys import exit as sys_exit
#from os import path as os_path
from unittest import TestLoader, TextTestRunner

#os_path, PROJECT_PATH, ROOT_PATH, entre outros, estão aqui
from common import * 

sys_path_append=sys_path.append
os_path_abspath=os_path.abspath

# FILENAME='tests/db_test.sqlite'
# # Pasta anterior a pasta atual (raiz projeto)
# PROJECT_PATH=os_path.sep.join(os_path_abspath(__file__).split(os_path.sep)[:-2])
# # Pasta atual, onde o run_tests.py está
# ROOT_PATH=os_path.dirname(__file__)
#adiciona no sys.path os diretorios que contém arquivos ou módulos a serem testados
mods=['controllers','modules','models','tests']
for m in mods:
    sys_path_append(os_path_abspath(PROJECT_PATH+'/'+m))

# def delete_file(filepath):
#     try:
#         os_remove(filepath)
#     except:
#         print '\nWARNING: Not found the file: '+filepath+'\n'

# def clearTemp():
#     # Exclui todos os arquivos da base de dados de teste que são temporários
#     delete_file(PROJECT_PATH+'/sql.log')
#     files = glob(PROJECT_PATH+'/*.table')
#     for f in files:
#         delete_file(f)
#     files = glob(PROJECT_PATH+'/'+FILENAME+'*')
#     for f in files:
#         delete_file(f)

# Roda os testes da pasta test/
if __name__=='__main__':
    # Pega todos os arquivos da pasta corrente que sejam .py
    tests=TestLoader().discover(ROOT_PATH,"*.py")
    # Roda os testes
    # verbosity=2 aumenta o nível de detalhe da saida
    result=TextTestRunner(verbosity=2).run(tests) 
    #result = TextTestRunner().run(tests)
    # Limpa o lixo que é criado temporariamente
    clearTemp()    
    # Se houver algum problema nos testes, fecha o programa
    if not result.wasSuccessful():
        sys_exit(1)
