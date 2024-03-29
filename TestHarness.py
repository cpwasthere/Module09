# ---------------------------------------------------------- #
# Title: Listing 10
# Description: A main module for testing
# ChangeLog (Who,When,What):
# ChrisPerry,12/2/19, Created started script
# ChrisPerry,12/6/19, testing
# ChrisPerry,12/7/19, Additional testing
# ---------------------------------------------------------- #
if __name__ == "__main__":
    from Listing09 import Employee as Emp  # Employee class only!
    import Listing07 as P  # processing classes
else:
    raise Exception("This file was not created to be imported")

# Test data module
objP1 = Emp(1, "cp", "cp")
objP2 = Emp(2, "cp", "dp")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test processing module
P.FileProcessor.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = P.FileProcessor.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))
for row in lstTable:
    print(row.to_string(), type(row))
