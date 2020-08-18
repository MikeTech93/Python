### Description 

This script will perform a menu with a choice of tools for linux administrators.

Each menu option will have a return to main menu and exit option for easy navigation.

### Usage 

1. File Permissions
	1. Perform basic ls command
		> This will prompt for a specified path and then perform an ls
	2. Advanced permissions review
		> This will prompt for a specified path and then break down all permissions
		> If a folder is specified this will run for each file in the folder
		> If a folder is specified ensure to prompt for user confirmation first
			Linux Permissions = wrx.....
			User Permissions = dave
			Group Permissions = root
				Group Members = dave, tom
			Everyone Permissions = none
			SUID = enabled/disabled
			SGID = enabled/disabled
				Group Members = dave, tom
			Umask Permissions = (What the permissions will be on new files created)

2. Network Settings
	1. View network settings
		> This will display a menu generated from available network adapters an then you can drill down e.g.
			Network Adapter Name
			IPv4 Addr
			Gateway
			DNS Servers
	2. Configure Network Settings
		 > This will display a menu generated from available network adapters and then you can drill down e.g.
			> This will generate a menu with the following items which you can then select and edit
				IPv4 Addr
				Gateway
				DNS Servers

3. File\folder Managmeent
	1. Create file/folder
		> This will prompt if you want to create a file or folder
		> Then where exactly you would like to create it
	2. Rename file/folder
		> This will prompt for a file/folder 
		> Then ask you what you would like it to be renamed too
	3. Copy file/folder
		> This will prompt you for a file/folder
		> If a folder is selected it will ask if you want to recursively copy
		> Then it will ask where you want to copy it to
	4. Move file/folder
		> This will prompt you for a file/folder
		> then it will ask where you want to move it to
	5. Delete file/folder
		> this will prompt you for a file/folder
		> then it will delete the file/folder

4. Display System Information
	1. Display System information
		> This will display a list of system information:
			Hostname
			Operating System
			Linux Kernel and Version
			Uptime
			CPU
			GPU
			RAM	

5. System Maintenance
	1. Top 5 processes by CPU%
		> This will display a list of Top 5 processes consuming processing power
	2. Top 5 processes by MEM%
		> This will display a list of Top 5 processes consuming RAM
	3. Top 5 folders by size on disk
		> This will display the largest 5 folders on the current running system.
	4. Launch HTOP
		> This will check if HTOP is installed and if not it will prompt you to install it
		> It will then launch HTOP
	5. Manage logs
		> This will prompt for a log folder location - It will give some common locations as examples
		> It will then search for log files in this destination and present these
		> This will then prompt for confirmation and compress all log files into a tar.gz file

6. User Management
	1. List Users
		1. Regular users
			> List all users who can login to a shell
		2. Root Users
			> List all users with root access
		3. Service accounts
			> List all service accounts
		4. All accounts
			> List all accounts
	2. Create User
		> This will prompt for a username
		> Ater checking the user does not already exist it will ask for a few details
		> Before creating the user it will display all values you entered and ask for confirmation
		> If enter is pressed it will keep the current value
	3. Edit User
		> This will prompt for a username
		> Ater matching the user it will loop through a few of the users details presenting the current set value and asking if the user would like to change this value
		> If enter is pressed it will keep the current value
	4. Change User Password
		> Prompt for a username
		> Ask if you want a randomly generated password or a custom password
	5. Delete User
		> Prompt for a username
		> Ask if you would like to do anything with the users home folder
		> if yes - prompt if they would like to delete or change ownership of the folder

7. Group Management
	1. List groups
	2. Create Group
	3. Edit Group
	4. Change group password
	5. Delete group

### Examples

1. Open Menu
2. Select 4. 

This will now display system information  

### Installation From Source 

Information on how to install from source

To install the package after you've cloned the repository, you'll want to run the following command from within the project directory: 

pip install --user -e . 

### Preparing for Development 

Follow these steps to start developing with this project: 

1. Ensure `pip` and `pipenv` are installed 

2. Clone repository: `git clone git@github.com:example/projectname` 

3. `cd` into the repository 

4. Activate virtualenv: `pipenv shell` 

5. Install dependencies: `pipenv install` 
