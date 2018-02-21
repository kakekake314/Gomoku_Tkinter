#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
from Player import Player
import random

class AlphaRandomPlayer(Player):

	# 置ける所にランダムに置く
	# 相手が３つ以上並べたら防ぐand自分が４つ並んでたら勝てる場所に置く
	def action(self,banmen):
		alignedNum = self.judge(banmen)
		if alignedNum == 1 or alignedNum == 2:
			for BandA in self.BandAList:
				col,row  = BandA
				if self.canPut(banmen,col,row):
					return col,row

		choice = []
		for row in range(len(banmen)):
			for col in range(len(banmen[row])):
				if self.canPut(banmen,col,row):
					choice.append([col,row])
		return random.choice(choice)

	# 置けるかどうか
	def canPut(self,banmen,col,row):
		if col<0 or row<0 or col>=len(banmen) or row>=len(banmen):
			return False
		else:
			return banmen[row][col] == 3

	# 左右確認
	def sideJudge(self,data,col,row):
		judge = False
		count = 0
		colRowList = []
		colRowList.append([col,row])
		judgeData = data[row][col]
		for i in range(2):
			if col+i+1 >= len(data):
				break
			if judgeData != data[row][col+i+1]:
				break
			count += 1
			colRowList.append([col+i+1,row])

		if count == 2:
			judge = True
			self.alignedColRow = colRowList
			self.BandAList.append([col-1,row])
			self.BandAList.append([col+3,row])
			return judge

		colRowList = []
		colRowList.append([col,row])
		count = 0
		for i in range(2):
			if col-i-1 <= -1:
				break
			if judgeData != data[row][col-i-1]:
				break
			count += 1
			colRowList.append([col-i-1,row])


		if count == 2:
			self.alignedColRow = colRowList
			self.BandAList.append([col-3,row])
			self.BandAList.append([col+1,row])
			judge = True

		return judge

	# 上下確認
	def verticalJudge(self,data,col,row):
		judge = False
		count = 0
		colRowList = []
		colRowList.append([col,row])
		judgeData = data[row][col]
		for i in range(2):
			if row+i+1 >= len(data):
				break
			if judgeData != data[row+i+1][col]:
				break
			count += 1
			colRowList.append([col,row+i+1])

		if count == 2:
			judge = True
			self.alignedColRow = colRowList
			self.BandAList.append([col,row-1])
			self.BandAList.append([col,row+3])
			return judge

		count = 0
		colRowList = []
		colRowList.append([col,row])
		for i in range(2):
			if row-i-1 <= -1:
				break
			if judgeData != data[row-i-1][col]:
				break
			count += 1
			colRowList.append([col,row-i-1])

		if count == 2:
			self.alignedColRow = colRowList
			self.BandAList.append([col,row+1])
			self.BandAList.append([col,row-3])
			judge = True

		return judge

	# 右ななめ確認
	def rDiagonalJudge(self,data,col,row):
		judge = False
		count = 0
		colRowList = []
		colRowList.append([col,row])
		judgeData = data[row][col]
		for i in range(2):
			if row+i+1 >= len(data) or col+i+1 >= len(data):
				break
			if judgeData != data[row+i+1][col+i+1]:
				break
			count += 1
			colRowList.append([col+i+1,row+i+1])

		if count == 2:
			self.alignedColRow = colRowList
			self.BandAList.append([col-1,row-1])
			self.BandAList.append([col+3,row+3])
			judge = True
			return judge

		count = 0
		colRowList = []
		colRowList.append([col,row])
		for i in range(2):
			if row-i-1 <= -1 or col-i-1 <= -1:
				break
			if judgeData != data[row-i-1][col-i-1]:
				break
			count += 1
			colRowList.append([col-i-1,row-i-1])

		if count == 2:
			self.alignedColRow = colRowList
			self.BandAList.append([col-3,row-3])
			self.BandAList.append([col+1,row+1])
			judge = True

		return judge

	# 左ななめ確認
	def lDiagonalJudge(self,data,col,row):
		judge = False
		count = 0
		colRowList = []
		colRowList.append([col,row])
		judgeData = data[row][col]
		for i in range(2):
			if row-i-1 >= -1 or col+i+1 >= len(data):
				break
			if judgeData != data[row-i-1][col+i+1]:
				break
			count += 1
			colRowList.append([col+i-1,row-i-1])

		if count == 2:
			self.alignedColRow = colRowList
			self.BandAList.append([col-1,row+3])
			self.BandAList.append([col-1,row+3])
			judge = True
			return judge

		count = 0
		colRowList = []
		colRowList.append([col,row])
		for i in range(2):
			if row+i+1 >= len(data) or col-i-1 <= -1:
				break
			if judgeData != data[row+i+1][col-i-1]:
				break
			count += 1
			colRowList.append([col-i-1,row+i+1])

		if count == 2:
			self.alignedColRow = colRowList
			self.BandAList.append([col-3,row+3])
			self.BandAList.append([col+1,row-1])
			judge = True

		return judge

	# 揃ってるか確認
	def judge(self,data):
		judge = False
		judgeData = 0
		self.BandAList = []
		for row in range(len(data)):
			for col in range(len(data)):
				if data[row][col] != 3:
					judge = self.sideJudge(data,col,row) or self.verticalJudge(data,col,row) or self.rDiagonalJudge(data,col,row) or self.lDiagonalJudge(data,col,row)
					if judge:
						judgeData = data[row][col]
		return judgeData # 勝敗なし0,先行（丸）勝ち:1,後攻（バツ）勝ち:2

