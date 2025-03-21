#!/usr/bin/env python3
# Student ID: [seneca_id]

def function1():
    global schoolName  # Use global to modify the global variable
    schoolName = 'SICT'  # This modifies the global schoolName variable
    print('print() in function1 on schoolName:', schoolName)

def function2():
    global schoolName  # Use global to modify the global variable
    schoolName = 'SSDO'  # This modifies the global schoolName variable
    print('print() in function2 on schoolName:', schoolName)

schoolName = 'Seneca'  # Global variable
print('print() in main on schoolName:', schoolName)
function1()  # function1 modifies the global schoolName
print('print() in main on schoolName:', schoolName)
function2()  # function2 modifies the global schoolName
print('print() in main on schoolName:', schoolName)

