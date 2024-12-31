import rest_data

# Function to get the list of restaurants that serve the food type chosen by the user
def get_restaurants(choice):
    for restaurant in rest_data.restaurant_data:
        if choice == restaurant[0]:
            print("Here are the restaurants that serve " + choice + " food:")
            print("Name: " , restaurant[1])
            print("Expense $$$ ", restaurant[2])
            print("Rating: ", restaurant[3])
            print("Address: " , restaurant[4])
    print("Would you like to look at another type of cuisine? (yes or no)")
    answer = input().lower()
    if answer == 'yes' or answer == 'y':
        get_choice(name)
    else:
        print("Thank you for using our service!")
    
# Function to ask the user for the type of cuisine they want to eat
def get_choice(name):
    chosen = input(f"Please enter the first letter of the type of cuisine you would like to eat {name}: ").lower()
    chosen_list = []
    for i in rest_data.types:
        if i[0] == chosen:
            chosen_list.append(i)
        else:
            print("Sorry, we do not have any restaurants that serve that type of cuisine. Please try again.")
            get_choice(name)
    print(f"The following cuisines are available of your choice: ", chosen_list, f"\nWhich one would you like to choose {name}?\n")
    choice = input().lower()
    get_restaurants(choice)

# Main function

print("Welcome to our restaurant service! We will help you pick the best restaurants nearby." )
print("Please state your name to get started: ")
name = input()
get_choice(name)

