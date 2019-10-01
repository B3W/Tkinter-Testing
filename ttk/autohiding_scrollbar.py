'''
Demonstrates an autohiding scrollbar
'''
import tkinter as tk
from tkinter import ttk


class AutoScrollbar(ttk.Scrollbar):
    '''
    A scrollbar that hides itself if it's not needed. Only
    works if you use the pack geometry manager.
    Reference: https://stackoverflow.com/q/57030781
    '''
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            self.pack_forget()
        else:
            if self.cget("orient") == tk.HORIZONTAL:
                self.pack(side=tk.BOTTOM, fill=tk.X)
            else:
                self.pack(side=tk.RIGHT, fill=tk.Y)

        ttk.Scrollbar.set(self, lo, hi)

    def grid(self, **kw):
        raise(tk.TclError, "cannot use grid with this widget")

    def place(self, **kw):
        raise(tk.TclError, "cannot use place with this widget")


# class AutoScrollbar(ttk.Scrollbar):
#     '''
#     A scrollbar that hides itself if it's not needed. Only
#     works if you use the grid geometry manager.
#     Reference: https://stackoverflow.com/q/41095385
#     '''
#     def set(self, lo, hi):
#         if float(lo) <= 0.0 and float(hi) >= 1.0:
#             self.grid_forget()
#         else:
#             self.grid()

#         ttk.Scrollbar.set(self, lo, hi)

#     def pack(self, **kw):
#         raise(tk.TclError, "cannot use pack with this widget")

#     def place(self, **kw):
#         raise(tk.TclError, "cannot use place with this widget")


class MainUI(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        # Initialize root window
        ttk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.title('Autohiding Scrollbar UI')

        # Center window
        self.master.eval('tk::PlaceWindow %s center'
                         % self.master.winfo_toplevel())

        # Root window grid
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.minsize(width=200, height=50)

        # Root frame grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # Place root frame
        self.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))

        # Frame for listbox/scrollbar
        frame = ttk.Frame(self)
        frame.grid(column=0, row=0, rowspan=2, sticky=(tk.N, tk.S, tk.E, tk.W))

        # Create vertical scrollbar
        self.yscroller = AutoScrollbar(master=frame, orient=tk.VERTICAL)

        # Create list box with scrollbar
        self.list_box = tk.Listbox(master=frame,
                                   yscrollcommand=self.yscroller.set,
                                   selectmode=tk.BROWSE,
                                   bg='#2B2B2B', fg='#FFFFFF',
                                   relief=tk.FLAT, bd=0,
                                   highlightthickness=0,
                                   activestyle=tk.NONE)

        self.list_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Link vertical scrollbar to listbox
        self.yscroller.configure(command=self.list_box.yview)

        # Buttons to add/del items to/from list box
        add_btn = ttk.Button(self, text='Add Item',
                             command=lambda: self.list_box.insert(tk.END,
                                                                  'ITEM'))
        add_btn.grid(column=1, row=0)

        del_btn = ttk.Button(self, text='Delete Item',
                             command=lambda: self.list_box.delete(tk.END))
        del_btn.grid(column=1, row=1)


if __name__ == '__main__':
    root = tk.Tk()
    app_ui = MainUI(root)
    app_ui.mainloop()
