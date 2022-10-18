#!/usr/bin/env python3

#Author: Bryan Troxel
#Description: This is midterm activity 2 and emphasizes slicing.

print("Name: Bryan Troxel")

password_database = {"Username":"dnedry",
                     "Password":"please"}

command_database = {"reboot":"OK. I will reboot all park systems.",
                    "shutdown":"OK. I will shut down all park systems.",
                    "done":"I hate all this hacker stuff."}

white_rabbit_object = 0
counter = 0

while white_rabbit_object == 0 and counter < 3:
    input_user = input("Enter Username: ")
    input_password = input("Enter Password: ")
    if input_user == password_database["Username"] and input_password == password_database["Password"]:
        white_rabbit_object += 1
        print("Hi, Dennis. You're still the best hacker in Jurassic Park.")
        comd = input(f"Please select a command: \n {command_database.keys()} \n")
        if comd == "reboot":
            print(command_database["reboot"])
        elif comd == "shutdown":
            print(command_database["shutdown"])
        elif comd == "done":
            print(command_database["done"])
        else:
            print("The Lysine Contingency has been put into effect.")
    else:
        counter += 1
        if counter == 3:
            print("You didn't say the magic word. \n" * 25)
        else:
            print(f"You didn't say the magic word.{counter}")