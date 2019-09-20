'''
Customization of look of Tkinter widgets
'''
import tkinter as tk
from tkinter import messagebox


class AppUI(tk.Frame):
    def __init__(self, master=None):
        # Initialize window
        super().__init__(master)
        self.master = master
        self.master.title('Window Title')

        # Center window
        self.master.eval('tk::PlaceWindow %s center'
                         % self.master.winfo_toplevel())

        # Area widgets will be placed
        self.pack(fill=tk.BOTH, expand=1)

        # Create the widgets
        self.__create_widgets()

    def __create_widgets(self):
        # Initialize buttons
        self.exit_btn = tk.Button(self,
                                  text='Exit',
                                  command=self.master.destroy,
                                  activeforeground='red',
                                  activebackground='black',
                                  bg='white',
                                  fg='green')

        self.msg_btn = tk.Button(self)
        self.msg_btn['text'] = 'A Message!'
        self.msg_btn['command'] = self.__show_message
        self.msg_btn['bg'] = 'blue'
        self.msg_btn['pady'] = 20
        self.msg_btn['relief'] = tk.RAISED

        # Place widgets
        self.exit_btn.pack(fill=tk.X, side='bottom')
        self.msg_btn.pack(side='top')

    def __show_message(self):
        messagebox.showinfo(title='Message!', message='Hi!')


if __name__ == '__main__':
    root = tk.Tk()
    app = AppUI(master=root)
    app.mainloop()
