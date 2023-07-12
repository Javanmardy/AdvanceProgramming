# Restaurant Ordering System

The Restaurant Ordering System is a simple implementation of a restaurant ordering system using Python classes. It allows a customer to place an order at a restaurant, view their order history, and perform actions such as adding/removing items from the order, updating menu items, and managing the order history.

## Classes

### Restaurant

The `Restaurant` class represents a restaurant and contains the following attributes:

- `name`: The name of the restaurant.
- `address`: The address of the restaurant.
- `contact_info`: The contact information of the restaurant.
- `menu`: A dictionary containing the menu items.

The `Restaurant` class provides methods to add, remove, update, and retrieve the menu.

### Menu

The `Menu` class represents a menu and contains the following attributes:

- `items`: A dictionary containing the menu items.

The `Menu` class provides methods to add, remove, update, and retrieve menu items.

### MenuItem

The `MenuItem` class represents an item on the menu and contains the following attributes:

- `name`: The name of the menu item.
- `description`: The description of the menu item.
- `price`: The price of the menu item.

### Customer

The `Customer` class represents a customer and contains the following attributes:

- `name`: The name of the customer.
- `address`: The address of the customer.
- `contact_info`: The contact information of the customer.
- `order_history`: A list containing the order history of the customer.

The `Customer` class provides methods to place an order at a restaurant, view order history, and perform actions such as adding/removing items from the order.

### Order

The `Order` class represents an order placed by a customer and contains the following attributes:

- `customer`: The customer who placed the order.
- `restaurant`: The restaurant where the order was placed.
- `items`: A list of items ordered.
- `total_price`: The total price of the order.

The `Order` class provides methods to add and remove items from the order and calculate the total price.

### OrderHistory

The `OrderHistory` class represents the history of orders placed by customers and contains the following attributes:

- `orders`: A list of orders.

The `OrderHistory` class provides methods to add, remove, and view orders.

## Usage

To use the Restaurant Ordering System, you can create instances of the `Restaurant`, `Menu`, `Customer`, and `Order` classes, and interact with their methods. The provided `main()` function demonstrates some sample usage scenarios, such as creating a restaurant, menu, customer, placing an order, updating menu items, removing menu items, and viewing order history.

Please note that this implementation provides a basic structure for a restaurant ordering system and may not include all the necessary error handling and validation. You can further extend and customize the code to meet your specific requirements.

## License

This code is provided under the [MIT License](https://opensource.org/licenses/MIT). You are free to modify, distribute, and use the code for personal and commercial purposes.
