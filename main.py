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
    # Get the first letter of the cuisine
    chosen = input(f"Please enter the first letter of the type of cuisine you would like to eat, {name}: ").strip().lower()
    
    # Filter cuisines based on the first letter
    chosen_list = [cuisine for cuisine in rest_data.types if cuisine.lower().startswith(chosen)]
    
    if not chosen_list:
        # Handle case where no cuisines match
        print(f"Sorry, {name}, we do not have any cuisines starting with '{chosen}'.")
        try_again = input("Would you like to try again? (yes or no): ").strip().lower()
        if try_again in ['yes', 'y']:
            get_choice(name)
        else:
            print(f"Thank you for using our service, {name}. Have a great day!")
        return

    # If only one cuisine matches
    if len(chosen_list) == 1:
        print(f"We only have one type of cuisine that matches your choice: {chosen_list[0]}.")
        print("Here is the list of restaurants that serve this type of cuisine:")
        get_restaurants(chosen_list[0])
    else:
        # Multiple cuisines match, ask the user to choose
        print(f"The following cuisines are available based on your choice: {', '.join(chosen_list)}")
        choice = input(f"Which one would you like to choose, {name}? Enter the exact name from the list: ").strip().lower()

        # Validate the user's choice
        matching_cuisine = next((c for c in chosen_list if c.lower() == choice), None)
        if matching_cuisine:
            get_restaurants(matching_cuisine)
        else:
            print("Sorry, we do not have any restaurants that serve the selected type of cuisine.")
            try_again = input("Would you like to try again? (yes or no): ").strip().lower()
            if try_again in ['yes', 'y']:
                get_choice(name)
            else:
                print(f"Thank you for using our service, {name}. Have a great day!")
# Main function

print("Welcome to our restaurant service! We will help you pick the best restaurants nearby." )
print("Please state your name to get started: ")
name = input()
get_choice(name)

