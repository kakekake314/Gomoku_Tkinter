#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import Tkinter


root = Tkinter.Tk()
root.title(u'五目並べ')
root.geometry("300x480+100+100")#ヨコ＊タテ+X+Y
root.minsize(300,480)
root.option_add('*font', ('FixedSys', 14))

var = Tkinter.StringVar()
var.set('koukou')

def setSenkou():
	var.set('senkou')

def setKoukou():
	var.set('koukou')

def getTurnNumber():
	print var.get()
	startButton.configure(state='disabled')
	gomokuFrame.pack(fill=Tkinter.BOTH)

settingFrame = Tkinter.Frame(root)
# ラジオボタン
for txt,com in [(u'先行',setSenkou), (u'後攻',setKoukou)]:
    Tkinter.Radiobutton(settingFrame, text = txt,value=txt,command=com).pack()

# スタートボタン
startButton = Tkinter.Button(settingFrame, text = u'スタート',command = getTurnNumber)
startButton.pack()

settingFrame.pack()
gomokuFrame = Tkinter.Frame(root)

button = Tkinter.Button(gomokuFrame, text = '00').grid(column=0,row=0)
button = Tkinter.Button(gomokuFrame, text = '00').grid(column=1,row=0)
button = Tkinter.Button(gomokuFrame, text = '00').grid(column=2,row=0)
button = Tkinter.Button(gomokuFrame, text = '00').grid(column=3,row=0)
button = Tkinter.Button(gomokuFrame, text = '00').grid(column=4,row=0)

root.mainloop()