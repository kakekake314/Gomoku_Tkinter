#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys

# 五目並べのプレイヤーの親クラス
# 他のプレイヤーはこのクラスを継承する
class Player:
	def __init__(self,name,isSenkou):
		self.name = name		# 名前
		self.isSenkou=isSenkou	# 先攻かどうか

	# 盤面情報に対する行動（どこに置くか）を返す
	def action(self,data):
		for row in range(len(data)):
			for col in range(len(data)):
				if data[row][col] == 3:
					return col,row

	# 名前を返す
	def getName(self):
		return self.name