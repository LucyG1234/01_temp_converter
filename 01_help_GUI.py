from tkinter import *
from functools import partial  # to prevent unwanted windows

import random


class Convertor:
    def __init__(self, parent):

        # Formatting variables...
        background_color = "blue"

        # convertor Main screen GUI...
        self.converter_frame = Frame(width=300, height=300, bg=background_color, pady=10)
        self.converter_frame.grid()



        # Temperature conversion heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # help button (row 1)
        self.help_button = Button(self.converter_frame, text="help",
                                  font=("Arial", "14"),
                                  padx=10, pady=10)
        self.help_button.grid(row=1)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor(root)
    root.mainloop()
