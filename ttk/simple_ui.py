'''
Barebones example of Themed Tkinter UI
'''
import tkinter as tk
from tkinter import ttk

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Tkinter Example')
    lbl = ttk.Label(root, text='This is a label')
    lbl.pack()
    root.mainloop()
