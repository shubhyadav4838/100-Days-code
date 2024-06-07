from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
TRUE_BUTTON_FILE ="100 Days code/Day 34 Api Quiz/images/true.png" 
FALSE_BUTTON_FILE = "100 Days code/Day 34 Api Quiz/images/false.png"

class QuizInterface:
    
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR)
        self.window.minsize(width = 400, height = 500)
        
        
        self.score_label = Label(text=f"Score: 0 ",padx = 20,pady = 20,bg=THEME_COLOR,fg="white")
        self.question_canvas = Canvas(self.window, width=350, height=290, bg="white")
        self.question_text = self.question_canvas.create_text(180, 150, text="Question text goes here",font="Arial 20 italic", width=300)
        
        self.score_label.grid(row = 0, column = 1)
        self.question_canvas.grid(row = 1 ,column = 0, columnspan = 2,padx=20, pady=20)
        
        self.timg = PhotoImage(file= TRUE_BUTTON_FILE)
        self.fimg = PhotoImage(file= FALSE_BUTTON_FILE)
        self.true_button = Button(image = self.timg, highlightthickness=0, bd=0, command = self.true_pressed)
        self.false_button = Button(image = self.fimg, highlightthickness=0, bd=0, command = self.false_pressed)
        
        self.true_button.grid(row = 2, column = 0,padx=20, pady=20)
        self.false_button.grid(row = 2, column = 1,padx=20, pady=20)
        
        self.get_next_question()
        self.window.mainloop()
        
    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.question_canvas.itemconfig(self.question_text, text = "You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback( self.quiz.check_answer("true"))
    
    
    def false_pressed(self):
        self.give_feedback( self.quiz.check_answer("false"))
        

    def give_feedback(self,is_right):
        if is_right:
            self.question_canvas.configure(bg="green")
            self.window.after(1000,self.change_to_white)
            self.change_score()
           
        else:
            self.question_canvas.configure( bg="red")
            self.window.after(1000,self.change_to_white)
           
            
            
    def change_to_white(self):
        self.question_canvas.configure(bg = "white")
        self.get_next_question()
        
    def change_score(self):
        self.score_label.config(text = f"Score: {self.quiz.score} ")