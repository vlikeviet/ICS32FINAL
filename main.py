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
root = tk.Tk()
root.geometry("720x480")
root.title('ICS 32 Appointment')

# adding this option removes some legacy behavior with menus that modern OSes don't support.
# If you're curious, feel free to comment out and see how the menu changes.
# This is from our professor :D
root.option_add('*tearOff', False)
# ========= TOP MENU AREA ===============

menu_bar = tk.Menu(root)
root['menu'] = menu_bar
menu_file = tk.Menu(menu_bar)
menu_bar.add_cascade(menu=menu_file, label='File')
menu_file.add_command(label='New Patient', command=new_patient)
menu_file.add_command(label='New Appointment', command=new_appointment)

# ========= CALENDAR AREA ===============
cal_frame = tk.Frame(master=root, width=250)


def print_sel():
    print(cal.selection_get())


cal = Calendar(root, font="Arial 14", foreground="green", selectbackground="red", selectforeground="green",
               selectmode='day', year=int(this_year), month=int(this_month), day=int(this_day))
cal.pack(fill="both", expand=True)



# Button to get date

# ========= APPOINTMENT AREA ===============

# ========= FOOTER / BUTTON AREA ===============

ttk.Button(root, text="ok", command=print_sel).pack()

root.mainloop()
