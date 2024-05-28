from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card={}



file = "100 Days code/Day 31 Flash Card Project/data/french_words.csv"
to_learn_file = "100 Days code/Day 31 Flash Card Project/data/words_to_learn.csv"

try:
    data = pd.read_csv(to_learn_file)
except FileNotFoundError: 
    original_data = pd.read_csv(file)
    to_learn = original_data.to_dict(orient="records")
else:    
    to_learn = data.to_dict(orient="records")
    
    

def new_random_word():
    global to_learn, flip_timer, current_card
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    word = current_card['French']
    canvas.itemconfigure(canvas_title, text = "French",fill="black")
    canvas.itemconfigure(canvas_word, text=word,fill="black")
    canvas.itemconfigure(card_backgound, image=front_image)
    flip_timer = window.after(3000,func=flip_card)
    
    
def flip_card():
    global to_learn, current_card
    canvas.itemconfigure(canvas_title, text= "English", fill="white")
    canvas.itemconfigure(canvas_word, text=current_card["English"], fill="white")
    canvas.itemconfigure(card_backgound,image= back_image )
     
def is_know():
    global current_card
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("100 Days code/Day 31 Flash Card Project/data/words_to_learn.csv",index=False)
    new_random_word()
    

window = Tk()
window.title("Flashy")
window.configure(padx=100,pady=100,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=flip_card)

#card image
front_image = PhotoImage(file="100 Days code/Day 31 Flash Card Project/images/card_front.png")
back_image = PhotoImage(file="100 Days code/Day 31 Flash Card Project/images/card_back.png")

canvas = Canvas(width=800, height=562,bg=BACKGROUND_COLOR,highlightthickness=0 )
card_backgound = canvas.create_image(400, 286,image = front_image)
canvas_title = canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
canvas_word = canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0, columnspan = 2)

#Image
wrong_img = PhotoImage(file="100 Days code/Day 31 Flash Card Project/images/wrong.png")
right_img = PhotoImage(file="100 Days code/Day 31 Flash Card Project/images/right.png")

#Buttons
wrong_button = Button(image=wrong_img,borderwidth=0, highlightthickness=0, command = new_random_word)
right_button = Button(image=right_img, borderwidth=0, highlightthickness=0, command = is_know)
wrong_button.grid(row=1, column = 0)
right_button.grid(row=1, column = 1)

new_random_word()

window.mainloop()