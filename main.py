from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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

canvas.create_text(
    473.0,
    156.0,
    anchor="nw",
    text="Line1",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    472.0,
    246.0,
    anchor="nw",
    text="Line4",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    473.0,
    186.0,
    anchor="nw",
    text="Line2",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    472.0,
    276.0,
    anchor="nw",
    text="Line5",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    473.0,
    216.0,
    anchor="nw",
    text="Line3",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    472.0,
    306.0,
    anchor="nw",
    text="Line6",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    473.0,
    336.0,
    anchor="nw",
    text="Line7",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    474.0,
    366.0,
    anchor="nw",
    text="Line8",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    473.0,
    456.0,
    anchor="nw",
    text="Line11",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    474.0,
    396.0,
    anchor="nw",
    text="Line9",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    473.0,
    486.0,
    anchor="nw",
    text="Line12",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    474.0,
    426.0,
    anchor="nw",
    text="Line10",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    473.0,
    516.0,
    anchor="nw",
    text="Line13",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
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

canvas.create_text(
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
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=1167.0,
    y=606.0,
    width=58.0,
    height=54.0
)
window.resizable(False, False)
window.mainloop()
