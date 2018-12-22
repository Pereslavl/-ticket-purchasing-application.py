
TICKET_PRICE = 10

tickets_remaining = 100

# Output how many tickets are remaining using the tickets_remaining variable
print("There are {} tickets remaining.".format(tickets_remaining))

# Gather the user's name and assign it to a new variable
name_user = input("What is your name? ")


# Prompt the user by name and ask how many tickets they  would like?
number_of_tickets = int(input("How many tickets do you need? "))

# Calculate the price (number of tickets multiplied by price) and assign variable
total_cost = number_of_tickets * TICKET_PRICE

# Output on the screen result
print(total_cost)
