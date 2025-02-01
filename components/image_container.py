import tkinter as tk
from PIL import Image, ImageTk

class ImageContainer(tk.Frame):
    def __init__(self, parent: tk.Frame, set_have_selection, is_input=False):
        super(ImageContainer, self).__init__()
        self.parent=parent
        self.set_have_selection = set_have_selection
        self.is_input = is_input
        self.canvas = tk.Canvas(
            self,
            width=500,
            height=400,
            bg="#FFF"
        )
        self.canvas.pack(side=tk.LEFT, padx=5, pady=5)
        self.image_loaded = False
        self.selection_box = None
        self.have_selection = False
        self.mouse_selection_start = [0, 0] # [x , y]
        self.mouse_selection_end = [0, 0]   # [x , y]

        # if this is the input canvas, set the selection box events
        if self.is_input:
            self.canvas.bind("<B1-Motion>", self.on_mouse_move) 
            self.canvas.bind("<ButtonPress-1>", self.on_mouse_button_down)

    def load_image(self, image):
        # convert to photo image    
        self.raw_image = image
        array_image = Image.fromarray(image)
        self.photo_image = ImageTk.PhotoImage(image=array_image)
        height, width, depth = image.shape
        self.canvas.config(width=width, height=height)
        self.canvas.create_image(0, 0, image=self.photo_image, anchor=tk.NW)
        self.canvas.update()
        self.image_loaded = True

    def on_mouse_button_down(self, event):
        if not self.image_loaded: return

        self.delete_selection_box()
        self.have_selection = False
        self.set_have_selection(False)
        self.mouse_selection_start = [event.x, event.y]

    def on_mouse_move(self, event):
        if not self.image_loaded: return

        self.delete_selection_box()

        self.mouse_selection_end = [event.x, event.y]
        self.have_selection = True
        self.set_have_selection(True)

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

    def get_selection(self):
        if not self.image_loaded or not self.have_selection:
            return []
        
        # ensure we have the ordering of x and y points for slicing
        x_min, x_max = min(self.mouse_selection_start[0], self.mouse_selection_end[0]), max(self.mouse_selection_start[0], self.mouse_selection_end[0])
        y_min, y_max = min(self.mouse_selection_start[1], self.mouse_selection_end[1]), max(self.mouse_selection_start[1], self.mouse_selection_end[1])
        
        return self.raw_image[y_min:y_max, x_min:x_max]
