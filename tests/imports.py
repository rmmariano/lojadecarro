#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gluon.cache import Cache 
from gluon.globals import Request, Response, Session

from gluon.http import HTTP, redirect
from gluon.sql import DAL, Field, SQLDB
from gluon.sqlhtml import SQLFORM 

from gluon.validators import * 
from gluon.html import * 

from gluon.tools import Auth, Crud, Mail, Service, PluginManager

# API objects
request = Request()
response = Response()
session = Session()
cache = Cache(request)
#T = translator(request)

db = DAL('sqlite://tests/db_test.sqlite', pool_size=1, check_reserved=['all'])
#auth = Auth(db)
#crud = Crud(db)
mail = Mail()
service = Service()
plugins = PluginManager()