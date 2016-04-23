from subprocess import Popen, PIPE
from glob import glob
from random import randint
from os.path import join, dirname
from kivy.app import App
from kivy.logger import Logger
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

class Picture(Scatter):
    source = StringProperty(None)

class PicturesApp(App):

    # the root is created in pictures.kv
    def build(root):
        root = root.root

        try:
            # load the image
            graph = Image(source='rplot.jpg', size_hint=(10, .4), pos_hint={'x':-4.15, 'y':.50})
	    table = Image(source='table.png', size_hint=(10, .4), pos_hint={'x':-4.17, 'y':.05})
	    image_material = Image(source='image_material.png', size_hint=(10, .4), pos_hint={'x':-4.419, 'y':.05})
            
            # add to the main field
            root.add_widget(graph)
            root.add_widget(table)
            root.add_widget(image_material)
        except Exception as e:
            Logger.exception('Pictures: Unable to load ')

        #labels
        main_label = Label(text = "Hello Engineer", size_hint=(1, .55),pos_hint={'x':0, 'y':.70})
        weight_label = Label(text = "Please specify the weight of the tube in Newtons", size_hint=(1, .55),pos_hint={'x':-.25, 'y':.60})
        angle1_label = Label(text = "Please specify the angle of tensor 1", size_hint=(1, .55),pos_hint={'x':-.25, 'y':.45})
        angle2_label = Label(text = "Please specify the angle of tensor 2", size_hint=(1, .55),pos_hint={'x':-.25, 'y':.30})
        material_label = Label(text = "Please specify the material of the tensioners", size_hint=(1, .55),pos_hint={'x':-.25, 'y':.15})
        pass_fail_label = Label(text = "PASS", size_hint=(1, .55),pos_hint={'x':-25, 'y':-1})
        
        #text inputs
        weight = TextInput(text='', multiline=False,password=False, size_hint=(.4, .10),pos_hint={'x':.05, 'y':.75})
        angle1 = TextInput(text='', multiline=False,password=False, size_hint=(.4, .10),pos_hint={'x':.05, 'y':.60})
        angle2 = TextInput(text='', multiline=False,password=False, size_hint=(.4, .10),pos_hint={'x':.05, 'y':.45})
        material = TextInput(text='', multiline=False,password=False, size_hint=(.4, .10),pos_hint={'x':.05, 'y':.30})


        #buttons
        go_button = Button(text = "CALCULATE", size_hint=(.3, .1),pos_hint={'x':.05, 'y':.2})

        
        
        # Gather the values from the ext box and pass them to the matrix
        # calculation, after that the value of the forces return
       

        def calculate_break_point(forces,material):

            materials = [1000,2000,3000,4000]

            print materials[int(material)]
            print abs(float(forces[0]))
            try:
                for force in forces:
                    if abs(float(forces[0])) > materials[int(material)]:
                        print "BREAKS"
                    else:
                        print "PASS"
            except Exception as e:
                Logger.exception('Material does not exist')


        def callback(instance):

            forces = []

            print('The button is being pressed')
            if {weight.text and angle1.text and angle2.text and material.text}:
            
               # execute the process 
                process = Popen(["./main",weight.text,angle1.text,angle2.text,material.text], stdout=PIPE)
                (output, err) = process.communicate()
                exit_code = process.wait()
        
                print(output)

                for line in output.splitlines():
                    if "Force" in line:
                        forces.append(line.split(":")[1].strip())
                
                print forces
                calculate_break_point(forces,material.text)
                # reload the image
                graph.reload()

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
