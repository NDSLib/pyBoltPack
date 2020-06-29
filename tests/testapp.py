print('hello world')
from kivy.app import App
from kivy.uix.button import Button

class A(App):
    def build(self):
        return Button()

if __name__ == '__main__':
    A().run()
