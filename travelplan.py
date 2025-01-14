import tkinter as tk
from tkinter import ttk
from tkcalendar import calendar

#add a calander event
def add_event():
    selected_date = cal.get_date()
    event = event_entry.get()
    if selected_date and event:
        event_calendar.insert(
            " ",
            "end"
            values=(selected_date,event))
        event_entry.delete(0,"end") 

#delete selected event
def delete_event():
    selected_item= event_calendar.seletion()
    if selected_item:
        event_calendar.delete(selected_item)      

# main window
root = tk.Tk()
root.title("Travel Planner") 
root.geometry("600x600")

#Header
header_frame = tk.Frame(root, bg="#3498db")
header_frame.pack(fill="x")

header_label = tk.Label(
    text= "Travel Planner"
    font= ("Helvetica",24),
    bg="#3498db",
    fg="white")
header_label.pack(pady=10)

#Calendar widget
cal= calendar(
    root,
    selectmode="day",
    date_pattern= "mm-dd-yyyy",
    font= ("Helvetica",16),
    background="white",
    forgeground="black"
)
cal.pack(pady=20, padx=10)

#input fields
event_frame = tk.Frame(root)
event_frame.pack(pady=10)

event_label = tk.Label(
    event_frame,
    text="Event:",
    font=("Helvetica",16)
)
event_label.grid(row=0,column=0)

event_entry= tk.Entry(
    event_frame,
    font=("Helvetica",16)
)
event_entry.grid(row=0, column=1)

add_button = tk.Button(
    event_frame,
    text="Add Event",
    command= add_event,
    font=("Helvetica", 16),
    bg="#2ecc71",
    fg="white")
add_button.grid(row=0, column=2,pradx=10)

delete_button= tk.Button(
    event_frame,
    text="Delete Event",
    command= delete_event,
    ont=("Helvetica", 16),
    bg="#e74c3c",
    fg="white")
delete_button.grid(row=0,column=3)

#Event Listbox
event_calendar = ttk.Treeview(
    root,
    columns= ("Date", "Event"),
    show="headings",
    selectmode="browse",
    height=10
)

event_calendar.heading("Date", text="Date", anchor="center")
event_calendar.heading("Event", text= "Event", anchor="center")
event_calendar.column("Date", width=150, anchor="center")
event_calendar.column("Event", width=400, anchor="center")
event_calendar.pack(padx=10,pady=20)

#main loop
root.mainlop()
