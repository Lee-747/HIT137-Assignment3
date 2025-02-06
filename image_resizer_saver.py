import cv2
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

class ImageResizer(tk.Frame):
    def __init__(self, parent, image_container):
        super().__init__(parent)
        self.image_container = image_container
        self.scale = tk.Scale(self, from_=10, to=200, orient=tk.HORIZONTAL, command=self.resize_image)
        self.scale.set(100)
        self.scale.pack()
        self.original_image = None

    def set_image(self, image):
        self.original_image = image
        self.resize_image()

    def resize_image(self, event=None):
        if self.original_image is None:
            return
        
        scale_percent = self.scale.get()
        width = int(self.original_image.shape[1] * scale_percent / 100)
        height = int(self.original_image.shape[0] * scale_percent / 100)
        dim = (width, height)
        
        resized_image = cv2.resize(self.original_image, dim, interpolation=cv2.INTER_LINEAR)
        self.image_container.load_image(resized_image)

class ImageSaver:
    def __init__(self, parent, image_container, top_frame):
        self.image_container = image_container
        self.save_button = tk.Button(top_frame, text='Save Image', command=self.save_image)
        self.save_button.pack(side=tk.LEFT, padx=5)

    def save_image(self):
        image = self.image_container.get_current_image()
        if image is None:
            return
        
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All Files", "*.*")])
        if file_path:
            Image.fromarray(image).save(file_path)


    