# Module 7 Assignment: Organizing Data with Lists and Tuples
# TechElectronics Inventory Tracking System

# we print our message that starts the code.
print("=" * 60)
print("TECHELECTRONICS INVENTORY TRACKING SYSTEM")
print("=" * 60)

# TODO 1: Create product tuples
# Each product is a tuple: (product_id, name, price, quantity, category)

product1 = ("P001", "AI smartphone", 799.99, 10, "Mobile Phones")
product2 = ("P002", "Professional Touch Computer", 1299.99, 5, "Laptops")
product3 = ("P003", "Wireless Headphones", 199.99, 15, "Audio")
product4 = ("P004", "Cinema Sound System", 1499.99, 3, "Audio")
product5 = ("P005", "Dj Mixer", 889.99, 20, "Audio")#these tuples help us because they cannot be changed, so we will always have the same products

# TODO 2: Create an inventory list containing all product tuples
inventory = [product1, product2, product3, product4, product5]

# TODO 3: Display all products
print("\nCurrent Inventory:")
print("-" * 60)

for product in inventory:
    print(product)
#this will showcase our current inventory, all the products with their specifics
# TODO 4: Access specific elements
print("\n\nAccessing Specific Products:")
print("-" * 60)

first_product = inventory[0] #our 1st product has index 0, it will display our AI smartphone
last_product = inventory[-1] #for our last product, we reverse-search, and look up index -1.
third_product_name = inventory[2][1] #index 2 selects our third product because index 0 is the 1st one, and then we select index 1 inside the product, for its name to show up
second_price = inventory[1][2] #same here, index 1 selects 2nd product, inside it we choose index 2 which is its price.
second_quantity = inventory[1][3] # on the same index 1 we look index 3, to look for its quantity

print("First product:", first_product)
print("Last product:", last_product)
print("Third product name:", third_product_name)
print("Second product price:", second_price)
print("Second product quantity:", second_quantity)

# TODO 5: Use slicing to get subsets
print("\n\nProduct Subsets Using Slicing:")
print("-" * 60)

first_three = inventory[:3]
middle_products = inventory[1:4]
all_except_first = inventory[1:]

print("First three:", first_three)
print("Middle products:", middle_products)
print("All except first:", all_except_first) #we use slicing to cut off different products for our list, and then display what is left

# TODO 6: Add new products to inventory
print("\n\nAdding New Products:")
print("-" * 60)

product6 = ("P006", "2-in-1 iPad", 599.99, 7, "Mobile Phones")
product7 = ("P007", "Two-way waterproof speaker", 249.99, 4, "Audio")

inventory.append(product6)
inventory.append(product7) #we use .append to add the new products to the end of the list

print("Updated Inventory:", inventory)

# TODO 7: Remove a product
print("\n\nRemoving a Product:")
print("-" * 60)

removed_product = inventory.pop(2) #we use .pop to remove our selected product from the list

print("Removed product:", removed_product)
print("Updated Inventory:", inventory)

# TODO 8: Insert a product at a specific position
print("\n\nInserting a Product:")
print("-" * 60)

product8 = ("P008", "Wearable Health Monitor", 399.99, 12, "Mobile Phones")

inventory.insert(1, product8) #we use .insert and then the index where we want to put the product

print("Updated Inventory:", inventory)

#now, we need to recheck our products
first_product = inventory[0]
last_product = inventory[-1]
third_product_name = inventory[2][1]
second_price = inventory[1][2]
second_quantity = inventory[1][3]

first_three = inventory[:3]
middle_products = inventory[2:5]
all_except_first = inventory[1:]

# TODO 9: Create category lists
mobile_phones = []
laptops = []
audio = []

print("\n\nProducts by Category:")
print("-" * 60)

for product in inventory:
    if product[4] == "Mobile Phones":
        mobile_phones.append(product)
    elif product[4] == "Laptops":
        laptops.append(product)
    elif product[4] == "Audio":
        audio.append(product)

print("Mobile Phones:", mobile_phones)
print("Laptops:", laptops)
print("Audio:", audio)

# TODO 10: Calculate inventory statistics
print("\n\nInventory Statistics:")
print("-" * 60)

total_products = len(inventory)

total_value = sum(product[2] * product[3] for product in inventory)

