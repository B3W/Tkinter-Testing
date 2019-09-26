'''
Module showing how to organize/structure UI with multiple sections
'''
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class MenuBar(tk.Menu):
    def __init__(self, master, exit_callback, *args, **kwargs):
        # Initialize Menu Bar to place menus into
        tk.Menu.__init__(self, master, *args, **kwargs)
        self.master = master
        self.exit_callback = exit_callback

        self.__create_menu()  # Create menu widgets

    def __create_menu(self):
        # Create file menu
        self.file_menu = tk.Menu(master=self, tearoff=False)

        # TODO Add file menu items (order matters)
        self.file_menu.add_command(label='Exit', command=self.exit_callback)

        # Create help menu
        self.help_menu = tk.Menu(master=self, tearoff=False)

        # TODO Add help menu items (order matters)
        self.help_menu.add_command(label='About')

        # Add menus to menu bar (order added == left-to-right order)
        self.add_cascade(label='File', menu=self.file_menu)
        self.add_cascade(label='Help', menu=self.help_menu)


class SideBar(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        # Initialize frame
        ttk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master

        self.pack(fill=tk.BOTH, expand=True)  # Let widgets occupy entire frame
        self.__create_sidebar()

    def __create_sidebar(self):
        pass


class MainUI(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        # Initialize root window
        ttk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.title('UI w/ Binding')

        # Center window
        self.master.eval('tk::PlaceWindow %s center'
                         % self.master.winfo_toplevel())

        # Used for configuring styles
        self.style = ttk.Style()

        # Configure area UI components will be placed into
        self.pack(fill=tk.BOTH, expand=True)

        # Initialize individual components of the main UI
        self.menu_bar = MenuBar(self.master, self.__window_close_callback)
        self.master.configure(menu=self.menu_bar)
        self.side_bar = SideBar(self)

        # Register event handlers for root window
        self.__register_handlers()

        # TODO Place components in the main window
        self.side_bar.pack(side=tk.LEFT, fill=tk.Y)

    def __register_handlers(self):
        # Handler for window close request
        self.master.protocol('WM_DELETE_WINDOW', self.__window_close_callback)

        # Handler for 'ESC' key
        self.master.bind('<Escape>', self.__window_close_callback)

    # Root window CALLBACKS
    def __window_close_callback(self, event=None):
        '''
        Confirms window close
        'protocol'/'command' pass no argument to callback
        'bind' passes an event argument to the callback
        '''
        if messagebox.askokcancel('Quit', 'Close Window?'):
            self.master.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    app_ui = MainUI(root)
    app_ui.mainloop()
