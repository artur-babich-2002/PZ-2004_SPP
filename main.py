import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import numpy
from numpy import asarray, array
import numpy as np
from PIL import Image, ImageTk
from tkinter import messagebox
try:
    import tkinter as tk
except:
    import Tkinter as tk
import os

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "newproject.ui")
PROJECT_IMG = os.path.join(PROJECT_PATH, "projectimage.jpg")

image = Image.open('projectimage.jpg')
pixels = image.load()
IMG_DATA = np.asarray(image)


class NewprojectApp:
    global text
    text = "hello"

    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('toplevel1', master)
        self.textframe = builder.get_object('text')

        builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()

    def changetext(self):
        global text
        # self.textframe.configure(width=5)
        self.textframe.insert(3.0, IMG_DATA)
    def on_image_button_clicked(self):
        global PROJECT_IMG
        self.canvas = self.builder.get_object('canva')
        self.aux = Image.open(PROJECT_IMG)
        self.img = ImageTk.PhotoImage(self.aux)
        self.canvas.create_image(180, 350, image=self.img, anchor=tk.W)
        # canvas.create_image(0,0, image=self.img, anchor='n')
        messagebox.showinfo('Image open', 'Image loaded!')

    def on_quit_button_clicked(self):
        self.mainwindow.quit()


if __name__ == '__main__':
    app = NewprojectApp()
    app.run()

