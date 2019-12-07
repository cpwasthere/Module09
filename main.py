# ------------------------------------------------------------------------ 
# Title: Assignment 09
# Description: Working with Modules
# ChangeLog (Who,When,What):
# ChrisPerry,12/2/19, Created started script
# ChrisPerry,12/6/19, Edits
# ChrisPerry,12/7/19, Final Edits to complete Assignment 9
# ------------------------------------------------------------------------ 
if __name__ == "__main__":
	from DataClasses import Employee as Emp
	from ProcessingClasses import FileProcessor as Fp 
	from IOClasses import EmployeeIO as Eio
else:
	raise Exception("This file was not created to be imported")

# Main Body of Script ---------------------------------------------------- # 
# Data #
lstEmployeeTable = [] # A list/table of Employee objects
lstFileData = [] # A list/table of string objects in a list



# Load data from file into a list of employee objects when script starts 
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
for row in lstFileData:
	lstEmployeeTable.append(Emp(row[0], row[1], row[2].strip()))

# Show user a menu of options
while True: 
	Eio.print_menu_items()
	# Get user's menu option choice
	strOption = Eio.input_menu_options() 
	if strOption == "1":
	# Show user current data in the list of employee objects
		Eio.print_current_list_items(lstEmployeeTable)
		continue
	elif strOption == "2":
	# Let user add data to the list of employee objects
		lstEmployeeTable.append(Eio.input_employee_data())
		continue
	elif strOption == "3":
		if("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):  # Double-check with user
			# Convert to function for processing
			Fp.save_data_to_file("EmployeeData.txt", lstEmployeeTable)
			input("Data saved to file! Press the [Enter] key to return to menu.")
		else:  # Let the user know the data was not saved
			input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")
		continue
	elif strOption == "4":
	# exit program
		break
# Main Body of Script ---------------------------------------------------- #