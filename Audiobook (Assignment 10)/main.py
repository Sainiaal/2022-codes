from tkinter import filedialog
from tkinter import *
import os
import PyPDF2
import requests


path = ""
API_KEY = "a178e2ec5c7144f8818a55d329ecc798"
text = ""
API_URL = "http://api.voicerss.org"


# -------------------------------- FUNCTIONS ---------------------------------------

def get_path():
    global path
    path = filedialog.askopenfilename(initialdir="C:/Users/user/Downloads", title="Select a Pdf")
    show_file()


def show_file():
    filename = path.split("/")[-1]
    file_dir.config(text=f"opened file: '{filename}'")
    generate_btn.place(x=202, y=250)
    openfile()


def openfile():
    global text
    with open(path, "rb") as data:
        pdfreader = PyPDF2.PdfFileReader(data)
        page_obj = pdfreader.getPage(0)
        text = page_obj.extractText()


def finalize():
    param = {
        "key": API_KEY,
        "src": text,
        "hl": "en-in",
        "c": "MP3"
    }
    response = requests.request("POST", API_URL, params=param)
    with open('movie.mp3', 'wb') as audio:
        audio.write(response.content)

    os.system("start movie.mp3")


# -------------------------------- INTERFACE ---------------------------------------

window = Tk()
window.config(bg="#00ABB3")
window.geometry("500x500")

heading = Label(window, text="Pdf To Audio", bg="#00ABB3", font=("Segoe Script", 40, "bold"), fg="#3C4048")
heading.place(x=50, y=0)

file_dir = Label(window, pady=50, text="opened file: ", bg="#00ABB3", font=("Arial", 15, "bold"), fg="#3C4048")
file_dir.place(x=50, y=100)

select_file = Button(window, text="Select Pdf", bg="#3C4048", font=("Arial", 10, "bold"),
                     fg="#EAEAEA", activebackground="#EAEAEA", command=get_path)
select_file.place(x=200, y=200)

generate_btn = Button(window, text="Generate", bg="#3C4048", font=("Arial", 10, "bold"),
                      fg="#EAEAEA", activebackground="#EAEAEA", command=finalize)

window.mainloop()
