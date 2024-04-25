import random
random_integer = random.randint(1,10)
print(random_integer)


# exercise
user = input().lower()
line1 = [" "," "," "]
line2 = [" "," "," "]
line3 = [" "," "," "]
mapp = [line1,line2,line3]
ln = user[1]
lst = [0,1,2]
if user[0]=='a':
    mapp[int(ln)-1][0]=user
elif user[0]=='b':
    mapp[int(ln)-1][1]=user
elif user[0]=='c':
    mapp[int(ln)-1][2]=user

print(f"{line1}\n{line2}\n{line3}")


# Stone paper scisser exercise
# user = int(input("0 for stone, 1 for paper and 2 for scissors:" ))
# comp = random.randint(0,2)
# lst = ['stone','paper','scissors']
# if user==comp:
#     print('Game Is Tie')
# elif comp==0 and user==1:
#     print("You won")
# elif comp==1 and user==2:
#     print("You won")
# elif comp==2 and user==0:
#     print("You won")
# else:
#     print("You lose...")
    
    
# print(f"computer choose {lst[comp]}\nYou  choose {lst[user]}")
