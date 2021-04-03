import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

class rootWindow(GridLayout):
    content = ObjectProperty(None)
    show = ObjectProperty(None)
    
    def fun_pressed(self):
        self.show.text = str(int(self.content.text)+1)
        

class ExampleApp(App):
    def build(self):
        return rootWindow()

if __name__ == "__main__":
    ExampleApp().run()
