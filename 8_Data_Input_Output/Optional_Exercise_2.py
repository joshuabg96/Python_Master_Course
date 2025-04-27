# Create an script that does the following task
# - Take 2 arguments, both numbers positive intergers between 1-9 otherwise an errro shows
# - First argument will be doing a reference to the rows of a table, second to collumns
# - In case that do not recive uno or both arg, show the information of how use the script
# - Script will have a for loop to titerate the number of the first arg
# - Inside the for loop add a new foor to iterate the second arg
# - inside second loop execute the instruction print("*", end=")
# - Execute it by terminal

import sys

if len(sys.argv) == 3:
    row = int(sys.argv[1])
    col = int(sys.argv[2])
    if row < 1 or row > 9 or col < 1 or col > 9:
        print("Error Arguments are not correct")
        print("Example: table.py [1-10] [1-10]")
    else:
        for f in range(row):
            for c in range(col):
                print(" * ", end='')
            print("")
else:
    print("Error Arguments are not correct")
    print("Example: table.py [1-10] [1-10]")