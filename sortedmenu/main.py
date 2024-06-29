# Sorted Burgers
# Menu+Prices list

#list of items: Chicken, Cheeseburger Fish, Grilled Steak, Philly Cheesesteak, Shroom, Turkey Sandwich, Veggie

#prices: 7.49, 8.49, 5.49, 12.99, 8.99,
#7.49, 0.99, 64.49 

#Solution 1: OOP with Linear Search 
class Menu:
  def __init__(self, name, price):
    self.name = name
    self.price = price

chicken = Menu("Chicken", 7.49)
cheeseBurger= Menu("Cheeseburger", 8.49)
fish = Menu("Fish", 5.49)
grilledSteak = Menu("Grilled Steak", 12.99)
phillyCheesesteak= Menu ("Philly Cheesesteak", 8.99)
shroom= Menu("Shroom", 7.49)
turkeySandwich = Menu("Turkey Sandwich", 0.99)
veggie = Menu ("Veggie", 64.99)


foods = [
    chicken, cheeseBurger, fish, grilledSteak, phillyCheesesteak, shroom, turkeySandwich, veggie 
]

orders = [
  ["Chicken", "Turkey Sandwich"],
  ["Veggie"]
]

for order in orders:
  total = 0
  for item in order:
   for food in foods:
    if(food.name == item):
      total += food.price
  print(total)

#Solution 2:
#Binary Search Algorithm
#MUST (array has to be sorted)
#Key Value would be the user input
#list of items and their prices
#no user input  - have datas instead

items_and_prices= [
  ("chicken", 7.49),
  ("Cheeseburger",8.49),
  ("Fish", 5.49),
  ("Grilled Steak",12.99),
  ("Philly cheesesteak",8.99),
  ("Turkey Sandwich", 10.99),
  ("shroom",7.49),
  ("Veggie",64.99)
]

def binary_search(items, key):
    left = 0
    right = len(items) - 1

    while left <= right:
        mid = left + (right - left) // 2
        mid_item, _ = items[mid]

        if mid_item == key:
            return mid
        elif mid_item < key:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # if the item is not found


#calculation the total 

def item_total(total_items):
    total_items.sort()  # Ensure selected items are sorted
    total_price = 0
    
    for item in total_items:
        index = binary_search(items_and_prices, item)
        if index != -1:
            _, price = items_and_prices[index]
            total_price += price
        else:
            print(f"Item '{item}' not found in the menu.")
            
    return total_price

user_input = ["Fish", "Grilled Steak", "Philly cheesesteak"]
#user_input = ["ham", "Grilled Steak", "Philly cheesesteak"]

total = item_total(user_input)
print(f"Total price: ${total:.2f}")



  
  
    
  
  
