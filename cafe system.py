
class Drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, drink):
        self.items.append(drink)
        print(f"Added {drink.name} to your order!")

    def calculate_total_price(self):
        return sum(item.price for item in self.items)

    def show_order_summary(self):
        if not self.items:
            print("No items in your order.")
            return

        print("\n================")
        print("== Your Order ==")
        print("================")

        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} || {item.price}$")

        print(f"Total: {self.calculate_total_price()}$\n")

    def checkout(self):
        if not self.items:
            print("Your cart is empty.")
            return

        self.show_order_summary()

        confirm = input(
            "Proceed to checkout? [Y/N]: "
        ).strip().lower()

        if confirm in ("yes", "y"):
            print("Order confirmed. Thank you!")
            self.items.clear()

        elif confirm in ("no", "n"):
            print("Checkout cancelled.")

        else:
            print("Invalid choice. Checkout cancelled.")


def main():
    menu = [
        Drink("Turkish", 15),
        Drink("Espresso Single", 20),
        Drink("Espresso Double", 35),
        Drink("Mocha", 25),
        Drink("Cappuccino", 35),
        Drink("Tea", 10),
        Drink("Green Tea", 10),
        Drink("Mint", 10),
        Drink("Hot Chocolate", 30),
        Drink("Yansoon", 10),
        Drink("Shisha Kas", 25),
        Drink("Shisha Fwakeh", 35),
        Drink("Water", 7)
    ]

    current_order = Order()

    while True:
        print("\n================")
        print("== Cafe Menu ==")
        print("================")

        for i, drink in enumerate(menu, 1):
            print(f"{i}. {drink.name} - {drink.price}$")

        print("_" * 40)

        print(f"{len(menu) + 1}. View Order")
        print(f"{len(menu) + 2}. Checkout")
        print(f"{len(menu) + 3}. Exit")

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Invalid choice. Please enter a number!")
            continue

        if 1 <= choice <= len(menu):
            current_order.add_item(menu[choice - 1])

        elif choice == len(menu) + 1:
            current_order.show_order_summary()

        elif choice == len(menu) + 2:
            current_order.checkout()

        elif choice == len(menu) + 3:
            print("Thank you for visiting. Goodbye!")
            break

        else:
            print("Invalid choice. Try again!")


if __name__ == "__main__":
    main()
