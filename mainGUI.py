from tkcalendar import Calendar, DateEntry

try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk
import datetime

date = datetime.date.today()
print("Today is:", date)
this_day = f"{date:%d}"
this_month = f"{date:%m}"
this_year = f"{date:%Y}"


def new_patient():
    pass


def new_appointment():
    pass


# ********
# ******** THE MAIN FRAME OF PROGRAM AREA ********
# Create root/main window with size 720x480. Set title and other config


# ========= MY CALENDAR WILL BE DISPLAY HERE ===============
class Cal_frame(tk.Frame):
    def __init__(self, root, select_callback=None):
        tk.Frame.__init__(self, root)
        self.root = root
        self._select_callback = select_callback

        # After all initialization is complete, call the _draw method to pack the widgets
        # into the Body instance
        self._draw()



    def reset_ui(self):
        pass


    """
    Draw stuff in my calendar section
    """

    def _draw(self):
        cal_frame = tk.Frame(master=self, width=250)
        cal_frame.pack(fill=tk.BOTH, side=tk.LEFT)
        self.calendar = Calendar(self, font="Arial 14", foreground="green", selectbackground="red",
                                 selectforeground="green",
                                 selectmode='day', year=int(this_year), month=int(this_month), day=int(this_day))
        self.calendar.pack(fill="both", expand=True)

        entry_frame = tk.Frame(master=self, bg="")
        entry_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        editor_frame = tk.Frame(master=entry_frame, bg="red")
        editor_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        scroll_frame = tk.Frame(master=entry_frame, bg="blue", width=10)
        scroll_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)

        self.entry_editor = tk.Text(editor_frame, width=0)
        self.entry_editor.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=0, pady=0)

        entry_editor_scrollbar = tk.Scrollbar(master=scroll_frame, command=self.entry_editor.yview)
        self.entry_editor['yscrollcommand'] = entry_editor_scrollbar.set
        entry_editor_scrollbar.pack(fill=tk.Y, side=tk.LEFT, expand=False, padx=0, pady=0)




# Button to get date

# ========= APPOINTMENT AREA ===============

# ========= FOOTER / BUTTON AREA ===============

class MainApp(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        self._draw()

    def _draw(self):
        # Build a menu and add it to the root frame.
        menu_bar = tk.Menu(self.root)
        self.root['menu'] = menu_bar
        menu_file = tk.Menu(menu_bar)
        menu_bar.add_cascade(menu=menu_file, label='File')
        menu_file.add_command(label='New Patient', command=self.new_patient)
        menu_file.add_command(label='New Appointment', command=self.new_appointment)
        menu_file.add_command(label='Close', command=self.close)

        self.calendar = Cal_frame(self.root)
        self.calendar.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

    def print_sel(self, frame:tk.Frame):
        print(frame.selection_get())
        return frame.selection_get()

    def new_patient(self):
        pass

    def new_appointment(self):
        pass

    def close(self):
        self.root.destroy()


if __name__ == "__main__":
    main = tk.Tk()
    main.geometry("720x480")
    main.title('ICS 32 Appointment')
    main.option_add('*tearOff', False)
    MainApp(main)
    main.update()
    main.minsize(main.winfo_width(), main.winfo_height())
    main.mainloop()
