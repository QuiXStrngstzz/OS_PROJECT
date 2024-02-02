from customtkinter import CTk, CTkLabel, CTkButton, CTkFrame, CTkEntry, CTkScrollableFrame
from Logic_processing import FCFS_sched, SJF_sched, STRF_sched, compare_burst_time, compare_arrival_time, Process, compare_remaining_burst_time
from tkinter import *
import customtkinter

count        = 1
processes    = []
        
def label(mstr, txt, fnt_size, TC, achr, expnd, pdy_T, pdy_B, pdx):
    label = CTkLabel(master =mstr, text = txt, font = ("Times New Roman", fnt_size), text_color = TC)
    label.pack(anchor = achr, expand = expnd, pady = (pdy_T, pdy_B), padx = pdx)
    
def inputs(At_input, BT_input):
    global count, added_p_frame, processes  # Use the global keyword for all variables
    arrival_time = int(At_input.get())
    burst_time = int(BT_input.get())

    process_label = CTkLabel(
        master=added_p_frame,
        text=f"ID: {count}    |    AT: {arrival_time}    |    BT: {burst_time}",
        font=("Times New Roman", 20)
    )
    process_label.pack(anchor="center")
    processes.append(Process(count, arrival_time, burst_time))
    count += 1
    
def fcfs_submit():
    global count
    for widget in result_frame.winfo_children():
        widget.destroy()
            
    result_list = FCFS_sched(processes)
    # Display the results in a formatted tabular format
    header = ["PID", "AT", "BT", "CT", "TT", "WT"]
    header_str = "    | ".join(f"{col:<5}" for col in header)
    result_label = CTkLabel(master=result_frame, text=header_str, font=("Times New Roman", 25), padx = 300)
    result_label.grid(row=0, column=0, sticky="w", pady=(0, 10))

    for row_idx, result in enumerate(result_list[:-1], start=1):  # Exclude the last entry (average turnaround and waiting times)
        data = [str(result[key]) for key in header]
        data_str = "      | ".join(f"{col:<5}" for col in data)
        result_label = CTkLabel(master=result_frame, text=data_str, font=("Times New Roman", 25), justify="center")
        result_label.grid(row=row_idx, column=0, sticky="w", pady=(0, 10), padx = 200)

    row_idx += 1
    average_label = CTkLabel(master=result_frame, text=f"Average Turnaround Time: {result_list[-1]['Average Turnaround Time']}", font=("Times New Roman", 25), justify="center", padx = 300)
    average_label.grid(row=row_idx, column=0, sticky="w", pady=(20, 10))

    row_idx += 1
    average_label = CTkLabel(master=result_frame, text=f"Average Waiting Time: {result_list[-1]['Average Waiting Time']}", font=("Times New Roman", 25), justify="center", padx = 300)
    average_label.grid(row=row_idx, column=0, sticky="w", pady=(0, 10))
    
    count = 1
    processes.clear()
    
def SJF_submit():
    global count
    for widget in result_frame.winfo_children():
        widget.destroy()
            
    result_list = SJF_sched(processes)
    # Display the results in a formatted tabular format
    header = ["PID", "AT", "BT", "CT", "TT", "WT"]
    header_str = "    | ".join(f"{col:<5}" for col in header)
    result_label = CTkLabel(master=result_frame, text=header_str, font=("Times New Roman", 25), padx = 300)
    result_label.grid(row=0, column=0, sticky="w", pady=(0, 10))

    for row_idx, result in enumerate(result_list[:-1], start=1):  # Exclude the last entry (average turnaround and waiting times)
        data = [str(result[key]) for key in header]
        data_str = "      | ".join(f"{col:<5}" for col in data)
        result_label = CTkLabel(master=result_frame, text=data_str, font=("Times New Roman", 25), justify="center")
        result_label.grid(row=row_idx, column=0, sticky="w", pady=(0, 10), padx = 200)

    # Display average turnaround and waiting times separately
    row_idx += 1
    average_label = CTkLabel(master=result_frame, text=f"Average Turnaround Time: {result_list[-1]['Average Turnaround Time']}", font=("Times New Roman", 25), justify="center", padx = 300)
    average_label.grid(row=row_idx, column=0, sticky="w", pady=(20, 10))

    row_idx += 1
    average_label = CTkLabel(master=result_frame, text=f"Average Waiting Time: {result_list[-1]['Average Waiting Time']}", font=("Times New Roman", 25), justify="center", padx = 300)
    average_label.grid(row=row_idx, column=0, sticky="w", pady=(0, 10))
    
    count = 1
    processes.clear()

def STRF_submit():
    global count
    for widget in result_frame.winfo_children():
        widget.destroy()

    row_idx = 0  # Initialize row_idx here

    result_list = STRF_sched(processes)
    # Display the results in a formatted tabular format
    header = ["PID", "AT", "BT", "CT", "TT", "WT"]
    header_str = "    | ".join(f"{col:<5}" for col in header)
    result_label = CTkLabel(master=result_frame, text=header_str, font=("Times New Roman", 25), padx=300)
    result_label.grid(row=row_idx, column=0, sticky="w", pady=(0, 10))

    row_idx = 0  # Initialize row_idx here

    for result in result_list[:-1]:  # Exclude the last entry (average turnaround and waiting times)
        row_idx += 1
        data = [str(result[key]) for key in header]
        data_str = "      | ".join(f"{col:<5}" for col in data)
        result_label = CTkLabel(master=result_frame, text=data_str, font=("Times New Roman", 25), justify="center")
        result_label.grid(row=row_idx, column=0, sticky="w", pady=(0, 10), padx=200)

    row_idx += 1
    average_label = CTkLabel(master=result_frame, text=f"Average Turnaround Time: {result_list[-1]['Average Turnaround Time']}",
                             font=("Times New Roman", 25), justify="center", padx=300)
    average_label.grid(row=row_idx, column=0, sticky="w", pady=(20, 10))

    row_idx += 1
    average_label = CTkLabel(master=result_frame, text=f"Average Waiting Time: {result_list[-1]['Average Waiting Time']}",
                             font=("Times New Roman", 25), justify="center", padx=300)
    average_label.grid(row=row_idx, column=0, sticky="w", pady=(0, 10))
    
    count = 1
    processes.clear()
    
