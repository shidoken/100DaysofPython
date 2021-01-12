import tkinter

# window properties
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

#labels
is_equal_to = tkinter.Label(text="is equal to", font=("Arial", 12))
is_equal_to.grid(column=0, row=1)

miles = tkinter.Label(text="Miles", font=("Arial", 12))
miles.grid(column=3, row=0)

Km = tkinter.Label(text="Km", font=("Arial", 12))
Km.grid(column=3, row=1)

answer = tkinter.Label(font=("Arial", 12))
answer.grid(column=1, row=1)

# button
def button_clicked():
    mile = input.get()
    km = int(mile) * 1.60934
    print("I got clicked")
    answer.config(text=round(km, 2))
    answer.grid(column=2, row=1)


button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=2)

# Entry

input = tkinter.Entry(width=10)
input.grid(column=2, row=0)
input.get()

window.mainloop()