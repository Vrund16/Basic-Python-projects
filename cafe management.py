import datetime
import random

menu = {
    "C101": {"name": "Coffee", "price": 50},
    "T102": {"name": "Tea", "price": 30},
    "S103": {"name": "Sandwich", "price": 70},
    "B104": {"name": "Burger", "price": 100},
    "P105": {"name": "Pastry", "price": 60}
}

order = {}

def show_menu():
    print("\n" + "-"*40)
    print("{:^40}".format("CAFFE MENU"))
    print("-"*40)
    print("{:<6} {:<15} {:>10}".format("Code", "Item", "Price (₹)"))
    print("-"*40)
    for code, item in menu.items():
        print(f"{code:<6} {item['name']:<15} ₹{item['price']:>10}")
    print("-"*40)

def take_order():
    show_menu()
    while True:
        code = input("\nEnter item code (or 'done' to finish): ").upper()
        if code == 'DONE':
            break
        elif code in menu:
            try:
                qty = int(input(f"Enter quantity for {menu[code]['name']}: "))
                if qty <= 0:
                    print("Quantity must be at least 1.")
                    continue
                if code in order:
                    order[code]["qty"] += qty
                else:
                    order[code] = {"name": menu[code]["name"], "price": menu[code]["price"], "qty": qty}
                print(f"✔️  {qty} x {menu[code]['name']} added to your cart.")
            except ValueError:
                print("❌ Invalid quantity. Please enter a number.")
        else:
            print("❌ Invalid code. Please choose from the menu.")

def clear_cart():
    global order
    order.clear()
    print("🧹 Cart cleared successfully.")

def generate_bill(customer_name):
    if not order:
        print("🛒 Your cart is empty. No bill to generate.")
        return
    
    print("\n" + "="*45)
    print("{:^45}".format("CAFFE BILL"))
    print("="*45)
    print(f"Customer: {customer_name}")
    now = datetime.datetime.now()
    print("Date:", now.strftime("%Y-%m-%d"), "Time:", now.strftime("%H:%M:%S"))
    order_id = random.randint(1000, 9999)
    print(f"Order ID: #{order_id}")
    print("-"*45)
    print("{:<15} {:<5} {:<8} {:>10}".format("Item", "Qty", "Price", "Subtotal"))
    print("-"*45)
    
    total = 0
    for item in order.values():
        subtotal = item["price"] * item["qty"]
        total += subtotal
        print("{:<15} {:<5} ₹{:<7} ₹{:>8}".format(item["name"], item["qty"], item["price"], subtotal))
    
    print("-"*45)
    print(f"{'Total Amount':<30} ₹{total:>10}")
    print("="*45)
    print("✅ Thank you for visiting our Caffe!\n")

def main():
    print("="*45)
    print("{:^45}".format("WELCOME TO PYTHON CAFFE"))
    print("="*45)
    customer_name = input("Enter Customer Name: ").title()
    
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Show Menu")
        print("2. Take Order")
        print("3. Generate Bill")
        print("4. Clear Cart")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            show_menu()
        elif choice == "2":
            take_order()
        elif choice == "3":
            generate_bill(customer_name)
            break
        elif choice == "4":
            clear_cart()
        elif choice == "5":
            print("👋 Exiting the system. Have a great day!")
            break
        else:
            print("❌ Invalid choice. Please enter 1 to 5.")

main()
