#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
from Player import Player
import random

class TestPlayer(Player,object):

	def __init__(self,name,isSenkou,banmen):
		super(TestPlayer,self).__init__(name,isSenkou)
		self.banmen = banmen
		self.count = 0

	def action(self):
		self.count += 1
		exist = False
		canputExist = False
		adjacentList = []
		canPutList = []
		canPutList2 = []
		data = self.banmen.getData()
		for row in range(len(data)):
			for col in range(len(data)):
				if data[row][col] == 3:
					canPutList2.append([col,row])
		for row in range(len(data)):
			for col in range(len(data)):
				if data[row][col] == 1:
					exist = True
					adjacentList.append([col,row+1])
					# adjacentList.append([col+1,row])
					adjacentList.append([col,row-1])
					# adjacentList.append([col-1,row])
		if exist:
			for adjacent in adjacentList:
				col,row = adjacent
				if self.canPut(col,row):
					canputExist = True
					canPutList.append([col,row])
			if canputExist:
				colRow = random.choice(canPutList)
				col,row = colRow
				return self.banmen.get1DNum(col,row)
			else:
				col,row = random.choice(canPutList2)
				return self.banmen.get1DNum(col,row)

		else:
			return random.randint(0,48)


	# 置ける所にランダムに置く
	def randomAction(self):
		self.count += 1
		choice = []
		for row in range(len(self.banmen.getData())):
			for col in range(len(self.banmen.getData())):
				if self.canPut(col,row):
					choice.append([col,row])
		c,r = random.choice(choice)
		return self.banmen.get1DNum(c,r)

	# 置けるかどうか
	def canPut(self,col,row):
		if col<0 or row<0 or col>=len(self.banmen.getData()) or row>=len(self.banmen.getData()):
			return False
		else:
			data = self.banmen.getData()
			return data[row][col] == 3

	def getCount(self):
		return self.count
	def setCount(self,count):
		self.count = count

