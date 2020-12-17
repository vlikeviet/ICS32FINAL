from tkcalendar import Calendar, DateEntry
from Appointments import *
from Patient import *
import os

try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk
import datetime

patient_data_file = os.path.dirname(os.path.realpath(__file__))+"/patient.pat"
appointment_data_file = os.path.dirname(os.path.realpath(__file__))+"/appointment.apt"


date = datetime.date.today()
print("Today is:", date)
this_day = f"{date:%d}"
this_month = f"{date:%m}"
this_year = f"{date:%Y}"

patient_file_path = "database/patient.pat"
appointment_file_path = "database/appointment.apt"


def new_patient():
    print("CREATE NEW PATIENT")
    my_patient = Patient()
    my_patient._fname = input("First name: ")
    my_patient._lname = input("Last name: ")
    my_patient._id = input("Patient ID: ")
    my_patient._symptom = input("Symptom: ")

    print(my_patient.patient_info())
    my_patient.save_patient(patient_data_file)

def new_appointment():
    apt_obj = Appointments()
    apt_obj.app_number = input("Appointment Number: ")
    apt_obj.app_time = input("Appointment Time: ")
    apt_obj.patient_ID = input("Patient ID: ")
    apt_obj.room = input("Room: ")

    # set treatment in each appointment
    treatment_obj = Treatment()
    treatment_obj.treatment = input("Treatment: ")
    treatment_obj.fee = input("Fee: ")
    treatment_obj.length = input("How long will it take?: ")
    apt_obj.add_treatment(treatment_obj)

    apt_obj.save_appointment(appointment_data_file)




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

    def print_sel(self):
        print(self.calendar.selection_get())

    """
    Draw stuff in my calendar section
    """

    def _draw(self):
        # I marked it in the blue area
        appointment_details_frame = tk.Frame(master=self, width=360, bg="Skyblue", padx=0, pady=0)
        appointment_details_frame.pack(fill=tk.BOTH, side=tk.RIGHT)
        # lbl_header = tk.Label(appointment_details_frame, text="Hello!", font=("Arial Bold", 50))
        # lbl_header.pack(side=tk.TOP, expand=True)

        # I marked it in the green area
        patient_frame = tk.Frame(master=self, width="360", bg="lime")
        patient_frame.pack(fill=tk.BOTH, side=tk.TOP)
        self.posts_tree = ttk.Treeview(patient_frame)
        self.posts_tree.bind("<<TreeviewSelect>>", self.node_select)
        self.posts_tree.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=10, pady=10)

        # draw the calendar
        self.calendar = Calendar(self, font="Arial 14", foreground="green", selectbackground="red",
                                 selectforeground="green",
                                 selectmode='day', year=int(this_year), month=int(this_month), day=int(this_day),padx=10, pady=10)
        self.calendar.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        # Remove week number (B/C this calendar add-ons create extra column to count how many weeks in year. Just don't
        # worry about this)
        for i in range(6):
            self.calendar._week_nbs[i].destroy()

        btn_select = tk.Button(self, text="Select", command=self.print_sel, padx=10, pady=10, bg="pink")
        btn_select.pack(fill=tk.BOTH, side=tk.TOP)

        # txt = tk.Entry(patient_frame, width=10, text = "TEXT")
        # txt.pack()

        btn_patient = tk.Button(self, text="New Patient", command=new_patient, padx=10, pady=10, bg='lime')
        btn_patient.pack(fill=tk.BOTH, side=tk.LEFT)
        btn_appointment = tk.Button(self, text="New Appointment", command=new_appointment, padx=10, pady=10)
        btn_appointment.pack(fill=tk.BOTH, side=tk.LEFT)

        btn_appointment = tk.Button(self, text="Close program", command=self.close, padx=10, pady=10)
        btn_appointment.pack(fill=tk.BOTH, side=tk.LEFT)

    def node_select(self, event):
        index = int(self.posts_tree.selection()[0]) - 1  # selections are not 0-based, so subtract one.
        entry = self._posts[index].entry
        self.set_text_entry(entry)





    def close(self):
        self.root.destroy()

    def save_patient(self):
        pass


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
        menu_file.add_command(label='New Patient', command=new_patient)
        menu_file.add_command(label='New Appointment', command=new_appointment)
        menu_file.add_command(label='Close', command=self.close)

        self.calendar = Cal_frame(self.root)
        self.calendar.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

    def print_sel(self, frame:tk.Frame):
        print(frame.selection_get())
        return frame.selection_get()





    def close(self):
        self.root.destroy()


if __name__ == "__main__":
    main = tk.Tk()
    main.geometry("720x640")
    main.title('ICS 32 Appointment')
    main.option_add('*tearOff', False)
    MainApp(main)
    main.update()
    main.minsize(main.winfo_width(), main.winfo_height())
    main.mainloop()
