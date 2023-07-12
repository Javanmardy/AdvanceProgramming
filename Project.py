class Restaurant:
    def __init__(self, name, address, contact_info):
        self.name = name
        self.address = address
        self.contact_info = contact_info
        self.menu = {}

    def add_menu(self, menu):
        self.menu = menu

    def remove_menu(self):
        self.menu = {}

    def update_menu(self, menu):
        self.menu = menu

    def get_menu(self):
        return self.menu


class Menu:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
        else:
            print("Item not found in the menu.")
            print()
            print(
                "----------------------------------------------------------------------------------------------------------------------------------------------------------"
            )
            print()

    def update_item(self, item_name, new_name, new_description, new_price):
        if item_name in self.items:
            item = self.items[item_name]
            item.name = new_name
            item.description = new_description
            item.price = new_price
        else:
            print("Item not found in the menu.")
            print()
            print(
                "----------------------------------------------------------------------------------------------------------------------------------------------------------"
            )
            print()

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
        order = Order(self, restaurant, items)
        self.order_history.append(order)
        print(
            "----------------------------------------------------------------------------------------------------------------------------------------------------------"
        )
        print()
        print("Order placed successfully.")
        print()
        print(
            "----------------------------------------------------------------------------------------------------------------------------------------------------------"
        )
        print()

    def view_order_history(self):
        if len(self.order_history) == 0:
            print("No order history found.")
            print()
            print(
                "----------------------------------------------------------------------------------------------------------------------------------------------------------"
            )
            print()
        else:
            for order in self.order_history:
                print("Order from:", order.restaurant.name)
                print("Items:")
                for item in order.items:
                    print(item.name, "-", item.price)
                print("Total price:", order.total_price)
            print()
            print(
                "----------------------------------------------------------------------------------------------------------------------------------------------------------"
            )
            print()


class Order:
    def __init__(self, customer, restaurant, items):
        self.customer = customer
        self.restaurant = restaurant
        self.items = items
        self.total_price = self.calculate_total_price()

    def add_item(self, item):
        self.items.append(item)
        self.total_price = self.calculate_total_price()
        print("Item added to the order.")
        print()
        print(
            "----------------------------------------------------------------------------------------------------------------------------------------------------------"
        )
        print()

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            self.total_price = self.calculate_total_price()
            print("Item removed from the order.")
        else:
            print("Item not found in the order.")
        print()
        print(
            "----------------------------------------------------------------------------------------------------------------------------------------------------------"
        )
        print()

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
        print()
        print(
            "----------------------------------------------------------------------------------------------------------------------------------------------------------"
        )
        print()

    def remove_order(self, order):
        if order in self.orders:
            self.orders.remove(order)
            print("Order removed from the history.")
        else:
            print("Order not found in the history.")
        print()
        print(
            "----------------------------------------------------------------------------------------------------------------------------------------------------------"
        )
        print()

    def view_orders(self):
        if len(self.orders) == 0:
            print("No orders found in the history.")
        else:
            for order in self.orders:
                print("Order from:", order.restaurant.name)
                print("Items:")
                for item in order.items:
                    print(item.name, "-", item.price)
                print("Total price:", order.total_price)
        print()
        print(
            "----------------------------------------------------------------------------------------------------------------------------------------------------------"
        )
        print()


def main():
    # Create a restaurant
    restaurant = Restaurant(
        "Perperook",
        "East Tehran - Tehranpars, West 142 St., between Rashid and 113 St., No. 108",
        "1541",
    )

    # Create a menu
    menu = Menu()
    item1 = MenuItem(
        "BBQ Chicken Pizza",
        "Barbecue chicken, mushroom sauce with black peppercorns, special Parproc cheese",
        230050,
    )
    item2 = MenuItem(
        "Pizza Plus Margarita Jumbo Size",
        "A combination of 2 types of pizza including: 16 slices of window pizza (ham, sausage, mushrooms, bell pepper) and 9 slices of margarita",
        299000,
    )
    item3 = MenuItem(
        "Sicilian Mixed Pizza",
        "Meat ham, sausage, mushrooms, green and colored bell peppers, mozzarella cheese, special sauce and cheese",
        207500,
    )
    menu.add_item(item1)
    menu.add_item(item2)
    menu.add_item(item3)
    restaurant.add_menu(menu)

    # Create a customer
    customer = Customer(
        "Amirhosein Javanmardy",
        "Tehran, Tehran Pars, first floor of Tehran Pars, Ezzatullah province",
        "09990000000",
    )

    # Place an order
    order_items = [item1, item2]
    customer.place_order(restaurant, order_items)

    # View order history
    customer.view_order_history()

    # Add and remove items from the order
    order = customer.order_history[0]
    order.add_item(item3)
    order.remove_item(item2)

    # Update a menu item
    menu.update_item(
        "BBQ Chicken Pizza",
        "Perproc Cheeseburger",
        "130 grams of special Perprok burger, Gouda cheese, lettuce, tomato, pickled cucumber, onion, special sauce, along with a mayonnaise and garlic sachet and a special Perprok ketchup",
        199500,
    )

    # Remove a menu item
    menu.remove_item("Sicilian Mixed Pizza")

    # View the updated menu
    menu_items = menu.get_items()
    for item_name, item in menu_items.items():
        print("Item:", item_name)
        print("Description:", item.description)
        print("Price:", item.price)
    print()
    print(
        "----------------------------------------------------------------------------------------------------------------------------------------------------------"
    )
    print()
    # View order history again
    customer.view_order_history()

    # Remove an order from history
    order_history = customer.order_history
    if len(order_history) > 0:
        order_to_remove = order_history[0]
        customer.order_history.remove(order_to_remove)

    # View updated order history
    customer.view_order_history()


if __name__ == "__main__":
    main()
