def vendingmachine(var):
    print("|############################################|")
    print("|#|                           |##############|")
    print("|#|  =====  ..--''`  |~~``|   |##|````````|##|")
    print("|#|  |   |  \     |  :    |   |##| Exact  |##|")
    print("|#|  |___|   /___ |  | ___|   |##| Change |##|")
    print("|#|  /=__\  ./.__\   |/,__\   |##| Only   |##|")
    print("|#|  \__//   \__//    \__//   |##|________|##|")
    print("|#|===========================|##############|")
    print("|#|```````````````````````````|##############|")
    print("|#| =.._      +++     //////  |##############|")
    print("|#| \/  \     | |     \    \  |#|`````````|##|")
    print(f"|#|  \___\    |_|     /___ /  |#|  {user}      |##|")
    print("|#|  / __\\  /|_|\   // __\    |#| |1|2|3| |##|")
    print("|#|  \__//-  \|_//   -\__//   |#| |4|5|6| |##|")
    print("|#|===========================|#| |7|8|9| |##|")
    print("|#|```````````````````````````|#| ``````` |##|")
    print("|#| ..--    ______   .--._.   |#|[=======]|##|")
    print("|#| \   \   |    |   |    |   |#|  _   _  |##|")
    print("|#|  \___\  : ___:   | ___|   |#| ||| ( ) |##|")
    print("|#|  / __\  |/ __\   // __\   |#| |||  `  |##|")
    print("|#|  \__//   \__//  /_\__//   |#|  ~      |##|")
    print("|#|===========================|#|_________|##|")
    print("|#|```````````````````````````|##############|")
    print("|#||||||||||||PUSH|||||||||||||####\|||||/###|")
def vendingmachinebase():
    print("|############################################|")
    print("|#|                           |##############|")
    print("|#|  =====  ..--''`  |~~``|   |##|````````|##|")
    print("|#|  |   |  \     |  :    |   |##| Exact  |##|")
    print("|#|  |___|   /___ |  | ___|   |##| Change |##|")
    print("|#|  /=__\  ./.__\   |/,__\   |##| Only   |##|")
    print("|#|  \__//   \__//    \__//   |##|________|##|")
    print("|#|===========================|##############|")
    print("|#|```````````````````````````|##############|")
    print("|#| =.._      +++     //////  |##############|")
    print("|#| \/  \     | |     \    \  |#|`````````|##|")
    print("|#|  \___\    |_|     /___ /  |#|         |##|")
    print("|#|  / __\\  /|_|\   // __\    |#| |1|2|3| |##|")
    print("|#|  \__//-  \|_//   -\__//   |#| |4|5|6| |##|")
    print("|#|===========================|#| |7|8|9| |##|")
    print("|#|```````````````````````````|#| ``````` |##|")
    print("|#| ..--    ______   .--._.   |#|[=======]|##|")
    print("|#| \   \   |    |   |    |   |#|  _   _  |##|")
    print("|#|  \___\  : ___:   | ___|   |#| ||| ( ) |##|")
    print("|#|  / __\  |/ __\   // __\   |#| |||  `  |##|")
    print("|#|  \__//   \__//  /_\__//   |#|  ~      |##|")
    print("|#|===========================|#|_________|##|")
    print("|#|```````````````````````````|##############|")
    print("|#||||||||||||PUSH|||||||||||||####\|||||/###|")
