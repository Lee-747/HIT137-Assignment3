# HIT 137 Assignment 3 
# Group Name: CAS/DAN 1
# Group Members:
# Lee Potter - S368675
# Sahil Badgal - S384037


import tkinter as tk
from components.image_container import ImageContainer

class ImageEditorApp():
    
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title('HIT137 Assignment 3 - Image Editor')
        self.root.geometry('1200x800')
        self._setup_gui()

    def _setup_gui(self):
        # create main container
        main_container = tk.Frame(self.root)
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self._setup_inputs(main_container)
        self._setup_image_containers(main_container)

    def _setup_inputs(self, main_container):
        self.input_frame = tk.Frame(main_container)
        self.input_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        self.open_file_button = tk.Button(self.input_frame, text="Open file")
        self.open_file_button.pack(side=tk.LEFT)


    def _setup_image_containers(self, main_container: tk.Frame):

        self.left_image = ImageContainer(main_container)
        self.left_image.pack(side=tk.LEFT)

        self.right_image = ImageContainer(main_container)
        self.right_image.pack(side=tk.RIGHT)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()

