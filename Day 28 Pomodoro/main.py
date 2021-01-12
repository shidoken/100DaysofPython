import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=200, pady=200)

#Label

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)


my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.config(padx=50, pady=50)

#button

def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())
    my_label.grid(column=0, row=0)


button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

#Entry

input = tkinter.Entry(width=10)
input.grid(column=3, row=2)
input.get()

button1 = tkinter.Button(text="Click Me", command=button_clicked)
button1.grid(column=2, row=0)





window.mainloop()

# def add(*arg):
#     return sum(arg)

# add(5,4,8,7,5,4,8)