def scheduller_picker():
    for widget in added_p_frame.winfo_children():
        widget.destroy()
        
    label(added_p_frame, "PROCESSES", 23, "white", "n", True, 0, 20, 0)
      
    selected_value = my_combo.get()
    if selected_value == "FCFS":
        fcfs_submit()
    elif selected_value == "SJF":
        SJF_submit()
    elif selected_value == "STRF":
        STRF_submit()
    else:
        global count
        count = 1
        processes.clear()
            
def update_display():
    # Clear the added_p_frame
    for widget in added_p_frame.winfo_children():
        widget.destroy()

    result_label = CTkLabel(master = added_p_frame, text = "PROCESSES", font=("Times New Roman", 23))
    result_label.pack(anchor="n", expand=True, pady=(0,15))
    
    # Display all processes
    for p in processes:
        process_label = CTkLabel(
            master=added_p_frame,
            text=f"ID: {p.id}    |    AT: {p.arrival_time}    |    BT: {p.burst_time}",
            font=("Times New Roman", 20)
        )
        process_label.pack(anchor="center")
            
def delete_process():
    global count, processes, added_p_frame
    
    # Check if there are processes to delete
    if processes:
        # Remove the last process
        last_process = processes.pop()
        
        # Destroy the corresponding label in the added_p_frame
        for widget in added_p_frame.winfo_children():
            if widget.winfo_class() == "Label" and f"ID: {last_process.id}" in widget.cget("text"):
                widget.destroy()
                break
        
        update_display()
        # Decrement the count
        count -= 1
        
    else:
        # Display a message if no processes are available to delete
        messagebox.showinfo("Info", "No processes to delete.")
 
app = CTk()          
width = app.winfo_screenwidth()
height = app.winfo_screenheight()
app.geometry(f"{width}x{height}+0+0")
app.title("Sync Queue Nays")

top_frame = CTkFrame(master=app, fg_color="#1A2546")
top_frame.pack(side="top", fill="both", expand="true")

bottom_frame = CTkFrame(master=app, fg_color="#1A2546")
bottom_frame.pack(side="top", fill="both", expand="true")
label(bottom_frame, "CALCULATION", 35, "white", "n", True, 0, 5, 30)

input_frame = CTkFrame(
    master=top_frame,
    border_width=1,
    width=550,
    border_color = "#465B87",
    fg_color = "#031C36",
    corner_radius=10,
)
input_frame.place(relx=0.3, rely=0.6, anchor="center")
label(input_frame, "ADD PROCESS", 15, "white", "s", True,  2, 2, 5)

At_input = CTkEntry(
    master=input_frame, 
    placeholder_text="Arrival Time:", 
    corner_radius=20, fg_color = "#021B31", 
    border_color = "#173562"
)
At_input.pack(anchor="s", expand=True, pady=4, padx=30)

BT_input = CTkEntry(
    master=input_frame, 
    placeholder_text="Burst Time:", 
    corner_radius=20, fg_color = "#021B31", 
    border_color = "#173562"
)
BT_input.pack(anchor="s", expand=True, pady=4, padx=30)

add_btn = CTkButton(
    master=input_frame,
    text="ADD",
    fg_color="#004155",
    hover_color = "#237DBF",
    corner_radius=20,
    border_color="#465B87",
    border_width=1,
    command=lambda: inputs(At_input, BT_input)
)
add_btn.pack(anchor="s", pady=7)

added_p_frame = CTkScrollableFrame(
    master=top_frame,  # Assign the global variable
    border_width=1,
    width=550,
    corner_radius=10,
    border_color = "#465B87",
    fg_color = "#031C36"
)
added_p_frame.place(relx=0.6, rely=0.6, anchor="center")
label(added_p_frame, "PROCESSES", 23, "white", "n", True, 0, 20, 0)
      
dlt_btn = CTkButton(
    master=input_frame,
    text="DELETE",
    fg_color="#004155",
    hover_color = "#EC4242",
    corner_radius=20,
    border_color="#465B87",
    border_width=1,
    command=delete_process
)
dlt_btn.pack(anchor="s", pady=7)

result_frame = CTkScrollableFrame(
    master=bottom_frame,
    border_width=1,
    width=900,
    height=250,
    fg_color = "#031C36",
    border_color="#465B87",
    corner_radius=10,)
result_frame.place(relx=0.5, rely=0.5, anchor="center")

my_combo = customtkinter.CTkComboBox(
    master=top_frame, 
    values=["CHOOSE ALGORITHM", "SJF", "FCFS", "STRF"], 
    width=574,
    height = 30,
    fg_color = "#031C36",
    border_color="#465B87",
    justify = "center",
    corner_radius=10,
    font = ("Times New Roman", 15)
)
my_combo.pack(pady=(180, 0), padx = (290,0))

submt_btn = customtkinter.CTkButton(
    master=input_frame,
    text="SUBMIT",
    fg_color="#004155",
    hover_color = "#93C775",
    corner_radius=20,
    border_color="#465B87",
    border_width=1,
    command=scheduller_picker)
submt_btn.pack(anchor="s", pady=7)

app.mainloop()
