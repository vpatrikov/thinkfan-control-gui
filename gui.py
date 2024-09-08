from pathlib import Path
from tkinter import Tk, Canvas, Text, Button, PhotoImage, messagebox
import subprocess
from time import sleep
from threading import Thread
import os
from platform import system

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame0")

current_speed = "auto"

def get_info():
    global current_speed
    try:
        info_lines = subprocess.check_output("sensors", text=True).split("\n")
        result = [f"Set Fan Speed: {current_speed}"]
        count = 1
        for line in info_lines:
            if "Core" in line:
                result.append(f"Core {count}: {line.split(':')[-1].split('(')[0].strip()}")
                count += 1
            if "fan" in line:
                result.append(f"Fan: {line.split(':')[-1].strip()}")
    except subprocess.CalledProcessError:
        result = ["Error fetching sensor data"]
    return result

def set_speed(speed=None):
    global current_speed
    try:
        command = f'pkexec sh -c "echo level {speed} > /proc/acpi/ibm/fan"'
        os.system(command)
        current_speed = speed
        print(f"Fan speed set to {speed}")
    except Exception as e:
        print(f"Failed to set fan speed to {speed}: {e}")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def start_display_loop():
    def display_loop():
        while True:
            sleep(0.5)
            new_text = "\n".join(get_info())
            entry_1.config(state='normal')
            entry_1.delete(1.0, 'end')
            entry_1.insert('end', new_text, "center")
            entry_1.config(state='disabled')
    Thread(target=display_loop, daemon=True).start()

window = Tk()

if system() != "Linux":
    messagebox.showerror(
        title="Program made for Linux!", 
        message="This program will not work on your OS."
    )
    window.destroy()
    exit(1)

window.geometry("1000x720")
window.configure(bg="#1E1E1E")

canvas = Canvas(
    window,
    bg="#1E1E1E",
    height=720,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png")
)
entry_bg_1 = canvas.create_image(
    763.0,
    360.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Inter", 20),  # Set larger font size
    wrap="word",  # Enable word wrapping
)
entry_1.place(
    x=616.0,
    y=91.0,  # Adjusted y position for new layout
    width=294.0,
    height=375.0
)
entry_1.tag_configure("center", justify="center")
entry_1.config(state='disabled')  # Disable editing by default

canvas.create_text(
    89.0,
    97.0,
    anchor="nw",
    text="Select fan speed:",
    fill="#FFFFFF",
    font=("Inter", 35 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png")
)
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: set_speed(1),
    relief="flat"
)
button_1.place(
    x=61.0,
    y=185.0,
    width=75.0,
    height=75.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png")
)
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: set_speed(2),
    relief="flat"
)
button_2.place(
    x=151.0,
    y=185.0,
    width=75.0,
    height=75.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png")
)
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: set_speed(3),
    relief="flat"
)
button_3.place(
    x=241.0,
    y=185.0,
    width=75.0,
    height=75.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png")
)
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: set_speed(4),
    relief="flat"
)
button_4.place(
    x=196.0,
    y=285.0,
    width=75.0,
    height=75.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png")
)
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: set_speed(5),
    relief="flat"
)
button_5.place(
    x=106.0,
    y=285.0,
    width=75.0,
    height=75.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png")
)
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: set_speed(6),
    relief="flat"
)
button_6.place(
    x=331.0,
    y=185.0,
    width=75.0,
    height=75.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png")
)
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: set_speed(7),
    relief="flat"
)
button_7.place(
    x=286.0,
    y=285.0,
    width=75.0,
    height=75.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png")
)
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: set_speed("auto"),
    relief="flat"
)
button_8.place(
    x=173.0,
    y=512.0,
    width=120.0,
    height=92.1
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png")
)
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: set_speed("full-speed"),
    relief="flat"
)
button_9.place(
    x=151.0,
    y=385.0,
    width=163.0,
    height=102.0
)

start_display_loop()
window.title("Thinkfan Control")
window.resizable(False, False)
window.mainloop()
