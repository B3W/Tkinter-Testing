'''
Example UI demonstrating theme switching
'''
import tkinter as tk
from tkinter import ttk


class MainUI(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        # Used for configuring styles/themes
        self.style = ttk.Style()
        self.available_themes = self.style.theme_names()

        # Initialize root window
        ttk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.title('Themed UI')

        # List for Theme OptionMenu
        # The initial themes in list are not OS dependent
        xplatform_thm_list = ['default', 'alt', 'clam', 'classic']

        if self.style.theme_use() not in xplatform_thm_list:
            # Put the currently used theme at the front of list
            xplatform_thm_list.insert(0, self.style.theme_use())

        self.valid_themes = tuple(xplatform_thm_list)

        # Center window
        self.master.eval('tk::PlaceWindow %s center'
                         % self.master.winfo_toplevel())

        # Configure root window grid
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.minsize(width=350, height=150)

        # Configure root Frame grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=3)
        self.columnconfigure(3, weight=4)
        self.columnconfigure(4, weight=5)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # Place root frame in root window
        self.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))

        # Create widgets
        self.__create_widgets()

    def __create_widgets(self):
        # Create
        btn = ttk.Button(self, text='Button')
        lbl = ttk.Label(self, text='Label')

        self.chkvar = tk.BooleanVar(value=False)
        chkbx = ttk.Checkbutton(self, text='Checkbutton',
                                variable=self.chkvar, onvalue=True)

        thm_lbl = ttk.Label(self, text='Theme')
        self.thm_val = tk.StringVar(value=self.valid_themes[0])

        # NOTE  Make sure to specify 'default' argument or it will mess up
        #       the available values in the option list
        thm_box = ttk.OptionMenu(self, self.thm_val, self.valid_themes[0],
                                 *self.valid_themes,
                                 command=self.__on_option_select)

        entry_lbl = ttk.Label(self, text='Entry')
        entry = ttk.Entry(self)

        # Place
        thm_lbl.grid(column=0, row=0)
        thm_box.grid(column=1, row=0)
        chkbx.grid(column=2, row=0)
        lbl.grid(column=3, row=0)
        btn.grid(column=4, row=0)

        entry_lbl.grid(column=0, row=1)
        entry.grid(column=1, row=1, columnspan=4, sticky=(tk.E, tk.W))

    # CALLBACKS
    def __on_option_select(self, val):
        if val in self.available_themes:
            self.style.theme_use(val)


if __name__ == '__main__':
    root = tk.Tk()
    app_ui = MainUI(root)
    app_ui.mainloop()
