import time

def display_menu(menu):
    """Display the menu with item numbers, names, and prices"""
    print('\n-------- Menu --------')
    for item_number, item_details in menu.items():
        print(f"{item_number}. {item_details['name']} - RM{item_details['price']:.2f}")
    print('----------------------')

def display_option(option):
    """Display the option with option numbers, names and prices"""
    print(f'\n-------- Option ---------')
    for option_number, option_details in option.items():
        print(f"{option_number}. {option_details['name']}")
    print('-------------------------')

def take_order(menu):
    order = {}
    while True:
        choice = input("Please enter the item number or 'done' to finish: ")
        if choice == 'done':
            break
        elif choice.isdigit() and int(choice) in menu:
            item_number = int(choice)
            item_name = menu[item_number]['name']
            while True:
                try:
                    quantity = int(input(f'How many do you want {item_name}: '))
                    if quantity > 0:
                        break
                    else:
                        print('Quantity must be at least 1')
                except ValueError:
                    print('Please enter a number')
            if item_name in order:
                order[item_name] += quantity
            else:
                order[item_name] = quantity
            print(f'{item_name} x {quantity} added to your order')
        else:
            print("Please enter listed item number only or 'done': ")
    return order

def remove_item(order):
    while True:
        choice = input("Please enter the item name from your order to remove or 'done' to finish: ")
        if choice.lower() == 'done':
            break
        elif choice in order:
            item_quantity = order[choice]
            while True:
                try:
                    remove_quantity = int(input(f'How many {choice} do you want to remove: '))
                    if remove_quantity >= item_quantity:
                        del order[choice]
                        break
                    elif remove_quantity > 0:
                        order[choice] -= remove_quantity
                        break
                    else:
                        print('Quantity must be at least 1')
                except ValueError:
                    print('Please enter a number')
        else:
            print("Please enter item name from your order only or 'done': ")
    return order

def calculate_total(order, menu):
    """Calculate the total cost of the orders"""
    total = 0
    print('\n------ Your Order -------')
    for item_name, quantity in order.items(): ## Loop each item in the order
    # Find the price of the item in the menu
        for item_details in menu.values():
            if item_details['name'] == item_name:
                price_per_item = item_details['price'] ## Look up item price in the menu
                break
                
        item_cost = price_per_item * quantity
        total += item_cost
        
        print(f'{item_name} x {quantity} - RM{item_cost:.2f}')
    print(f'Total: ${total:.2f}')
    print('-------------------------')
    return total
                
def after_order(option, order, menu):
    while True:
        try:
            choice = input("\nPlease choose to edit your order or proceed to payment: ")
            if choice == '1':
                new_order = take_order(menu)
                for item, quantity in new_order.items():
                    order[item] = order.get(item, 0) + quantity
                calculate_total(order,menu)
            elif choice == '2':
                remove_item(order)
                calculate_total(order, menu)
            elif choice == '3':
                print('\nProceeding to payment...')
                time.sleep(1)
                calculate_total(order, menu)
                print('\nYour order will be deliver shortly')
            else:
                print('\nThank you!\nPlease come again!')
                time.sleep(1)
                break
        except ValueError:
            print('Please enter listed option numbers only')
    return order

def main():
    """Main function to run the ordering system."""
    menu = {
        1: {'name': 'Burger', 'price': 5.00},
        2: {'name': 'Fries', 'price': 3.50},
        3: {'name': 'Soda', 'price': 1.50},
        4: {'name': 'Pizza Slice', 'price': 4.50},
        5: {'name': 'Salad', 'price': 3.50}
    }

    option = {
        1: {'name': 'Add more items'},
        2: {'name': 'Delete an item'},
        3: {'name': 'Payment'},
        4: {'name': 'Exit'}
        }

    print('Welcome! We serve foods and drinks for you\nPlease take a look at our menu')
    display_menu(menu)
    customer_order = take_order(menu)
    time.sleep(1)
    if customer_order: ## If user picked something
        calculate_total(customer_order, menu)
    else: ## If user didnt order anything
        print("Your order is empty. Please try again.")

    display_option(option)
    customer_option = after_order(option, customer_order, menu)

if __name__ == "__main__":
    main()
    

