
TICKET_PRICE = 10
tickets_remaining = 100

while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("What is your name? ")
    num_tickets = input("How many tickets would you like, {}?  ".format(name))
    # Except a ValueEror to happen and handle it appropriately...remember test it  out:
    try:
        num_tickets = int(num_tickets)

    # Raise a ValueError if the requst is for more tickets  than are availiable
    if num_tickets > tickets_remaining:
        raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError:
        # Include the error text int the output
        print("Oh no that no value !!!!!")
    else:
        amount_due = num_tickets * TICKET_PRICE
        print("The total due is $ {}".format(amount_due))
        should_proceed = input("Do you want to proceed? Y/N")
        if should_proceed.lower() == "y":
            print("SOLD!")
            tickets_remaining - num_tickets
        else:
            print("Thank you anyways, {}!".formate(name))
print("Sorry the tickets are all sold out!!!")
