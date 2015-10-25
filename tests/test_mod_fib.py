#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase

# Importa o módulo que será testado
import fib

# Testes relacionado ao Módulo Fib
class TestModFib(TestCase):
	def test0(self):
		self.assertEqual(fib.fib(1), 1)
	def test1(self):
		self.assertEqual(fib.fib(2), 1)
	def test10(self):
		self.assertEqual(fib.fib(10), 55)
	# def test0_erro(self):
	# 	self.assertEqual(fib.fib(10), 90)

# Não necessita do main() do unittest aqui, pois este arquivo será
# chamado pelo run_tests.py