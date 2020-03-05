import kivy 
from kivy.app import App
from kivy.uix.label import label
from kivy.uix.gridlayout import gridlayout
from kiy.uix.textinput import TextInput

kivy.require("1.10.1")

class ConnectPage(Gridlayout):
	def __init__(self, **kwargs):
		super().__init__(self, **kwargs)

class EpicApp(App):
	def build(self):
		return ConnectPage()


if __name__ == "__Main__":
	EpicApp().run()