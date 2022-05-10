from gtts import gTTS
import os

myText1 = "i love you douaa"
fh = open("C:\\PycharmProjects\\pythonProject\\P1_APP_ADaptation\\Classes_Test\\test.txt","r")
myText = fh.read().replace("\n", " ")
save_path = "C:\\PycharmProjects\\pythonProject\\P1_APP_ADaptation\\Classes_Test"
language = 'en'

output = gTTS(text=myText,lang=language,slow=False)
#filesave = os.path.join(save_path,output.save("output.mp3"))
output.save("output.mp3")
fh.close()

os.system("start output.mp3")