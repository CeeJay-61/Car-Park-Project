# import Car_Park file functions
import Car_Park as cp


# create code for the Main menu
def main_menu():
    print(f"""
    Welcome to KeeleSU Car Park
    What would you like to do?
    [1] Enter The Car Park (Hourly rate £2)
    [2] Exit The Car Park
    [3] View Available Parking Spaces
    [4] Query Parking Record By Ticket Number
    [5] Quit
     """)


# call the csc dataset
cp.create_car_park_dataset()

# create a loop for the options in the main menu
while True:
    main_menu()
    option = input("Enter Your Option: ")

    # if the client enters option 1 - Enter car park
    if option == "1":
        if cp.check_spaces_left() <= 0:
            print("*** Car Park Is Full,Please Come Back Later***")
        else:
            vehicle_num = input("Enter First Four Characters Of Vehicle Number: ").upper()
            if len(vehicle_num) == 4 and vehicle_num[:2].isupper() and vehicle_num[2:].isdigit():
                if not cp.enter_car_park(vehicle_num):
                    print("*** Vehicle Number Already Exists ***")
                else:
                    print("*** Vehicle Number Accepted ***")
                    cp.enter_car_park(vehicle_num)
                    print(f" Ticket Number Is: {cp.ticket_num}")
                    print(f" Entry Time is: {cp.entry_time}")
                    print(f" Parking Space Identifier Is: {cp.parking_space_id}")
                    print(f" Vehicle Registration Number Is: {vehicle_num}")
                    print(f" Spaces Left In The Car Park Is: {cp.check_spaces_left()}")
            elif vehicle_num == "":
                print("*** Enter Vehicle Number ***")
            else:
                print("*** Vehicle Number Invalid ***")

    # if the client enters option 2 - Exit car park
    elif option == "2":
        vehicle_num = input("Enter First Four Characters Of Vehicle Number: ").upper()
        if vehicle_num == "":
            print("*** Enter Vehicle Number ***")
        elif len(vehicle_num) == 4 and vehicle_num[:2].isupper() and vehicle_num[2:].isdigit():
            print("*** Vehicle Number Accepted ***")
            record = cp.exit_car_park(vehicle_num)
            print(f" Spaces Left In The Car Park Is: {cp.check_spaces_left()}")
            print(f" Ticket Number Is: {record[1]}")
            print(f" Entry Time Is: {record[2]}")
            print(f" Parking Space Identifier Is: {record[3]}")
            print(f" Exit Time Is: {record[4]}")
            print(f" Cost Is: £{record[5]}")
        else:
            print("*** Vehicle Number Invalid ***")

    # if the client enters option 3 - Check available spaces in the Car Park
    elif option == "3":
        cp.check_spaces_left()
        print(f"Spaces Left In The Car Park Is: {cp.check_spaces_left()}")

    # if the client enters option 4 - Query Car Park with Ticket Number
    elif option == "4":
        current_ticket_num = input("Enter Ticket Number: ")
        record = cp.query_record_with_ticket_number(current_ticket_num)
        if record is None:
            print('TICKET DOES NOT EXIST')
        else:
            print(f" Ticket Number Is:, {record[1]}")
            print(f" Vehicle Number Is:, {record[0]}")
            print(f" Entry Time Is: , {record[2]}")
            print(f" Parking Space Identifier Is: , {record[3]}")
            print(f" Exit Time Is: , {record[4]}")
            print(f" Cost Is: , {record[5]}")

    # if the client enters option 5 - Quit
    elif option == "5":
        print("Thank You For Visiting The KeeleSU Car Park. Goodbye")

    else:
        print("*** Invalid Option, Please Enter a Valid Option From The List ***")
