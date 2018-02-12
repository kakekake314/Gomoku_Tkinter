#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import Tkinter as tk


root = tk.Tk()
root.title(u'五目並べ')
root.geometry("+300+300")#ヨコ＊タテ+X+Y
# root.resizable(width=False, height=False)
root.option_add('*font', ('FixedSys', 14))

var = tk.StringVar()
var.set('koukou')

isSenkou = tk.BooleanVar()
isSenkou.set(True)

isStart = tk.BooleanVar()
isStart.set(False)

def setSenkou():
	var.set('senkou')

def setKoukou():
	var.set('koukou')

def start():
	isStart.set(True)
	print var.get()
	startButton.configure(state='disabled')


def pushButton(event):
	if isStart.get():
		if isSenkou.get():
			event.widget['text'] = '◯'
			isSenkou.set(False)
		else:
			event.widget['text'] = '✕'
			isSenkou.set(True)


settingFrame = tk.Frame(root)
# ラジオボタン
for txt,com in [(u'先行',setSenkou), (u'後攻',setKoukou)]:
    tk.Radiobutton(settingFrame, text = txt,value=txt,command=com).pack()

# スタートボタン
startButton = tk.Button(settingFrame, text = u'スタート',command = start)
startButton.pack()

settingFrame.pack(padx=100)

gomokuFrame = tk.Frame(root)
gomokuFrame.pack()



banmen=[[],[],[],[],[]]

for col in range(5):
	for row in range(5):
		button = tk.Button(gomokuFrame,text='　')
		button.bind('<Button-1>',pushButton)
		button.grid(column=col,row=row)
		banmen[col].append(button)

for aaa in range(5):
	for bbb in range(5):
		print banmen[aaa][bbb]['text']


root.mainloop()