import random
from art import stages
word_list = ["python", "java", "csharp", "swift", "kotlin"]



chosen_word = random.choice(word_list)
display = list("_"*(len(chosen_word)))
print(display)

lives = 6

end_of_game = False
while not end_of_game:
    guess = input("Guess the Letter:")
    for letter in range(len(chosen_word)):
        if chosen_word[letter] == guess:
            display[letter]=guess
        if lives ==0:
            end_of_game=True
            break
    if guess not in chosen_word:
        lives-=1
        print("Lives Left: ",lives)
        
    print(display)
    if "_" not in display:
        end_of_game = True
        # print(stages[0])
        print("You won the game")
    elif lives == 0:
        end_of_game = True
        print(stages[0])
        print("You lose the game")
        break
    print(stages[lives])
        
                
   