#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys

class Player:
	def __init__(self,name,isSenkou):
		self.name = name
		self.isSenkou=isSenkou

	def action(self,data):
		for row in range(len(data)):
			for col in range(len(data)):
				if data[row][col] == 0:
					return col,row

	def getName(self):
		return self.name