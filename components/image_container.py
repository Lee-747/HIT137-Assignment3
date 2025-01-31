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

        self.selection_box = None
        self.mouse_selection_start = [0, 0] # [x , y]
        self.mouse_selection_end = [0, 0]   # [x , y]
        self.have_selection = False
        self.canvas.bind("<B1-Motion>", self.on_mouse_move) 
        self.canvas.bind("<ButtonPress-1>", self.on_mouse_button_down)
        # self.canvas.bind("<ButtonRelease-1>", self.on_mouse_button_up)

    def load_image(self, image):
        # convert to photo image    
        array_image = Image.fromarray(image)
        self.image = ImageTk.PhotoImage(image=array_image)
        height, width, depth = image.shape
        self.canvas.config(width=width, height=height)
        self.canvas.create_image(0, 0, image=self.image, anchor=tk.NW)
        self.canvas.update()

    def on_mouse_button_down(self, event):
        self.delete_selection_box()
        self.have_selection = False
        self.mouse_selection_start = [event.x, event.y]

    def on_mouse_move(self, event):
        self.delete_selection_box()

        self.mouse_selection_end = [event.x, event.y]
        self.have_selection = True

        # draw vertical and horizontal selection lines
        self.selection_box = self.canvas.create_rectangle(self.mouse_selection_start[0], 
                                                          self.mouse_selection_start[1],
                                                          event.x, 
                                                          event.y,
                                                          outline="navy",
                                                          fill="RoyalBlue1",
                                                          stipple="gray50")

    def delete_selection_box(self):
        if self.selection_box != None:
            self.canvas.delete(self.selection_box)
            self.selection_box = None