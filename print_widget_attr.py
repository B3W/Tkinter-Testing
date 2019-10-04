'''
Prints all attributes for the inputted widget if it exists
'''
import tkinter as tk
from tkinter import ttk

ATTR_COL_WIDTH = 20
TYPE_COL_WIDTH = 30
TK_MAP = {
    'button': tk.Button,
    'canvas': tk.Canvas,
    'checkbutton': tk.Checkbutton,
    'entry': tk.Entry,
    'frame': tk.Frame,
    'label': tk.Label,
    'labelframe': tk.LabelFrame,
    'menu': tk.Menu,
    'menubutton': tk.Menubutton,
    'message': tk.Message,
    'optionmenu': tk.OptionMenu,
    'panedwindow': tk.PanedWindow,
    'radiobutton': tk.Radiobutton,
    'scale': tk.Scale,
    'scrollbar': tk.Scrollbar,
    'text': tk.Text,
    'toplevel': tk.Toplevel,
}
TTK_MAP = {
    'button': ttk.Button,
    'checkbutton': ttk.Checkbutton,
    'combobox': ttk.Combobox,
    'entry': ttk.Entry,
    'frame': ttk.Frame,
    'label': ttk.Label,
    'labelframe': ttk.LabelFrame,
    'labeledscale': ttk.LabeledScale,
    'menubutton': ttk.Menubutton,
    'notebook': ttk.Notebook,
    'optionmenu': ttk.OptionMenu,
    'panedwindow': ttk.PanedWindow,
    'progressbar': ttk.Progressbar,
    'radiobutton': ttk.Radiobutton,
    'scale': ttk.Scale,
    'scrollbar': ttk.Scrollbar,
    'separator': ttk.Separator,
    'sizegrip': ttk.Sizegrip,
    'treeview': ttk.Treeview
}


def print_attributes(widget_class):
    # Get all attribute keys for widget
    widget_instance = widget_class()
    keys = widget_instance.keys()

    # Print out the attribute keys with corresponding values
    attr_fmt = 'Attribute: {:<%d}' % ATTR_COL_WIDTH
    type_fmt = 'Type: {:<%d}' % TYPE_COL_WIDTH

    for key in keys:
        val = widget_instance[key]
        val_type = type(val)
        print('%s %s Value: %s' % (attr_fmt.format(key),
                                   type_fmt.format(str(val_type)),
                                   val))


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()

    # Add required positional argument for passing kml file and outfile name
    parser.add_argument('widget', type=str,
                        help='Widget to display attributes'
                        ' for (format: [t[t]k.]widget)')

    # Add optional conversion type flag arguments
    parser.add_argument('-n', '--non_themed', action='store_true',
                        help='Print attributes of non-themed Tk widget')

    # Parse arguments
    args = parser.parse_args()

    widget = args.widget.lower()
    non_themed = args.non_themed
    dot_pos = None

    try:
        dot_pos = widget.index('.')
        widget = widget[dot_pos + 1:]

    except ValueError:
        pass

    # Check if entered widget was prefixed with 'tk' or 'ttk'
    # Ignore the prefix if 'non_themed' was specified
    if not non_themed and dot_pos:
        if dot_pos == len('tk'):
            non_themed = True

        elif dot_pos == len('ttk'):
            non_themed = False

        else:
            print('Invalid widget: %s' % widget)
            exit(-1)

    widget_class = None

    if non_themed:
        try:
            widget_class = TK_MAP[widget]
        except KeyError:
            print('No tk widget named \'%s\'' % widget)
            exit(-1)

        print('Attribute definitions for TK widget: \'%s\'\n' % widget)

    else:
        try:
            widget_class = TTK_MAP[widget]
        except KeyError:
            print('No ttk widget named \'%s\'' % widget)
            exit(-1)

        print('Attribute definitions for TTK widget: \'%s\'\n' % widget)

    print_attributes(widget_class)
