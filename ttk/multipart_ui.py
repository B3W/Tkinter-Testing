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

        self.pack(fill=tk.BOTH)  # Let widgets occupy entire frame
        self.__create_sidebar()

    def __create_sidebar(self):
        # Listbox label
        self.item_label = ttk.Label(master=self,
                                    text='Listbox',
                                    style='DarkHeading.TLabel')

        self.item_label.pack(side=tk.TOP, fill=tk.X)

        # Create vertical scroll bar
        self.yscroller = ttk.Scrollbar(master=self, orient=tk.VERTICAL)
        self.yscroller.pack(side=tk.RIGHT, fill=tk.Y)

        # Create list box with scrollbar
        self.item_list = tk.Listbox(master=self,
                                    yscrollcommand=self.yscroller.set,
                                    selectmode=tk.BROWSE,
                                    bg='#2B2B2B', fg='#FFFFFF',
                                    relief=tk.FLAT, bd=0,
                                    highlightthickness=0,
                                    activestyle=tk.NONE)

        self.item_list.pack(side=tk.LEFT, fill=tk.BOTH)
        self.item_list.bind('<<ListboxSelect>>', SideBar.__on_select)

        # Link vertical scrollbar to listbox
        self.yscroller.configure(command=self.item_list.yview)

        # Populate list box
        for i in range(50):
            self.item_list.insert(tk.END, 'ITEM %d' % i)

    # CALLBACKS
    def __on_select(event):
        listbox = event.widget  # Event contains Listbox
        index = int(listbox.curselection()[0])  # Get selection
        value = listbox.get(index)
        print('Selected \'%s\' at index \'%d\'' % (value, index))


class MainArea(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        # Initialize frame
        ttk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master

        self.pack(fill=tk.BOTH, expand=True)  # Let widgets occupy entire frame


class MainUI(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        # Used for configuring styles
        self.style = ttk.Style()
        self.__configure_styles()

        # Initialize root window
        ttk.Frame.__init__(self, master, *args, **kwargs)
        self.configure(style='DarkMain.TFrame')
        self.master = master
        self.master.title('Multipart UI')

        # Center window
        self.master.eval('tk::PlaceWindow %s center'
                         % self.master.winfo_toplevel())

        # Configure area UI components will be placed into
        self.pack(fill=tk.BOTH, expand=True)

        # Initialize individual components of the main UI
        self.menu_bar = MenuBar(self.master, self.__window_close_callback)
        self.master.configure(menu=self.menu_bar)
        self.side_bar = SideBar(self, style='DarkNested.TFrame')
        self.main_area = MainArea(self, style='DarkNested.TFrame')

        # Register event handlers for root window
        self.__register_handlers()

        # TODO Place components in the main window
        self.side_bar.pack(side=tk.LEFT, fill=tk.Y)
        self.main_area.pack(side=tk.RIGHT, fill=tk.BOTH)

    def __configure_styles(self):
        # Style for main window frame
        self.style.configure('DarkMain.TFrame',
                             background='#2B2B2B')

        # Style for nested frames
        self.style.configure('DarkNested.TFrame',
                             background='#2B2B2B')

        # Style for nested frames
        self.style.configure('DarkHeading.TLabel',
                             background='#3B3B3B',
                             foreground='#FFFFFF',
                             font='tkDefaultFont 16',
                             anchor=tk.CENTER)

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
