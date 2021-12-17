from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import os
from os import walk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#

def display_profile(strength, vitality, focus, state):
    x = ""

def runcode():
    if state == "reqsave":
        inp = entry_1.get()
        if str(inp) == "NEW":
            wipelines()
            canvas.itemconfig(line1, text = "Insert Creation 'ere")
        else:
            strength = 0 
            vitality = 0 
            focus = 0 
            mood = 0 
            for i, row in enumerate(open("saves/" + str(inp) + ".hz")): 
            #  LOAD STRENGTH
                if i in range(0,1): 
                    strength = (row)
            #  LOAD VITALITY
                if i in range(1,2): 
                    vitality = (row)
            #  LOAD FOCUS
                if i in range(2,3): 
                    focus = (row)
            #  LOAD MOOD
                if i in range(3,4): 
                    mood = (row)
            wipelines()
            canvas.itemconfig(line1, text = "Loaded Save!")
            display_profile(strength, vitality, focus, mood)

def display_profile(strength, vitality, focus, mood):
    string = "S: " + strength + "   " + "V: " + vitality + "   " + "F: " + focus + "   " + "M: " + mood + "   "
    ssize = 16
    amount = ssize - len(string)
    canvas.itemconfig(stattext, text = string.center(amount))

def wipelines():
    canvas.itemconfig(line1, text = " ")
    canvas.itemconfig(line2, text = " ")
    canvas.itemconfig(line3, text = " ")
    canvas.itemconfig(line4, text = " ")
    canvas.itemconfig(line5, text = " ")
    canvas.itemconfig(line6, text = " ")
    canvas.itemconfig(line7, text = " ")
    canvas.itemconfig(line8, text = " ")
    canvas.itemconfig(line9, text = " ")
    canvas.itemconfig(line10, text = " ")
    canvas.itemconfig(line11, text = " ")
    canvas.itemconfig(line12, text = " ")
    canvas.itemconfig(line13, text = " ")
    canvas.itemconfig(line14, text = " ")
    
#

window = Tk()

window.geometry("1280x720")
window.configure(bg = "#222222")


canvas = Canvas(
    window,
    bg = "#222222",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    214.0,
    359.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    848.0,
    409.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    1065.0,
    49.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    959.0,
    87.0,
    image=image_image_4
)

line1 = canvas.create_text(
    473.0,
    156.0,
    anchor="nw",
    text="Line1",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

line4 = canvas.create_text(
    472.0,
    246.0,
    anchor="nw",
    text="Line4",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

line2 = canvas.create_text(
    473.0,
    186.0,
    anchor="nw",
    text="Line2",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

line5 = canvas.create_text(
    472.0,
    276.0,
    anchor="nw",
    text="Line5",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

line3 = canvas.create_text(
    473.0,
    216.0,
    anchor="nw",
    text="Line3",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

line6 = canvas.create_text(
    472.0,
    306.0,
    anchor="nw",
    text="Line6",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

line7 = canvas.create_text(
    473.0,
    336.0,
    anchor="nw",
    text="Line7",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

line8 = canvas.create_text(
    474.0,
    366.0,
    anchor="nw",
    text="Line8",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

line11 = canvas.create_text(
    473.0,
    456.0,
    anchor="nw",
    text="Line11",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

line9 = canvas.create_text(
    474.0,
    396.0,
    anchor="nw",
    text="Line9",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

line12 = canvas.create_text(
    473.0,
    486.0,
    anchor="nw",
    text="Line12",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

line10 = canvas.create_text(
    474.0,
    426.0,
    anchor="nw",
    text="Line10",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

line13 = canvas.create_text(
    473.0,
    516.0,
    anchor="nw",
    text="Line13",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

line14 = canvas.create_text(
    474.0,
    546.0,
    anchor="nw",
    text="Line14",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    814.0,
    633.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#ECECEC",
    highlightthickness=0
)
entry_1.place(
    x=507.0,
    y=606.0,
    width=614.0,
    height=52.0
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    210.0,
    644.0,
    image=image_image_5
)

stattext = canvas.create_text(
    73.0,
    633.0,
    anchor="nw",
    text="S: 0    V: 0    F: 0    S: 0",
    fill="#FFFFFF",
    font=("Roboto", 18 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: runcode(),
    relief="flat"
)
button_1.place(
    x=1167.0,
    y=606.0,
    width=58.0,
    height=54.0
)

#

state = "none"

wipelines()
filenames = next(walk("saves"), (None, None, []))[2]  # [] if no file
if len(filenames) < 1:
    canvas.itemconfig(line1, text = "No prior saves found - initialising profile creation.")
    #create_profile()
else:
    debounce = False
    for i in range(0, len(filenames)):
        if ".hz" in filenames[i]:
            debounce = True
    if debounce == True:
        amount = 0
        for i in range(0, len(filenames)):
            if ".hz" in filenames[i]:
                amount += 1
        canvas.itemconfig(line1, text = "We've managed to find " + str(amount) + " save/s.")
        for i in range(0, len(filenames)):
            if ".hz" in filenames[i]:
                savedisplay = filenames[i]
                savedisplay = savedisplay[:-3]
                canvas.itemconfig(line2, text = " | " + savedisplay)
        canvas.itemconfig(line4, text = "[Type 'NEW' to create a new save, or specify the save name to load it!]")
        state = "reqsave"
    else:
        print("No prior saves found - initialising profile creation.")
        #create_profile()
#

window.resizable(False, False)
window.mainloop()

