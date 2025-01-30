import tkinter as tk

class ImageContainer(tk.Frame):
    def __init__(self, parent: tk.Frame):
        super(ImageContainer, self).__init__()
        self.parent=parent
        self.canvas = tk.Canvas(
            self,
            background="#FFF",
        )
        self.canvas.pack(side=tk.LEFT, padx=5, pady=5)