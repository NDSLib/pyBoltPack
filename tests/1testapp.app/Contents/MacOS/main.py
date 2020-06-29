#!/usr/local/bin/python3
print('hello kivy')

#from easygui import *
#name = enterbox("Input your name", default="Guido")
#msgbox("Hello, " + name)
#if ynbox("あなたは18歳以上ですか？"):
#    age = integerbox("何歳ですか？", lowerbound=18, upperbound=10000)
#filename = fileopenbox("ファイルを開く")
from kivy.app import App
from kivy.uix.button import Button

class A(App):
    def build(self):
        return Button(text='test app')


A().run()
