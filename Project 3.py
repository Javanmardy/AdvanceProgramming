from colorama import Fore, Style, init

# Initialize colorama for colored text
init(autoreset=True)


class InvalidInputError(Exception):
    pass


def validate_positive_number(value):
    try:
        number = float(value)
        if number < 0:
            raise InvalidInputError(
                "Invalid input. Please enter a non-negative numeric value."
            )
        return number
    except ValueError:
        raise InvalidInputError("Invalid input. Please enter a numeric value.")


def validate_menu_item(item):
    if not isinstance(item, MenuItem):
        raise InvalidInputError("Invalid item object provided.")


def validate_menu_item_name(item_name):
    if not isinstance(item_name, str):
        raise InvalidInputError("Invalid item name provided.")


def validate_restaurant(restaurant):
    if not isinstance(restaurant, Restaurant):
        raise InvalidInputError("Invalid restaurant object provided.")


def validate_menu(menu):
    if not isinstance(menu, Menu):
        raise InvalidInputError("Invalid menu object provided.")


def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a valid integer.")


def get_positive_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError()
            return value
        except ValueError:
            print(
                Fore.RED + "Invalid input. Please enter a non-negative numeric value."
            )


def get_non_empty_string_input(prompt):
    while True:
        value = input(prompt)
        if value.strip() == "":
            print(Fore.RED + "Invalid input. Please enter a non-empty string.")
        else:
            return value


class Restaurant:
    def __init__(self, name, address, contact_info):
        self.name = name
        self.address = address
        self.contact_info = contact_info
        self.menu = {}
        self.order_history = OrderHistory()

    def add_menu(self, menu):
        try:
            validate_menu(menu)
            self.menu = menu
        except InvalidInputError as e:
            print(Fore.RED + f"Error: {str(e)}")

    def remove_menu(self):
        self.menu = {}

    def update_menu(self, menu):
        try:
            validate_menu(menu)
            self.menu = menu
        except InvalidInputError as e:
            print(Fore.RED + f"Error: {str(e)}")

    def get_menu(self):
        return self.menu

    def get_order_history(self):
        return self.order_history


class Menu:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        try:
            validate_menu_item(item)
            self.items[item.name] = item
        except InvalidInputError as e:
            print(Fore.RED + f"Error: {str(e)}")

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

    def update_item(self, item_name, new_description, new_price):
        try:
            if not all(isinstance(arg, str) for arg in [item_name, new_description]):
                raise TypeError(Fore.RED + "Invalid arguments provided.")
            if not isinstance(new_price, (int, float)) or new_price < 0:
                raise ValueError(
                    Fore.RED
                    + "Invalid price. Please enter a non-negative numeric value."
                )
            if item_name in self.items:
                item = self.items[item_name]
                item.description = new_description
                item.price = new_price
            else:
                raise ValueError(Fore.RED + "Item not found in the menu.")
        except (TypeError, ValueError) as e:
            print(Fore.RED + f"Error: {str(e)}")

    def get_items(self):
        return self.items


class MenuItem:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price


class Customer:
    def __init__(self, name, address, contact_info):
        self.name = name
        self.address = address
        self.contact_info = contact_info
        self.order_history = []

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


class Order:
    def __init__(self, customer, restaurant, items):
        self.customer = customer
        self.restaurant = restaurant
        self.items = items
        self.total_price = self.calculate_total_price()

    def add_item(self, item):
        try:
            validate_menu_item(item)
            self.items.append(item)
            self.total_price = self.calculate_total_price()
            print(Fore.GREEN + "Item added to the order.")
        except InvalidInputError as e:
            print(Fore.RED + f"Error: {str(e)}")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            self.total_price = self.calculate_total_price()
            print(Fore.GREEN + "Item removed from the order.")
        else:
            print(Fore.RED + "Item not found in the order.")

    def calculate_total_price(self):
        total = 0
        for item in self.items:
            total += item.price
        return total


