from glob import glob
from random import randint
from os.path import join, dirname
from kivy.app import App
from kivy.logger import Logger
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty
from kivy.uix.label import Label
import os
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class Picture(Scatter):
    source = StringProperty(None)

class PicturesApp(App):


    # the root is created in pictures.kv
    def build(root):
        root = root.root

        try:
            # load the image
            picture = Picture(source="rplot.jpg",pos_hint={'x':.50, 'y':.20})
            # add to the main field
            root.add_widget(picture)
        except Exception as e:
            Logger.exception('Pictures: Unable to load <%s>' % filename)

        #labels
        main_label = Label(text = "Hello Engineer", size_hint=(1, .55),pos_hint={'x':0, 'y':.70})
        weight_label = Label(text = "Please specify the weight of the tube in Newtons", size_hint=(1, .55),pos_hint={'x':-.25, 'y':.60})
        angle1_label = Label(text = "Please specify the angle of tensor 1", size_hint=(1, .55),pos_hint={'x':-.25, 'y':.45})
        angle2_label = Label(text = "Please specify the angle of tensor 2", size_hint=(1, .55),pos_hint={'x':-.25, 'y':.30})
        material_label = Label(text = "Please specify the material of the tensioners", size_hint=(1, .55),pos_hint={'x':-.25, 'y':.15})
        pass_fail_label = Label(text = "PASS", size_hint=(1, .55),pos_hint={'x':0.3, 'y':.1})
        
        #text inputs
        weight = TextInput(text='', multiline=False,password=False, size_hint=(.4, .10),pos_hint={'x':.05, 'y':.75})
        angle1 = TextInput(text='', multiline=False,password=False, size_hint=(.4, .10),pos_hint={'x':.05, 'y':.60})
        angle2 = TextInput(text='', multiline=False,password=False, size_hint=(.4, .10),pos_hint={'x':.05, 'y':.45})
        material = TextInput(text='', multiline=False,password=False, size_hint=(.4, .10),pos_hint={'x':.05, 'y':.30})


        #buttons
        go_button = Button(text = "CALCULATE", size_hint=(.3, .1),pos_hint={'x':.05, 'y':.2})

        def callback(instance):
            print('The button is being pressed')
            if {weight.text and angle1.text and angle2.text and material.text}:
                
                cmd = "./main " + weight.text \
                        + " " + angle1.text \
                        + " " + angle2.text \
                        + " " + material.text

                print(cmd)
            
                # load the image
                os.system(cmd)

        go_button.bind(on_press=callback)

        #add to frame
        root.add_widget(main_label)
        root.add_widget(weight)
        root.add_widget(angle1)
        root.add_widget(angle2)
        root.add_widget(material)
        root.add_widget(weight_label)
        root.add_widget(angle1_label)
        root.add_widget(angle2_label)
        root.add_widget(material_label)
        root.add_widget(pass_fail_label)
        root.add_widget(go_button)

    def on_pause(root):
        return True


        """
        """

if __name__ == '__main__':
    PicturesApp().run()
