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

    if (len(chosen_list)) == 1:
        print("We only have one type of cuisine that serves {0}. Here is the list of restaurants that serve that type of cuisine:".format(chosen_list))
        get_restaurants(chosen_list[0])
    else:
        print(f"The following cuisines are available of your choice: ", chosen_list, f"\nWhich one would you like to choose {name}?, Enter the first 2 letters from the given list.\n")
        choice = input().lower()
        for i in chosen_list:
            if choice == i[0:2]:
                get_restaurants(i)
            else:
                print("Sorry, we do not have any restaurants that serve that type of cuisine. Please try again.")
                get_choice(name)

# Main function

print("Welcome to our restaurant service! We will help you pick the best restaurants nearby." )
print("Please state your name to get started: ")
name = input()
get_choice(name)

