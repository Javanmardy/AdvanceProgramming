class Restaurant:
    def __init__(self, name, address, contact_info):
        self.name = name
        self.address = address
        self.contact_info = contact_info
        self.menu = {}
        self.order_history = OrderHistory()

    def add_menu(self, menu):
        self.menu = menu

    def remove_menu(self):
        self.menu = {}

    def update_menu(self, menu):
        self.menu = menu

    def get_menu(self):
        return self.menu

    def get_order_history(self):
        return self.order_history


class Menu:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item

    def remove_item(self, item_name):
        try:
            if item_name in self.items:
                del self.items[item_name]
                print("Item removed from the menu.")
            else:
                raise ValueError("Item not found in the menu.")
        except ValueError as e:
            print(f"Error: {str(e)}")

    def update_item(self, item_name, new_name, new_description, new_price):
        if item_name in self.items:
            item = self.items[item_name]
            item.name = new_name
            item.description = new_description
            item.price = new_price
        else:
            print("Item not found in the menu.")

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

    def place_order(self, restaurant, items):
        try:
            if not isinstance(restaurant, Restaurant):
                raise TypeError("Invalid restaurant object provided.")
            if not all(isinstance(item, MenuItem) for item in items):
                raise TypeError("Invalid items provided.")

            order = Order(self, restaurant, items)
            self.order_history.append(order)
            restaurant.order_history.add_order(order)
            print("Order placed successfully.")
        except TypeError as e:
            print(f"Error: {str(e)}")

    def view_order_history(self):
        if len(self.order_history) == 0:
            print("No order history found.")
        else:
            for order in self.order_history:
                print("Order from:", order.restaurant.name)
                print("Restaurant Address:", order.restaurant.address)
                print("Restaurant Contact Info:", order.restaurant.contact_info)
                print("Customer:", order.customer.name)
                print("Customer Address:", order.customer.address)
                print("Customer Contact Info:", order.customer.contact_info)
                print("Items:")
                for item in order.items:
                    print(item.name, "-", item.price)
                print("Total price:", order.total_price)


class Order:
    def __init__(self, customer, restaurant, items):
        self.customer = customer
        self.restaurant = restaurant
        self.items = items
        self.total_price = self.calculate_total_price()

    def add_item(self, item):
        try:
            if not isinstance(item, MenuItem):
                raise TypeError("Invalid item object provided.")

            self.items.append(item)
            self.total_price = self.calculate_total_price()
            print("Item added to the order.")
        except TypeError as e:
            print(f"Error: {str(e)}")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            self.total_price = self.calculate_total_price()
            print("Item removed from the order.")
        else:
            print("Item not found in the order.")

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
        print("Order added to the history.")

    def remove_order(self, order):
        if order in self.orders:
            self.orders.remove(order)
            print("Order removed from the history.")
        else:
            print("Order not found in the history.")

    def view_orders(self):
        if len(self.orders) == 0:
            print("No orders found in the history.")
        else:
            for order in self.orders:
                print("Order from:", order.restaurant.name)
                print("Restaurant Address:", order.restaurant.address)
                print("Restaurant Contact Info:", order.restaurant.contact_info)
                print("Customer:", order.customer.name)
                print("Customer Address:", order.customer.address)
                print("Customer Contact Info:", order.customer.contact_info)
                print("Items:")
                for item in order.items:
                    print(item.name, "-", item.price)
                print("Total price:", order.total_price)
                print()

    def count_item_orders(self, item_name):
        count = 0
        for order in self.orders:
            for item in order.items:
                if item.name.lower() == item_name.lower():
                    count += 1
        return count


