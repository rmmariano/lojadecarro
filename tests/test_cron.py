#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from importlib import import_module
from os import path as os_path

PROJECT_PATH=os_path.sep.join(os_path.abspath(__file__).split(os_path.sep)[:-2])
filename = 'saida_cron.txt'
path = PROJECT_PATH+'/cron/'+filename

class TestCron(TestCase): 
	def test_caminho_existe(self): 
		mod = import_module("background")
		self.assertEqual(os_path.exists(path),True)

	def test_arquivo_comecacom(self): 
		arquivo = open(path, 'r')
		texto = arquivo.read()
		self.assertEqual(texto.startswith('Comecando em'),True)