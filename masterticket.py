
TICKET_PRICE = 10

tickets_remaining = 100

# Output how many tickets are remaining using the tickets_remaining variable
print("There are {} tickets remaining.".format(tickets_remaining))

# Gather the user's name and assign it to a new variable
name = input("What is your name? ")

# Prompt the user by name and ask how many tickets they  would like?
num_tickets = input("How many tickets would you like, {}?  ".format(name))
num_tickets = int(num_tickets)
# Calculate the price (number of tickets multiplied by price) and assign variable
amount_due = num_ickets * TICKET_PRICE

# Output on the screen result
print("The total due is $ {}".format(amount_due))
