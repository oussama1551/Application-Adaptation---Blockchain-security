from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import serial
import time
from kivymd.uix.list import OneLineListItem






class MenuScreen(Screen):
    pass
class ProfileScreen(Screen):
    pass
class UploadScreen(Screen):
    pass
# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(UploadScreen(name='upload'))


class DemoApp(MDApp):
    dialog = None

    def build(self):
        self.title='UI app'
        Window.size = (380, 600)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        self.data = []
        #return Builder.load_file('DemoApp.kv')
    

    def receivefromarduino(self):
        print("test ")
        self.getData()

    def getData(self):
            self.ser = serial.Serial('COM3', 9800, timeout=1)
            time.sleep(2)
            for i in range(100):
                self.line = self.ser.readline()   # read a byte string
                if self.line:
                    string = self.line.decode()  # convert the byte string to a unicode string
                    # convert the unicode string to an int
                    f = float(string)
                    print(string)
                    self.data.append(string)
                    if f < 300 :
                        print("Sound High")
                        self.root.ids.screen_manager.get_screen("menu").ids.container.add_widget(
                            OneLineListItem(text=f"{string} -- Sound Low",theme_text_color="Primary")
                        
                    )
            self.ser.close()
           

    




DemoApp().run()