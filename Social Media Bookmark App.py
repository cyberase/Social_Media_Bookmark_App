import tkinter as tk
import webbrowser


def github(event):
    webbrowser.open_new_tab('https://github.com/cyberase')


def twitter(event):
    webbrowser.open_new_tab('https://twitter.com/cyberasee?t=gHzWF_z2INYqiiAhNXr-8w&s=09')


def instagram(event):
    webbrowser.open_new_tab('https://www.instagram.com/xappinez/')


window = tk.Tk()
window.geometry("350x220")
window.title("Social Media Bookmark App")

label1 = tk.Label(text="My Social Media")
label1.grid(column=0, row=0)

button1 = tk.Button(window, text="GitHub", bg="yellow")
button1.grid(column=1, row=1)
button2 = tk.Button(window, text="Twitter", bg="blue")
button2.grid(column=3, row=1)
button3 = tk.Button(window, text="Instagram", bg="pink")
button3.grid(column=5, row=1)

button1.bind("<Button-1>", github)
button2.bind("<Button-1>", twitter)
button3.bind("<Button-1>", instagram)

window.mainloop()
