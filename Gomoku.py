#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import Tkinter as tk
from tkinter import ttk
from Battle import Battle
from time import sleep

class Gomoku:
	def roop(self):
		self.root = tk.Tk()
		self.setButton()
		self.root.mainloop()

	def setButton(self):
		self.root.title(u'五目並べ')
		self.root.geometry("+300+300")#ヨコ＊タテ+X+Y
		self.root.resizable(width=False, height=False)
		self.root.option_add('*font', ('FixedSys', 14))

		# コンボボックスのデフォルトの値
		self.senkouName = tk.StringVar()
		self.senkouName.set(u'人間')
		self.koukouName = tk.StringVar()
		self.koukouName.set(u'人間')

		# スタートボタンが押されたかどうか
		self.isStart = tk.BooleanVar()
		self.isStart.set(False)

		# プレイヤーの設定をするフレーム
		self.settingFrame = tk.Frame(self.root)
		self.senkouFrame = tk.Frame(self.settingFrame)
		self.senkouFrame.pack()
		self.koukouFrame = tk.Frame(self.settingFrame)
		self.koukouFrame.pack()

		# 盤面が表示されるフレーム（プレイヤーに人間がいる場合のみ）
		self.battleFrame = tk.Frame(self.root)

		# 先攻の設定
		self.senkouLabel = tk.Label(self.senkouFrame,text = u'先攻：◯')
		self.senkouLabel.pack(side=tk.LEFT)
		self.comboboxS = ttk.Combobox(self.senkouFrame,textvariable = self.senkouName)
		self.comboboxS.bind('<<ComboboxSelected>>',self.comboboxSelected)
		self.comboboxS['values'] = (u'人間',u'ランダム君',u'強いランダム君','DQN')
		self.comboboxS.pack()

		# 後攻の設定
		self.koukouLabel = tk.Label(self.koukouFrame,text = u'後攻：✕')
		self.koukouLabel.pack(side=tk.LEFT)
		self.comboboxK = ttk.Combobox(self.koukouFrame,textvariable = self.koukouName)
		self.comboboxK.bind('<<ComboboxSelected>>',self.comboboxSelected)
		self.comboboxK['values'] = (u'人間',u'ランダム君',u'強いランダム君','DQN')
		self.comboboxK.pack()

		# スタートボタン
		self.startButton = tk.Button(self.settingFrame, text = u'スタート',command = self.start)
		self.startButton.pack()

		# リスタートボタン
		self.restartButton = tk.Button(self.settingFrame, text = u'リスタート',command = self.restart,state='disabled')
		self.restartButton.pack()

		# フレームの設置
		self.settingFrame.pack(padx=100)
		self.battleFrame.pack()
		self.gomokuFrame = tk.Frame(self.root)
		self.gomokuFrame.pack()

	# コンボボックスが選択された時のイベント
	def comboboxSelected(self,event):
		print self.senkouName.get() +" vs "+ self.koukouName.get()

	# スタートボタンが押されたときのイベント
	def start(self):
		self.battle = Battle(self.battleFrame)
		self.isStart.set(True)
		# スタートボタン，コンボボックスを押せなくする
		self.startButton.configure(state='disabled')
		self.comboboxS.configure(state='disabled')
		self.comboboxK.configure(state='disabled')
		# リスタートボタンを押せるようにする
		self.restartButton.configure(state='normal')
		# 対戦スタート
		self.battle.setPlayer(self.senkouName.get(),self.koukouName.get())
		self.battle.progress()

	# リスタートボタンが押されたときのイベント
	def restart(self):
		self.battle.reset()
		self.battle.progress()




gomoku = Gomoku()
gomoku.roop()
