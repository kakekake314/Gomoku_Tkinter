#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import Tkinter


root = Tkinter.Tk()
root.title(u"Software Title")
root.geometry("660x480+100+100")#ヨコ＊タテ+X+Y
root.minsize(660,480)
root.option_add('*font', ('FixedSys', 14))

#ラベル
Label1 = Tkinter.Label(text=u'五目並べ')
Label1.pack()

var = Tkinter.StringVar()
var.set('koukou')

def setSenkou():
	var.set('senkou')

def setKoukou():
	var.set('koukou')

def getTurnNumber():
	print var.get()

# ラジオボタンの設定
for txt,com,x,y in [(u'先行',setSenkou,220,30), (u'後攻',setKoukou,280,30)]:
    Tkinter.Radiobutton(root, text = txt,value=txt,command=com).place(x=x,y=y)

# ボタン
startButton = Tkinter.Button(root, text = 'スタート',command = getTurnNumber)
startButton.place(x=350,y=28)

root.mainloop()