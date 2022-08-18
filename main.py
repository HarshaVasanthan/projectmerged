import login
import staff
import doctor

print("**************************************")
print("Welcome to walk in clinic application")
print("**************************************")

choice = 1
userId = 0
while choice != 3:
    while True:
        try:
            print("1. Staff / Doctor Login")
            print("2. Admin Login")
            print("3. Quit Application")
            choice = int(input("Please select an operation (eg: 1) : "))
            break
        except:
            print("Please input a digit (eg: 1)")
    if choice > 3 or choice <= 0:
        print("Invalid choice. Please try again.")
    else:
        try:
            if choice == 1:
                type = login.login()
                if type[3] == False:
                    print("Invalid Login.")
                else:
                    if type[3] == "staff":
                        staff.options(type[0])
                    else:
                        doctor.options(type[0])
        except:
            print("Unexpected error occured.")
print("3. Quit Application selected")
print("Exiting application.")