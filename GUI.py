import tkinter as tk
import Car_Park as cp

# create root window
root = tk.Tk()
root.title("KeeleSU Car Park")
root.iconbitmap("SU-logo_16x16.png")
root.geometry("700x450")

# create main_menu frame and pack the main_menu in the root
main_menu_frame = tk.Frame(root, bg="white")
main_menu_frame.pack(fill="both", expand=True)

# create the other frames to place the main menu commands
enter_car_park_frame = tk.Frame()
exit_car_park_frame = tk.Frame()
query_record_frame = tk.Frame()

# call car park dataset for GUI
cp.create_car_park_dataset()


# create functions to call the frames for the options in the main menu
def switch_to_enter_car_park_frame():
    main_menu_frame.forget()
    exit_car_park_frame.forget()
    query_record_frame.forget()
    enter_car_park_frame.pack()


def switch_to_exit_car_park():
    main_menu_frame.forget()
    enter_car_park_frame.forget()
    query_record_frame.forget()
    exit_car_park_frame.pack()


def switch_to_query_record_frame():
    main_menu_frame.forget()
    exit_car_park_frame.forget()
    enter_car_park_frame.forget()
    query_record_frame.pack()


def return_main_menu():
    exit_car_park_frame.forget()
    query_record_frame.forget()
    enter_car_park_frame.forget()
    vehicle_num_entry.delete(0, tk.END)
    vehicle_num_entry_exit.delete(0, tk.END)
    ticket_num_entry.delete(0, tk.END)
    data.set("")
    result_label_enter.config(text="")
    result_label_exit.config(text="")
    result_label_query.config(text="")
    main_menu_frame.pack(fill="both", expand=True)


# function for the Enter Park Button on the main menu
def enter_car_park():
    vehicle_num = vehicle_num_entry.get().upper()
    if cp.check_spaces_left() <= 0:
        result_label_enter.config(text="*** Car Park Is Full,Please Come Back Later***", fg="black")
        tk.Button(enter_car_park_frame, text="Return To Main Menu", font=("Arial", 20), fg="green", borderwidth=8,
                  command=return_main_menu).pack(pady=25, padx=35)
    else:
        if len(vehicle_num) == 4 and vehicle_num[:2].isupper() and vehicle_num[2:].isdigit():
            if not cp.enter_car_park(vehicle_num):
                result_label_enter.config(text="*** Vehicle Number Already Exists ***", fg="red")
                tk.Button(enter_car_park_frame, text="Return To Main Menu", font=("Arial", 20), fg="green",
                          borderwidth=8, command=return_main_menu).pack(pady=25, padx=35)
            else:
                result_label_enter.config(text="*** Vehicle Number Accepted ***", fg="red")
                cp.enter_car_park(vehicle_num)
                ticket_num = cp.ticket_num
                entry_time = cp.entry_time
                parking_space_id = cp.parking_space_id
                spaces_left = cp.check_spaces_left()
                result_label_enter.config(
                    text=f"Ticket number is: {ticket_num}\nEntry time: {entry_time}\n"
                         f"Parking space identifier is: {parking_space_id}\n"
                         f"Spaces left in the car park is: {spaces_left}", fg="black")
                tk.Button(enter_car_park_frame, text="Click To Complete", font=("Arial", 20), fg="green", borderwidth=8,
                          command=return_main_menu).pack(pady=25, padx=35)
        elif vehicle_num == "":
            result_label_enter.config(text="*** Enter Vehicle Number ***", fg="red")
            tk.Button(enter_car_park_frame, text="Return To Main Menu", font=("Arial", 20), fg="green", borderwidth=8,
                      command=return_main_menu).pack(pady=25, padx=35)
        else:
            result_label_enter.config(text="*** Vehicle Number Invalid ***", fg="red")
            tk.Button(enter_car_park_frame, text="Return To Main Menu", font=("Arial", 20), fg="green", borderwidth=8,
                      command=return_main_menu).pack(pady=25, padx=35)


# create the vehicle number label and entry widgets for enter_car_park_frame
tk.Label(enter_car_park_frame, text="Enter First Four Characters of Vehicle Number. \n For Example AB12",
         font=("Arial", 20)).pack(pady=10)
data = tk.StringVar()
vehicle_num_entry = tk.Entry(enter_car_park_frame, textvariable=data, width=50)
vehicle_num_entry.pack(pady=20, padx=20)
enter_car_park_button = tk.Button(enter_car_park_frame, text="Enter",
                                  command=enter_car_park, font=("Arial", 13), borderwidth=8, )
enter_car_park_button.pack(pady=13, padx=13)
result_label_enter = tk.Label(enter_car_park_frame, text="", font=("Arial", 15))
result_label_enter.pack()


