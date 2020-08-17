#!/usr/bin/env python3.7
# Menu system for SysAdminTools script

# import modules

import sys #this allows you to use the sys.exit command to quit/logout of the application

# functions definitions start

def mainmenu():
    print("************MAIN MENU**************")
    #time.sleep(1)
    print()
    choice = input("""
1: File Permissions
2: Network Settings
3. File/Folder Management
4. Display System Information
5. System Maintenance
6. Exit

Please enter your choice: """)

    if choice == "1":
        filepermissions()
    elif choice == "2":
        networksettings()
    elif choice == "3":
        filefoldermanagement()
    elif choice == "4":
        systeminformation()
    elif choice == "5":
        systemmaintenance()
    elif choice == "6":
        sys.exit
    else:
        print("You must only select either 1,2,3,4,5 or 6")
        print("Please try again")
        mainmenu()

def filepermissions():
    print("************FILE PERMISSIONS MENU**************")
    #time.sleep(1)
    print()
    choice = input("""
1: Perform basic ls command
2. Advanced Permissions review
3. Return to main menu
4. Exit 

Please enter your choice: """)

    if choice == "1":
        print("You selected Perform basic ls command")
    elif choice == "2":
        print("You selected Advanced Permissions review")
    elif choice == "3":
        mainmenu()
    elif choice == "4":
        sys.exit
    else:
        print("You must only select either 1,2,3 or 4")
        print("Please try again")
        filepermissions()

def networksettings():
    print("You selected the Network Settings option")

def filefoldermanagement():
    print("You selected the File/Folder Management option")

def systeminformation():
    print("You have selected the System Information option")

def systemmaintenance():
    print(f"You have selected the System Maintenance option")


# function definitions end

# script start

mainmenu()

# script end
