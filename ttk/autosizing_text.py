'''
'''
import tkinter as tk
from tkinter import ttk


class AutosizingText(ttk.Frame):
    '''
    '''
    def __init__(self, master, *args, **kwargs):
        # Initialize root frame
        ttk.Frame.__init__(self, master, *args, **kwargs)
        self.pack(fill=tk.BOTH)

        # Initialize text widget
        self.text = tk.Text(self,
                            width=20, height=2,
                            relief=tk.GROOVE,
                            wrap=tk.WORD)
        self.text.pack(expand=True)

        # Logic for resizing the text widget to it's contents


class MainUI(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        # Initialize root window
        ttk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.title('Autosizing Text UI')

        # Center window
        self.master.eval('tk::PlaceWindow %s center'
                         % self.master.winfo_toplevel())

        # Root window grid
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.minsize(width=200, height=100)

        # Root frame grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # Place root frame
        self.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))

        # Autosizing text
        self.auto_text = AutosizingText(self)
        self.auto_text.grid(column=0, row=1)

        # Dummy widgets
        lbl = ttk.Label(self, text='Autosizing Text')
        lbl.grid(column=0, row=0)

        btn1 = ttk.Button(self, text='Enable/Disable',
                          command=self.__inverse_text_state)
        btn1.grid(column=1, row=0)

        btn2 = ttk.Button(self, text='Print Contents',
                          command=self.__print_text)
        btn2.grid(column=1, row=1)

    # CALLBACKS
    def __inverse_text_state(self):
        if self.auto_text.text.cget('state') == tk.NORMAL:
            self.auto_text.text.config(state=tk.DISABLED)
        else:
            self.auto_text.text.config(state=tk.NORMAL)

    def __print_text(self):
        print(self.auto_text.text.get(1.0, tk.END), end='')


if __name__ == '__main__':
    root = tk.Tk()
    app_ui = MainUI(root)
    app_ui.mainloop()
