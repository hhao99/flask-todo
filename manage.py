#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from flask.ext.script import Manager, Server
from microblog import app

manager = Manager(app)
manager.add_command('runserver',Server(use_debugger = True,
	use_reloader=True, host= '0.0.0.0'))

if __name__ == '__main__':
	manager.run()
