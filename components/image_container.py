import tkinter as tk
from PIL import Image, ImageTk

class ImageContainer(tk.Frame):
    def __init__(self, parent: tk.Frame):
        super(ImageContainer, self).__init__()
        self.parent=parent
        self.canvas = tk.Canvas(
            self,
            width=500,
            height=400,
            bg="#FFF"
        )
        self.canvas.pack(side=tk.LEFT, padx=5, pady=5)
        self.mouse_button_down = False
        self.mouse_selection_start = [0, 0] # [x , y]
        self.mouse_selection_end = [0, 0]   # [x , y]
        self.canvas.bind("<Motion>", self.on_mouse_move) 
        self.canvas.bind("<ButtonPress-1>", self.on_mouse_button_down)

    def load_image(self, image):
        # convert to photo image    
        array_image = Image.fromarray(image)
        self.image = ImageTk.PhotoImage(image=array_image)
        height, width, depth = image.shape
        self.canvas.config(width=width, height=height)
        self.canvas.create_image(0, 0, image=self.image, anchor=tk.NW)

    def on_mouse_button_down(self, event):
        self.mouse_button_down = True
        self.mouse_selection_start = [event.x, event.y]

    def on_mouse_move(self, event):
        self.mouseX = event.x
        self.mouseY = event.y
        # print(f'X:{self.mouseX} Y:{self.mouseY}')

    def on_mouse_button_up(self, event):
        self.mouse_button_down = False
        self.mouse_end_x = event.x
        self.mouse_end_y = event.y
        