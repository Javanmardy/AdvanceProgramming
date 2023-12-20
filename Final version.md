# Restaurant Management System 

This is a Python command-line application for a basic restaurant management system. The application allows users to interact with the system as either a "Restaurant" or a "Customer" to perform various actions related to managing the restaurant menu and placing orders.

youtube: [https://youtu.be/QDksIsXj9NE](https://www.youtube.com/watch?v=QDksIsXj9NE)

## Getting Started

To run the restaurant management system, you need Python 3.x installed on your machine. Clone this repository and navigate to the project's root directory in your terminal.

**Requirements:**
- Python 3.x
- colorama (install using `pip install colorama`)

## File Structure

- `restaurant_management.py`: The main Python script containing the implementation of the restaurant management system.
- `README.md`: This README file explaining the project and its usage.

## Usage

Run the `restaurant_management.py` script using the following command in your terminal:

```
python restaurant_management.py
```

## Classes and Methods

```python
from colorama import Fore, Style, init
init(autoreset=True)
```
- The code imports necessary modules from the `colorama` library, which is used for adding colored text to the terminal output. The `init(autoreset=True)` ensures that the color changes are automatically reset after each print statement.

```python
class InvalidInputError(Exception):
    pass
```
- Defines a custom exception class `InvalidInputError` which will be raised when there is an error related to invalid input.

```python
def validate_positive_number(value):
    try:
        number = float(value)
        if number < 0:
            raise InvalidInputError("Invalid input. Please enter a non-negative numeric value.")
        return number
    except ValueError:
        raise InvalidInputError("Invalid input. Please enter a numeric value.")
```
- A utility function `validate_positive_number` is defined to validate if a value is a positive numeric value. It attempts to convert the input to a float, and if successful, checks if it is a positive number. If not, it raises the `InvalidInputError` with appropriate error messages.

```python
def validate_menu_item(item):
    if not isinstance(item, MenuItem):
        raise InvalidInputError("Invalid item object provided.")
```
- Another utility function `validate_menu_item` is defined to validate if an object is an instance of the `MenuItem` class. If not, it raises the `InvalidInputError` with an error message.

```python
def validate_menu_item_name(item_name):
    if not isinstance(item_name, str):
        raise InvalidInputError("Invalid item name provided.")
```
- A utility function `validate_menu_item_name` is defined to validate if the provided item name is a string. If not, it raises the `InvalidInputError` with an error message.

```python
def validate_restaurant(restaurant):
    if not isinstance(restaurant, Restaurant):
        raise InvalidInputError("Invalid restaurant object provided.")
```
- A utility function `validate_restaurant` is defined to validate if an object is an instance of the `Restaurant` class. If not, it raises the `InvalidInputError` with an error message.

```python
def validate_menu(menu):
    if not isinstance(menu, Menu):
        raise InvalidInputError("Invalid menu object provided.")
```
- A utility function `validate_menu` is defined to validate if an object is an instance of the `Menu` class. If not, it raises the `InvalidInputError` with an error message.

```python
def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a valid integer.")
```
- The function `get_integer_input` takes a `prompt` as input and repeatedly prompts the user for input until a valid integer is entered. If an invalid input is provided, it prints an error message.

```python
def get_positive_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError()
            return value
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a non-negative numeric value.")
```
- The function `get_positive_float_input` takes a `prompt` as input and repeatedly prompts the user for input until a valid non-negative float is entered. If an invalid input is provided, it prints an error message.

```python
def get_non_empty_string_input(prompt):
    while True:
        value = input(prompt)
        if value.strip() == "":
            print(Fore.RED + "Invalid input. Please enter a non-empty string.")
        else:
            return value
```
- The function `get_non_empty_string_input` takes a `prompt` as input and repeatedly prompts the user for input until a non-empty string is entered. If an empty string is provided, it prints an error message.

```python
class Restaurant:
    def __init__(self, name, address, contact_info):
        self.name = name
        self.address = address
        self.contact_info = contact_info
        self.menu = {}
        self.order_history = OrderHistory()
```
- The `Restaurant` class is defined with an `__init__` method that initializes a new restaurant object with a name, address, contact information, an empty menu dictionary, and an instance of `OrderHistory` for keeping track of orders.

```python
def add_menu(self, menu):
    try:
        validate_menu(menu)
        self.menu = menu
    except InvalidInputError as e:
        print(Fore.RED + f"Error: {str(e)}")
```
- The `add_menu` method of the `Restaurant` class is defined to add a menu to the restaurant. It validates the menu using the `validate_menu` function and then sets the restaurant's menu attribute. If an invalid menu is provided, it prints an error message.

```python
def remove_menu(self):
    self.menu = {}
```
- The `remove_menu` method of the `Restaurant` class sets the restaurant's menu attribute to an empty dictionary, effectively removing the menu.

```python
def update_menu(self, menu):
    try:
        validate_menu(menu)
        self.menu = menu
    except InvalidInputError as e:
        print(Fore.RED + f"Error: {str(e)}")
```
- The `update_menu` method of the `Restaurant` class is defined to update the restaurant's menu. It validates the new menu using the `validate_menu` function and then sets the restaurant's menu attribute. If an invalid menu is provided, it prints an error message.

```python
def get_menu(self):
    return self.menu
```
- The `get_menu` method of the `Restaurant` class returns the restaurant's menu attribute.

```python
def get_order_history(self):
    return self.order_history
```
- The `get_order_history` method of the `Restaurant` class returns the restaurant's order history attribute.

```python
class Menu:
    def __init__(self):
        self.items = {}
```
- The `Menu` class is defined with an `__init__` method that initializes a new menu object with an empty dictionary for storing menu items.

```python
def add_item(self, item):
    try:
        validate_menu_item(item)
        self.items[item.name] = item
    except InvalidInputError as e:
        print(Fore.RED + f"Error: {str(e)}")
```
- The `add_item` method of the `Menu` class is defined to add an item to the menu. It validates the item using the `validate_menu_item` function and then adds the item to the `items` dictionary with the item's name as the key. If an invalid item is provided, it prints an error message.

```python
def remove_item(self, item_name):
    try:
        validate_menu_item_name(item_name)
        if item_name in self.items:
            del self.items[item_name]
            print(Fore.GREEN + "Item removed from the menu.")
        else:
            raise ValueError(Fore.RED + "Item not found in the menu.")
    except (InvalidInputError, ValueError) as e:
        print(Fore.RED + f"Error: {str(e)}")
```
- The

 `remove_item` method of the `Menu` class is defined to remove an item from the menu by its name. It validates the item name using the `validate_menu_item_name` function. If the item name is found in the `items` dictionary, the item is removed. If the item name is not found, it raises a ValueError. If any invalid input is provided, it prints an error message.

```python
def update_item(self, item_name, new_description, new_price):
    try:
        if not all(isinstance(arg, str) for arg in [item_name, new_description]):
            raise TypeError(Fore.RED + "Invalid arguments provided.")
        if not isinstance(new_price, (int, float)) or new_price < 0:
            raise ValueError(Fore.RED + "Invalid price. Please enter a non-negative numeric value.")
        if item_name in self.items:
            item = self.items[item_name]
            item.description = new_description
            item.price = new_price
        else:
            raise ValueError(Fore.RED + "Item not found in the menu.")
    except (TypeError, ValueError) as e:
        print(Fore.RED + f"Error: {str(e)}")
```
- The `update_item` method of the `Menu` class is defined to update an item in the menu with new description and price. It validates the input arguments for item name and description to be strings, and the new price to be a non-negative numeric value using appropriate checks. If the item name is found in the `items` dictionary, the item's description and price are updated. If the item name is not found, it raises a ValueError. If any invalid input is provided, it prints an error message.

```python
def get_items(self):
    return self.items
```
- The `get_items` method of the `Menu` class returns the dictionary of items in the menu.

```python
class MenuItem:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
```
- The `MenuItem` class is defined with an `__init__` method that initializes a new menu item object with a name, description, and price.

```python
class Customer:
    def __init__(self, name, address, contact_info):
        self.name = name
        self.address = address
        self.contact_info = contact_info
        self.order_history = []
```
- The `Customer` class is defined with an `__init__` method that initializes a new customer object with a name, address, contact information, and an empty list for order history.

```python
def place_order(self, restaurant, order_items):
    try:
        validate_restaurant(restaurant)
        if not isinstance(order_items, dict) or not all(
            isinstance(item, MenuItem)
            and isinstance(quantity, int)
            and quantity > 0
            for item, quantity in order_items.items()
        ):
            raise InvalidInputError("Invalid order_items provided.")

        items = []
        for item, quantity in order_items.items():
            items.extend([item] * quantity)

        order = Order(self, restaurant, items)
        self.order_history.append(order)
        restaurant.order_history.add_order(order)
        print(Fore.GREEN + "Order placed successfully.")
    except InvalidInputError as e:
        print(Fore.RED + f"Error: {str(e)}")
```
- The `place_order` method of the `Customer` class is defined to place an order with a restaurant. It validates the restaurant using the `validate_restaurant` function and the order_items using custom checks. If valid, it creates an order object with the customer, restaurant, and items. The order is added to the customer's order history and the restaurant's order history. If any invalid input is provided, it prints an error message.

```python
def view_order_history(self):
    if len(self.order_history) == 0:
        print(Fore.YELLOW + "No order history found.")
    else:
        for order in self.order_history:
            print(Fore.CYAN + "Order from:", order.restaurant.name)
            print("Restaurant Address:", order.restaurant.address)
            print("Restaurant Contact Info:", order.restaurant.contact_info)
            print("Customer:", order.customer.name)
            print("Customer Address:", order.customer.address)
            print("Customer Contact Info:", order.customer.contact_info)
            print(Fore.CYAN + "Items:")
            for item in order.items:
                print(Fore.CYAN + item.name, "-", item.price)
            print("Total price:", order.total_price)
```
- The `view_order_history` method of the `Customer` class displays the customer's order history. If there are no orders, it prints a message. Otherwise, it prints details of each order in the order history.
Continuing from the previous explanation:

```python
class Order:
    def __init__(self, customer, restaurant, items):
        self.customer = customer
        self.restaurant = restaurant
        self.items = items
        self.total_price = sum(item.price for item in items)
```
- The `Order` class is defined with an `__init__` method that initializes a new order object with a customer, restaurant, and a list of items. It calculates the total price of the order based on the prices of the items.

```python
class OrderHistory:
    def __init__(self):
        self.orders = []
```
- The `OrderHistory` class is defined with an `__init__` method that initializes a new order history object with an empty list for storing orders.

```python
def add_order(self, order):
    if not isinstance(order, Order):
        print(Fore.RED + "Invalid order object provided.")
    else:
        self.orders.append(order)
```
- The `add_order` method of the `OrderHistory` class is defined to add an order to the order history. It checks if the provided object is an instance of the `Order` class and then appends it to the `orders` list. If an invalid order object is provided, it prints an error message.

```python
def main():
    # ... (code for the main function and menu interactions, not provided in the previous code)

if __name__ == "__main__":
    main()
```
- The `main` function is defined to handle the interactions with the program's menu, but its implementation is not included in the provided code. The code block at the end ensures that the `main` function is called when the script is run.

Overall, the provided code consists of classes and methods that represent a simple ordering system involving restaurants, menus, menu items, customers, and order history. It uses utility functions to validate inputs and custom exception classes to handle errors. The code aims to be user-friendly, as it includes colored terminal output to highlight errors and success messages.

As the owner of the project, you can further enhance the code by implementing the `main` function and adding user interactions to make the program functional and user-friendly. Additionally, you might consider adding features such as saving and loading data to and from external files, implementing more advanced error handling, or improving the user interface for a more polished user experience.
Apologies for the oversight. Let's continue the detailed explanation of the code, line by line:

```python
if __name__ == "__main__":
    main()
```
- This block of code ensures that the `main()` function is executed only when the script is run as the main program (not when imported as a module).

```python
def main():
    restaurants = []
    customers = []
    selected_restaurant = None
    customer = None
    while True:
        print(Fore.CYAN + "In which section do you need changes?")
        print(Fore.GREEN + "1- Restaurant")
        print(Fore.BLUE + "2- Customer")
        print(Fore.RED + "E- Exit")
        print(Style.RESET_ALL)
        choice = input().lower()  # Convert input to lowercase for case-insensitivity

        if choice == "e":
            print(Fore.YELLOW + "Exiting the program...")
            break

        try:
            choice = int(choice)  # Convert input to integer

            if choice == 1:
                # ... (Code for handling restaurant section interactions)

            elif choice == 2:
                # ... (Code for handling customer section interactions)

            else:
                print(Fore.RED + "Invalid option. Please try again.")
        except ValueError:
            print(Fore.RED + "Invalid option. Please enter a valid number.")
```
- The `main()` function is the entry point of the program. It contains a loop that repeatedly displays a menu to the user and handles their choices based on different sections (Restaurant or Customer). The user can also choose to exit the program. It takes care of handling invalid inputs by catching `ValueError` and displaying appropriate error messages.

The explanations for the `Restaurant` and `Customer` classes, along with their methods, were provided in the previous explanations. The code below handles interactions specific to the `Restaurant` section:

```python
if choice == 1:
    if selected_restaurant is None:
        # ... (Code for restaurant login/registration)

    while selected_restaurant is not None:
        print(Fore.YELLOW + "Select the desired option:")
        print(Fore.MAGENTA + "1- Add item to menu")
        print(Fore.BLUE + "2- Remove item from menu")
        print(Fore.CYAN + "3- Update item in menu")
        print(Fore.GREEN + "4- Display menu")
        print(Fore.YELLOW + "5- Order history")
        print(Fore.RED + "L- Log out")
        option = input()

        if option.lower() == "l":
            selected_restaurant = None
            print(Fore.YELLOW + "Logged out successfully.")
            break

        option = int(option)

        if option == 1:
            # ... (Code for adding an item to the menu)

        elif option == 2:
            # ... (Code for removing an item from the menu)

        elif option == 3:
            # ... (Code for updating an item in the menu)

        elif option == 4:
            # ... (Code for displaying the menu)

        elif option == 5:
            # ... (Code for handling order history interactions)

        else:
            print(Fore.RED + "Invalid option. Please try again.")
```
- Within the `main()` function, when the user chooses option 1 (Restaurant section), it checks if the user is logged in as a restaurant or not. If not logged in, it handles restaurant login/registration. If logged in, it enters a nested loop where it displays a menu for restaurant-specific actions. The user can add, remove, update items, display the menu, view order history, or log out.

The code for handling interactions specific to the `Customer` section is as follows:

```python
elif choice == 2:
    if customer is None:
        # ... (Code for customer login/registration)

    while True:
        print(Fore.YELLOW + "Select the desired option:")
        print(Fore.CYAN + "1- Nearby restaurants")
        print(Fore.GREEN + "2- View order history")
        print(Fore.RED + "L- Log out")
        option = input()

        if option.lower() == "l":
            customer = None
            print(Fore.YELLOW + "Logged out successfully.")
            break

        option = int(option)

        if option == 1:
            # ... (Code for finding nearby restaurants and placing orders)

        elif option == 2:
            # ... (Code for viewing order history)

        else:
            print(Fore.RED + "Invalid option. Please try again.")
```
- Within the `main()` function, when the user chooses option 2 (Customer section), it checks if the user is logged in as a customer or not. If not logged in, it handles customer login/registration. If logged in, it enters a nested loop where it displays a menu for customer-specific actions. The user can find nearby restaurants, place orders, view order history, or log out.

## Contributing

This project is currently maintained by Amirhosein Javanmardy. If you find any issues or have suggestions for improvements, feel free to create a pull request or submit an issue in the repository.

## Acknowledgments

Thanks to the professors of Khatam University and my friends who accompanied me in this project.
