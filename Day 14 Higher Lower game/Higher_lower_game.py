import random
import logoart
from gamedata import data

print(logoart.logo)

score = 0
game = True

while game:
    
    select = random.choices(data, k=2)
    if score>=1:
        print(f"You're right! Current score is {score}")
    print(f" Compare A: {select[0]['name']} a {select[0]['description']} from {select[0]['country']}")
    print(logoart.vs)
    print(f" Compare B: {select[1]['name']} a {select[1]['description']} from {select[1]['country']}")
    user = input("Select form 'a' and 'b': ")
    
    if user=='a':
        if select[0]['follower_count']>select[1]["follower_count"]:
            score+=1
            
        else:
            print(f"You losse {select[1]['name']} has {select[1]['follower_count']} and {select[0]['name']} has {select[0]['follower_count']}")
            game = False
            print(f"Your Final Score is {score}")

    elif user =='b':
        if select[0]['follower_count']<select[1]["follower_count"]:
            score+=1
            
        else:
            print(f"You losse {select[0]['name']} has {select[0]['follower_count']} and {select[1]['name']} has {select[1]['follower_count']}")
            game=False
            print(f"Your Final Score is {score}")
    else:
        print(f"INVALID INPUT....")
        game = False
    print("\n\n")
    