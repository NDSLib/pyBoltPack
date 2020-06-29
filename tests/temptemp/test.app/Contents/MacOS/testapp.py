print('hello world')
from kivy.app import App
from kivy.uix.button import Button

class A(App):
    def build(self):
        return Button()

A().run()
