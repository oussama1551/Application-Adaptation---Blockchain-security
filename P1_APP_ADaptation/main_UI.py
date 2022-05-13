from importlib.resources import path
from logging import root
from select import select
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
from kivymd.uix.filemanager import MDFileManager
from email.mime import audio
import speech_recognition as sr
from kivy.clock import Clock





class MenuScreen(ScreenManager):   
    pass
class testAPP(MDApp):
    dialog = None
    i = 0
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file_manager_obj = MDFileManager(
            select_path=self.select_path,
            exit_manager=self.exit_manager,
            #preview=True,
            #show_hidden_files=True
        )
        
    def select_path(self,path):
        print(path)
        self.textfile_path = path
        self.exit_manager()
    def open_file_manager(self):
        self.file_manager_obj.show('/')
    def exit_manager(self):
        self.file_manager_obj.close() 
       
    def build(self):
        self.title='Adaptation Application'
        Window.size = (360, 600)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        self.data = []
        Builder.load_file('myUI1.kv')
        return MenuScreen()
    def on_start(self):
        Clock.schedule_once(self.login, 7)
        Clock.schedule_interval(self.startprogress_bar,0.5)
        
    def login(self,*args):
        self.root.current = "screen1"
    
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
        self.root.current = "screen3"
        self.root.transition.direction = "left"
        self.dialog.dismiss()
    def texttospeech_FileText(self):
        #myText1 = "Real Madrid" hhhhhh
        fh = open(self.textfile_path,"r")
        myText = fh.read().replace("\n", " ")
        language = 'en'
        output = gTTS(text=myText,lang=language,slow=False)
        output.save("output1.mp3")
        os.system("start output1.mp3")
    def texttospeech(self):
        #myText1 = "Real Madrid"
        #fh = open(self.textfile_path,"r")
        #myText = fh.read().replace("\n", " ")
        language = 'en'
        output = gTTS(text=self.textfieldtext,lang=language,slow=False)
        output.save("output1.mp3")
        os.system("start output1.mp3")
    def savetextfromtextfield(self):
        self.textfieldtext = self.root.ids.textfieldspeech.text
        print(self.textfieldtext)
        self.texttospeech()
    def adaptTextfile(self):
        self.texttospeech_FileText()

    def recordsound(self):
        self.recordaction()
    def recordaction(self):
        r = sr.Recognizer()
        self.outfileaudio_Text = open('data_audio.txt', 'w')
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            #self.root.ids.labelsay.text = "Please say something .."
            print("Please say something ..")
            self.audio = r.listen(source)
            try:
                #print("you have said : \n "+ r.recognize_google(audio))
                self.root.ids.labelwhatdoyousay.text = "you have said : \n "+ r.recognize_google(self.audio)
                self.audio_text = r.recognize_google(self.audio)
                self.outfileaudio_Text.write(self.audio_text)
                self.outfileaudio_Text.close()
            except Exception as e:
                print("Error : "+ str(e))
    def savesound(self):
        print("teststst")
        with open("recodedaudio.wav","wb") as f:
            f.write(self.audio.get_wav_data())
        os.system("recodedaudio.wav")
    def opentext(self):
        os.system("data_audio.txt")
    def adaptSound(self):
        filesound = open(self.textfile_path,"rb")
        r = sr.Recognizer()
        with sr.AudioFile(filesound) as source:
            # listen for the data (load audio to memory)
            audio_data = r.record(source)
            # recognize (convert from speech to text)
            text = r.recognize_google(audio_data)
            print(text)
            self.root.ids.lastlabel.text = text
    def startprogress_bar(self,*args):
        try:
            self.i += 10
            self.root.ids.progress_bar.value = self.i
        except:
            Clock.unschedule(self.startprogress_bar)




        

    




testAPP().run()