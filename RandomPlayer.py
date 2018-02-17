#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
from Player import Player
import random

# ランダムに行動するプレイヤー
class RandomPlayer(Player):

	# 置ける所にランダムに置く
	def action(self,banmen):
		choice = []
		for row in range(len(banmen)):
			for col in range(len(banmen[row])):
				if self.canPut(banmen,col,row):
					choice.append([col,row])
		return random.choice(choice)

	# 置けるかどうか確認
	def canPut(self,banmen,col,row):
		return banmen[row][col] == 0