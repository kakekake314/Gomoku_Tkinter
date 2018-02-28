#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import Tkinter as tk
from tkinter import ttk
from Battle import Battle
from time import sleep
import tkinter.filedialog as tkfd
import DQN
import os

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

		# リスタートボタンとプレイヤー変更ボタンが置かれるフレーム
		self.restartFrame = tk.Frame(self.settingFrame)
		self.restartFrame.pack()

		# プレイヤー変更ボタン
		self.changePlayerButton = tk.Button(self.restartFrame, text = u'プレイヤー変更',command = self.changePlayer,state = 'disabled')
		self.changePlayerButton.pack(side=tk.LEFT)

		# リスタートボタン
		self.restartButton = tk.Button(self.restartFrame, text = u'リスタート',command = self.restart,state='disabled')
		self.restartButton.pack()

		# 学習ボタン
		self.learningButton = tk.Button(self.settingFrame, text = u'学習' ,command = self.learning)
		self.learningButton.pack()

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
		# リスタートボタンとプレイヤー変更ボタンを押せるようにする
		self.restartButton.configure(state='normal')
		self.changePlayerButton.configure(state='normal')
		# 対戦スタート
		self.battle.setPlayer(self.senkouName.get(),self.koukouName.get())
		self.battle.progress()

	# リスタートボタンが押されたときのイベント
	def restart(self):
		self.battle.reset()
		self.battle.progress()

	# プレイヤー変更ボタンが押されたときのイベント
	def changePlayer(self):
		self.startButton.configure(state='normal')
		self.comboboxS.configure(state='normal')
		self.comboboxK.configure(state='normal')
		self.restartButton.configure(state='disabled')
		self.changePlayerButton.configure(state='disabled')
		self.battle.reset()

	# 学習を行うボタン
	def learning(self):
		self.learningButton.configure(state='disabled')
		self.dqn = DQN.DQNPlayer("learning",True)
		self.learningWindow = tk.Toplevel()
		self.loadFileFrame = tk.Frame(self.learningWindow)
		self.loadFileFrame.pack()
		self.outputFileFrame = tk.Frame(self.learningWindow)
		self.outputFileFrame.pack()
		self.episodeFrame = tk.Frame(self.learningWindow)
		self.episodeFrame.pack()
		self.loadFileLabel = tk.Label(self.loadFileFrame,text = u'読み込みファイル名：')
		self.loadFileLabel.pack(side=tk.LEFT)
		self.loadFileLabel2 = tk.Label(self.loadFileFrame,text = self.dqn.getLoadFile())
		self.loadFileLabel2.pack(side=tk.LEFT)
		self.selectButton = tk.Button(self.loadFileFrame,text = u'選択',command = self.fileSelection)
		self.selectButton.pack()
		self.outputFileLabel = tk.Label(self.outputFileFrame,text = u'出力ファイル名：')
		self.outputFileLabel.pack(side=tk.LEFT)
		self.editBox = tk.Entry(self.outputFileFrame)
		self.editBox.insert(tk.END,self.dqn.getOutputFile())
		self.editBox.pack()
		self.episodeLabel = tk.Label(self.episodeFrame,text = u'エピソード数')
		self.episodeLabel.pack(side=tk.LEFT)
		self.episodeNumber = tk.StringVar()
		self.episodeNumber.set('10000')
		self.combobox = ttk.Combobox(self.episodeFrame,textvariable = self.episodeNumber)
		self.combobox['values'] = ('10000','20000')
		self.combobox.pack()
		self.learningStartButton = tk.Button(self.learningWindow,text = u'学習スタート',command = self.learningStart)
		self.learningStartButton.pack()


	def fileSelection(self):
		self.iDir = os.path.abspath(os.path.dirname(__file__))
		self.iDir += "/result"
		self.filename = tkfd.askdirectory(initialdir=self.iDir)
		self.loadFileLabel2['text'] = self.filename

	def learningStart(self):
		self.dqn.setLoadFile(self.loadFileLabel2['text'])
		self.dqn.setOutputFile(self.editBox.get())
		print "エピソード数"+self.episodeNumber.get()
		self.root.destroy()
		self.dqn.learning(int(self.episodeNumber.get()))


gomoku = Gomoku()
gomoku.roop()
