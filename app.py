import kivy 
from kivy.app import App
from kivy.uix.label import label
from kivy.uix.gridlayout import gridlayout
from kiy.uix.textinput import TextInput
from kivy.uix.button import Button
kivy.require("1.10.1")

class ConnectPage(Gridlayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.cols = 2 

		self.add_widget(Label9(text = "IP:"))

		self.ip = TextInput(multiline = False)
		self.add_widget(self.ip)


		self.add_widget(Label9(text = "Usernmae:"))

		self.ip = TextInput(multiline = False)
		self.add_widget(self.Usernmae)




		self.add_widget(Label9(text = "Port:"))

		self.ip = TextInput(multiline = False)
		self.add_widget(self.Port)

		self.add_widget(Label())
		self.join = Button(text = "Join")
		self.add_widget(self.join)



class EpicApp(App):
	def build(self):
		return ConnectPage()


if __name__ == "__Main__":
	EpicApp().run()