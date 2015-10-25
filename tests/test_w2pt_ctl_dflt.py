#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importa a classe de teste W2PTestCase do pacote w2ptests
from w2ptests import W2PTestCase

# Importa o controlador que será testado
import default

# Testes relacionado ao Controlador Default
class TestCtlDefault(W2PTestCase):
	def setUp(self):
		# Chama o metodo do setUp() do W2PTestCase para inicializar os mocks
		# passando apos o self os controllers que serao testados
		W2PTestCase.setUp(self,default)
	def test_cfib(self):
		self.assertEqual(default.cfib()['message'],'55')
	def test_text(self):
		self.assertEqual(default.ctext()['text'],'Text')

# Não necessita do main() do unittest aqui, pois este arquivo será
# chamado pelo run_tests.py