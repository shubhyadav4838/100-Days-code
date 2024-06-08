logo ='''
                             ______________________
                            (___________           |
                              [XXXXX]   |          |
                         __  /~~~~~~~\  |          |
       CT               /  \|@@@@@@@@@\ |          |
         )              \   |@@@@@@@@@@||          |
        (                   \@@@@@@@@@@||  ______  |
       __)__                 \@@@@@@@@/ | |on|off| |
    C\|     \               __\@@@@@@/__|  ~~~~~~  |
      \     /              (____________|__________|
       \___/               |_______________________|
  
'''
    
print(logo)

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":100
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {'quarters': 0.25, 'dimes': 0.1, 'nickels': 0.05,'pennies': 0.01,}

def make_coffee(coffee):
    resources["water"]-=MENU[coffee]['ingredients']['water']
    resources['coffee']-= MENU[coffee]['ingredients']['coffee']
    resources['milk']-= MENU[coffee]['ingredients']['milk']
    
    

def check(coffee):
    ingredient = False
    if resources['water']>=MENU[coffee]['ingredients']['water']:
        if resources['milk']>=MENU[coffee]['ingredients']['milk']:
            if resources['coffee']>=MENU[coffee]['ingredients']['coffee']:
                 ingredient= True
            else:
                print("Not enough coffee")
                return False     
        else:
            print("Not enough Milk")
            return False         
    else:
        print("Not enough water")
        return False
    return ingredient   
        
    


def collect_money():
    print('Please insert coins.')
    quarters = input("How many quarters?: ")
    dimes = input("How many dimes?: ")
    nickles = input("How many nickles?: ")
    pennies = input("How many pennies?: ")
    money_received = int(quarters)*0.25 + int(dimes)*0.1+int(nickles)*0.05+int(pennies)*0.01
    round_money = round(float(money_received),2)
    return round_money
    
def report():
    print(f"Water:{resources['water']}\nMilk:{resources['milk']}\nCoffee:{resources['coffee']}")

start = True
while start:
    order = input("What do you want to have?(espresso/latte/cappuccino) ")
    if order=='no':
        start=False
        break
    if order == 'espresso':
        cost=1.5
        paid = collect_money()
        if paid > cost:
            
            print(f"Here is ${paid-cost} in change")
        status = check(order)
        if status:
            make_coffee(order)
            print(f"Here is your coffee")
        if not status:
            print(check(order))
                
    elif order == 'latte':
        cost=2.5
        paid = collect_money()
        if paid > cost:
            print(f"Here is ${round(paid-cost,2)} in change")
        status = check(order)
        if status:
            make_coffee(order)
            print(f"Here is your coffee")
        if not status:
            print(check(order))
            
    elif  order == 'cappuccino':
        cost=3
        paid = collect_money()
        if paid > cost:
            print(f"Here is ${paid-cost} in change")
        status = check(order)
        if status:
            make_coffee(order)
            print(f"Here is your coffee")
        if not status:
            print(check(order))
        
    elif order == 'report':
        report()
    