def main():
    restaurants = []
    customers = []
    selected_restaurant = None
    customer = None
    while True:
        print("In which section do you need changes?")
        print("1- Restaurant")
        print("2- Customer")
        print("E- Exit")
        choice = input()

        if choice.lower() == "e":
            print("Exiting the program...")
            break

        choice = int(choice)

        if choice == 1:
            if selected_restaurant is None:
                restaurant_name = input("Enter the restaurant name: ")
                address = input("Enter the restaurant address: ")
                contact_info = input("Enter the contact information: ")

                matching_restaurants = [
                    restaurant
                    for restaurant in restaurants
                    if (
                        restaurant.name.lower() == restaurant_name.lower()
                        and restaurant.address.lower() == address.lower()
                        and restaurant.contact_info.lower() == contact_info.lower()
                    )
                ]

                if matching_restaurants:
                    selected_restaurant = matching_restaurants[0]
                    print("Restaurant login successful.")
                else:
                    selected_restaurant = Restaurant(
                        restaurant_name, address, contact_info
                    )
                    selected_restaurant.menu = Menu()
                    selected_restaurant.order_history = OrderHistory()
                    restaurants.append(selected_restaurant)
                    print("New restaurant account created and logged in.")

            while selected_restaurant is not None:
                print("Select the desired option:")
                print("1- Add item to menu")
                print("2- Remove item from menu")
                print("3- Update item in menu")
                print("4- Display menu")
                print("5- Order history")
                print("L- Log out")
                option = input()

                if option.lower() == "l":
                    selected_restaurant = None
                    print("Logged out successfully.")
                    break

                option = int(option)

                if option == 1:
                    item_name = input("Enter the item name: ")
                    item_description = input("Enter the item description: ")
                    item_price = float(input("Enter the item price: "))

                    item = MenuItem(item_name, item_description, item_price)
                    selected_restaurant.menu.add_item(item)
                    print("Item added to the menu.")

                elif option == 2:
                    if not selected_restaurant.menu.get_items():
                        print("No items in the menu.")
                    else:
                        print("Menu Items:")
                        for i, (item_name, item) in enumerate(
                            selected_restaurant.menu.get_items().items(), start=1
                        ):
                            print(f"{i}. {item_name} - {item.price}")

                        item_index = (
                            int(input("Select the item number to remove: ")) - 1
                        )

                        if item_index < 0 or item_index >= len(
                            selected_restaurant.menu.get_items()
                        ):
                            print("Invalid item selection.")
                        else:
                            selected_item = list(
                                selected_restaurant.menu.get_items().values()
                            )[item_index]
                            selected_restaurant.menu.remove_item(selected_item.name)

                elif option == 3:
                    if not selected_restaurant.menu.get_items():
                        print("No items in the menu.")
                    else:
                        print("Menu Items:")
                        for i, (item_name, item) in enumerate(
                            selected_restaurant.menu.get_items().items(), start=1
                        ):
                            print(f"{i}. {item_name} - {item.price}")

                        item_index = (
                            int(input("Select the item number to update: ")) - 1
                        )

                        if item_index < 0 or item_index >= len(
                            selected_restaurant.menu.get_items()
                        ):
                            print("Invalid item selection.")
                        else:
                            selected_item = list(
                                selected_restaurant.menu.get_items().values()
                            )[item_index]

                            new_name = input(
                                f"Enter the new name for {selected_item.name}: "
                            )
                            new_description = input(
                                f"Enter the new description for {selected_item.name}: "
                            )
                            new_price = float(
                                input(f"Enter the new price for {selected_item.name}: ")
                            )

                            selected_restaurant.menu.update_item(
                                selected_item.name,
                                new_name,
                                new_description,
                                new_price,
                            )
                            print("Item updated.")

                elif option == 4:
                    items = selected_restaurant.menu.get_items()
                    if not items:
                        print("No items in the menu.")
                    else:
                        print("Menu Items:")
                        for i, (item_name, item) in enumerate(items.items(), start=1):
                            print(f"{i}. {item_name} - {item.price}")

                elif option == 5:
                    print("Select the desired option:")
                    print("1- Count of item orders")
                    print("2- View all orders with details")
                    sub_option = input()

                    sub_option = int(sub_option)

                    if sub_option == 1:
                        print("Logged in Restaurant:", selected_restaurant.name)
                        menu_items = selected_restaurant.menu.get_items()
                        if not menu_items:
                            print("No items in the menu.")
                        else:
                            print("Menu Items:")
                            for i, (item_name, item) in enumerate(
                                menu_items.items(), start=1
                            ):
                                print(f"{i}. {item_name}")

                            item_index = (
                                int(input("Select the item number to count orders: "))
                                - 1
                            )

                            if item_index < 0 or item_index >= len(menu_items):
                                print("Invalid item selection.")
                            else:
                                selected_item = list(menu_items.values())[item_index]
                                count = (
                                    selected_restaurant.order_history.count_item_orders(
                                        selected_item.name
                                    )
                                )
                                print(
                                    f"The item '{selected_item.name}' has been ordered {count} times."
                                )

                    elif sub_option == 2:
                        selected_restaurant.order_history.view_orders()

                    else:
                        print("Invalid option. Please try again.")

                else:
                    print("Invalid option. Please try again.")

        elif choice == 2:
            if customer is None:
                customer_name = input("Enter your name: ")
                address = input("Enter your address: ")
                contact_info = input("Enter your contact information: ")

                existing_customer = None
                for c in customers:
                    if (
                        c.name == customer_name
                        and c.address == address
                        and c.contact_info == contact_info
                    ):
                        existing_customer = c
                        break

                if existing_customer:
                    customer = existing_customer
                    print("Customer login successful.")
                else:
                    customer = Customer(customer_name, address, contact_info)
                    customers.append(customer)
                    print("New customer registered and logged in.")

            while True:
                print("Select the desired option:")
                print("1- Nearby restaurants")
                print("2- View order history")
                print("L- Log out")
                option = input()

                if option.lower() == "l":
                    customer = None
                    print("Logged out successfully.")
                    break

                option = int(option)

                if option == 1:
                    if customer is None:
                        print("Please register as a customer first.")
                        continue

                    matching_restaurants = [
                        restaurant
                        for restaurant in restaurants
                        if restaurant.address.lower() == customer.address.lower()
                    ]

                    if not matching_restaurants:
                        print("No restaurants found with the same address.")
                        continue

                    print("Available Restaurants:")
                    for i, restaurant in enumerate(matching_restaurants, start=1):
                        print(f"{i}. {restaurant.name}")

                    selected_restaurant_index = int(input("Select a restaurant: ")) - 1

                    if (
                        selected_restaurant_index < 0
                        or selected_restaurant_index >= len(matching_restaurants)
                    ):
                        print("Invalid restaurant selection.")
                        continue

                    selected_restaurant = matching_restaurants[
                        selected_restaurant_index
                    ]

                    while True:
                        print("Select the desired option:")
                        print("1- Add item")
                        print("2- Remove item")
                        print("3- Calculate total price")
                        print("B- Go back")
                        option = input()

                        if option.lower() == "b":
                            break

                        option = int(option)

                        if option == 1:
                            menu = selected_restaurant.get_menu()
                            if menu:
                                items = menu.get_items()
                                if items:
                                    print("Menu Items:")
                                    for i, (item_name, item) in enumerate(
                                        items.items(), start=1
                                    ):
                                        print(f"{i}. {item_name} - {item.price}")
                                    selected_item_index = (
                                        int(input("Select an item: ")) - 1
                                    )

                                    if (
                                        selected_item_index < 0
                                        or selected_item_index >= len(items)
                                    ):
                                        print("Invalid item selection.")
                                        continue

                                    selected_item = list(items.values())[
                                        selected_item_index
                                    ]
                                    customer.place_order(
                                        selected_restaurant, [selected_item]
                                    )
                                    print("Item added to the order.")
                                else:
                                    print("No items in the menu.")
                            else:
                                print("No menu found for the restaurant.")

                        elif option == 2:
                            order = (
                                customer.order_history[-1]
                                if customer.order_history
                                else None
                            )

                            if order:
                                items = order.items
                                if items:
                                    print("Order Items:")
                                    for i, item in enumerate(items, start=1):
                                        print(f"{i}. {item.name} - {item.price}")
                                    selected_item_index = (
                                        int(input("Select an item to remove: ")) - 1
                                    )

                                    if (
                                        selected_item_index < 0
                                        or selected_item_index >= len(items)
                                    ):
                                        print("Invalid item selection.")
                                        continue

                                    selected_item = items[selected_item_index]
                                    order.remove_item(selected_item)
                                    print("Item removed from the order.")
                                else:
                                    print("No items in the order.")
                            else:
                                print("No order placed yet.")

                        elif option == 3:
                            order = (
                                customer.order_history[-1]
                                if customer.order_history
                                else None
                            )

                            if order:
                                total_price = order.calculate_total_price()
                                print(f"Customer Name: {customer.name}")
                                print(f"Address: {customer.address}")
                                print(f"Contact Info: {customer.contact_info}")
                                print("Order Items:")
                                for item in order.items:
                                    print(f"{item.name} - {item.price}")
                                print(f"Total Price: {total_price}")
                            else:
                                print("No order placed yet.")

                        else:
                            print("Invalid option. Please try again.")

                elif option == 2:
                    if customer is None:
                        print("Please register as a customer first.")
                        continue

                    customer.view_order_history()

                else:
                    print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
