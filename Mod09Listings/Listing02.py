# ---------------------------------------------------------- #
# Title: Listing02
# Description: A script that uses a module
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ---------------------------------------------------------- #
import Listing01Module

# Calling a standalone function
Listing01Module.standalone_function()

# Creating an object from a class
objMD = Listing01Module.MyData()

# Calling static methods in two classes
Listing01Module.FileProcessor.process_data()
Listing01Module.IO.print_data()
