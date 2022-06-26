import speech_recognition as sr
from tkinter import *
import pyperclip
 

window = Tk()
window.title("Speech To Text")
window.geometry("500x600")
l = Label(window, text="")

r = sr.Recognizer()
m = sr.Microphone()
def speechText():
    with m as source:
        try:
            l.config(text = "listening...")
            audio = r.listen(source)
            l.config(text = "Recognizing...")
            MyText = r.recognize_google(audio)
            #txt = txt + MyText
            l.config(text = MyText)
        except Exception as e:
            l.config(text = "Could you say that again please")
            print(e)
def copytext():
    pyperclip.copy(l.cget("text"))

B = Button(window, text = "Click Button To Speak", command = speechText)
C = Button(window, text = "Click to Copy", command = copytext)
B.pack(pady = 100)
C.pack()
l.pack()
window.mainloop()
