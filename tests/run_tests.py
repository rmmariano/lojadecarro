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
from unittest import TestLoader, TextTestRunner

#os_path, PROJECT_PATH, ROOT_PATH, entre outros, estão aqui
from common import * 

sys_path_append=sys_path.append
os_path_abspath=os_path.abspath

#adiciona no sys.path os diretorios que contém arquivos ou módulos a serem testados
mods=['controllers','modules','models','tests']
for m in mods:
    sys_path_append(os_path_abspath(PROJECT_PATH+'/'+m))

# Roda os testes da pasta test/
if __name__=='__main__':
    # Pega todos os arquivos da pasta corrente que sejam .py
    tests=TestLoader().discover(ROOT_PATH,"*.py")
    # Roda os testes
    # verbosity=2 aumenta o nível de detalhe da saida
    result=TextTestRunner(verbosity=2).run(tests) 
    #result = TextTestRunner().run(tests)
    # Exclui o lixo que é criado temporariamente
    #deleteDB()    
    # Se houver algum problema nos testes, fecha o programa
    if not result.wasSuccessful():
        sys_exit(1)