#user will input any amount of cash they want
cash= int(input("You walk to a vending to buy something. You checked your pockets and you have how much money?\n"))
print("You have",cash,"AED in your pockets.")
#To keep track of items bought
inventory=[]
#stock of items start at 10
stock1,stock2,stock3,stock4,stock5,stock6,stock7,stock8,stock9,stock10=10,10,10,10,10,10,10,10,10,10
#cost of all the items
cost1,cost2,cost3,cost4,cost5,cost6,cost7,cost8,cost9,cost10=2,2,3,3,4,4,5,5,6,6
vendingmachinebase()
#if the cash entered can afford the cheapest item
while cash>=cost1 or cash>=cost3 or cash>=cost5 or cash>=cost7 or cash>=cost9:
    user=int(input("You look and see the menu: 1-Bread(2AED): 2-Water(2AED): 3-Chocolate(3AED): 4-Hot Drink(3AED): 5-Chips(4AED): 6-Tea(4AED): 7-Sandwich(5AED): 8-Soda(5AED): 9-Energy Drinks(6AED): 0-Exit. The vending machine requires a number:\n"))
    vendingmachine(user)
    #if the user entered 1
    if user==1:
    #checks if the stock left is greater than 1 and if the cash can cover the cost
        if stock1>=1 and cash>=cost1:
            #reduces stock by 1
            stock1=stock1-1
            #reduces cash by the cost
            cash=cash-cost1 
            #output that you have bought the item along with money and stock left.
            print("You bought bread for",cost1,"AED. You have",cash,"AED left. There's",stock1," bread left.")
            #adds item to inventory
            inventory.append("bread")
            #checks if stock is greater than 1 and if the cash can cover cost.
            if stock2>=1 and cash>=cost2:
                #vending machine suggesting another item
                print("This pairs well with water for",cost2,"AED.")
                #prompts if the user wants to buy or not.
                user2=input("Would you like to buy water? (y/n)") 
                #answer is yes
                if user2=='y':
                    cash=cash-cost2
                    stock2=stock2-1
                    print(f"You bought water for {cost2} AED. You have {cash} AED left. The amount of stock remaining is: {stock2}.")
                    inventory.append("water")
                    #prompts if the user wants to leave
                    user3=input("Would you like to leave? (yes/no)")
                    #answered yes to leaving
                    if user3=='yes':
                        break
                    #answered no to leaving
                    elif user3=='no':
                        continue
                #answer is no
                elif user2=='n':
                    continue
            #if the suggested item ran out of stocks or user cannot afford it.
            else:
                continue
        #if the first item you're trying to buy has no more stocks or user cannot afford it
        else:
            print("Cannot purchase item")
            continue
    elif user==2:
        if stock2>=1 and cash>=cost2:
            stock2=stock2-1
            cash=cash-cost2
            print("You bought water for",cost2,"AED. You have",cash," AED left. There's",stock2,"water left.")
            inventory.append("water")
            if stock1>=1 and cash>=cost1:
                print("This pairs well with bread for",cost1,"AED.")
                user2=input("Would you like to buy bread? (y/n)")
                if user2=='y':
                    cash=cash-cost2
                    stock1=stock1-1
                    print(f"You bought bread for {cost1} AED. You have {cash} AED left. The amount of stock remaining is: {stock1}.")
                    inventory.append("bread")
                    user3=input("Would you like to leave? (yes/no)")
                    if user3=='yes':
                        break
                    elif user3=='no':
                        continue
                elif user2=='n':
                    continue
            else:
                continue
        else:
            print("Cannot purchase item.")
            continue
    elif user==3:
        if stock3>=1 and cash>=cost3:
            stock3=stock3-1
            cash=cash-cost3
            print("You bought chocolate for",cost3,"AED. You have",cash,"AED left. There's",stock3,"chocolate left.")
            inventory.append("chocolate")
            if stock4>=1 and cash>=cost4:
                print("This pairs well with hot drink for",cost4,"AED.")
                user2=input("Would you like to buy hot drink? (y/n)")
                if user2=='y':
                    cash=cash-cost4
                    stock4=stock4-1
                    print(f"You bought a hot drink for {cost4} AED. You have {cash} AED left. The amount of stock remaining is: {stock4}.")
                    inventory.append("hot drink")
                    user3=input("Would you like to leave? (yes/no)")
                    if user3=='yes':
                        break
                    elif user3=='no':
                        continue
                elif user2=='n':
                    continue
            else:
                continue
        else:
            print("Cannot purchase item.")
            continue
    elif user==4:
        if stock4>=1 and cash>=cost4:
            stock4=stock4-1
            cash=cash-cost4
            print("You bought a hot drink for",cost4,"AED. You have",cash,"AED left. There's",stock4,"hot drink left.")
            inventory.append("hot drink")
            if stock3>=1 and cash>-stock3:
                print("This pairs well with chocolate for",cost3,"AED.")
                user2=input("Would you like to buy chocolate? (y/n)")
                if user2=='y':
                    cash=cash-cost3
                    stock3=stock3-1
                    print(f"You bought chocolate for {cost3} AED. You have {cash} AED left. The amount of stock remaining is: {stock3}.")
                    inventory.append("chocolate")
                    user3=input("Would you like to leave? (yes/no)")
                    if user3=='yes':
                        break
                    elif user3=='no':
                        continue
                elif user2=='n':
                    continue
            else: 
                continue
        else:
            print("Cannot purchase item.")
            continue
    elif user==5:
        stock5=stock5-1
        if stock5>=1 and cash>=cost5:
            cash=cash-cost5
            print("You bought chips for",cost5,"AED. You have",cash,"AED left. There's",stock5,"chips left.")
            inventory.append("chips")
            if stock5>=1 and cash>=cost5:
                print("This pairs well with tea for",cost6,"AED.")
                user2=input("Would you like to buy tea? (y/n)")
                if user2=='y':
                    cash=cash-cost6
                    stock6=stock6-1
                    print(f"You bought tea for {cost6} AED. You have {cash} AED left. The amount of stock remaining is: {stock6}.")
                    inventory.append("tea")
                    user3=input("Would you like to leave? (yes/no)")
                    if user3=='yes':
                        break
                    elif user3=='no':
                        continue
                elif user2=='n':
                    continue
            else:
                continue
        else:
            print("Cannot purchase item.")
            continue
    elif user==6:
        stock6=stock6-1
        if stock6>=1 and cash>=cost6:
            cash=cash-cost6
            print("You bought tea for",cost6,"AED. You have",cash,"AED left. There's",stock6,"chips left.")
            inventory.append("chips")
            if stock5>=1 and cash>=cost5:
                print("This pairs well with chips for",cost5,"AED.")
                user2=input("Would you like to buy chips? (y/n)")
                if user2=='y':
                    cash=cash-cost5
                    stock5=stock5-1
                    print(f"You bought chips for {cost5} AED. You have {cash} AED left. The amount of stock remaining is: {stock5}.")
                    inventory.append("chips")
                    user3=input("Would you like to leave? (yes/no)")
                    if user3=='yes':
                        break
                    elif user3=='no':
                        continue
            elif user2=='n':
                continue
        else:
            print("Cannot purchase item.")
            continue
    elif user==7:
        stock7=stock7-1
        if stock7>=1 and cash>=cost7:
            cash=cash-cost7
            print("You bought sandwich for",cost7,"AED. You have",cash,"AED left. There's",stock7,"sandwich left.")
            inventory.append("sandwich")
            if stock8>=1 and cash>=cost8:
                print("This pairs well with soda for",cost8,"AED.")
                user2=input("Would you like to buy soda? (y/n)")
                if user2=='y':
                    cash=cash-cost8
                    stock8=stock8-1
                    print(f"You bought soda for {cost8} AED. You have {cash} AED left. The amount of stock remaining is: {stock8}.")
                    inventory.append("soda")
                    user3=input("Would you like to leave? (yes/no)")
                    if user3=='yes':
                        break
                    elif user3=='no':
                        continue
                elif user2=='n':
                    continue
        else:
            print("Cannot purchase item.")
            continue
    elif user==8:
        stock8=stock8-1
        if stock8>=1 and cash>=cost8:
            cash=cash-cost8
            print("You bought soda for",cost8,"AED. You have",cash,"AED left. There's",stock8,"soda left.")
            inventory.append("soda")
            if stock7>=1 and cash>=cost7:
                print("This pairs well with sandwich for",cost7,"AED.")
                user2=input("Would you like to buy sandwich? (y/n)")
                if user2=='y':
                    cash=cash-cost7
                    stock7=stock7-1
                    print(f"You bought sandwich for {cost7} AED. You have {cash} AED left. The amount of stock remaining is: {stock7}.")
                    inventory.append("sandwich")
                    user3=input("Would you like to leave? (yes/no)")
                    if user3=='yes':
                        break
                    elif user3=='no':
                        continue
                elif user2=='n':
                    continue
        else:
            print("Cannot purchase item.")
            continue
    elif user==9:
        stock9=stock9-1
        if stock9>=1 and cash>=cost9:
            cash=cash-cost9
            print("You bought an energy drink for",cost9,"AED. You have",cash,"AED left. There's",stock9,"energy drink left.")
            inventory.append("energy drink")
            if stock10>=1 and cash>=cost10:
                print("This pairs well with candy for",cost10,"AED.")
                user2=input("Would you like to buy candy? (y/n)")
                if user2=='y':
                    cash=cash-cost10
                    stock10=stock10-1
                    print(f"You bought candy for {cost10} AED. You have {cash} AED left. The amount of stock remaining is: {stock10}.")
                    inventory.append("candy")
                    user3=input("Would you like to leave? (yes/no)")
                    if user3=='yes':
                        break
                    elif user3=='no':
                        continue
                elif user2=='n':
                    continue
            else:
                continue
        else:
            print("Cannot purchase item.")
            continue
    elif user==0:
        break
    else:
        print("Invalid number.")
        continue
items=len(inventory)
if items==0:
    print("You left with",cash,"AED in your pockets. You didn't buy anything.")
elif items==1:
    print("You left with",cash,"AED in your pockets. And the item you bought is:",inventory)
else:
    print("You left with",cash,"AED in your pockets. And the items you bought are:",inventory)
