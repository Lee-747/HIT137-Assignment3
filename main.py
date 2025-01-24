# HIT 137 Assignment 3 
# Group Name: CAS/DAN 1
# Group Members:
# Lee Potter - S368675
# Sahil Badgal - S384037
# Jaafar Mehydeen - S367627


import tkinter as tk


class ImageEditorApp():
    
    def __init__(self, root):
        self.root = root
        self.root.title('HIT137 Assignment 3 - Image Editor')
        self.root.geometry('1200x800')



root = tk.Tk()
app = ImageEditorApp(root)
root.mainloop()