product_names = [product[1] for product in inventory]
product_prices = [product[2] for product in inventory]

print("Total products:", total_products)
print("Total inventory value:", total_value)
print("Product names:", product_names)
print("Product prices:", product_prices)

# TODO 11: Find expensive products using list comprehension
print("\n\nExpensive Products (> $500):")
print("-" * 60)

expensive_products = [product for product in inventory if product[2] > 500] #all products above $500 will be added

print(expensive_products)

# TODO 12: Low stock alert using list comprehension
print("\n\nLow Stock Alert (< 5 units):")
print("-" * 60)

low_stock = [product for product in inventory if product[3] < 5]

print(low_stock)

# TODO 13: Create price list using list comprehension
print("\n\nPrice Lists:")
print("-" * 60)

original_prices = [product[2] for product in inventory]
discounted_prices = [price * 0.9 for price in original_prices]

print("Original prices:", original_prices)
print("Discounted prices:", discounted_prices)

# TODO 14: Product name formatting using list comprehension
print("\n\nFormatted Product Names:")
print("-" * 60)

uppercase_names = [product[1].upper() for product in inventory] #puts all of the names in capital letters. 

product_codes = [product[0][:3] + product[1][:3] for product in inventory]

print("Uppercase names:", uppercase_names)
print("Product codes:", product_codes)

# TODO 15: Using Loops to Process Inventory
print("\n\nLoop-Based Analysis:")
print("-" * 60)

mobile_count = 0
laptop_value = 0
most_expensive = inventory[0]

for product in inventory:
    if product[4] == "Mobile Phones":
        mobile_count += 1

    if product[4] == "Laptops":
        laptop_value += product[2] * product[3]

    if product[2] > most_expensive[2]:
        most_expensive = product

print("Mobile phone count:", mobile_count)
print("Total laptop value:", laptop_value)
print("Most expensive product:", most_expensive)

# TODO 16: Using Conditionals with Lists
print("\n\nConditional Analysis:")
print("-" * 60)

restock_list = []
high_value_items = []

price_ranges = {
    "under_100": 0,
    "100_to_500": 0,
    "over_500": 0
}

for product in inventory:

    if product[3] < 5:
        restock_list.append(product)

    if product[2] > 500 and product[3] > 10:
        high_value_items.append(product)

    if product[2] < 100:
        price_ranges["under_100"] += 1
    elif 100 <= product[2] <= 500:
        price_ranges["100_to_500"] += 1
    else:
        price_ranges["over_500"] += 1

print("Restock list:", restock_list)
print("High value items:", high_value_items)
print("Price ranges:", price_ranges)

# TODO 17: Define and Use Functions

def calculate_product_value(product):
    return product[2] * product[3]

def find_products_by_category(inventory, category):
    return [product for product in inventory if product[4] == category]

def apply_discount(inventory, discount_percent):
    new_inventory = []
    for product in inventory:
        new_price = product[2] * (1 - discount_percent / 100)
        new_product = (product[0], product[1], new_price, product[3], product[4])
        new_inventory.append(new_product)
    return new_inventory

print("\n\nFunction-Based Operations:")
print("-" * 60)

total_inventory_value = sum(calculate_product_value(p) for p in inventory)

audio_products = find_products_by_category(inventory, "Audio") #will find all the audio type products

discounted_inventory = apply_discount(inventory, 15) #this will add the 15% discount rate to the product

print("Total inventory value:", total_inventory_value)
print("Audio products:", audio_products)
print("Discounted inventory:", discounted_inventory)

# TODO 18: Inventory report function

def generate_inventory_report(inventory):

    total_products = len(inventory)
    total_value = sum(product[2] * product[3] for product in inventory)

    categories = list(set(product[4] for product in inventory))

    low_stock = [product for product in inventory if product[3] < 5]

    average_price = sum(product[2] for product in inventory) / total_products

    report = {
        "total_products": total_products,
        "total_value": total_value,
        "categories": categories,
        "low_stock": low_stock,
        "average_price": average_price
    }

    return report
#we use this function to generate our report with the desired variables 

print("\n\nComprehensive Inventory Report:")
print("-" * 60)

report = generate_inventory_report(inventory)

print(report)
#lastly, we print our final report