import tkinter

window = tkinter.Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a label",font=("Arial", 12, "bold"))
my_label.pack(side = "left")
# my_label.pack(expand = True)







window.mainloop()