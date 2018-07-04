# -*- coding: utf-8 -*-

import vim
import os

from orgmode._vim import echo, echom, echoe, ORGMODE, apply_count, repeat
from orgmode.menu import Submenu, Separator, ActionEntry
from orgmode.keybinding import Keybinding, Plug, Command

from orgmode.py3compat.py_py3_string import *

# from string import Template

class Capture(object):
	u""" Capture plugin """

	def __init__(self):
		u""" Initialize plugin """
		object.__init__(self)
		# menu entries this plugin should create
		self.menu = ORGMODE.orgmenu + Submenu(u'&Capture')

		# key bindings for this plugin
		# key bindings are also registered through the menu so only additional
		# bindings should be put in this variable
		self.keybindings = []

		# commands for this plugin
		self.commands = []

	@classmethod
	def action(cls):
		u""" Some kind of action

		:returns: TODO
		"""
		kind = 'todo'
		path = os.path.expanduser("~/.vim/capture/"+kind+".org")
		vim.command(":new "+path)
		pass

	@classmethod
	def save(cls):
		u""" Save captures to their respective files

		:returns: TODO
		"""
		captures  = os.path.expanduser("~/.vim/capture")
		for filename in os.listdir(captures):
		    source_file = os.path.expanduser("~/.vim/capture/"+filename)
		    with open(source_file) as source:
			item = source.read()
			kind = 'inbox.org' if filename == 'todo.org' else filename
			destination_file = os.path.expanduser("~/.org/"+kind)

			with open(destination_file, 'a') as destination:
			    destination.write("\n" + item)
			destination.closed
		    source.closed
		    os.remove(source_file)
		vim.command(':read!')
		pass


	def register(self):
		u"""
		Registration of plugin. Key bindings and other initialization should be done.
		"""
		# an Action menu entry which binds "keybinding" to action ":action"
		self.commands.append(Command(u'OrgCapture', u'%s ORGMODE.plugins[u"Capture"].action()' % VIM_PY_CALL, u'1'))
		self.commands.append(Command(u'OrgCaptureSave', u'%s ORGMODE.plugins[u"Capture"].save()' % VIM_PY_CALL))
		self.menu + ActionEntry(u'&Capture', self.commands[-1])
