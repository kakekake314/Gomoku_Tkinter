#!/usr/bin/env python
# -*- coding: utf8 -*-

class Banmen:
	#盤面初期化
	def __init__(self):
		self.size = 10#盤面の大きさ
		self.alignedColRow = []#揃った座標リスト
		self.data=[]
		for row in range(self.size):
			self.data.append([])
			for col in range(self.size):
				self.data[row].append(0)

	# 碁を置く
	def put(self,col,row,isCircle):
		if isCircle:
			self.data[row][col] = 1
		else:
			self.data[row][col] = 2

	# 左右確認
	def sideJudge(self,col,row):
		judge = False
		count = 0
		colRowList = []
		colRowList.append([col,row])
		judgeData = self.data[row][col]
		for i in range(4):
			if col+i+1 >= self.size:
				break
			if judgeData != self.data[row][col+i+1]:
				break
			count += 1
			colRowList.append([col+i+1,row])

		if count == 4:
			judge = True
			self.alignedColRow = colRowList
			return judge

		colRowList = []
		colRowList.append([col,row])
		count = 0
		for i in range(4):
			if col-i-1 <= -1:
				break
			if judgeData != self.data[row][col-i-1]:
				break
			count += 1
			colRowList.append([col-i-1,row])


		if count == 4:
			self.alignedColRow = colRowList
			judge = True

		return judge

	# 上下確認
	def verticalJudge(self,col,row):
		judge = False
		count = 0
		colRowList = []
		colRowList.append([col,row])
		judgeData = self.data[row][col]
		for i in range(4):
			if row+i+1 >= self.size:
				break
			if judgeData != self.data[row+i+1][col]:
				break
			count += 1
			colRowList.append([col,row+i+1])

		if count == 4:
			judge = True
			self.alignedColRow = colRowList
			return judge

		count = 0
		colRowList = []
		colRowList.append([col,row])
		for i in range(4):
			if row-i-1 <= -1:
				break
			if judgeData != self.data[row-i-1][col]:
				break
			count += 1
			colRowList.append([col,row-i-1])

		if count == 4:
			self.alignedColRow = colRowList
			judge = True

		return judge

	# 右ななめ確認
	def rDiagonalJudge(self,col,row):
		judge = False
		count = 0
		colRowList = []
		colRowList.append([col,row])
		judgeData = self.data[row][col]
		for i in range(4):
			if row+i+1 >= self.size or col+i+1 >= self.size:
				break
			if judgeData != self.data[row+i+1][col+i+1]:
				break
			count += 1
			colRowList.append([col+i+1,row+i+1])

		if count == 4:
			self.alignedColRow = colRowList
			judge = True
			return judge

		count = 0
		colRowList = []
		colRowList.append([col,row])
		for i in range(4):
			if row-i-1 <= -1 or col-i-1 <= -1:
				break
			if judgeData != self.data[row-i-1][col-i-1]:
				break
			count += 1
			colRowList.append([col-i-1,row-i-1])

		if count == 4:
			self.alignedColRow = colRowList
			judge = True

		return judge

	# 左ななめ確認
	def lDiagonalJudge(self,col,row):
		judge = False
		count = 0
		colRowList = []
		colRowList.append([col,row])
		judgeData = self.data[row][col]
		for i in range(4):
			if row-i-1 >= -1 or col+i+1 >= self.size:
				break
			if judgeData != self.data[row-i-1][col+i+1]:
				break
			count += 1
			colRowList.append([col+i-1,row-i-1])

		if count == 4:
			self.alignedColRow = colRowList
			judge = True
			return judge

		count = 0
		colRowList = []
		colRowList.append([col,row])
		for i in range(4):
			if row+i+1 >= self.size or col-i-1 <= -1:
				break
			if judgeData != self.data[row+i+1][col-i-1]:
				break
			count += 1
			colRowList.append([col-i-1,row+i+1])

		if count == 4:
			self.alignedColRow = colRowList
			judge = True

		return judge

	# 揃ってるか確認
	def judge(self):
		judge = False
		judgeData = 0
		for row in range(self.size):
			for col in range(self.size):
				if self.data[row][col] != 0:
					judge = self.sideJudge(col,row) or self.verticalJudge(col,row) or self.rDiagonalJudge(col,row) or self.lDiagonalJudge(col,row)
					if judge:
						judgeData = self.data[row][col]
		return judgeData # 勝敗なし0,先行（丸）勝ち:1,後攻（バツ）勝ち:2

	def getAlignedColRow(self):
		return self.alignedColRow

	# すべて埋まっている
	def isAllFilled(self):
		for row in range(self.size):
			for col in range(self.size):
				if self.data[row][col] == 0:
					return False
		return True

	# 盤面表示
	def printData(self):
		for row in range(self.size):
			for col in range(self.size):
				print self.data[row][col],
			print ' '
		print' '

	# 盤面出力
	def getData(self):
		return self.data

	def reset(self):
		for row in range(self.size):
			for col in range(self.size):
				self.data[row][col] = 0
		self.alignedColRow = []

