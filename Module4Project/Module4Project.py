# The DunnDelivery class demonstrates core OOP concepts:
# - Encapsulation: Data (menu and prices) and methods are bundled in the class.
# Abstraction: Complex delivery logic is hidden behind simple method calls.

class DunnDelivery:
    # Constructor method - creates a new instance of a delivery
    def __init__ (self): 
        # Class attributes demonstrate encapsulation 
        # by keeping related data together

        # Menu Attribute - menu of items you can order from delivery
        # Add 3 seasonal flavors to Coffee Drinks
        self.menu = {
            "Energy Drinks": ["Monster", "Rockstar"],
            "Coffee Drinks": ["Latte", "Cappuccino", "Pumpkin Spice", "Caramel Apple", "Witches Brew"],
            "Breakfast": ["Bagel", "Muffin", "Scone"],
            "Lunch": ["Falafel Wrap", "Hummus & Pita", "Chicken Wrap"]
        }

        # Prices encapsulated within the class
        # Add seasonal coffee prices
        self.prices = {
            "Monster": 3.99, "Rockstar": 3.99, 
            "Latte": 4.99, "Cappuccino": 4.99,
            "Pumpkin Spice": 5.99,
            "Caramel Apple": 5.99,
            "Witches Brew": 6.99,
            "Bagel": 2.99, "Muffin": 2.99,
            "Scone": 2.99, "Falafel Wrap": 8.99,
            "Hummus & Pita": 7.99, "Chicken Wrap": 8.99
        }

        # Delivery locations and number of minutes to deliver to that location
        self.delivery_locations = {
            "Library": 10,
            "Academic Success Center": 8,
            "ITEC Computer Lab": 5
        }

    # Show the menu of items available for delivery 
    def show_menu(self, category=None):
        if category:
            # Show the menu items for the chosen category
            print(f"\n=== {category} ===")
            # Loop through the items in that specific category on the menu 
            # and display them to the user
            for item in self.menu[category]:
                print(f"{item}: ${self.prices[item]:.2f}")
        else:
            # Show the entire menu
            for category in self.menu:
                # First, display the category name
                print(f"\n=== {category} ===")
                # Then display the items within the category
                for item in self.menu[category]:
                    print(f"{item}: ${self.prices[item]:.2f}")

    # Method to calculate the total cost of the order
    def calculate_total(self, items, has_student_id=False, priority_delivery=False):
        # student id is for calculating possible discount
        # Calculate the total
        total = sum(self.prices[item] for item in items)

        #  Calculate priority delivery into cost
        if priority_delivery:
            total += 2.0

        # Calculate the discount based on the student id
        if has_student_id and total > 10:
            total *= 0.9

        # Return the total cost of order to the code that...
        # called the method.
        return total

    # Method to calculate the delivery time based on location and time of day
    def estimate_delivery(self, location, current_hour, priority_delivery=False):
        # Calculate the base time for the delivery
        base_time = self.delivery_locations[location]
        # Calculate the delivery time based on the time of day (adjust for rush hour)
        if (9 <= current_hour <= 10) or (11 <= current_hour <= 13):
            return base_time + 5
        if priority_delivery:
            base_time -= 3
        # If they aren't ordering during rush hour, return the base time unaffected
        return base_time

    # Method to rate deliveries 1-5 stars
    # Elif condition used for grammatically correct print statements
    def delivery_rating(self, stars):
        if stars < 1 or stars > 5:
            print("Please rate 1 to 5 stars.")
        elif stars == 1:
            print(f"You rated your delivery {stars} star.")
        else:
            print(f"You rated your delivery {stars} stars.")

    # Method that prints the order (receipt)
    def print_order(self, location, items, current_hour, has_student_id=False, priority_delivery=False):
        # Display the order information
        print("\n=== Order Summary===")
        print(f"Delivery to: {location}")
        print("\nItems Ordered:")

        # Loop through the list of menu items the user ordered
        for item in items:
            print(f"- {item}: ${self.prices[item]:.2f}")

        # Call the methods to get the total cost and the delivery time
        total = self.calculate_total(items, has_student_id, priority_delivery)
        delivery_time = self.estimate_delivery(location, current_hour, priority_delivery)

        # Display the subtotal 
        print(f"\nSubtotal: ${sum(self.prices[item] for item in items):.2f}")

        # Calculate the total with the discount if the customer has a student id
        if has_student_id and total < sum(self.prices[item] for item in items):
            print("Student discount applied!")

        # If priority delivery was chosen by the user, print this statement.
        if priority_delivery is True:
            print(f"You selected priority delivery.")

        # Display total after discount & delivery time
        print(f"Total after discount: ${total:.2f}")
        print(f"Estimated delivery time: {delivery_time} minutes")

    # Create search_items method to search menu items under a specified amount by the user
    def search_items(self, search_input):
        print(f"\n=== Menu Items Under ${search_input:.2f} ===")
        items_under_price = []
        for item, price in self.prices.items():
            if price <= search_input:
                items_under_price.append(f"{item}: ${price:.2f}")
        if items_under_price:
            print("\n".join(items_under_price))
        else:
            print("No items found under that price.")


# main method is executed as soon as the program runs
def main():
    # Create a new delivery object - instantiating a new object,
    delivery = DunnDelivery()

    # use while True to search for menu items under specified conditions
    # use try-except block to catch value errors inputted by the user (non-float input)
    while True:
        try:
            search_input = float(input("Search for menu items under dollar amount: $"))
            delivery.search_items(search_input)
            break
        except ValueError:
            print("Invalid search input.")

    # Show menu
    delivery.show_menu("Coffee Drinks")

    # Sample order at 9:30 am (peak morning hour)
    order = ["Latte", "Bagel"]

    # Display receipt for the order
    delivery.print_order("ITEC Computer Lab", order, 9, has_student_id=True, priority_delivery=True)

    # Ask user to rate their delivery 1-5 stars
    while True:
        try:
            rating = int(input("Please rate your delivery 1-5 stars: "))
            delivery.delivery_rating(rating)
            break
        except ValueError:
            print("Invalid rating.")
            break

# Add the line of code to automatically call the main method
if __name__ == "__main__":
    main()

