import time
import pyautogui
import tkinter as tk
from PIL import Image

def screenshot():
    root.withdraw()  # Hide the Tkinter window
    time.sleep(1)
    name = int(round(time.time() * 1000))  # Use current time for unique filenames
    file_path = 'Screenshot App/screenshots{}.png'.format(name)
    image = pyautogui.screenshot(file_path)  # Save directly to the file path
    image.show()  # Show the screenshot

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text = "Take Screenshot",
    command = screenshot)

button.pack(side=tk.LEFT)

close = tk.Button(
    frame,
    text = "Quit",
    command = quit)

close.pack(side=tk.LEFT)

root.mainloop()