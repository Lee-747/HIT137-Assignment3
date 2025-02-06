# HIT 137 Assignment 3 
# Group Name: CAS/DAN 1
# Group Members:
# Lee Potter - S368675
# Sahil Badgal - S384037


import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import os.path
import cv2


from components.image_container import ImageContainer
from components.image_resizer_saver import ImageResizer, ImageSaver

class ImageEditorApp():
    
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title('HIT137 Assignment 3 - Image Editor')
        # self.root.geometry('1200x800')
        self._setup_gui()

    def _setup_gui(self):
        # create main container
        main_container = tk.Frame(self.root)
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self._setup_inputs(main_container)
        self._setup_image_containers(main_container)

    def _setup_inputs(self, main_container):
        self.input_frame = tk.Frame(main_container)
        self.input_frame.pack(side=tk.TOP, fill=tk.X)

        self.open_file_button = tk.Button(self.input_frame, text="Open file", command=self._click_open_image)
        self.open_file_button.pack(side=tk.LEFT)

        self.crop_button = tk.Button(self.input_frame, text="Crop\nSelected\nArea", command=self.click_crop, state="disabled")
        self.crop_button.pack(side=tk.LEFT)

        self.scale = ttk.Scale(self.input_frame, from_=200, to=0, orient=tk.HORIZONTAL)
        self.scale.pack(side=tk.RIGHT)
        self.scale.set(100)

    def _setup_image_containers(self, main_container: tk.Frame):

        self.left_image = ImageContainer(main_container, self.set_have_selection, is_input=True)
        self.left_image.pack(side=tk.LEFT)


        self.right_image = ImageContainer(main_container, None, is_input=False)
        self.right_image.pack(side=tk.RIGHT)

    def _click_open_image(self):
        try:
            file_path = filedialog.askopenfilename()
            if not os.path.isfile(file_path):
                return
            
            self.input_image = cv2.cvtColor(cv2.imread(file_path), cv2.COLOR_BGR2RGB)

            # load image onto container
            self.left_image.load_image(self.input_image)

            #TODO set right image to same size
            
        
        except Exception as ex:
            print(f"Error attempting to open input file from {file_path}")
            error_message_template = "Exception of type {0} raised. {1!r}"
            message = error_message_template.format(type(ex).__name__, ex.args)
            print(message)

    def set_have_selection(self, have_selection):
        if not have_selection:
            self.crop_button["state"] = "disabled"
        else:
            self.crop_button["state"] = "active"

    def click_crop(self):
        cropped_img = self.left_image.get_selection()
        if len(cropped_img) == 0:
            return
        
        self.right_image.load_image(cropped_img)

    def _setup_gui(self):
        main_container = tk.Frame(self.root)
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Create top frame for buttons
        top_frame = tk.Frame(main_container)
        top_frame.pack(side=tk.TOP, fill=tk.X)

        self._setup_inputs(top_frame)  # Pass top_frame instead of main_container
        self._setup_image_containers(main_container)

    # Add Image Saver to the top frame
        self.saver = ImageSaver(self.root, self.right_image, top_frame)



if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()

