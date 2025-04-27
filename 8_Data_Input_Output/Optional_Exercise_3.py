# Create a script that perform the following tasks
# - Take 1 positive int argument
# - In case the argument is not correct show information aboyt how to use the script
# - Break Down the number in unit, tens, hy¿undreds, etc.
# - Example: 3647
# -         0007
# -         0040
# -         0600
# -         3000

import sys

if len(sys.argv) == 2:
    number = int(sys.argv[1])
    if number < 0:
        print("Argument is not correct")
        print("Example: Optional_Exercise_3.py [1-infinite]")
    else:
        S_num = str(number)
        for i in range(len(S_num)):
            print("{:04d}".format(int(S_num[len(S_num)-1-i]) * 10 **i))

else:
    print("Argument is not correct")
    print("Example: Optional_Exercise_3.py [1-infinite]")
