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
from os import path as os_path
from os import remove as os_remove
from unittest import TestLoader, TextTestRunner
sys_path_append=sys_path.append
os_path_abspath=os_path.abspath

# # Localizando a pasta onde o Web2py está para colocá-lo no sys.path
# W2P = '/web2py/applications/' # se estiver rodando dentro do Web2py, o caminho deve conter esta string
# JNKS = '/jenkins/jobs/' # se estiver rodando dentro do Jenkins, o caminho deve conter esta string
# PATH = os_path.sep.join(os_path.abspath(__file__).split(os_path.sep))
# if W2P in PATH:
#     W2P_PATH = os_path.sep.join(os_path.abspath(__file__).split(os_path.sep)[:-4])
# elif JNKS in PATH:
#     W2P_PATH = os_path.sep.join(os_path.abspath(__file__).split(os_path.sep)[:-6])
#     W2P_PATH = W2P_PATH+'/web2py'
# else:
#     print 'Problem with the PATH. Please, contact an administrator!'
#     sys_exit(1)
# # Coloca o caminho do Web2py no sys.path, para que as bibliotecas dele possam ser importadas
# sys_path_append(os_path_abspath(W2P_PATH))

# Pasta anterior a pasta atual (raiz projeto)
PROJECT_PATH=os_path.sep.join(os_path_abspath(__file__).split(os_path.sep)[:-2])
# Pasta atual, onde o run_tests.py está
ROOT_PATH=os_path.dirname(__file__)
#adiciona no sys.path os diretorios que contém arquivos ou módulos a serem testados
mods=['controllers','modules']
for m in mods:
    sys_path_append(os_path_abspath(PROJECT_PATH+'/'+m))

# def clear():
#     file_name = '/storage.sqlite'
#     # DB_PATH aponta para o arquivo storage.sqlite dentro da pasta tests/
#     DB_PATH = (os_path.sep.join(os_path.abspath(__file__).split(os_path.sep)[:-1])) + file_name
#     try:
#         os_remove(DB_PATH)
#     except:
#         raise OSError('WARNING: Not found the file: '+DB_PATH)

# def clear():
#     file_name = '/storage.sqlite'
#     try:
#         # DB_PATH aponta para o arquivo storage.sqlite dentro da pasta raiz
#         DB_PATH = PROJECT_PATH + file_name
#         os_remove(DB_PATH)
#     except:
#         try:
#             # DB_PATH aponta para o arquivo storage.sqlite dentro da pasta tests/
#             DB_PATH_TESTS = (os_path.sep.join(os_path.abspath(__file__).split(os_path.sep)[:-1])) + file_name
#             os_remove(DB_PATH_TESTS)
#         except:
#             print 'WARNING: Not found the files: '+DB_PATH+" and "+DB_PATH_TESTS
#             sys_exit(1)

# Roda os testes da pasta test/
if __name__=='__main__':
    # Pega todos os arquivos da pasta corrente que sejam .py
    tests=TestLoader().discover(ROOT_PATH,"*.py")
    # Roda os testes
    # verbosity=2 aumenta o nível de detalhe da saida
    result=TextTestRunner(verbosity=2).run(tests) 
    #result = TextTestRunner().run(tests)
    # Limpa o lixo que é criado temporariamente
    # clear()    
    # Se houver algum problema nos testes, fecha o programa
    if not result.wasSuccessful():
        sys_exit(1)