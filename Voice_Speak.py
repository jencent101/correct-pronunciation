from tkinter import *
from tkinter import messagebox
import pyttsx3

author = "Jencent Dizon"
link = "https://github.com/I-am-Programmer-101"
print("Author:", author, "\t\tLink:",link)

rt = Tk()
rt.title("Voice Speak")

engine = pyttsx3.init()
def Enter():
    entry_message = enter_entry.get()
    engine.say(entry_message)
    engine.runAndWait()

def Reset():
    enter_entry.delete(0, END)

frame = LabelFrame(rt,padx=70, pady=70, bg="lightblue")
enter_label  = Label(frame, text="Enter a string to say : ", bg="lightblue", fg="darkviolet")
enter_entry  = Entry(frame, width=25)
enter_button = Button(frame, text="Enter", padx=20, command=Enter, bg="lightblue", fg="blue")
reset_button = Button(frame, text="Reset",padx=20, command=Reset, bg="lightblue", fg="green")
exit_button  = Button(frame, text="Exit", padx=20, command=rt.destroy, bg="lightblue", fg="red")

frame.pack(padx=25, pady=25)
enter_label.grid(row=0, column=0)
enter_entry.grid(row=0, column=1)
enter_button.grid(row=1, column=0)
reset_button.grid(row=1, column=1)
exit_button.grid(row=1, column=2)

rt.mainloop()
