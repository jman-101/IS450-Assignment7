"""
IS 450 - Assignment 7
File: myProgram.py
Description: Order total and discount calculator demonstrating functions,
             dictionaries, loops, conditionals, and formatted output.
"""

MENU = {
    "Coffee": 3.50,
    "Latte": 5.00,
    "Cold Brew": 4.50,
    "Muffin": 3.75,
    "Bagel": 4.00
}

def display_menu(menu_items):
    print("----- Wolf Pack Café Menu -----")
    for item, price in menu_items.items():
        print(f"{item:<12} : ${price:.2f}")
    print("-------------------------------")

def calculate_discount(subtotal):
    if subtotal >= 15.00:
        return subtotal * 0.10
    return 0.0

def process_order():
    display_menu(MENU)
    order_items = []
    
    print("Enter item names from the menu (type 'done' to complete order):")
    while True:
        choice = input("Enter item: ").strip()
        if choice.lower() == "done":
            break
        
        matched_item = None
        for item in MENU:
            if item.lower() == choice.lower():
                matched_item = item
                break
        
        if matched_item:
            order_items.append(matched_item)
            print(f"Added {matched_item} (${MENU[matched_item]:.2f})")
        else:
            print("Item not found on menu. Please try again.")

    if not order_items:
        print("\nNo items ordered.")
        return

    subtotal = sum(MENU[item] for item in order_items)
    discount = calculate_discount(subtotal)
    tax = (subtotal - discount) * 0.0825
    final_total = (subtotal - discount) + tax

    print("\n========== Order Receipt ==========")
    for item in order_items:
        print(f"1x {item:<12} : ${MENU[item]:.2f}")
    print("-----------------------------------")
    print(f"Subtotal      : ${subtotal:.2f}")
    if discount > 0:
        print(f"Discount (10%): -${discount:.2f}")
    print(f"Tax (8.25%)   : ${tax:.2f}")
    print(f"Final Total   : ${final_total:.2f}")
    print("===================================")

if __name__ == "__main__":
    process_order()