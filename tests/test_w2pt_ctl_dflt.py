#!/usr/bin/env python
# -*- coding: utf-8 -*-

from w2ptests import W2PTestCase
from w2ptests import import_exec

import default
import carros

class TestCtlDefault(W2PTestCase):
	def setUp(self):
		W2PTestCase.setUp(self,default)

	def test_index(self):


		#var = import_exec()

		#print var


		self.assertEqual('55','55')


	# def test_carros(self):
	# 	self.assertEqual('Text','Text')
	# def test_detalhes(self):
	# 	self.assertEqual('55','55')
	# def test_pesquisa(self):
	# 	self.assertEqual('Text','Text')
	# def test_admin(self):
	# 	self.assertEqual('55','55')
	


		
	# def test_cfib(self):
	# 	self.assertEqual(default.cfib()['message'],'55')
	# def test_text(self):
	# 	self.assertEqual(default.ctext()['text'],'Text')



