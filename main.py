# HIT 137 Assignment 3 
# Group Name: CAS/DAN 1
# Group Members:
# Lee Potter - S368675
# Sahil Badgal - S384037
# Jaafar Mehydeen - S367627


import tkinter as tk


class Application(tk.Frame):
    
    def __init__(self, master):
        super().__init__(master)
        master.title('HIT137 Assignment 3 - Image Editor')


root = tk.Tk()
app = Application(master=root)
app.mainloop()

