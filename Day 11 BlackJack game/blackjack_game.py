import random
from logoart import logo

def blackjack(person:list,computer:list):
    if sum(person)>21:
        return "You Loss!"
    elif sum(computer) >21:
        return "You Win!"
    
    man = 21-sum(person)
    com = 21-sum(computer)
    
    if man<com:
        return "You win"
    elif man==com:
        return "The Game is Draw"
    elif man>com:
        return "You lose!"
    

lst = [2,3,4,5,6,7,8,9,10,10,10,11]

play =True

while play:
    print(logo)
    your_cards = random.choices(lst,k=2)
    print(f"Yours Cards are {your_cards}")

    com_cards = random.choices(lst,k=2)
    print(f"Computer's first card is {com_cards[0]}")

    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card=='y':
        your_cards.append(random.choice(lst))
    
    if sum(com_cards)<17:
        com_cards.append(random.choice(lst))
        
    print(f"Your final Cards are :{your_cards}")
    print(f"Computer's final cards are {com_cards}")
    print(blackjack(your_cards,  com_cards))
    user = input("Do you want to play again? Type 'y' for yes and type 'n' for no: ")
    
    if user=='n':
        play=False
        print(f"Thanks for playing the Game!")





