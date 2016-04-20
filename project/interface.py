from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout



class Hello(FloatLayout):
    def __init__(self,**kwargs):
        super(Hello,self).__init__(**kwargs)

        
        self.main_label = Label(text = "Hello Engineer", size_hint=(1, .55),pos_hint={'x':0, 'y':.70})
        self.weight_label = Label(text = "Please specify the weight of the tube in Newtons", size_hint=(1, .55),pos_hint={'x':-.25, 'y':.60})
        self.angle1_label = Label(text = "Please specify the angle of tensor 1", size_hint=(1, .55),pos_hint={'x':-.25, 'y':.45})
        self.angle2_label = Label(text = "Please specify the angle of tensor 2", size_hint=(1, .55),pos_hint={'x':-.25, 'y':.30})
        self.material_label = Label(text = "Please specify the material of the tensioners", size_hint=(1, .55),pos_hint={'x':-.25, 'y':.15})
        self.pass_fail_label = Label(text = "PASS", size_hint=(1, .55),pos_hint={'x':0.3, 'y':.1})
	self.weight = TextInput(password=False, size_hint=(.4, .10),pos_hint={'x':.05, 'y':.75})
	self.angle1 = TextInput(password=False, size_hint=(.4, .10),pos_hint={'x':.05, 'y':.60})
	self.angle2 = TextInput(password=False, size_hint=(.4, .10),pos_hint={'x':.05, 'y':.45})
	self.material = TextInput(password=False, size_hint=(.4, .10),pos_hint={'x':.05, 'y':.30})
    #Main Buttons
        self.go_button = Button(text = "CALCULATE", size_hint=(.3, .1),pos_hint={'x':.05, 'y':.2})
	self.add_widget(self.weight)
	self.add_widget(self.angle1)
	self.add_widget(self.angle2)
	self.add_widget(self.material)
        self.add_widget(self.main_label)
        self.add_widget(self.weight_label)
        self.add_widget(self.angle1_label)
        self.add_widget(self.angle2_label)
        self.add_widget(self.material_label)
        self.add_widget(self.pass_fail_label)
        self.add_widget(self.go_button)

        self.current_text = "Default"



    def update(self,event):
        self.main_label.text = "Changed to change"

class FinalProject(App):
    def build(self):
        return Hello()
if __name__=="__main__":
     FinalProject().run()
