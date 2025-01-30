import tkinter as tk

class ImageContainer(tk.Frame):
    def __init__(self, parent: tk.Frame):
        super(ImageContainer, self).__init__()
        self.parent=parent
        self.canvas = tk.Canvas(
            self,
            width=500,
            height=400,
            background="#FFF",
        )
        self.canvas.pack(side=tk.LEFT, padx=5, pady=5)

    def load_image(self, image):
        print(image)
        self.canvas.create_image(0, 0, image=image)
        