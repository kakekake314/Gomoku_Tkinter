#!/usr/bin/env python
# -*- coding: utf8 -*-

class Banmen:
	#盤面初期化
	def __init__(self):
		self.size = 10#盤面の大きさ
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

	# 置けるかどうか
	def canPut(self,col,row):
		return self.data[row][col] == 0

	# 左右確認
	def sideJudge(self,col,row):
		judge = False
		count = 0
		judgeData = self.data[row][col]
		for i in range(4):
			if col+i+1 >= self.size:
				break
			if judgeData != self.data[row][col+i+1]:
				break
			count += 1

		if count == 4:
			judge = True

		count = 0
		for i in range(4):
			if col-i-1 >= -1:
				break
			if judgeData != self.data[row][col-i-1]:
				break
			count += 1

		if count == 4:
			judge = True

		return judge

	# 上下確認
	def verticalJudge(self,col,row):
		judge = False
		count = 0
		judgeData = self.data[row][col]
		for i in range(4):
			if row+i+1 >= self.size:
				break
			if judgeData != self.data[row+i+1][col]:
				break
			count += 1

		if count == 4:
			judge = True

		count = 0
		for i in range(4):
			if row-i-1 >= -1:
				break
			if judgeData != self.data[row-i-1][col]:
				break
			count += 1

		if count == 4:
			judge = True

		return judge

	# ななめ確認
	def diagonalJudge(self,col,row):
		judge = False
		count = 0
		judgeData = self.data[row][col]
		for i in range(4):
			if row+i+1 >= self.size or col+i+1 >= self.size:
				break
			if judgeData != self.data[row+i+1][col+i+1]:
				break
			count += 1

		if count == 4:
			judge = True

		count = 0
		for i in range(4):
			if row-i-1 >= -1 or col-i-1 >= -1:
				break
			if judgeData != self.data[row-i-1][col-i-1]:
				break
			count += 1

		if count == 4:
			judge = True

		return judge

	# 揃ってるか確認
	def judge(self):
		judge = False
		judgeData = 0
		for row in range(self.size):
			for col in range(self.size):
				if self.data[row][col] != 0:
					judge = self.sideJudge(col,row) or self.verticalJudge(col,row) or self.diagonalJudge(col,row)
					if judge:
						judgeData = self.data[row][col]
		return judgeData # 勝敗なし0,先行（丸）勝ち:1,後攻（バツ）勝ち:2

	# 盤面出力
	def printData(self):
		for row in range(self.size):
			for col in range(self.size):
				print self.data[row][col],
			print ''
		print''

