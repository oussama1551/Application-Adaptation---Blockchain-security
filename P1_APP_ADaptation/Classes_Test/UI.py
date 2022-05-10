
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.config import Config
from kivy.core.window import Window



class myapp(MDApp):
    def build(self):
        self.title='UI app'
        Window.size = (380, 600)



        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"


myapp().run()



