#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys

class Player:
	def __init__(self,name,isSenkou):
		self.name = name
		self.isSenkou=isSenkou

	def action(self,data):
		col = 0
		row = 0
		return col,row