import email
from importlib.resources import path
from logging import root
from select import select
from tkinter import dialog
from tkinter.ttk import Label
from unicodedata import name
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
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
import Service_VideoToImages
from kivy.uix.videoplayer import VideoPlayer
import glob
from kivy.core.text import LabelBase
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.snackbar import Snackbar
from kivy.properties import StringProperty
from kivymd.icon_definitions import md_icons
from kivymd.uix.list import OneLineListItem
from kivymd.uix.list import TwoLineAvatarIconListItem
from kivymd.uix.list import IRightBodyTouch
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.selectioncontrol import MDCheckbox


class YourContainer(IRightBodyTouch, MDBoxLayout):
    adaptive_width = True


class Content(BoxLayout):
    pass

class ContentNavigationDrawer(BoxLayout):
    pass

class MenuScreen(ScreenManager):   
    pass



class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        '''Called when tap on a menu item.'''

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color




class testAPP(MDApp):
    mail = None
    passw =None
    namee =None
    secondN=None
    date=None
    adresse=None
    phone=None

    dialog = None
    i = 0
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file_manager_obj = MDFileManager(
            select_path=self.selectFunction,
            exit_manager=self.exit_manager,
            #preview=True,
            #show_hidden_files=True
        )


    
    def selectFunction(self,path):
        if self.root.current == "screen3":
            print(path)
            self.textfile_path = path
            self.exit_manager()

        elif self.root.current == "screen4":
            Service_VideoToImages.filep = path
            self.loadvideo(path)
            self.exit_manager()
        elif self.root.current == "screen1":
            print(path)
            
            self.exit_manager()
            for fp in [path]:
                # Split the extension from the path and normalise it to lowercase.
                ext = os.path.splitext(fp)[-1].lower()

                # Now we can simply use == to check for equality, no need for wildcards.
                if ext == ".mp3":
                    print(fp, "is an mp3!")
                    self.FileType=fp, "is an mp3!"
                    self.show_alert_dialog()

                elif ext == ".mp4":
                    print(fp, "is an mp4!")
                    self.FileType=fp, "is an mp4!"
                    self.show_alert_dialog()
                elif ext == ".avi":
                    print(fp, "is an avi!")
                    self.FileType=fp, "is an avi!"
                    self.show_alert_dialog()
                elif ext == ".wav":
                    print(fp, "is an wav!")
                    self.FileType=fp, "is an wav!"
                    self.show_alert_dialog()
                elif ext == ".png":
                    print(fp, "is an png!")
                    self.FileType=fp, "is an png!"
                    self.show_alert_dialog()
                elif ext == ".pdf":
                    print(fp, "is an pdf!")
                    self.FileType=fp, "is an pdf!"
                    self.show_alert_dialog()
                elif ext == ".jpg":
                    print(fp, "is an jpg!")
                    self.FileType=fp, "is an jpg!"
                    self.show_alert_dialog()
                else:
                    print(fp, "is an unknown file format.")
                    self.FileType=fp, "is an unknown file format."


    def open_file_manager(self):
        self.file_manager_obj.show('/')
    def open_file_manager_myfolder(self):
        self.file_manager_obj.show('C:\PycharmProjects\pythonProject\data')
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
        Clock.schedule_once(self.login, 5)
        Clock.schedule_interval(self.startprogress_bar,0)

        
        
    def login(self,*args):
        #self.root.current = "screenlogin"
        self.root.current = "screen1"
    
    def datausershow(self):
        self.root.ids.listdatauser.add_widget(
            TwoLineAvatarIconListItem(text="Email",secondary_text=self.mail)
        )
        self.root.ids.listdatauser.add_widget(
            TwoLineAvatarIconListItem(text="Password",secondary_text=self.passw)
        )
        self.root.ids.listdatauser.add_widget(
            TwoLineAvatarIconListItem(text="Name",secondary_text=self.namee),
        )
        self.root.ids.listdatauser.add_widget(
            TwoLineAvatarIconListItem(text="Second_name",secondary_text=self.secondN),
        )
        self.root.ids.listdatauser.add_widget(
            TwoLineAvatarIconListItem(text="Birthday Date",secondary_text=self.date),
        )
        self.root.ids.listdatauser.add_widget(
            TwoLineAvatarIconListItem(text="Adresse",secondary_text=self.adresse),
        )
        self.root.ids.listdatauser.add_widget(
            TwoLineAvatarIconListItem(text="Phone Number",secondary_text=self.phone),
        )
       



    
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
                title = "Notice",
                text = str(self.FileType) + "the System will check possibilty Adaptation within seconds ..",
                buttons = [
                    MDFlatButton(
                        text = "CANCEL",on_release = self.close_dialog 
                    ),
                    MDRectangleFlatButton(
                        text = "َ Approval",
                        on_release = self.checkspinner 
                    )
                ]             
            )
        self.dialog.open()
   

    def close_dialog(self,obj):
        self.dialog.dismiss()
    def closespiiner(self,obj):
        self.root.ids.sppp.active = False
        self.show_alert_dialog()
    def checkspinner(self,obj):
        self.dialog.dismiss()
        self.root.ids.sppp.active = True
        Clock.schedule_once(self.closespiiner,5)
    

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
            self.i += 3
            self.root.ids.progress_bar.value = self.i
        except:
            Clock.unschedule(self.startprogress_bar)
    
    def lanceconvertvideotoimages(self):
        Service_VideoToImages.convert()
    def loadvideo(self,pathVID):
        self.root.ids.screenviedo.add_widget(VideoPlayer(source = pathVID,state='play')
                )
    def lancdeconvert(self):
        Service_VideoToImages.ddeconvert()

    def saveFileType(self):
        filepaths = ["/folder/soundfile.mp4"]
        for fp in filepaths:
            # Split the extension from the path and normalise it to lowercase.
            ext = os.path.splitext(fp)[-1].lower()

            # Now we can simply use == to check for equality, no need for wildcards.
            if ext == ".mp3":
                print(fp, "is an mp3!")
            elif ext == ".flac":
                print(fp, "is a flac file!")
            else:
                print(fp, "is an unknown file format.")
    def checkFileType(self):
        self.open_file_manager()
        

    def snackbar_show(self):
        self.snackbar = Snackbar(
            text="This is a snackbar!",
            snackbar_x="10dp",
            snackbar_y="60dp",
        )
        self.snackbar.size_hint_x = (
            Window.width - (self.snackbar.snackbar_x * 2)
        ) / Window.width
        self.snackbar.buttons = [
            MDFlatButton(
                text="UPDATE",
                text_color=(1, 1, 1, 1),
                on_release= self.snackbar.dismiss,
            ),
            MDFlatButton(
                text="CANCEL",
                text_color=(1, 1, 1, 1),
                on_release=self.snackbar.dismiss,
            ),
        ]

        self.snackbar.open()
        
    def send_data_to_firebase(self,email,password,name,secondname,datebirth,adresse,number):
        from firebase import firebase

        firebase = firebase.FirebaseApplication(
            'https://masterapptestadaptation-default-rtdb.firebaseio.com/',None)

        data = {
            'Email': email,
            'Password' :password,
            'Name' : name,
            'Second_name' : secondname,
            'Birthday Date':datebirth,
            'Adresse':adresse,
            'Phone Number':number
        }

        firebase.post('https://masterapptestadaptation-default-rtdb.firebaseio.com/Users',data)
    
    def verify_data_login(self,email,password):
        print("check login")
        from firebase import firebase

        firebase = firebase.FirebaseApplication('https://masterapptestadaptation-default-rtdb.firebaseio.com/',None)
        result = firebase.get('https://masterapptestadaptation-default-rtdb.firebaseio.com/Users','')

        for i in result.keys():
            if result[i]['Email'] == email:
                if result[i]['Password'] == password:
                    print(email+"Logges In ! ")
                    self.root.current = "screen1"
                    self.root.ids.labelemailprofile.text = result[i]['Email'] 
                    self.mail=result[i]['Email']
                    self.passw=result[i]['Password']
                    self.namee=result[i]['Name']
                    self.secondN=result[i]['Second_name']
                    self.adresse=result[i]['Adresse']
                    self.date=result[i]['Birthday Date']
                    self.phone=result[i]['Phone Number']
                    self.root.ids.labelnameprofile.text = result[i]['Name'] + "  "+result[i]['Second_name']
                    #self.datausershow()
                else :print("paswword incorrect")
            else : print("Email incorrecte")    


    def launchcheck(self,obj):
        self.verify_data_login(self.root.ids.email_log.text,self.root.ids.password_log.text)

    def loginactionspinner(self):
        self.root.ids.splogin.active = True
        Clock.schedule_once(self.launchcheck,3)


    










LabelBase.register(name="MPoppins",fn_regular="C:\\PycharmProjects\\pythonProject\\P1_APP_ADaptation\\font\\Poppins"
                                              "-Medium.ttf")
LabelBase.register(name="BPoppins",fn_regular="C:\\PycharmProjects\\pythonProject\\P1_APP_ADaptation\\font\\Poppins"
                                              "-SemiBold.ttf")

testAPP().run()