from logging import root
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import serial
import time
from kivymd.uix.list import OneLineListItem
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from gtts import gTTS
import os


class MenuScreen(ScreenManager):
    pass



class testAPP(MDApp):
    dialog = None
   
    def build(self):
        self.title='UI app'
        Window.size = (380, 600)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        self.data = []
        Builder.load_file('myUI1.kv')
        return MenuScreen()
    

    def receivefromarduino(self):
        print("test ")
        self.getData()
        #self.show_alert_dialog()

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
                        self.root.ids.container.add_widget(
                            OneLineListItem(text=f"{string} -- Sound Low",theme_text_color="Primary")
                        
                    )
                    else:
                        self.root.ids.container.add_widget(
                            OneLineListItem(text=f"{string} -- Sound High",theme_text_color="Error")
                            
                        )
                        print("Sound High")
                        self.show_alert_dialog()

                else: print("no data received")
            self.ser.close()

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title = "Attention",
                text = "The system detects that the volume is too high, the Adaptation will start within seconds ..",
                buttons = [
                    MDFlatButton(
                        text = "CANCEL",on_release = self.close_dialog
                    ),
                    MDRectangleFlatButton(
                        text = "َ Approval",on_release =self.change_screen


                    )
                ]
                
            )
        self.dialog.open()

    def close_dialog(self,obj):
        self.dialog.dismiss()
    def change_screen(self,obj):
        self.root.current = "screen2"
        self.root.transition.direction = "left"
        self.dialog.dismiss()

    def texttospeech(self):
        #myText1 = "Real Madrid"
        #fh = open("C:\\PycharmProjects\\pythonProject\\P1_APP_ADaptation\\Classes_Test\\test.txt","r")
        #myText = fh.read().replace("\n", " ")
        language = 'en'
        output = gTTS(text=self.textfieldtext,lang=language,slow=False)
        output.save("output1.mp3")
        os.system("start output1.mp3")

    def savetextfromtextfield(self):
        self.textfieldtext = self.root.ids.textfieldspeech.text
        print(self.textfieldtext)
        self.texttospeech()

           

    




testAPP().run()