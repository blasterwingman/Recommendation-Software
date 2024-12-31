**Restaurant Recommendation Service**

Overview

This program helps users find the best restaurants nearby based on their preferred type of cuisine. It uses a predefined dataset of cuisines and restaurants to provide tailored recommendations. Users can browse available cuisines, view restaurant details, and explore other options if desired.

Features
	1.	Interactive Cuisine Selection:
	•	Users enter the first letter of the cuisine type they want.
	•	The program suggests all available cuisines starting with the input letter.
	2.	Restaurant Recommendations:
	•	For the chosen cuisine, the program displays:
	•	Restaurant name
	•	Expense level (in $$$)
	•	Rating
	•	Address
	3.	Error Handling:
	•	If no cuisines match the user’s input, the program prompts the user to try again.
	4.	Dynamic Choices:
	•	Handles cases where:
	•	Only one cuisine matches the input.
	•	Multiple cuisines are available, prompting the user to choose from the list.
	5.	Graceful Exit:
	•	Users can exit the program at any point by declining to continue.

How to Run
	1.	Ensure you have the rest_data module, containing:
	•	rest_data.types: A list of cuisine types (e.g., ["Indian", "Italian", "Chinese"]).
	•	rest_data.restaurant_data: A list of restaurants, where each entry is structured as:

[cuisine_type, restaurant_name, expense_level, rating, address]

**Example:**

rest_data.restaurant_data = [
    ["Indian", "Spice Hub", 2, 4.5, "123 Main Street"],
    ["Italian", "Pasta Palace", 3, 4.0, "456 Maple Avenue"]
]


	2.	Run the script in a Python environment:

**python3 main.py**


	3.	Follow the on-screen instructions to:
	•	Enter your name.
	•	Select a cuisine type by entering the first letter.
	•	View restaurant recommendations.
	4.	Continue exploring different cuisines or exit the service as desired.

**Code Structure**
	1.	get_restaurants(choice):
	•	Displays the list of restaurants for the selected cuisine.
	•	Prompts the user to explore another cuisine or exit.
	2.	get_choice(name):
	•	Filters available cuisines based on the user’s input.
	•	Handles cases with one or multiple matching cuisines.
	•	Manages invalid inputs and retries.
	3.	Main Program:
	•	Greets the user.
	•	Initiates the get_choice() function to start the selection process.

**Sample Interaction**

Input:

Please state your name to get started: John
Please enter the first letter of the type of cuisine you would like to eat, John: I

**Output:**

The following cuisines are available based on your choice: Indian, Italian
Which one would you like to choose, John? Enter the exact name from the list: Indian

Here are the restaurants that serve Indian food:
Name: Spice Hub
Expense $$$: 2
Rating: 4.5
Address: 123 Main Street
Would you like to look at another type of cuisine? (yes or no)

**Enhancements**

This program can be extended with additional features:
	•	Support for filtering based on expense level or rating.
	•	Integration with real-time restaurant APIs for live recommendations.
	•	Multi-word input handling for cuisines.

Feel free to explore and modify the program to suit your needs!
