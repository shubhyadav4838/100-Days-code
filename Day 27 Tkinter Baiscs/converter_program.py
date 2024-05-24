import tkinter as tk

window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=120,pady=50)

input = tk.Entry(width=5)
input.grid(row=0, column=1)

miles = tk.Label(text="Miles")
miles.grid(row=0, column=2)

equal = tk.Label(text='is equal to').grid(row=1, column=0)
ans = tk.Label(text="00")
ans.grid(row=1, column=1)
km = tk.Label(text='KM').grid(row=1, column=2)

def calculate():
    miles_input = float(input.get()) 
    ans.config(text=str(miles_input * 1.6))

tk.Button(text="Calculate", command = calculate).grid(row=2, column=1)




window.mainloop()