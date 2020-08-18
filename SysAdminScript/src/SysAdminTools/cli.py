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
6. User Management
7. Group Management
8. Exit

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
        UserManagement()
    elif choice == "7":
        GroupManagement()
    elif choice == "8":
        sys.exit
    else:
        print("You must only select either 1,2,3,4,5,6,7 or 8")
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
    print("************NETWORK SETTINGS MENU**************")
    #time.sleep(1)
    print()
    choice = input("""
1: View Network Settings
2. Configure Network Settings
3. Return to main menu
4. Exit 

Please enter your choice: """)

    if choice == "1":
        print("You selected to View Network Settings")
    elif choice == "2":
        print("You selected to Configure Network Settings")
    elif choice == "3":
        mainmenu()
    elif choice == "4":
        sys.exit
    else:
        print("You must only select either 1,2,3 or 4")
        print("Please try again")
        networksettings()

def filefoldermanagement():
    print("************File\Folder Management**************")
    #time.sleep(1)
    print()
    choice = input("""
1: Create file/folder
2: Rename file/folder
3. Copy file/folder
4. Move file/folder
5. Delete file/folder
6. Return to main menu
7. Exit

Please enter your choice: """)

    if choice == "1":
        print("You selected to Create file/folder")
    elif choice == "2":
        print("You selected to Rename file/folder")
    elif choice == "3":
        print("You selected to Copy file/folder")
    elif choice == "4":
        print("You selected to Move file/folder")
    elif choice == "5":
        print("You selected to Delete file/folder")
    elif choice == "6":
        mainmenu()
    elif choice == "7":
        sys.exit
    else:
        print("You must only select either 1,2,3,4,5,6 or 7")
        print("Please try again")
        filefoldermanagement()

def systeminformation():
    print("************NETWORK SETTINGS MENU**************")
    #time.sleep(1)
    print()
    choice = input("""
1: Display System Information
2. Return to main menu
3. Exit 

Please enter your choice: """)

    if choice == "1":
        print("You selected to Display System Information")
    elif choice == "2":
        mainmenu()
    elif choice == "3":
        sys.exit
    else:
        print("You must only select either 1,2 or 3")
        print("Please try again")
        systeminformation()

def systemmaintenance():
    print("************System Maintenance**************")
    #time.sleep(1)
    print()
    choice = input("""
1: Top 5 Processes by CPU%
2: Top 5 Processes by MEM%
3. Top 5 folders by size on disk
4. Launch HTOP
5. Manage Logs
6. Return to main menu
7. Exit

Please enter your choice: """)

    if choice == "1":
        print("You selected to view top 5 processes by CPU%")
    elif choice == "2":
        print("You selected to view top 5 processes by MEM%")
    elif choice == "3":
        print("You selected to view top 5 folders by size on disk")
    elif choice == "4":
        print("You selected to launch HTOP")
    elif choice == "5":
        print("You selected to manage logs")
    elif choice == "6":
        mainmenu()
    elif choice == "7":
        sys.exit
    else:
        print("You must only select either 1,2,3,4,5,6 or 7")
        print("Please try again")
        systemmaintenance()

def UserManagement():
    print("************User Management**************")
    #time.sleep(1)
    print()
    choice = input("""
1: List Users
2: Create User
3. Edit User
4. Change User Password
5. Delete User
6. Return to main menu
7. Exit

Please enter your choice: """)

    if choice == "1":
        UserManagementListSubMenu()
    elif choice == "2":
        print("You have selected to create a new user")
    elif choice == "3":
        print("You have selected to Edit a user")
    elif choice == "4":
        print("You have selected to change a user password")
    elif choice == "5":
        print("You have selected to delete a user")
    elif choice == "6":
        mainmenu()
    elif choice == "7":
        sys.exit
    else:
        print("You must only select either 1,2,3,4,5,6 or 7")
        print("Please try again")
        UserManagement()

def UserManagementListSubMenu():
    print("************List Users**************")
    #time.sleep(1)
    print()
    choice = input("""
1: Regular Users
2: Root Users
3. Service Accounts
4. All Accounts
5. Return to main menu
6. Exit

Please enter your choice: """)

    if choice == "1":
        print("You have selected to list all regular users")
    elif choice == "2":
        print("You have selected to list root users")
    elif choice == "3":
        print("You have selected to list all service accounts")
    elif choice == "4":
        print("You have selected to list all accounts")
    elif choice == "5":
        mainmenu()
    elif choice == "6":
        sys.exit
    else:
        print("You must only select either 1,2,3,4,5 or 6")
        print("Please try again")
        UserManagementListSubMenu()

def GroupManagement():
    print("************Group Management**************")
    #time.sleep(1)
    print()
    choice = input("""
1: List Groups
2: Create Group
3. Edit Group
4. Change Group Password
5. Delete Group
6. Return to main menu
7. Exit

Please enter your choice: """)

    if choice == "1":
        print("You have selected to list Groups")
    elif choice == "2":
        print("You have selected to create a new Group")
    elif choice == "3":
        print("You have selected to Edit a Group")
    elif choice == "4":
        print("You have selected to change a Groups password")
    elif choice == "5":
        print("You have selected to delete a Group")
    elif choice == "6":
        mainmenu()
    elif choice == "7":
        sys.exit
    else:
        print("You must only select either 1,2,3,4,5,6 or 7")
        print("Please try again")
        GroupManagement()


# function definitions end

# script start

mainmenu()

# script end