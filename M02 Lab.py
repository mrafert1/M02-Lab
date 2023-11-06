## Max Rafert
## C:\Users\maxra\OneDrive\Desktop\M02 Lab.py
## ----------------------------------------------------------------
## This app allows a user to input a last name, first name, and GPA of a student
## and recieve a message telling them if that student was put on Dean's List, Honor Roll
## or missed academic awards.
## ----------------------------------------------------------------
## Variables
## lastName: user inputed last name
## firstName: user inputed first name
## gpa: user inputed gpa
## ----------------------------------------------------------------
## Last name prompt initializes program. Gives option of entering 'ZZZ' to exit program
lastName = ""

## While loop accepts user inputed information then runs the GPA through an if/elseif loop
## do determine whether academic awards were recieved. 
while lastName != "ZZZ":
    lastName = input ("Enter student's last name: ")
    if lastName != "ZZZ":
        firstName = input ("Enter student's first name: ")
        gpa = float(input("Enter student's GPA:"))
        if gpa >= 3.5:
            print (firstName, lastName, "has made the Dean's List. Congrats!")
     
        elif gpa >=  3.25:
            print (firstName, lastName, "has made the Honor Roll. Congrats!")
           
        else:
            print (firstName, lastName, "did not recieve any honors. Keep studying!")
       



