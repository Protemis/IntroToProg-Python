# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# EWaktola,8.11.2021,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFilename = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
lstTabletemp = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
try: # error handling if file has not been created
    objFile = open(objFilename, "r")  # open the text file and read the data
    for row in objFile:  # when the data returns
        lstRow = row.split(",")  # split the data into a list
        dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}  # put in the keys and extract values
        lstTable.append(dicRow)  # append to the table itself
    objFile.close()  # closing the file is best practice
except:
    print()
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        print('task','-','priority (1-5)')
        print('_'*50)
        # try:
        for row in lstTable:
            print(row['Task'],' - ',row['Priority'])
        # except:
        #     print('\nNo data, add a new item and save data to file before trying to see current data. Returning to main menu.')
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        strtodo = input('Enter task name:')
        strpriority = input('Enter task priority (1-5):')
        dicRow = {'Task':strtodo,'Priority':strpriority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        strtaskremove = input('Which task would you like to remove?')
        strtaskremove = strtaskremove.lower()
        for row in lstTable:
            if row["Task"].lower() == strtaskremove.lower():
                lstTable.remove(row)
                print(strtaskremove, " has been removed")

        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        objFile = open(objFilename, "w")
        for row in lstTable:
            objFile.write(row["Task"] + "," + row["Priority"] + "\n")
        objFile.close()
        print("Your data has been saved")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        strexitverification = input('Are you sure? (y/n)')

        if strexitverification == 'y':
            print('Exit confirmed..... Goodbye')
            break  # and Exit the program
        elif strexitverification == 'n':
            print('\nReturning to main menu.\n')
        else:
            print('\nYour input is not a valid choice. Returning to the main menu.\n')
        continue