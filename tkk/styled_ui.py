'''
Customization of look of Themed Tkinter widgets
'''
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class AppUI(ttk.Frame):

    def __init__(self, master=None):
        # Initialize root window
        super().__init__(master)
        self.master = master
        self.master.title('Window')

        # Center window
        self.master.eval('tk::PlaceWindow %s center'
                         % self.master.winfo_toplevel())

        # Area widgets will be placed
        self.pack(fill=tk.BOTH, expand=1)

        # Used for configuring styles
        self.style = ttk.Style()

        # Create the widgets
        self.__create_widgets()

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
                                   command=self.master.destroy)

        self.msg_btn = ttk.Button(self)
        self.msg_btn['text'] = 'A Message!'
        self.msg_btn['command'] = self.__show_message

        # Place buttons
        self.exit_btn.pack(fill=tk.X, side='bottom')
        self.msg_btn.pack(pady=10, side='top')

    def __show_message(self):
        messagebox.showinfo(title='Message!', message='Hi!')


if __name__ == '__main__':
    root = tk.Tk()
    app = AppUI(master=root)
    app.mainloop()
