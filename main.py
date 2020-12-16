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

#Create root window size 720x480, set title
root = tk.Tk()
root.geometry("720x480")
root.title('ICS 32 Appointment')

# adding this option removes some legacy behavior with menus that modern OSes don't support.
# If you're curious, feel free to comment out and see how the menu changes.
# This is from our professor :D
root.option_add('*tearOff', False)


cal_frame = tk.Frame(master=root, width=250)
cal_frame.pack(fill=tk.BOTH, side=tk.LEFT) = tk.frame
def print_sel():
    print(cal.selection_get())
    cal.see(datetime.date(year=2020, month=2, day=5))


cal = Calendar(root, font="Arial 14", foreground="green", selectbackground="red", selectforeground = "green" ,selectmode='day', year=int(this_year), month=int(this_month), day=int(this_day))
cal.pack(fill="both", expand=True)

# Remove week number
for i in range(6):
    cal._week_nbs[i].destroy()

# Button to get date
ttk.Button(root, text="ok", command=print_sel).pack()

root.mainloop()
