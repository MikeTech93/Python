### Description 

This script will perform a menu with a choice of tools for linux administrators

### Usage 

1. File Permissions#
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
	2. Rename file/folder
	3. Copy file/folder
	4. Move file/folder
	5. Delete file/folder

4. Display System Information
	Computer Name
	Operating System
	Host
	Kernel Version
	Uptime
	CPU
	GPU
	RAM

5. System Maintenance
	1. Top 5 CPU processes
	2. Top 5 RAM Processes
	3. Top 5 Size folders
	4. Manage logs

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
