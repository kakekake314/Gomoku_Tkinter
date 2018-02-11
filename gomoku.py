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
Static1 = Tkinter.Label(text=u'五目並べ')
Static1.pack()

root.mainloop()