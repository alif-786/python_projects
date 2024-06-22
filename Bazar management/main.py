from colorama import Fore, Style
from tabulate import tabulate

class Product:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

class Cart:
    def __init__(self):
        self.products = list()

    def add_product(self, product):
        self.products.append(product)

    def total(self):
        total = sum(product.price * product.qty for product in self.products)
        return total

def get_receipt(ct, total):
    print(Fore.GREEN + Style.BRIGHT + "Receipt" + Style.RESET_ALL)
    print(Fore.YELLOW + "-" * 40 + Style.RESET_ALL)

    table_data = []
    for product in ct.products:
        table_data.append([product.name, product.price, product.qty, product.price * product.qty])

    # Calculate the grand total
    grand_total = sum(product.price * product.qty for product in ct.products)

    # Add the grand total row to the table data

    headers = ["Product", "Price", "Quantity", "Total"]
    table = tabulate(table_data, headers=headers, tablefmt="grid")
    print(Fore.CYAN + table + Style.RESET_ALL)

    print(Fore.CYAN + f"Grand Total: {grand_total}" + Style.RESET_ALL)
    print(Fore.YELLOW + "-" * 40 + Style.RESET_ALL)

def menu():
    print(Fore.BLUE + Style.BRIGHT + "WELCOME TO BAZAR MANAGEMENT SYSTEM" + Style.RESET_ALL)
    print(Fore.YELLOW + "-" * 40 + Style.RESET_ALL)
    print(Fore.CYAN + "1. Add product to cart")
    print("2. Calculate total")
    print("3. Get receipt")
    print("4. Exit" + Style.RESET_ALL)

def main():
    ct = Cart()

    while True:
        menu()
        choice = int(input(Fore.MAGENTA + "Enter your choice: " + Style.RESET_ALL))

        if choice == 1:
            name = input(Fore.YELLOW + "Enter product name: " + Style.RESET_ALL)
            price = int(input(Fore.YELLOW + "Enter product price: " + Style.RESET_ALL))
            quantity = int(input(Fore.YELLOW + "Enter product quantity: " + Style.RESET_ALL))

            prod = Product(name, price, quantity)
            ct.add_product(prod)

        elif choice == 2:
            total = ct.total()
            print(Fore.GREEN + f"Total amount: {total}" + Style.RESET_ALL)

        elif choice == 3:
            total = ct.total()
            get_receipt(ct, total)

        elif choice == 4:
            print(Fore.BLUE + Style.BRIGHT + "Thank you for using Bazar Management System!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