# function for the Exit Car Park Button on the main menu
def exit_car_park():
    vehicle_num = vehicle_num_entry_exit.get().upper()
    if vehicle_num == "":
        result_label_exit.config(text="*** Enter Vehicle Number ***", fg="red")
        tk.Button(exit_car_park_frame, text="Return To Main Menu", font=("Arial", 20), fg="green", borderwidth=8,
                  command=return_main_menu).pack(pady=25, padx=35)
    elif len(vehicle_num) == 4 and vehicle_num[:2].isupper() and vehicle_num[2:].isdigit():
        result_label_exit.config(text="*** Vehicle Number Accepted ***", fg="green")
        record = cp.exit_car_park(vehicle_num)
        result_label_exit.config(
            text=f"Spaces Left In The Car Park Is: {cp.check_spaces_left()}\nTicket Number Is: {record[1]}\n"
                 f"Entry Time Is: {record[2]}\nParking Space Identifier Is: {record[3]}\nExit Time Is: {record[4]}\n"
                 f"Cost Is: £{record[5]}", fg="black")
        tk.Button(exit_car_park_frame, text="Click To Complete", font=("Arial", 20), fg="green", borderwidth=8,
                  command=return_main_menu).pack(pady=25, padx=35)
    else:
        result_label_exit.config(text="*** Vehicle Number Invalid ***", fg="red")
        tk.Button(exit_car_park_frame, text="Return To Main Menu", font=("Arial", 20), fg="green", borderwidth=8,
                  command=return_main_menu).pack(pady=25, padx=35)


# create the vehicle number label and entry widgets for exit_car-park_frame
tk.Label(exit_car_park_frame, text="Enter First Four Characters of Vehicle Number.\n For Example AB12 ",
         font=("Arial", 20,)).pack(pady=10)
data = tk.StringVar()
vehicle_num_entry_exit = tk.Entry(exit_car_park_frame, textvariable=data, width=50)
vehicle_num_entry_exit.pack(pady=20, padx=20)
tk.Button(exit_car_park_frame, text="Enter", command=exit_car_park,
          font=("Arial", 13), borderwidth=8, ).pack(pady=13, padx=13)
result_label_exit = tk.Label(exit_car_park_frame, text="", font=("Arial", 15))
result_label_exit.pack()


# function for the View Spaces Left Button on the main menu
def view_spaces_left(result_label_spaces_left):
    spaces_left = cp.check_spaces_left()
    result_label_spaces_left.config(text=f"Spaces Left In The Car Park Is: {spaces_left}",
                                    font=("Arial", 20,), bg="white")


# function for the Query Record Button on the main menu
def query_record():
    current_ticket_num = ticket_num_entry.get()
    record = cp.query_record_with_ticket_number(current_ticket_num)
    if record is None:
        result_label_query.config(text="*** TICKET DOES NOT EXIST ***", fg="red")
        tk.Button(query_record_frame, text="Return To Main Menu", font=("Arial", 20), fg="green", borderwidth=8,
                  command=return_main_menu).pack(pady=25, padx=35)
    else:
        vehicle_num, ticket_num, entry_time, parking_space_id, exit_time, cost = record
        result_label_query.config(
            text=f"Ticket Number Is: {ticket_num}\nVehicle Number Is: {vehicle_num}\nEntry Time Is: {entry_time}\n"
                 f"Parking Space Identifier Is: {parking_space_id}\nExit Time Is: {exit_time}\n"
                 f"Cost Is: £{cost}", fg="black")
    tk.Button(query_record_frame, text="Click To Complete", font=("Arial", 20), fg="green", borderwidth=8,
              command=return_main_menu).pack(pady=25,
                                             padx=35)


# create the ticket number label and entry widgets for query_record_frame
tk.Label(query_record_frame, text="Enter Ticket Number", font=("Arial", 20)).pack(pady=10)
data = tk.StringVar()
ticket_num_entry = tk.Entry(query_record_frame, textvariable=data, width=50)
ticket_num_entry.pack(pady=20, padx=20)
tk.Button(query_record_frame, text="Enter", command=query_record, font=("Arial", 13),
          borderwidth=8, ).pack(pady=13, padx=13)
result_label_query = tk.Label(query_record_frame, text="", font=("Arial", 15))
result_label_query.pack()


# function for the QUit Button on the main menu
def quit_program():
    main_menu_frame.forget()
    tk.Label(root, text="Thanks For Visiting\nThe KeeleSU Car Park\n Goodbye...\n\U0001F600",
             fg="black", font=("Arial", 45)).pack()


# main_menu labels and buttons
def call_main_menu():
    tk.Label(main_menu_frame, text="Welcome to KeeleSU Car Park\nWhat Would You Like To Do?",
             font=("Arial", 16, "bold"), bg="white").pack(pady=10)
    tk.Button(main_menu_frame, text="Enter The Car Park (Hourly Rate £2)", font=("Arial", 14), borderwidth=8,
              command=switch_to_enter_car_park_frame).pack(pady=5)
    tk.Button(main_menu_frame, text="Exit The Car Park", font=("Arial", 14), borderwidth=8,
              command=switch_to_exit_car_park).pack(pady=5)
    tk.Button(main_menu_frame, text="View Available Parking Spaces", font=("Arial", 14), borderwidth=8,
              command=lambda: view_spaces_left(result_label_spaces_left)).pack(pady=5)
    tk.Button(main_menu_frame, text="Query Record With Ticket Number", font=("Arial", 14), borderwidth=8,
              command=switch_to_query_record_frame).pack(pady=5)
    tk.Button(main_menu_frame, text="Quit", font=("Arial", 14), fg="red",
              command=quit_program, borderwidth=8, ).pack(pady=5)
    result_label_spaces_left = tk.Label(main_menu_frame, text="")
    result_label_spaces_left.pack()


if __name__ == "__main__":
    call_main_menu()
    root.mainloop()
