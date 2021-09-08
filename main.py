import pydbus
import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class ButtonApp(App):
    def build(self):
        layout = BoxLayout(padding=100)
        btn = Button(text="Click me",
                     background_color=[1,1,1,1])
        layout.add_widget(btn)
        return layout

    def on_press_button(self):
        print("Hello")

if __name__ == '__main__':
    app = ButtonApp()
    app.run()