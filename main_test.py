import tkinter as tk

def say_hello():
    label.config(text="You clicked the button!")

window = tk.Tk()
window.title("Hello Tkinter")
label = tk.Label(window, text="Hello, Tkinter")
label.pack()

button = tk.Button(window, text="Klick me", command=say_hello)
button.pack()


window.mainloop()