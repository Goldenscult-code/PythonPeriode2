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

while shop_open:
    print(f"Welcome {player_name}! You have {player_gold} gold.\n")

    for item in shopitems:
        print(f"buy {item['name']}? {item['price']} gold")
    print("\ninventory (to see your items.) \nexit (to leave the shop.)\n")

    choice = input("what do you want to buy? (type the item/name) \n> ")
    print()
    if choice == "exit":
        shop_open = False
        print(f"Thanks for visiting the shop {player_name} you still have {player_gold} gold!")
    else:
        match choice:
            case "sword":
                if player_gold >= 50:
                    player_gold -= 50
                    inventory.append("Sword")
                    print("You bought a Sword!")
                else:
                    print("You don't have enough gold for a Sword.")
            case "shield":
                if player_gold >= 40:
                    player_gold -= 40
                    inventory.append("Shield")
                    print("You bought a Shield!")
                else:
                    print("You don't have enough gold for a Shield.")
            case "potion":
                if player_gold >= 20:
                    player_gold -= 20
                    inventory.append("Potion")
                    print("You bought a Potion!")
                else:
                    print("You don't have enough gold for a Potion.")
            case "bow":
                if player_gold >= 60:
                    player_gold -= 60
                    inventory.append("Bow")
                    print("You bought a Bow!")
                else:
                    print("You don't have enough gold for a Bow.")
            case "inventory":
                print("opening backpack...")
                time.sleep(2)
                for item in inventory:
                    print(f"{item}\n")
                    time.sleep(2)
            case _:
                print("Invalid choice. Please select an item from the shop or type 'exit' to leave.")
        time.sleep(2)
        print("\n")
