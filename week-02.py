import time


player_name = input("Wat is je naam? \n> ")
print()

player_gold = 100
inventory = []




#=======
shop_open = True
#=======


#shop
shopitems = [
    {"id": 1, "name": "Sword", "price": 50},
    {"id": 2, "name": "Shield", "price": 40},
    {"id": 3, "name": "Potion", "price": 20},
    {"id": 4, "name": "Bow", "price": 60}
]
shopitemschecker = ["sword", "shield", "potion", "bow"]

def show_menu():
    print(f"Welcome {player_name}! You have {player_gold} gold.\n")

    for item in shopitems:
        print(f"buy {item['name']}? {item['price']} gold")
    print("\ninventory (to see your items.) \nexit (to leave the shop.)\n")


def show_inventory(players_inventory):
    print("opening backpack...")
    time.sleep(2)
    total_items = len(players_inventory)
    if total_items == 0:
        print("Your inventory is empty.")
    else:
        for item in players_inventory:
            print(f"{item}\n")
            time.sleep(2)

def canbuy(gold, price):
     if gold >= price:
          return True
     else:
          return False

def buy_item(gold, item, price):
    gold -= price
    inventory.append(item)
    print(f"You bought a {item} and have {gold} bucks!")
    return(gold)

     

while shop_open:
    show_menu()
    choice = input("what do you want to buy? (type the item/name) \n> ")
    print()
    if choice == "exit":
        shop_open = False
        print(f"Thanks for visiting the shop {player_name} you still have {player_gold} gold!")
    else:
        match choice:
            case "inventory":
                show_inventory(inventory)
            case _:
                if choice in shopitemschecker:
                    for item in shopitems:
                        if item["name"] == choice:
                            price = item["price"]
                            item_name = item["name"]
                        else:
                             price = item["price"]
                             item_name = item["name"]
                    if canbuy(player_gold, price) == True:
                        player_gold = buy_item(player_gold, item_name, price)
                    else:
                        print(f"You don't have enough gold for a {item_name}.")
                else:
                    print(f"{choice} is not available in the shop.")
        time.sleep(2)
        print("\n")