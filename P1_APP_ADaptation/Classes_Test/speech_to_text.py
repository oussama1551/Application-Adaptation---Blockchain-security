from email.mime import audio
import speech_recognition as sr




def main():
    r = sr.Recognizer()
    outfileaudio_Text = open('data_audio.txt', 'w')

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please say something ..")
        audio = r.listen(source)
        try:
            print("you have said : \n "+ r.recognize_google(audio))
            audio_text = r.recognize_google(audio)
            outfileaudio_Text.write(audio_text)
            outfileaudio_Text.close()
            print("Audio Recorder Successfully\n")
        except Exception as e:
            print("Error : "+ str(e))

        with open("recodedaudio.wav","wb") as f:
            f.write(audio.get_wav_data())

if __name__=="__main__":
    main()