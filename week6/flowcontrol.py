#!/usr/bin/env python3

print("""You enter a dark room with three doors.
Do you go through door #1, door #2, or door #3?""")

door = input("-> ")

# == Door Number 1 logic ===============================
if door == "1":

    print("You see a football and two contracts from the NFL.")
    print("What do you do?\n")

    print("1. Sign the first contract and play for the Packers.")
    print("2. Sign the second contract and play for the Vikings.")

    # == Football logic ====================================
    sports = input("-> ")

    if sports == "1":
        print("1) You throw an interception and lose the NFC Championship.")
    elif sports == "2":
        print("2) You never win a Super Bowl.")
    else:
        print(f"N) The Canadian Football League might be a better choice for you.")
        print("Enjoy the CFL!")

# == Door Number 2 Logic ===============================
elif door == "2":
    print("Your driveway is covered in 6 feet of snow and you're late to work.\n")
    print("What do you do?\n")

    print("1. Pay the neighbor kid $20 to shovel.")
    print("2. Hitchhike to work.")
    print("3. Walk to work.")

    # == snow Logic ================================
    snow = input("-> ")

    if snow == "2" or snow == "3":
        print("1) You are frozen and wake up 400 years later in a museum.")
        print("1) Have fun being a relic!")
    else:
        print("N) The neighbor kid steals your $20 and runs away.")
        print("N) Now you're broke too!")

# == Door Number 3 logic ===============================
elif door == "3":

    print("You walk into a room containing a tv and a book.")
    print("What will you do?")

    print("1. Turn on the tv.")
    print("2. Open the book.")

    # == tvbook logic ====================================
    tvbook = input("-> ")

    if tvbook == "1":
        print("1) You turn on the tv and are forced to watch reruns of Three's Company for the rest of your life.")
    elif tvbook == "2":
        print("2) You open the book and learn the history of the kazoo.")
    else:
        print(f"N) You must be more of an outside person.")
else:
    print("You did not select a door? What a rebel.")