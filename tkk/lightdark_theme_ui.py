'''
Example UI demonstrating light/dark style switching.
Clunky but provides granular control over each widget's style.
Better than manually changing each widget's style via 'widget.configure' call.
'''
import tkinter as tk
from tkinter import ttk


class Styler(object):
    _DARK_DARK = '#000000'
    _DARK = '#1B1B1B'
    _LIGHT_DARK = '#2B2B2B'
    _DARK_GREY = '#4B4B4B'
    _GREY = '#5B5B5B'
    _LIGHT_GREY = '#BBBBBB'
    _DARK_LIGHT = '#CCCCCC'
    _LIGHT = '#DDDDDD'
    _LIGHT_LIGHT = '#FFFFFF'

    def __init__(self):
        self._style = ttk.Style()

        # { 'style_name': func_to_configure_style }
        self._style_map = {
            'light': self.__configure_light,
            'dark': self.__configure_dark
        }

        # Tuple of all available styles provided by Styler
        self.style_options = tuple(self._style_map)

        self.active_style = None

    def configure(self, style):
        '''
        Raises key error if an invalid style is passed
        '''
        configure_func = self._style_map[style]
        configure_func()

        self.active_style = style

    def __configure_light(self):
        # Frames
        self._style.configure('TFrame',
                              background=Styler._LIGHT)

        # Buttons (use bordercolor to color Button border)
        self._style.configure('TButton',
                              background=Styler._DARK_LIGHT,
                              foreground=Styler._DARK_DARK)

        self._style.map('TButton', background=[('active', Styler._LIGHT)])

        # Labels
        self._style.configure('TLabel',
                              background=Styler._LIGHT,
                              foreground=Styler._DARK_DARK)

        # Check boxes
        self._style.configure('TCheckbutton',
                              background=Styler._LIGHT,
                              foreground=Styler._DARK_DARK)

        self._style.map('TCheckbutton',
                        background=[('active', Styler._DARK_LIGHT)])

        # OptionMenus
        self._style.configure('TMenubutton',
                              background=Styler._LIGHT,
                              foreground=Styler._DARK_DARK)

        self._style.map('TMenubutton',
                        background=[('hover', Styler._DARK_LIGHT)])

        # Entries
        self._style.configure('TEntry',
                              fieldbackground=Styler._LIGHT_LIGHT,
                              foreground=Styler._DARK_DARK)

    def __configure_dark(self):
        # Frames
        self._style.configure('TFrame',
                              background=Styler._GREY)

        # Buttons
        self._style.configure('TButton',
                              background=Styler._DARK,
                              foreground=Styler._LIGHT)

        self._style.map('TButton',
                        background=[('active', Styler._LIGHT_GREY)])

        # Labels
        self._style.configure('TLabel',
                              background=Styler._GREY,
                              foreground=Styler._LIGHT)

        # Check boxes
        self._style.configure('TCheckbutton',
                              background=Styler._GREY,
                              foreground=Styler._LIGHT)

        self._style.map('TCheckbutton',
                        background=[('active', Styler._LIGHT_GREY)])

        # OptionMenus
        self._style.configure('TMenubutton',
                              background=Styler._DARK_GREY,
                              foreground=Styler._LIGHT)

        self._style.map('TMenubutton',
                        background=[('active', Styler._GREY)])

        # Entries
        self._style.configure('TEntry',
                              fieldbackground=Styler._DARK_GREY,
                              foreground=Styler._LIGHT_LIGHT)


class MainUI(ttk.Frame):
    # 'clam' should be OS agnostic
    _TARGET_THM = 'clam'

    def __init__(self, master, *args, **kwargs):
        # Used for configuring styles/themes
        self.style = ttk.Style()
        self.available_themes = self.style.theme_names()

        # Initialize root window
        ttk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.title('Light/Dark UI')

        # Set the theme for the Tkinter application
        if MainUI._TARGET_THM in self.style.theme_names():
            self.style.theme_use(MainUI._TARGET_THM)

        # Object for configuring styles
        self.styler = Styler()
        self.styler.configure('light')

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
        self.thm_val = tk.StringVar(value=self.styler.style_options[0])

        # NOTE  Make sure to specify 'default' argument or it will mess up
        #       the available values in the option list
        thm_box = ttk.OptionMenu(self, self.thm_val,
                                 self.styler.style_options[0],
                                 *self.styler.style_options,
                                 command=self.__on_option_select)

        entry_lbl = ttk.Label(self, text='Entry')
        entry = ttk.Entry(self)

        # Place
        thm_lbl.grid(column=0, row=0, sticky=(tk.E,))
        thm_box.grid(column=1, row=0)
        chkbx.grid(column=2, row=0)
        lbl.grid(column=3, row=0, sticky=(tk.E,))
        btn.grid(column=4, row=0)

        entry_lbl.grid(column=0, row=1)
        entry.grid(column=1, row=1, columnspan=4, sticky=(tk.E, tk.W))

    # CALLBACKS
    def __on_option_select(self, val):
        self.styler.configure(val)


if __name__ == '__main__':
    root = tk.Tk()
    app_ui = MainUI(root)
    app_ui.mainloop()
