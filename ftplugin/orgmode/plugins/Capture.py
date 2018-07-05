# -*- coding: utf-8 -*-

import vim
import os

from orgmode._vim import echo, echom, echoe, ORGMODE, apply_count, repeat
from orgmode.menu import Submenu, Separator, ActionEntry
from orgmode.keybinding import Keybinding, Plug, Command
from orgmode.py3compat.py_py3_string import *
from datetime import datetime

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
	def create_todo(cls):
		u""" Create a new todo list item for the inbox

		:returns: TODO
		"""
		path = os.path.expanduser("~/.vim/capture/todo.org")
		vim.command(":new "+path)
		pass

	@classmethod
	def create_journal(cls):
		u""" Create a new journal entry

		:returns: TODO
		"""
		path = os.path.expanduser("~/.vim/capture/journal.org")
		vim.command(":new "+path)
		pass

	@classmethod
	def save_todo(cls):
		u""" Save the latest todo capture

		:returns: TODO
		"""
		source_file = os.path.expanduser("~/.vim/capture/todo.org")
		with open(source_file) as source:
		    item = source.read()
		    destination_file = os.path.expanduser("~/.org/inbox.org")

		    with open(destination_file, 'a') as destination:
			destination.write("\n" + item)
		    destination.closed
		source.closed
		os.remove(source_file)
		vim.command(':read!')
		pass

	@classmethod
	def save_journal(cls):
		u""" Save the latest journal capture

		:returns: TODO
		"""
		source_file = os.path.expanduser("~/.vim/capture/journal.org")
		with open(source_file) as source:
		    text = source.read()
		    destination_file = os.path.expanduser("~/.org/journal.org")
		    now = datetime.now()
		    title = text.splitlines()[0][8:]
		    entry = "".join(text.splitlines()[1:])
		    date = now.strftime('* %A, %Y-%m-%d')
		    time = now.strftime('** %H:%M') + title
		    newline = "\n\n"

		    with open(destination_file, 'a') as destination:
			contents = newline.join([date, time, entry])
			destination.write("\n" + contents)
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
		self.commands.append(Command(u'OrgCaptureTodo', u'%s ORGMODE.plugins[u"Capture"].create_todo()' % VIM_PY_CALL))
		self.commands.append(Command(u'OrgCaptureJournal', u'%s ORGMODE.plugins[u"Capture"].create_journal()' % VIM_PY_CALL))
		self.commands.append(Command(u'OrgCaptureSaveTodo', u'%s ORGMODE.plugins[u"Capture"].save_todo()' % VIM_PY_CALL))
		self.commands.append(Command(u'OrgCaptureSaveJournal', u'%s ORGMODE.plugins[u"Capture"].save_journal()' % VIM_PY_CALL))
		self.menu + ActionEntry(u'&Capture', self.commands[-1])
