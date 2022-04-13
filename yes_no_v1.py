looping = True

while looping:
    # Ask user if played before
    yes_no = input("Have you played before ?").lower().strip()

    # if the input is yes the 'program continues'
    if yes_no.lower() == "yes":
        print("Program continues")


    elif yes_no.lower() == "y":
        print("program continues")


    # if no output 'display instructions'
    elif yes_no.lower() == "no":
        print("display instructions")


    elif yes_no.lower() == "n":
        print("display instructions")


    else:
        print("please enter yes or no")
