#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import Tkinter as tk
import Banmen

class Gomoku:
	def __init__(self):
		self.root = tk.Tk()
		self.root.title(u'五目並べ')
		self.root.geometry("+300+300")#ヨコ＊タテ+X+Y
		# root.resizable(width=False, height=False)
		self.root.option_add('*font', ('FixedSys', 14))

		self.maxBanmen=10


		self.var = tk.StringVar()
		self.var.set('koukou')

		self.teban = tk.BooleanVar()
		self.teban.set(True)#True＝先行＝◯

		self.isStart = tk.BooleanVar()
		self.isStart.set(False)


		self.settingFrame = tk.Frame(self.root)
		# ラジオボタン
		for txt,com in [(u'先行',self.setSenkou), (u'後攻',self.setKoukou)]:
		    tk.Radiobutton(self.settingFrame, text = txt,value=txt,command=com).pack()

		# スタートボタン
		self.startButton = tk.Button(self.settingFrame, text = u'スタート',command = self.start)
		self.startButton.pack()

		self.settingFrame.pack(padx=100)

		self.gomokuFrame = tk.Frame(self.root)
		self.gomokuFrame.pack()



		self.banmen=[]

		for row in range(self.maxBanmen):
			self.banmen.append([])
			for col in range(self.maxBanmen):
				button = tk.Button(self.gomokuFrame,text=u'　')
				button.bind('<Button-1>',self.pushButton)
				button.grid(column=col,row=row)
				self.banmen[row].append(button)


		self.root.mainloop()

	def setSenkou(self):
		self.var.set('senkou')

	def setKoukou(self):
		self.var.set('koukou')

	def start(self):
		self.isStart.set(True)
		print self.var.get()
		self.startButton.configure(state='disabled')


	def pushButton(self,event):
		if self.isStart.get() and event.widget['text'] == u'　':
			if self.teban.get():
				event.widget['text'] = u'◯'
				self.teban.set(False)
			else:
				event.widget['text'] = u'✕'
				self.teban.set(True)


	def banmenReset():
		for row in range(self.maxBanmen):
			for col in range(self.maxBanmen):
				self.banmen[row][col]['text'] = u'　'




