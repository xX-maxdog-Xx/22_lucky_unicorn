
yes_no = ""

while yes_no.lower() != 'xxx':

    #Ask user if they ave played before

    yes_no = input("Have you played lucky unicorn before").lower()


    #if yes, output 'program continues'
    if yes_no.lower() == "yes" or yes_no == "y":
        print("program continues")


    # if no output 'display instructions'
