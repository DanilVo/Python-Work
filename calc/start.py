from cProfile import label
from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'height', '500')
Config.set('graphics', 'width', '400')


#To import and start work with application
from kivy.app import App 
#Button module
from kivy.uix.button import Button
#Module to create an IDE
from kivy.uix.codeinput import CodeInput
#Module to see colors of code (https://pygments.org/docs/lexers/)
from pygments.lexers import CythonLexer
#Let us desize widgets
from kivy.uix.scatter import Scatter
#One of options on setting windgets on screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
#module to input text
from kivy.uix.textinput import TextInput
#module for empty widget
from kivy.uix.widget import Widget

from kivy.uix.label import Label


#set a class to start 
# class BoxApp(App):

#     #function to apply our visual buttond and etc
#     def build(self):
#         #Simulator of fingers
#         s = Scatter()
#         #We should return element to see it in this case it is the IDE
#         # return CodeInput(lexer=CythonLexer())
#         fl = FloatLayout(size = (300,300))
#         s.add_widget(fl)

#         #Set button, giving it text, on_press will do command, bg_color(mixed with grey font), bg_normal(set only inputed color)
#         fl.add_widget(Button(text = 'hello world!',
#                         font_size = 30,
#                         on_press = self.btn_press,
#                         background_color = 'red',
#                         background_normal = "",
#                         size_hint = (.5,.25),
#                         pos = (480/2 - 120,640/2-160)))
#         return s
#     #in order to get callback we need to set (instance)
#     def btn_press(self,instance):
#         instance.text = "clicked!"
        
# #If app started through teminal (name == main) else through side file or app (name == "name module") 
# if __name__ == "__main__":
#     BoxApp().run()


# class _BoxLayout(App):
#     def build(self):
#         #Padding to make space between border and windget [top/bottom,left/right]
#         #Spacing - space between objects
#         bl = BoxLayout(orientation = "horizontal", padding = [50,25], spacing = 3)
#         bl.add_widget(Button(text = "1"))
#         bl.add_widget(Button(text = "2"))
#         bl.add_widget(Button(text = "3"))

#         return bl

# if __name__ == "__main__":
#     _BoxLayout().run()

# class _GridLayout(App):
#     def build(self):
#         #Padding to make space between border and windget [top/bottom,left/right]
#         #Spacing - space between objects
#         bl = GridLayout(rows = 10,cols = 10, padding  = [30], spacing = 3)
#         for x in range(99):
#             bl.add_widget(Button(text = "1"))

#         return bl

# if __name__ == "__main__":
#     _GridLayout().run()

# class _AnchorLayout(App):
#     def build(self):
#         #Padding to make space between border and windget [top/bottom,left/right]
#         #Spacing - space between objects
#         al = AnchorLayout(anchor_x = 'right',anchor_y = 'bottom')
#         #size_hint - let us change size of buttom!!!!
#         al.add_widget(Button(text = 'hello world', size_hint = [.5,.5]))

#         return al

# if __name__ == "__main__":
#     _AnchorLayout().run()

# class _TextInput(App):
#     def build(self):
#         al = AnchorLayout()
#         #size_hint has priority on size, so in order to make it unchangable we need to set 
#         #size_hint both parametrs (None)
#         bl = BoxLayout(orientation = 'vertical',size_hint = [None,None], size = [300,300])

#         bl.add_widget(TextInput())
#         bl.add_widget(TextInput())
#         bl.add_widget(Button(text = 'enter'))

#         al.add_widget(bl)
#         return al

# if __name__ == "__main__":
#     _TextInput().run()

class Calculator(App):
    def build(self):
        bl = BoxLayout(orientation = 'vertical', padding = [25])
        gl = GridLayout(cols = 4, spacing = 5, size_hint = (1,.6))
    
        al = AnchorLayout(anchor_x = "right",valign="center", anchor_y = "center", size_hint = (1,.4), text_size=(400 - 50, 500*.4-50))
        al.add_widget(Label(text='0', font_size = 40, halign ="right"))
        bl.add_widget(al)

        gl.add_widget(Button(text = '7'))
        gl.add_widget(Button(text = '8'))
        gl.add_widget(Button(text = '9'))
        gl.add_widget(Button(text = 'X'))

        gl.add_widget(Button(text = '4'))
        gl.add_widget(Button(text = '5'))
        gl.add_widget(Button(text = '6'))
        gl.add_widget(Button(text = '-'))

        gl.add_widget(Button(text = '3'))
        gl.add_widget(Button(text = '2'))
        gl.add_widget(Button(text = '1'))
        gl.add_widget(Button(text = '+'))

        gl.add_widget(Widget())
        gl.add_widget(Button(text = '0'))
        gl.add_widget(Button(text = '.'))
        gl.add_widget(Button(text = '='))

        bl.add_widget(gl)
        return bl

if __name__ == "__main__":
    Calculator().run()