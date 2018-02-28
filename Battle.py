#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
from Banmen import Banmen
from Player import Player
from RandomPlayer import RandomPlayer
from AlphaRandomPlayer import AlphaRandomPlayer
from MonteCalroPlayer import MonteCalroPlayer
import DQN
import Tkinter as tk

# ２人のプレイヤーが対戦を行う
class Battle:
	def __init__(self,root):
		self.banmen = Banmen()					#共通の盤面
		self.isSenkouTurn = True				#先攻かどうか
		self.banmenData = self.banmen.getData()	#盤面情報
		self.winner = -1						#勝者（-1:なし,0:引き分け,1:先攻,2:後攻）
		# プレイヤーに人間が選択された場合にボタンを表示する
		self.isSenkouHuman = False
		self.isKoukouHuman = False
		self.isCreate = False					#ボタンが生成されたかどうか
		self.root = root						#ボタンを表示するフレーム

	# 対戦するプレイヤーをセットする
	def setPlayer(self,senkouName,koukouName):
		if senkouName == u'人間':
			self.isSenkouHuman = True
		elif senkouName == u'ランダム君':
			self.senkouP = RandomPlayer(senkouName,True)
		elif senkouName == u'強いランダム君':
			self.senkouP = AlphaRandomPlayer(senkouName,True)
		# elif senkouName == u'モンテカルロ君':
		# 	self.senkouP = MonteCalroPlayer(senkouName,True)
		elif senkouName == 'DQN':
			self.senkouP = DQN.DQNPlayer(senkouName,True)

		if koukouName == u'人間':
			self.isKoukouHuman = True
		elif koukouName == u'ランダム君':
			self.koukouP = RandomPlayer(koukouName,False)
		elif koukouName == u'強いランダム君':
			self.koukouP = AlphaRandomPlayer(koukouName,False)
		# elif koukouName == u'モンテカルロ君':
		# 	self.koukouP = MonteCalroPlayer(koukouName,False)
		elif koukouName == 'DQN':
			self.koukouP = DQN.DQNPlayer(koukouName,False)

	# 対戦を進める
	def progress(self):
		# 人間がプレイする場合はボタン押下で行う
		if self.isSenkouHuman or self.isKoukouHuman:
			self.createButton(len(self.banmenData))
			if not self.isSenkouHuman:#先攻がコンピュータの時は先に打っておく
				col,row = self.senkouP.action(self.banmenData)
				self.banmen.put2D(col,row,True)
				self.banmenUpdate(self.banmen.getData())
				self.isSenkouTurn = False
		else:#コンピュータ同士の場合，終わるまで戦う（ボタンは表示されない）
			count = 0
			senkouWin = 0
			koukouWin = 0
			draw = 0
			miss = 0
			# 100試合行う
			while count < 100:
				self.banmen.reset()
				while not self.isFinished():
					if self.isSenkouTurn:
						col,row = self.senkouP.action(self.banmenData)
						self.banmen.put2D(col,row,True)
						self.isSenkouTurn = False
					else:
						col,row = self.koukouP.action(self.banmenData)
						self.banmen.put2D(col,row,False)
						self.isSenkouTurn = True
					self.banmenData = self.banmen.getData()
				if self.winner == 1:
					senkouWin += 1
				elif self.winner == 2:
					koukouWin += 1
				elif self.winner == -1:
					miss += 1
				else:
					draw += 1
				count += 1
			print "先攻:"+str(senkouWin)+",後攻:"+str(koukouWin)+",引き分け:"+str(draw)+",置きミス:"+str(miss)

	# 決着が付いたかどうか
	def isFinished(self):
		if self.banmen.isFinished():
			self.winner = self.banmen.getAlignedNumber()
			if self.isSenkouHuman or self.isKoukouHuman:
				if self.winner == 1 or self.winner == 2:
					# 揃ったボタンの背景を赤くする
					self.buttonColoring(self.banmen.getAlignedColRow(),'red')
				if self.winner == 1:
					print "先攻の勝ち"
				elif self.winner == 2:
					print "後攻の勝ち"
				elif self.winner == -1:
					print "置きミス"
				else:
					print "引き分け"
			return True
		else:
			return False

	# 勝者を返す
	def getWinner(self):
		return self.winner

	# ボタンを生成する
	def createButton(self,size):
		self.buttons=[]
		for row in range(size):
			self.buttons.append([])
			for col in range(size):
				button = tk.Button(self.root,text=u'　',command=self.callback(col,row))
				button.grid(column=col,row=row)
				self.buttons[row].append(button)

	# 押されたボタンの座標に応じた行動
	def callback(self,col,row):
		def x():
			# どちらも置いていない場所　かつ　決着が付いていない
			if self.buttons[row][col]['text'] == u'　' and not self.isFinished():
				# 先攻の場合'◯'を表示し，碁を置く
				if self.isSenkouTurn:
					self.buttons[row][col]['text'] = u'◯'
					self.banmen.put2D(col,row,self.isSenkouTurn)
					self.banmenData = self.banmen.getData()
					self.isSenkouTurn = False
					# 決着が付いていなければコンピュータの手を打つ
					if not self.isFinished():
						if self.isSenkouHuman and not self.isKoukouHuman:
							col2,row2 = self.koukouP.action(self.banmenData)
							self.banmen.put2D(col2,row2,False)
							self.isSenkouTurn = True
						self.banmenUpdate(self.banmen.getData())
						self.isFinished()
				else:
					self.buttons[row][col]['text'] = u'✕'
					self.banmen.put2D(col,row,self.isSenkouTurn)
					self.banmenData = self.banmen.getData()
					self.isSenkouTurn = True
					if not self.isFinished():
						if self.isKoukouHuman and not self.isSenkouHuman:
							col2,row2 = self.senkouP.action(self.banmenData)
							self.banmen.put2D(col2,row2,True)
							self.isSenkouTurn = False
						self.banmenUpdate(self.banmen.getData())
						self.isFinished()
		return x

	# ボタンのテキストの更新
	def banmenUpdate(self,data):
		for row in range(len(data)):
			for col in range(len(data)):
				self.buttons[row][col]['text'] = self.circleOrCrossMark(data[row][col])

	# 数字に応じたテキストを返す
	def circleOrCrossMark(self,number):
		if number == 1:
			return u'◯'
		elif number == 2:
			return u'✕'
		else:
			return u'　'

	# ボタンの背景色を変更する
	def buttonColoring(self,alignedColRow,color):
		for colRow in alignedColRow:
			col,row = colRow
			self.buttons[row][col]['highlightbackground'] = color

	# 初期化（プレイヤー情報は保持）
	def reset(self):
		if self.winner != -1 and (self.isSenkouHuman or self.isKoukouHuman):
			self.buttonColoring(self.banmen.getAlignedColRow(),'white')
		self.banmen.reset()
		self.banmenData = self.banmen.getData()
		self.isSenkouTurn = True
		self.winner = -1
		if self.isSenkouHuman or self.isKoukouHuman:
			for row in range(len(self.banmenData)):
				for col in range(len(self.banmenData)):
					self.buttons[row][col]['text'] = u'　'

