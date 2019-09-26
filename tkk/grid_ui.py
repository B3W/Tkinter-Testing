'''
Example demonstrating Tkinter's grid manager
'''
import tkinter as tk
from tkinter import ttk


class MainUI(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        # Initialize root window
        ttk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.title('Grid UI')

        self.col_cnt = 3  # Number of cols/rows in demo
        self.row_cnt = 3

        # Center window
        self.master.eval('tk::PlaceWindow %s center'
                         % self.master.winfo_toplevel())

        # Configure root window grid
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.minsize(width=250, height=250)

        # Configure root frame grid
        weight = 1
        for col in range(self.col_cnt):
            self.columnconfigure(col, weight=weight)
            weight += 2

        weight = 1
        for row in range(self.row_cnt):
            self.rowconfigure(row, weight=weight)
            weight += 1

        # Place root frame in root window
        self.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))

        self.__create_frames()

    def __create_frames(self):
        for col in range(self.col_cnt):
            for row in range(self.row_cnt):
                frame = tk.Frame(self, bd=2, relief=tk.GROOVE)
                frame.grid(column=col, row=row,
                           sticky=(tk.N, tk.S, tk.E, tk.W))


if __name__ == '__main__':
    root = tk.Tk()
    app_ui = MainUI(root)
    app_ui.mainloop()
