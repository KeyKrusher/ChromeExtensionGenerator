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

_Extension = {
  "manifest_version": 2,

  "name": "Place Extension Name Here",
  "description": "Place description here.",
  "version": "Place version here",

  "browser_action": {
    "default_icon": "icon.png",
    "default_popup": "popup.html"
  },
  "permissions": [
    "activeTab",
    "https://ajax.googleapis.com/"
  ]
}
{
  "browser_action": {
    "default_icon": "icon.png",
    "default_popup": "popup.html",
    "default_title": "Click here!"
  },
}
def getExtensionInformation():
	extension_name = input("Extension name:")
	extension_description = input("Extension description:")
	extension_version = input("Extension version:")
	extension_icon = input("Icon:")
	extension_popup = input("Popup:")

	UserExtension = Extension(extension_name, extension_description, extension_version, extension_icon, extension_popup)

class Extension(extension_name, extension_description, extension_version, extension_icon, extension_popup):
	Extension_ = {
  		"manifest_version": 2,
  		"name": _name,
  		"description": _description,
  		"version": _version,
  	"browser_action": {
    	"default_icon": _icon,
    	"default_popup": _popup
  	},
  	"permissions": [
    	"activeTab",
    	"https://ajax.googleapis.com/"
  	]
	}
	{
  	"browser_action": {
    	"default_icon": "icon.png",
    	"default_popup": "popup.html",
    	"default_title": "Click here!"
  	},
	}
	def generate(extension_to_make):
		# Dump the JSON
		json.dumps(extension_to_make)
	def __init__(self, extension_name, extension_description, extension_version, extension_popup, extension_icon):
		self._name = extension_name
		self._description = extension_description
		self._version = extension_version
		self._popup = extension_popup
		self._icon = extension_icon
#    _extension_name = json.loads('{"name": "Place Extension Name Here"')
#    _extension_description = json.loads('{"description": "Place description here."}')
#    _extension_version = json.loads('{"version": "Place version here"}')
#    _extension_icon = json.loads('{"": ""}')
#    _extension_popup = json.loads('{"": ""}')
    

getExtensionInformation()
