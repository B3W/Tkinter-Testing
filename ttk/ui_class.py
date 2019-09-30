'''
Demonstrates use of objects in Tkinter UI development
'''
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class ApplicationUI(ttk.Frame):

    def __init__(self, master=None):
        # Initialize root window
        super().__init__(master)
        self.master = master

        # Widget placement manager
        self.pack()

        # Create the widgets
        self.__create_widgets()

    def __create_widgets(self):
        # Initialize buttons
        self.exit_btn = ttk.Button(self,
                                   text='Exit',
                                   command=self.master.destroy)

        self.msg_btn = ttk.Button(self)
        self.msg_btn['text'] = 'A Message!'
        self.msg_btn['command'] = self.__show_message

        # Place buttons
        self.exit_btn.pack(side='bottom')
        self.msg_btn.pack(side='top')

    def __show_message(self):
        messagebox.showinfo(title='Message!', message='Hi!')


if __name__ == '__main__':
    root = tk.Tk()
    app = ApplicationUI(master=root)
    app.mainloop()
