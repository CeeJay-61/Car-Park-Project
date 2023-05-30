# Car Park.py
import csv
import datetime as dt
import random
import os

# global variables
KSU_PARK_CAPACITY = 8
car_park_data = []
occupied_spaces = set()
ticket_num = 0
parking_space_id = 0
parking_cost = 0
entry_time = dt.datetime.now()
exit_time = dt.datetime.now()


# create csv dataset
def create_car_park_dataset():
    if not os.path.isfile("car_park_data.csv"):

        with open("car_park_data.csv", "w", newline="") as d:
            writer = csv.writer(d)
            writer.writerow(
                ["Vehicle Number", "Ticket Number", "Entry Time", "Parking Space Identifier", "Exit Time", "Cost"])
    else:
        return


# generate random ticket number
def generate_ticket(vehicle_num):
    return str(random.randint(1000, 9999)) + vehicle_num[2:]


# identify occupied spaces in the car park
def get_assigned_parking_spaces():
    with open("car_park_data.csv", mode='r') as d:
        reader = csv.reader(d)
        global occupied_spaces
        for row in reader:
            if row[4] == '' and row[5] == '':
                occupied_spaces.add(row[3])
    d.close()
    return True


# identify unoccupied spaces in the car park
def get_unassigned_parking_spaces():
    global occupied_spaces
    for i in range(1, 9):
        if str(i) in occupied_spaces:
            continue
        else:
            return i


# calculate parking duration and cost
def calculate_parking_cost(current_exit_time, current_entry_time):
    current_entry_time = dt.datetime.strptime(current_entry_time, '%Y-%m-%d %H:%M:%S.%f')
    duration = current_exit_time - current_entry_time
    duration_per_hour = duration.total_seconds() / 3600
    return duration_per_hour * 2


# create code for option1 - Enter the car park (Hourly rate £2)
def enter_car_park(vehicle_num):
    with open("car_park_data.csv", mode="r") as d:
        reader = csv.reader(d)
        for row in reader:
            if vehicle_num == row[0]:
                d.close()
                return False
    if check_spaces_left() > 0:
        global ticket_num
        global parking_space_id
        global entry_time
        get_unassigned_parking_spaces()
        parking_space_id = get_unassigned_parking_spaces()
        entry_time = dt.datetime.now()
        ticket_num = generate_ticket(vehicle_num)
        with open("car_park_data.csv", mode="a", newline="") as d:
            writer = csv.writer(d)
            writer.writerow([vehicle_num, ticket_num, entry_time, parking_space_id, "", ""])
            d.close()
    return True


# create code for option2 - Exit car park
def exit_car_park(vehicle_num):
    with open("car_park_data.csv", mode="r") as d:
        global ticket_num
        global entry_time
        global parking_space_id
        rows = list(csv.reader(d))
        get_assigned_parking_spaces()
        for i, row in enumerate(rows):
            if row[0] == vehicle_num:
                ticket_num = row[1]
                entry_time = row[2]
                parking_space_id = row[3]
                global parking_cost
                global exit_time
                exit_time = dt.datetime.now()
                parking_cost = calculate_parking_cost(exit_time, entry_time)
                rows[i] = [vehicle_num, ticket_num, entry_time, parking_space_id, exit_time, parking_cost]
                occupied_spaces.remove(parking_space_id)
    with open("car_park_data.csv", "w", newline='') as d:
        csv_writer = csv.writer(d)
        csv_writer.writerows(rows)
        d.close()
        row2 = [vehicle_num, ticket_num, entry_time, parking_space_id, exit_time, parking_cost]
    return row2


# create code for option3 - View available parking spaces
def check_spaces_left():
    global KSU_PARK_CAPACITY
    global occupied_spaces
    get_assigned_parking_spaces()
    return KSU_PARK_CAPACITY - len(occupied_spaces)


# create code for option4 - Query parking record by ticket number
def query_record_with_ticket_number(current_ticket_num):
    with open("car_park_data.csv", "r") as d:
        reader = csv.reader(d)
        next(reader)
        for row in reader:
            if row[1] == current_ticket_num:
                return list(row)
