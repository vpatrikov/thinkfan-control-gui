#!/usr/bin/python3
import tkinter as tk
import subprocess
from time import sleep
from threading import Thread
import os

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

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.parent.minsize(width=500, height=300)
        self.parent.title("Thinkfan Control")
        self.config(bg='#222')

        self.status_panel = tk.Label(self, bg='white', fg='black', font=('Helvetica', 12), text="", anchor='center', justify='center')
        self.status_panel.place(x=250, y=0, width=250, height=300)

        self.buttons_frame = tk.Frame(self, bg='#222')
        self.buttons_frame.place(x=0, y=0, width=240, height=300)

        buttons = [str(i) for i in range(7)]
        for i, speed in enumerate(buttons):
            button = tk.Button(self.buttons_frame, text=speed, command=lambda s=speed: set_speed(s),
                               bg='#337ab7', fg='white', font=('Helvetica', 10), width=5, height=2)
            row, col = divmod(i, 4)
            button.grid(row=row, column=col, padx=5, pady=5)

        button7 = tk.Button(self.buttons_frame, text="7", command=lambda: set_speed("7"),
                            bg='#337ab7', fg='white', font=('Helvetica', 10), width=5, height=2)
        button7.grid(row=2, column=0, padx=5, pady=5)

        full_button = tk.Button(self.buttons_frame, text="Full", command=lambda: set_speed("full-speed"),
                                bg='#337ab7', fg='white', font=('Helvetica', 10), width=5, height=2)
        auto_button = tk.Button(self.buttons_frame, text="Auto", command=lambda: set_speed("auto"),
                                bg='#337ab7', fg='white', font=('Helvetica', 10), width=5, height=2)
        full_button.grid(row=3, column=1, padx=5, pady=5)
        auto_button.grid(row=3, column=2, padx=5, pady=5)

        self.start_display_loop()

    def start_display_loop(self):
        def display_loop():
            while True:
                sleep(0.5)
                new_text = "\n".join(get_info())
                if self.status_panel["text"] != new_text:
                    self.status_panel["text"] = new_text
        Thread(target=display_loop, daemon=True).start()

if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(0, 0)
    app = MainApplication(root)
    app.pack(expand=True, fill=tk.BOTH)
    root.mainloop()
