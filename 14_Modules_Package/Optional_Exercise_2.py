# Develop a clock with hours minutes ans seconds using datatime module
# Create the script and execute it in terminal
# time module have a method called sleep(seconds)
# os has a method called system('clr') to clean the terminal

import datetime, os, time

while True:
    date = datetime.datetime.now()
    print("{}:{}:{}".format(date.hour, date.minute, date.second))
    time.sleep(0.50)
    os.system('cls')