from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.uix.textinput import TextInput



class Hello(FloatLayout):
    def __init__(self,**kwargs):
        super(Hello,self).__init__(**kwargs)

        
        self.main_label = Label(text = "Default_text", size_hint=(1, .55),pos_hint={'x':0, 'y':.35})
	self.text = TextInput(password=False, size_hint=(.4, .10),pos_hint={'x':.3, 'y':.30})
    #Main Buttons
        self.back_button = Button(text = "GO", size_hint=(.3, .1),pos_hint={'x':.65, 'y':.2})
        self.go_button = Button(text = "BACK", size_hint=(.3, .1),pos_hint={'x':.05, 'y':.2})
	self.add_widget(self.text)
        self.add_widget(self.back_button)
        self.add_widget(self.main_label)
        self.add_widget(self.go_button)


        self.current_text = "Default"

    def update(self,event):
        self.main_label.text = "Changed to change"

class app1(App):
    def build(self):
        return Hello()
if __name__=="__main__":
     app1().run()
