#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
from Banmen import Banmen
from Player import Player
from RandomPlayer import RandomPlayer
from AlphaRandomPlayer import AlphaRandomPlayer
import Tkinter as tk

class Battle:
	def __init__(self,root):
		self.banmen = Banmen()
		self.isSenkouTurn = True
		self.banmenData = self.banmen.getData()
		self.isCreate = False
		self.isSenkouHuman = False
		self.isKoukouHuman = False
		self.root = root
		self.winner = -1

	def setPlayer(self,senkouName,koukouName):
		if senkouName == u'人間':
			self.isSenkouHuman = True
		elif senkouName == u'ランダム君':
			self.senkouP = RandomPlayer(u'ランダム君',True)
		elif senkouName == 'com':
			# self.senkouP = ComputerPlayer('com',True)
			self.senkouP = AlphaRandomPlayer('com',True)

		if koukouName == u'人間':
			self.isKoukouHuman = True
		elif koukouName == u'ランダム君':
			self.koukouP = RandomPlayer(u'ランダム君',False)
		elif koukouName == 'com':
			# self.koukouName = ComputerPlayer('com',True)
			self.koukouP = AlphaRandomPlayer('com',False)


	def progress(self):
		if self.isSenkouHuman or self.isKoukouHuman:
			self.createButton(len(self.banmenData))
			if not self.isSenkouHuman:#先攻がコンピュータの時
				col,row = self.senkouP.action(self.banmenData)
				self.banmen.put(col,row,True)
				self.banmenUpdate(self.banmen.getData())
				self.isSenkouTurn = False
		else:#コンピュータ同士(終わるまで戦う)
			while not self.isFinished():
				if self.isSenkouTurn:
					col,row = self.senkouP.action(self.banmenData)
					self.banmen.put(col,row,True)
					self.isSenkouTurn = False
				else:
					col,row = self.koukouP.action(self.banmenData)
					self.banmen.put(col,row,False)
					self.isSenkouTurn = True
				self.banmen.printData()
				self.banmenData = self.banmen.getData()


	def isFinished(self):
		isFinished = False
		if self.isSenkouWon():
			isFinished = True
			self.winner = 1
		elif self.isKoukouWon():
			isFinished = True
			self.winner = 2
		elif self.isDraw():
			isFinished = True
			self.winner = 0
		else:
			isFinished = False

		if isFinished:
			self.buttonColoring(self.banmen.getAlignedColRow(),'red')
		return isFinished

	def getWinner(self):
		return self.winner


	def createButton(self,size):
		self.buttons=[]
		for row in range(size):
			self.buttons.append([])
			for col in range(size):
				button = tk.Button(self.root,text=u'　',command=self.callback(col,row))
				button.grid(column=col,row=row)
				self.buttons[row].append(button)

	def callback(self,col,row):
		def x():
			if self.buttons[row][col]['text'] == u'　' and not self.isFinished():
				if self.isSenkouTurn:
					self.buttons[row][col]['text'] = u'◯'
					self.banmen.put(col,row,self.isSenkouTurn)
					self.banmenData = self.banmen.getData()
					self.isSenkouTurn = False
					if not self.isFinished():
						if self.isSenkouHuman and not self.isKoukouHuman:
							col2,row2 = self.koukouP.action(self.banmenData)
							self.banmen.put(col2,row2,False)
							self.isSenkouTurn = True
						self.banmenUpdate(self.banmen.getData())
						self.isFinished()
				else:
					self.buttons[row][col]['text'] = u'✕'
					self.banmen.put(col,row,self.isSenkouTurn)
					self.banmenData = self.banmen.getData()
					self.isSenkouTurn = True
					if not self.isFinished():
						if self.isKoukouHuman and not self.isSenkouHuman:
							col2,row2 = self.senkouP.action(self.banmenData)
							self.banmen.put(col2,row2,True)
							self.isSenkouTurn = False
						self.banmenUpdate(self.banmen.getData())
						self.isFinished()
		return x



	def banmenUpdate(self,data):
		for row in range(len(data)):
			for col in range(len(data)):
				self.buttons[row][col]['text'] = self.circleOrCrossMark(data[row][col])

	def circleOrCrossMark(self,number):
		if number == 1:
			return u'◯'
		elif number == 2:
			return u'✕'
		else:
			return u'　'

	def buttonColoring(self,alignedColRow,color):
		if self.isSenkouHuman or self.isKoukouHuman:
			for colRow in alignedColRow:
				col,row = colRow
				self.buttons[row][col]['highlightbackground'] = color

	def isSenkouWon(self):
		return self.banmen.judge() == 1

	def isKoukouWon(self):
		return self.banmen.judge() == 2

	def isDraw(self):
		return self.banmen.isAllFilled()


	def banmenReset(self):
		self.banmen.reset()

