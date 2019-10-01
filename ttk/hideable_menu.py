'''
Show/Hide the window menu with 'Control-+'
'''
import tkinter as tk
from tkinter import ttk


class MenuBar(tk.Menu):
    def __init__(self, master, exit_callback, *args, **kwargs):
        # Initialize Menu Bar to place menus into
        tk.Menu.__init__(self, master, *args, **kwargs)
        self.master = master

        self.__create_menu(exit_callback)  # Create menu widgets

    def __create_menu(self, exit_callback):
        # Create file menu
        self.file_menu = tk.Menu(master=self, tearoff=False)

        # TODO Add file menu items (order matters)
        self.file_menu.add_command(label='Exit', command=exit_callback)

        # Create help menu
        self.help_menu = tk.Menu(master=self, tearoff=False)

        # TODO Add help menu items (order matters)
        self.help_menu.add_command(label='About')

        # Add menus to menu bar (order added == left-to-right order)
        self.add_cascade(label='File', menu=self.file_menu)
        self.add_cascade(label='Help', menu=self.help_menu)


class MainUI(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        # Initialize root window
        ttk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.title('Hiding Menu UI')

        # Center window
        self.master.eval('tk::PlaceWindow %s center'
                         % self.master.winfo_toplevel())

        # Root window grid
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.minsize(width=250, height=150)

        # Root frame grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # Place root frame
        self.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))

        # Dummy labels
        lbl1 = ttk.Label(self, text='Label1')
        lbl1.grid(column=0, row=0)
        lbl2 = ttk.Label(self, text='Label2')
        lbl2.grid(column=1, row=0)

        # Window menu
        self.menu_bar = MenuBar(self.master, self.master.destroy)

        # Initialize menu state
        self.menu_visible = False  # Flag tracking menu visibility
        self.hidden_menu = tk.Menu(self.master)  # Empty menu (hides menu)
        self.master.configure(menu=self.hidden_menu)  # No menu to start

        # Show/Hide menu key handler
        self.master.bind('<Control-+>',
                         self.__inverse_menu_state_callback)

    # CALLBACKS
    def __inverse_menu_state_callback(self, event):
        if self.menu_visible:
            # Hide
            self.master.configure(menu=self.hidden_menu)
            self.menu_visible = False

        else:
            # Show
            self.master.configure(menu=self.menu_bar)
            self.menu_visible = True


if __name__ == '__main__':
    root = tk.Tk()
    app_ui = MainUI(root)
    app_ui.mainloop()
