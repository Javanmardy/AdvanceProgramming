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

### Menu

The `Menu` class represents a menu and has the following attributes:

- `items`: A dictionary that stores `MenuItem` objects, where the keys are the names of the items.

The `Menu` class provides methods to add, remove, and update items in the menu, as well as retrieve the current list of items.

### MenuItem

The `MenuItem` class represents a single item on the menu and has the following attributes:

- `name`: The name of the item.
- `description`: A description of the item.
- `price`: The price of the item.

### Customer

The `Customer` class represents a customer and has the following attributes:

- `name`: The name of the customer.
- `address`: The address of the customer.
- `contact_info`: The contact information of the customer.
- `order_history`: A list of `Order` objects representing the customer's order history.

The `Customer` class provides methods to place an order and view the order history.

### Order

The `Order` class represents an order placed by a customer and has the following attributes:

- `customer`: The `Customer` object who placed the order.
- `restaurant`: The `Restaurant` object from which the order was placed.
- `items`: A list of `MenuItem` objects representing the items ordered.
- `total_price`: The total price of the order.

The `Order` class provides methods to add and remove items from the order, as well as calculate the total price of the order.

### OrderHistory

The `OrderHistory` class is a utility class to manage a collection of orders. It has the following attributes:

- `orders`: A list of `Order` objects representing the order history.

The `OrderHistory` class provides methods to add, remove, and view orders in the history.

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

Please note that this implementation is a basic example and may require further refinement and enhancements based on specific requirements.
