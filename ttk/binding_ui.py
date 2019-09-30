'''
UI demonstrating events and binding functions to them
'''
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class AppUI(ttk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        # Initialize root window
        ttk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.title('UI w/ Binding')

        # Center window
        self.master.eval('tk::PlaceWindow %s center'
                         % self.master.winfo_toplevel())

        # Area widgets will be placed
        self.pack(fill=tk.BOTH, expand=1)

        # Used for configuring styles
        self.style = ttk.Style()

        self.__create_widgets()  # Create widgets
        self.__register_handlers()  # Register event handlers for root window

    def __create_widgets(self):
        # Configure default style for buttons
        self.style.configure('TButton',
                             background='light blue',
                             foreground='green',
                             pady=5)

        # Dynamic styling with mapping -> (state, value)
        self.style.map('TButton',
                       background=[('pressed', 'red')])

        # Initialize buttons
        self.exit_btn = ttk.Button(self,
                                   text='Exit',
                                   command=self.__window_close_callback)

        self.msg_btn = ttk.Button(self)
        self.msg_btn['text'] = 'A Message!'
        self.msg_btn['command'] = self.__show_message

        # Place buttons
        self.exit_btn.pack(fill=tk.X, side='bottom')
        self.msg_btn.pack(pady=10, side='top')

    def __show_message(self):
        messagebox.showinfo(title='Message!', message='Hi!')

    def __register_handlers(self):
        # Handler for window close request
        self.master.protocol('WM_DELETE_WINDOW', self.__window_close_callback)

        # Handler for 'ESC' key
        self.master.bind('<Escape>', self.__window_close_callback)

    # CALLBACKS
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
    app_ui = AppUI(master=root)
    app_ui.mainloop()
