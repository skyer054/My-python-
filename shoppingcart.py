#shopping Cart 

foods =[]
prices = []
drinks = []
total = 0

while True:
    food = input("Enter food you want to buy or press q to quit : ")
    if food.lower() == 'q':
        break
    else:
        food_price = float(input(f"Enter the price of the {food}: R"))
        drink = input("Enter drink you want (or press n if you don't want a drink): ")
    if drink.lower() == 'n':
        drink = "No drink"
        drink_price = 0
    else:
        drink_price = float(input(f"Enter the price of {drink}: R"))
        
        foods.append(food)
        prices.append(food_price + drink_price)
        drinks.append(drink)
        
        
print("\n-----YOUR CART-----\n")

for food in foods:
    print(food)
    
for drink in drinks :
    print(drink)
    
for price in prices:
    total += price

    
    
print("\n")
    
print(f"Your total is: R{total}")