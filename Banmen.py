#!/usr/bin/env python
# -*- coding: utf8 -*-

import numpy as np

class Banmen:
	#盤面初期化
	def __init__(self):
		self.size = 7			#盤面の大きさ
		self.winNum = 5			#何個並べたら勝ちか
		self.alignedColRow = []	#揃った座標リスト
		self.alignedNum = -1	#揃った数字(勝者)
		self.data=[]			#盤面を二次元配列で保持
		self.missed = False		#置けない所に置こうとしたかどうか
		self.done = False		#終了判定
		# すべて3にする
		for row in range(self.size):
			self.data.append([])
			for col in range(self.size):
				self.data[row].append(3)

	# 碁を置く（１：◯ , ２：✕）
	def put2D(self,col,row,isCircle):
		if self.data[row][col] != 3:
			self.missed = True
			self.done = True
			#間違えてない方を勝者とする
			if isCircle:
				self.alignedNum = 2
			else:
				self.alignedNum = 1
		if isCircle:
			self.data[row][col] = 1
		else:
			self.data[row][col] = 2

	#一次元パターン
	def put(self,num,isCircle):
		oneDData = self.convertTo1D()
		if oneDData[num] != 3:
			self.missed = True
			self.done = True
			if isCircle:
				self.alignedNum = 2
			else:
				self.alignedNum = 1
		else:
			if isCircle:
				oneDData[num] = 1
			else:
				oneDData[num] = 2
			self.convertTo2D(oneDData)


	# 左右確認
	def sideJudge(self,col,row):
		judge = False				# 揃っているかどうか
		count = 1					# 揃っている個数
		colRowList = []				# 揃っている盤面情報を格納する
		colRowList.append([col,row])
		judgeData = self.data[row][col]

		# 右方向に確認
		for i in range(self.winNum - 1):
			if col+i+1 >= self.size:
				break
			if judgeData != self.data[row][col+i+1]:
				break

			# 同じだった場合
			count += 1
			colRowList.append([col+i+1,row])

		# ５個揃っていたら
		if count == self.winNum:
			judge = True
			self.alignedColRow = colRowList
			return judge

		# 左方向に確認
		colRowList = []
		colRowList.append([col,row])
		count = 1
		for i in range(self.winNum - 1):
			if col-i-1 <= -1:
				break
			if judgeData != self.data[row][col-i-1]:
				break
			count += 1
			colRowList.append([col-i-1,row])


		if count == self.winNum:
			self.alignedColRow = colRowList
			judge = True

		return judge

	# 上下確認
	def verticalJudge(self,col,row):
		judge = False
		count = 1
		colRowList = []
		colRowList.append([col,row])
		judgeData = self.data[row][col]
		for i in range(self.winNum - 1):
			if row+i+1 >= self.size:
				break
			if judgeData != self.data[row+i+1][col]:
				break
			count += 1
			colRowList.append([col,row+i+1])

		if count == self.winNum:
			judge = True
			self.alignedColRow = colRowList
			return judge

		count = 1
		colRowList = []
		colRowList.append([col,row])
		for i in range(self.winNum - 1):
			if row-i-1 <= -1:
				break
			if judgeData != self.data[row-i-1][col]:
				break
			count += 1
			colRowList.append([col,row-i-1])

		if count == self.winNum:
			self.alignedColRow = colRowList
			judge = True

		return judge

	# 右ななめ確認
	def rDiagonalJudge(self,col,row):
		judge = False
		count = 1
		colRowList = []
		colRowList.append([col,row])
		judgeData = self.data[row][col]
		for i in range(self.winNum - 1):
			if row+i+1 >= self.size or col+i+1 >= self.size:
				break
			if judgeData != self.data[row+i+1][col+i+1]:
				break
			count += 1
			colRowList.append([col+i+1,row+i+1])

		if count == self.winNum:
			self.alignedColRow = colRowList
			judge = True
			return judge

		count = 1
		colRowList = []
		colRowList.append([col,row])
		for i in range(self.winNum - 1):
			if row-i-1 <= -1 or col-i-1 <= -1:
				break
			if judgeData != self.data[row-i-1][col-i-1]:
				break
			count += 1
			colRowList.append([col-i-1,row-i-1])

		if count == self.winNum:
			self.alignedColRow = colRowList
			judge = True

		return judge

	# 左ななめ確認
	def lDiagonalJudge(self,col,row):
		judge = False
		count = 1
		colRowList = []
		colRowList.append([col,row])
		judgeData = self.data[row][col]
		for i in range(self.winNum - 1):
			if row-i-1 >= -1 or col+i+1 >= self.size:
				break
			if judgeData != self.data[row-i-1][col+i+1]:
				break
			count += 1
			colRowList.append([col+i-1,row-i-1])

		if count == self.winNum:
			self.alignedColRow = colRowList
			judge = True
			return judge

		count = 1
		colRowList = []
		colRowList.append([col,row])
		for i in range(self.winNum - 1):
			if row+i+1 >= self.size or col-i-1 <= -1:
				break
			if judgeData != self.data[row+i+1][col-i-1]:
				break
			count += 1
			colRowList.append([col-i-1,row+i+1])

		if count == self.winNum:
			self.alignedColRow = colRowList
			judge = True

		return judge

	# 揃ってるか確認
	def judge(self):
		judge = False
		judgeData = 0
		for row in range(self.size):
			for col in range(self.size):
				if self.data[row][col] != 3:
					judge = self.sideJudge(col,row) or self.verticalJudge(col,row) or self.rDiagonalJudge(col,row) or self.lDiagonalJudge(col,row)
					if judge:
						judgeData = self.data[row][col]
		return judgeData # 勝敗なし0,先行（丸）勝ち:1,後攻（バツ）勝ち:2

	# すべて埋まっているか確認
	def isAllFilled(self):
		for row in range(self.size):
			for col in range(self.size):
				if self.data[row][col] == 3:
					return False
		return True

	# 終了判定
	def isFinished(self):
		alignedNum = self.judge()
		if self.getMissed():
			self.alignedNum = -1
			self.done = True
			return True
		elif alignedNum == 1 or alignedNum == 2 or self.isAllFilled():
			self.alignedNum = alignedNum
			self.done = True
			return True
		else:
			return False

	# 盤面表示
	def printData(self):
		for row in range(self.size):
			for col in range(self.size):
				if int(self.data[row][col]) == 3:
					print '-',
				elif int(self.data[row][col]) == 1:
					print '◯',
				elif int(self.data[row][col]) == 2:
					print '✕',
			print ' '
		print' '

	# 盤面情報を一次元にして返す（学習用）
	def convertTo1D(self):
		oneDData = []
		for row in range(self.size):
			for col in range(self.size):
				oneDData.append(self.data[row][col])
		return np.array(oneDData,dtype=np.float32)

	# 一次元のデータを二次元のデータにセットし直す
	def convertTo2D(self,data):
		col = 0
		row = 0
		for d in data:
			self.data[row][col] = d
			col += 1
			if col == self.size:
				col = 0
				row += 1

	# 二次元の座標が一次元で何番目のデータになるか返す
	def get1DNum(self,col,row):
		count = 0
		for r in range(self.size):
			for c in range(self.size):
				if c == col and r == row:
					return count
				count += 1


	# 盤面を初期化する
	def reset(self):
		for row in range(self.size):
			for col in range(self.size):
				self.data[row][col] = 3
		self.alignedColRow = []
		self.missed = False
		self.done = False


	# １と２を入れ替える（学習用）
	def change(self):
		for row in range(self.size):
			for col in range(self.size):
				if self.data[row][col] == 1:
					self.data[row][col] = 2
				elif self.data[row][col] == 2:
					self.data[row][col] = 1

	# 揃った番号を返す
	def getAlignedNumber(self):
		return self.alignedNum

	# 揃った座標リストを返す
	def getAlignedColRow(self):
		return self.alignedColRow

	# 盤面情報を返す
	def getData(self):
		return self.data

	# 失敗してるかを返す
	def getMissed(self):
		return self.missed

	# 二次元データをセットする
	def setData(self,data):
		self.data = [d[:] for d in data]