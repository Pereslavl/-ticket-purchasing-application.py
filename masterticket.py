
TICKET_PRICE = 10

tickets_remaining = 100


# Run this code continuosly until we run of tickets

# Output how many tickets are remaining using the tickets_remaining variable
print("There are {} tickets remaining.".format(tickets_remaining))

# Gather the user's name and assign it to a new variable
name = input("What is your name? ")

# Prompt the user by name and ask how many tickets they  would like?
num_tickets = input("How many tickets would you like, {}?  ".format(name))
num_tickets = int(num_tickets)
# Calculate the price (number of tickets multiplied by price) and assign variable
amount_due = num_tickets * TICKET_PRICE

# Output on the screen result
print("The total due is $ {}".format(amount_due))


# Prompt to user if they want to proceed. Y/N
should_proceed = input("Do you want to proceed? Y/N")

# if they want to proceed
if should_proceed.lower() == "y":
     # print out to the screen "SOLD!" to confirm purchase
    #TODO: Gather credit card information and process it.
    print("SOLD!")
    # and then decrement the tickets remaining by the number of tickets purchased
    tickets_remaining - num_tickets
# Otherwise...
else:
    # Thanks them by name
    print("Thank you anyways, {}!".formate(name))


# Notify user that tickets are sold out.
