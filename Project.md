---
# Restaurant Ordering System

This is a simple implementation of a restaurant ordering system. It consists of several classes that model various entities and their interactions within the system.

## Classes

### Restaurant

The `Restaurant` class represents a restaurant and has the following attributes:

- `name`: The name of the restaurant.
- `address`: The address of the restaurant.
- `contact_info`: The contact information of the restaurant.
- `menu`: An instance of the `Menu` class representing the menu of the restaurant.

The `Restaurant` class provides methods to add, remove, and update the menu, as well as retrieve the current menu.

```python
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
```

### Menu

The `Menu` class represents a menu and has the following attributes:

- `items`: A dictionary that stores `MenuItem` objects, where the keys are the names of the items.

The `Menu` class provides methods to add, remove, and update items in the menu, as well as retrieve the current list of items.

```python
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
```

### MenuItem

The `MenuItem` class represents a single item on the menu and has the following attributes:

- `name`: The name of the item.
- `description`: A description of the item.
- `price`: The price of the item.

```python
class MenuItem:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
```

### Customer

The `Customer` class represents a customer and has the following attributes:

- `name`: The name of the customer.
- `address`: The address of the customer.
- `contact_info`: The contact information of the customer.
- `order_history`: A list of `Order` objects representing the customer's order history.

The `Customer` class provides methods to place an order and view the order history.

```python
class Customer:
    def __init__(self, name, address, contact_info):
        self.name = name
        self.address = address
        self.contact_info = contact_info
        self.order_history = []

    def place_order(self, restaurant, items):
        order = Order(self, restaurant, items)
        self.order_history.append(order)
        print("Order placed successfully.")

    def view_order_history(self):
        if len(self.order_history) == 0:
            print("No order history found.")
        else:
            for order in self.order_history:
                print("Order from:", order.restaurant.name)
                print("Items:")
                for item in order.items:
                    print(item.name, "-", item.price)
                print("Total price:", order.total_price)
```

### Order

The `Order` class represents an order placed by a customer and has the following attributes:

- `customer`: The `Customer` object who placed the order.
- `restaurant`: The `Restaurant` object from which the order was placed.
- `items`: A list of `MenuItem` objects representing the items ordered.
- `total_price`: The total price of the order.

The `Order` class provides methods to add and remove items from the order, as well as calculate the total price of the order.

```python
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
```

### OrderHistory

The `OrderHistory` class is a utility class to manage a collection of orders. It has the following attributes:

- `orders`: A list of `Order` objects representing the order history.

The `OrderHistory` class provides methods to add, remove, and view orders in the history.

```python
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
                print("Items:")
                for item in order.items:
                    print(item.name, "-", item.price)
                print("Total price:", order.total_price)
```

## Code Usage

The `main()` function demonstrates the usage of the classes by creating instances of `Restaurant`, `Menu`, and `Customer`. It then performs the following actions:

1. Creates a restaurant and a menu, and adds items to the menu.
2. Creates a customer and places an order by selecting items from the menu.
3. Views the order history of the customer.
4. Adds and removes items from the order.
5. Updates a menu item.
6. Removes a menu item.
7. Views the updated menu.
8. Views the order history again.
9. Removes an order from the history.
10. Views the updated order history.

```python
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
    item2

 = MenuItem(
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
```

Please note that this implementation is a basic example and may require further refinement and enhancements based on specific requirements.

---
You can copy the above Markdown code and save it as `README.md` in your project directory or wherever you want to include the README file.
