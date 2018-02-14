#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
from Banmen import Banmen

class Battle:
	def __init__(self,senkouP,koukouP):
		self.senkouP = senkouP
		self.koukouP = koukouP
		self.isSenkouTurn = True
		self.banmen = Banmen()

	def progress(self):
		self.banmen.getData()
		if self.isSenkouTurn:
			self.senkouP.action(self.banmen)
			self.isSenkouTurn = False
		else:
			self.koukouP.action(self.banmen)
			self.isSenkouTurn = True


	def isFinished(self):
		isFinished = False
		if self.isSenkouWon():
			isFinished = True
		elif self.isKoukouWon():
			isFinished = True
		elif self.isDraw():
			isFinished = True
		else:
			isFinished = False
		return isFinished

	def isSenkouWon(self):
		return self.banmen.judge() == 1

	def isKoukouWon(self):
		return self.banmen.judge() == 2

	def isDraw(self):
		return self.banmen.isAllFilled()