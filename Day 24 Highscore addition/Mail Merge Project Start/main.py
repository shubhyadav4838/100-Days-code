#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
PLACEHOLDER = "[name]"
name_path = "100 Days code/Day 24 Highscore addition/Mail Merge Project Start/Input/Names/invited_names.txt"
with open(name_path, "r") as name_file:
    names = name_file.readlines()

starting_letter_path = "100 Days code/Day 24 Highscore addition/Mail Merge Project Start/Input/Letters/starting_letter.txt"
with open(starting_letter_path) as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"100 Days code/Day 24 Highscore addition/Mail Merge Project Start/Output/ReadyToSend/letter_for_{stripped_name}.txt","w") as completed_letter:
           completed_letter.write(new_letter)
