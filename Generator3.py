# Code written by Jack Clark
# Copyright 2017(c) the G.N.U. General Public License
# This code takes in a webpage and some information, and then it generates a chrome extension that you can add
# your browser very seamlessly
"""
NOTE: This code is the Python 3 script. Check in the repository for the Python 2 scirpt
"""
import os
import sys
import platform
import json

def getExtensionInformation():
	extension_name = input("Extension name:")
	extension_description = input("Extension description:")
	extension_version = input("Extension version:")
	extension_icon = input("Icon:")
	extension_popup = input("Popup:")

	UserExtension = Extension(extension_name, extension_description, extension_verion, extension_icon, extension_popup)

class Extension(extension_name, extension_description, extension_version, extension_icon, extension_popup):
	def __init__(self, extension_name, extension_description, extension_version, extension_popup, extension_icon):
		self.extension_name = extension_name
		self.extension_description = extension_description
		self.extension_version = extension_version
		self.extension_popup = extension_popup
		self.extension_icon = extension_icon

getExtensionInformation()
