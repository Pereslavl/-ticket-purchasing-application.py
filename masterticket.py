
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
amount_due = num_tickets * TICKET_PRICE

# Output on the screen result
print("The total due is $ {}".format(amount_due))


# Prompt to user if they want to proceed. Y/N
question = input("Do you want to proceed?")

# if they want to proceed
if question = "y":
    print("SOLD!, to confirm purchase")
     # print out to the screen "SOLD!" to confirm purchase
else:
    print("Buy!")
 # and then decrement the tickets remaining by the number of tickets purchased
residue = tickets_remaining - amount_due
print(residue)
# Otherwise...

     # Thanks them by name