class OrderHistory:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)
        print(Fore.GREEN + "Order added to the history.")

    def remove_order(self, order):
        if order in self.orders:
            self.orders.remove(order)
            print(Fore.GREEN + "Order removed from the history.")
        else:
            print(Fore.RED + "Order not found in the history.")

    def view_orders(self):
        if len(self.orders) == 0:
            print(Fore.YELLOW + "No orders found in the history.")
        else:
            for order in self.orders:
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
                print()

    def count_item_orders(self, item_name):
        count = 0
        for order in self.orders:
            for item in order.items:
                if item.name == item_name:
                    count += 1
        return count


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
                if selected_restaurant is None:
                    contact_info = input(Fore.YELLOW + "Enter the phone number: ")

                    matching_restaurants = [
                        restaurant
                        for restaurant in restaurants
                        if restaurant.contact_info.lower() == contact_info.lower()
                    ]

                    if matching_restaurants:
                        selected_restaurant = matching_restaurants[0]
                        print(Fore.GREEN + "Restaurant login successful.")
                    else:
                        restaurant_name = input("Enter the restaurant name: ")
                        address = input("Enter the restaurant address: ")
                        selected_restaurant = Restaurant(
                            restaurant_name, address, contact_info
                        )
                        selected_restaurant.menu = Menu()
                        selected_restaurant.order_history = OrderHistory()
                        restaurants.append(selected_restaurant)
                        print(
                            Fore.GREEN + "New restaurant account created and logged in."
                        )

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
                        item_name = input("Enter the item name: ")
                        item_description = input("Enter the item description: ")
                        item_price = 0
                        try:
                            item_price = float(input("Enter the item price: "))
                        except ValueError:
                            print(
                                Fore.RED
                                + "Invalid price. Please enter a numeric value."
                            )

                        item = MenuItem(item_name, item_description, item_price)
                        selected_restaurant.menu.add_item(item)
                        print(Fore.GREEN + "Item added to the menu.")

                    elif option == 2:
                        if not selected_restaurant.menu.get_items():
                            print(Fore.YELLOW + "No items in the menu.")
                        else:
                            print(Fore.GREEN + "Menu Items:")
                            for i, (item_name, item) in enumerate(
                                selected_restaurant.menu.get_items().items(), start=1
                            ):
                                print(f"{i}. {item_name} - {item.price}")

                            item_index = 0
                            try:
                                item_index = (
                                    int(input("Select the item number to remove: ")) - 1
                                )
                            except ValueError:
                                print(
                                    Fore.RED
                                    + "Invalid input. Please enter a valid item number."
                                )

                            if item_index < 0 or item_index >= len(
                                selected_restaurant.menu.get_items()
                            ):
                                print(Fore.RED + "Invalid item selection.")
                            else:
                                selected_item = list(
                                    selected_restaurant.menu.get_items().values()
                                )[item_index]
                                selected_restaurant.menu.remove_item(selected_item.name)

                    elif option == 3:
                        if not selected_restaurant.menu.get_items():
                            print(Fore.YELLOW + "No items in the menu.")
                        else:
                            print(Fore.GREEN + "Menu Items:")
                            for i, (item_name, item) in enumerate(
                                selected_restaurant.menu.get_items().items(), start=1
                            ):
                                print(f"{i}. {item_name} - {item.price}")

                            item_index = 0
                            try:
                                item_index = (
                                    int(input("Select the item number to update: ")) - 1
                                )
                            except ValueError:
                                print(
                                    Fore.RED
                                    + "Invalid input. Please enter a valid item number."
                                )

                            if item_index < 0 or item_index >= len(
                                selected_restaurant.menu.get_items()
                            ):
                                print(Fore.RED + "Invalid item selection.")
                            else:
                                selected_item = list(
                                    selected_restaurant.menu.get_items().values()
                                )[item_index]

                                new_description = input(
                                    f"Enter the new description for {selected_item.name}: "
                                )
                                new_price = 0
                                try:
                                    new_price = float(
                                        input(
                                            f"Enter the new price for {selected_item.name}: "
                                        )
                                    )
                                except ValueError:
                                    print(
                                        Fore.RED
                                        + "Invalid price. Please enter a numeric value."
                                    )

                                selected_restaurant.menu.update_item(
                                    selected_item.name,
                                    new_description,
                                    new_price,
                                )
                                print(Fore.GREEN + "Item updated.")

                    elif option == 4:
                        items = selected_restaurant.menu.get_items()
                        if not items:
                            print(Fore.YELLOW + "No items in the menu.")
                        else:
                            print(Fore.GREEN + "Menu Items:")
                            for i, (item_name, item) in enumerate(
                                items.items(), start=1
                            ):
                                print(f"{i}. {item_name} - {item.price}")

                    elif option == 5:
                        print(Fore.YELLOW + "Select the desired option:")
                        print(Fore.CYAN + "1- Count of item orders")
                        print(Fore.GREEN + "2- View all orders with details")
                        sub_option = input()

                        sub_option = int(sub_option)

                        if sub_option == 1:
                            print(
                                Fore.CYAN + "Logged in Restaurant:",
                                selected_restaurant.name,
                            )
                            menu_items = selected_restaurant.menu.get_items()
                            if not menu_items:
                                print(Fore.YELLOW + "No items in the menu.")
                            else:
                                print(Fore.GREEN + "Menu Items:")
                                for i, (item_name, item) in enumerate(
                                    menu_items.items(), start=1
                                ):
                                    print(f"{i}. {item_name}")

                                item_index = 0
                                try:
                                    item_index = (
                                        int(
                                            input(
                                                "Select the item number to count orders: "
                                            )
                                        )
                                        - 1
                                    )
                                except ValueError:
                                    print(
                                        Fore.RED
                                        + "Invalid input. Please enter a valid item number."
                                    )

                                if item_index < 0 or item_index >= len(menu_items):
                                    print(Fore.RED + "Invalid item selection.")
                                else:
                                    selected_item = list(menu_items.values())[
                                        item_index
                                    ]
                                    count = selected_restaurant.order_history.count_item_orders(
                                        selected_item.name
                                    )
                                    print(
                                        Fore.GREEN
                                        + f"The item '{selected_item.name}' has been ordered {count} times."
                                    )

                        elif sub_option == 2:
                            selected_restaurant.order_history.view_orders()

                        else:
                            print(Fore.RED + "Invalid option. Please try again.")

                    else:
                        print(Fore.RED + "Invalid option. Please try again.")

            elif choice == 2:
                if customer is None:
                    contact_info = input(Fore.YELLOW + "Enter your phone number: ")

                    existing_customer = None
                    for c in customers:
                        if c.contact_info == contact_info:
                            existing_customer = c
                            break

                    if existing_customer:
                        customer = existing_customer
                        print(Fore.GREEN + "Customer login successful.")
                    else:
                        customer_name = input("Enter your name: ")
                        address = input("Enter your address: ")
                        customer = Customer(customer_name, address, contact_info)
                        customers.append(customer)
                        print(Fore.GREEN + "New customer registered and logged in.")

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
                        if customer is None:
                            print(Fore.RED + "Please register as a customer first.")
                            continue

                        matching_restaurants = [
                            restaurant
                            for restaurant in restaurants
                            if restaurant.address.lower() == customer.address.lower()
                        ]

                        if not matching_restaurants:
                            print(
                                Fore.YELLOW
                                + "No restaurants found with the same address."
                            )
                            continue

                        print(Fore.GREEN + "Available Restaurants:")
                        for i, restaurant in enumerate(matching_restaurants, start=1):
                            print(f"{i}. {restaurant.name}")

                        selected_restaurant_index = 0
                        try:
                            selected_restaurant_index = (
                                int(input("Select a restaurant: ")) - 1
                            )
                        except ValueError:
                            print(
                                Fore.RED
                                + "Invalid input. Please enter a valid restaurant number."
                            )

                        if (
                            selected_restaurant_index < 0
                            or selected_restaurant_index >= len(matching_restaurants)
                        ):
                            print(Fore.RED + "Invalid restaurant selection.")
                            continue

                        selected_restaurant = matching_restaurants[
                            selected_restaurant_index
                        ]

                        while True:
                            print(Fore.YELLOW + "Select the desired option:")
                            print(Fore.MAGENTA + "1- Add item")
                            print(Fore.BLUE + "2- Remove item")
                            print(Fore.CYAN + "3- Calculate total price")
                            print(Fore.RED + "B- Go back")
                            option = input()

                            if option.lower() == "b":
                                break

                            option = int(option)

                            if option == 1:
                                menu = selected_restaurant.get_menu()
                                if menu:
                                    items = menu.get_items()
                                    if items:
                                        print(Fore.GREEN + "Menu Items:")
                                        for i, (item_name, item) in enumerate(
                                            items.items(), start=1
                                        ):
                                            print(f"{i}. {item_name} - {item.price}")
                                        selected_item_index = 0
                                        try:
                                            selected_item_index = (
                                                int(input("Select an item: ")) - 1
                                            )
                                        except ValueError:
                                            print(
                                                Fore.RED
                                                + "Invalid input. Please enter a valid item number."
                                            )

                                        if (
                                            selected_item_index < 0
                                            or selected_item_index >= len(items)
                                        ):
                                            print(Fore.RED + "Invalid item selection.")
                                            continue

                                        selected_item = list(items.values())[
                                            selected_item_index
                                        ]
                                        quantity = get_integer_input(
                                            "Enter the quantity for the selected item: "
                                        )
                                        order_items = {selected_item: quantity}
                                        customer.place_order(
                                            selected_restaurant, order_items
                                        )

                                    else:
                                        print(Fore.YELLOW + "No items in the menu.")
                                else:
                                    print(
                                        Fore.RED + "No menu found for the restaurant."
                                    )

                            elif option == 2:
                                order = (
                                    customer.order_history[-1]
                                    if customer.order_history
                                    else None
                                )

                                if order:
                                    items = order.items
                                    if items:
                                        print(Fore.GREEN + "Order Items:")
                                        for i, item in enumerate(items, start=1):
                                            print(f"{i}. {item.name} - {item.price}")
                                        selected_item_index = 0
                                        try:
                                            selected_item_index = (
                                                int(input("Select an item to remove: "))
                                                - 1
                                            )
                                        except ValueError:
                                            print(
                                                Fore.RED
                                                + "Invalid input. Please enter a valid item number."
                                            )

                                        if (
                                            selected_item_index < 0
                                            or selected_item_index >= len(items)
                                        ):
                                            print(Fore.RED + "Invalid item selection.")
                                            continue

                                        selected_item = items[selected_item_index]
                                        order.remove_item(selected_item)
                                        print(
                                            Fore.GREEN + "Item removed from the order."
                                        )
                                    else:
                                        print(Fore.YELLOW + "No items in the order.")
                                else:
                                    print(Fore.RED + "No order placed yet.")

                            elif option == 3:
                                order = (
                                    customer.order_history[-1]
                                    if customer.order_history
                                    else None
                                )

                                if order:
                                    total_price = order.calculate_total_price()
                                    print(
                                        Fore.GREEN + f"Customer Name: {customer.name}"
                                    )
                                    print(Fore.GREEN + f"Address: {customer.address}")
                                    print(
                                        Fore.GREEN
                                        + f"Contact Info: {customer.contact_info}"
                                    )
                                    print(Fore.CYAN + "Order Items:")
                                    for item in order.items:
                                        print(Fore.CYAN + f"{item.name} - {item.price}")
                                    print(Fore.GREEN + f"Total Price: {total_price}")
                                else:
                                    print(Fore.YELLOW + "No order placed yet.")

                            else:
                                print(Fore.RED + "Invalid option. Please try again.")

                    elif option == 2:
                        if customer is None:
                            print(Fore.RED + "Please register as a customer first.")
                            continue

                        customer.view_order_history()

                    else:
                        print(Fore.RED + "Invalid option. Please try again.")

            else:
                print(Fore.RED + "Invalid option. Please try again.")
        except ValueError:
            print(Fore.RED + "Invalid option. Please enter a valid number.")


if __name__ == "__main__":
    main()
