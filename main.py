import pydbus
import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

bus = pydbus.SystemBus()

adapter = bus.get('org.bluez', '/org/bluez/hci0')
mngr = bus.get('org.bluez', '/')

class ButtonApp(App):
    def build(self):
        layout = BoxLayout(padding=100)
        btn = Button(text="Click me",
                     background_color=[1,1,1,1])
        layout.add_widget(btn)
        return layout

    def on_press_button(self):
        list_connected_devices()

def list_connected_devices():
    mngd_objs = mngr.GetManagedObjects()
    for path in mngd_objs:
        con_state = mngd_objs[path].get('org.bluez.Device1', {}).get('Connected', False)
        if con_state:
            addr = mngd_objs[path].get('org.bluez.Device1', {}).get('Address')
            name = mngd_objs[path].get('org.bluez.Device1', {}).get('Name')
            print(f'Device {name} [{addr}] is connected')

if __name__ == '__main__':
    list_connected_devices()
    app = ButtonApp()
    app.run()