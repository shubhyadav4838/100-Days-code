import pandas as pd

df = pd.read_csv("100 Days code/Day 26 List Comphrension/nato_phonetic_alphabet.csv")

word_dict = {row.letter:row.code for (index,row) in df.iterrows()}

user = input("Enter a word: ").upper()

result = [ word_dict[letter] for letter in user]
print(result)
