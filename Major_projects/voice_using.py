import pyttsx3
from tkinter import *
from tkinter import scrolledtext, ttk
import speech_recognition as sr
import threading
import math


engine=pyttsx3.init()
recognizer=sr.Recognizer()
engine.setProperty('rate',130)


def speak(text):
    engine.say(text)
    engine.runAndWait()



def listen():
    global stop_listening
    stop_listening=False

    with sr.Microphone() as source:

        while not stop_listening:

            try:
                root.after(0,status_label.config,{'text':'listening'})
                audio=recognizer.listen(source,timeout=10)

                command=recognizer.recognize_google(audio)

                status_label.config(text=f"You said : {command}")

                result=calculate(command)

                if result is not None:
                    display_text.insert(END,f"You said : {command}\n")
                    display_text.insert(END,f"Result: {result}\n\n")

            except sr.UnknownValueError:
                print("Sorry I did not understand")
                status_label.config(text="I dont Understand")
            
            except sr.WaitTimeoutError:
                print("Time our Error")
                status_label.config(text="Time out Error")


            
            except sr.RequestError:
                print("You are offline")
                status_label.config(text="You are offline")




def calculate(command):
    command=command.lower()
    operator=[word for word in command if word in ["+","-","/","*"]]

    if len(operator)>1:
        result="Unsupported Operation"
        print("Unsupported Operation")
        return result


    try:
        if "add" in command or "+" in command or "plus" in command or "addition" in command or "sum" in command:
            numbers=[float(n) for n in command.split() if n.replace(".","",1).isdigit()]
            result=sum(numbers)
            
        elif "subtract" in command or "-" in command or "minus" in command:
            numbers=[float(n) for n in command.split() if n.replace(".","",1).isdigit()]
            result=numbers[0]-numbers[1]

        elif "multiply" in command or "*" in command or "x" in command or "times" in command:
            numbers=[float(n) for n in command.split() if n.replace(".","",1).isdigit()]
            result=numbers[0]*numbers[1]

        elif "divide" in command or "/" in command or "divided" in command:
            numbers=[float(n) for n in command.split() if n.replace(".","",1).isdigit()]
            result=numbers[0]/numbers[1]

        elif "power" in command or "raised to" in command or "exponent" in command:
            numbers=[float(n) for n in command.split() if n.replace(".","",1).isdigit()]
            result=math.pow(numbers[0],numbers[1])

        elif "square root" in command:
            numbers=[float(n) for n in command.split() if n.replace(".","",1).isdigit()]
            result=math.sqrt(numbers[0])

        elif "square" in command:
            numbers=[float(n) for n in command.split() if n.replace(".","",1).isdigit()]
            result=numbers[0]**2

        elif "cube root" in command:
            numbers=[float(n) for n in command.split() if n.replace(".","",1).isdigit()]
            result=numbers[0]**(1/3)
        
        elif "cube" in command:
            numbers=[float(n) for n in command.split() if n.replace(".","",1).isdigit()]
            result=numbers[0]**3

        elif "even" in command or "odd" in command:
            numbers=[float(n) for n in command.split() if n.replace(".","",1).isdigit()]
            if numbers[0]%2==0:
                result="Even"
            else:
                result="Odd"

        elif "tan" in command or "tangent" in command:
            numbers=[float(n) for n in command.split() if n.replace(".","",1).isdigit()]
            result=math.tan(math.radians(numbers[0]))

        elif "sin" in command:
            numbers=[float(n) for n in command.split() if n.replace(".","",1).isdigit()]
            result=math.sin(math.radians(numbers[0]))
        elif "cos" in command:
            numbers=[float(n) for n in command.split() if n.replace(".","",1).isdigit()]
            result=math.cos(math.radians(numbers[0]))

        elif "hcf" in command or "highest common factor" in command:
            numbers=[float(n) for n in command.split() if n.replace(".","",1).isdigit()]
            result=math.gcd(numbers[0],numbers[1])

        else:
            speak("Operation Unsupported")
            result="Unsupported Operation"


    except Exception:
        print("Error")
        result="Error"

    return result




def start_listening():
    threading.Thread(target=listen).start()


def stop_listening():
    global stop_listening
    stop_listening=True
    status_label.config(text="Listening Stopped")

def clear_conversation():
  display_text.delete(1.0,END)
  status_label.config(text="Conversation Deleted")



root=Tk()
root.title("Voice Calculator")
root.geometry("700x500")
root.resizable(False,False)
root.configure(bg="#CCD4D4")
style=ttk.Style()
style.theme_use("clam")


style.configure("TButton", font=("Arial",10,"bold"),background="#008000",foreground="BLACK",padding=10)

style.map("TButtone", background=[("active","#FFA500")])


style.configure("TLable", font=("Arial",10,"bold"),background="CYAN",foreground="BLACK",padding=10)

style.configure("TScrolledText", font=("Arial",10,"bold"),background="WHITE",foreground="BLACK",padding=10)

display_text=scrolledtext.ScrolledText(root,height=15,width=70, wrap=WORD, background="#F7C878",foreground="BLACK",font=("Arial,12"))
display_text.pack(pady=10)


button_frame=ttk.Frame(root)
button_frame.pack()


start_button=ttk.Button(button_frame, text="Start_Listening",command=start_listening)

start_button.pack(side=LEFT, padx=10)


stop_button=ttk.Button(button_frame, text="Stop_Listening",command=stop_listening)

stop_button.pack(side=LEFT, padx=10)


clear_button=ttk.Button(button_frame, text="Clear_Conversation",command=clear_conversation)

clear_button.pack(side=LEFT, padx=10)


status_label=ttk.Label(root,text="Welcome to Voice Calculator")
status_label.pack(pady=20)


speak("Welcome to Voice Calculator. Click on Start Listening to Begin")
root.mainloop()