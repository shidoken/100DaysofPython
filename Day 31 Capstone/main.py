import tkinter
import pandas
import random
from tkinter.messagebox import _show

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# read from file
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill='black')
    canvas.itemconfig(card_word, text=current_card["French"], fill='black')
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)
    
    # canvas.itemconfig(card_front, fill=BACKGROUND_COLOR))

def flip_card():
    # to change the image
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)
    window.after_cancel()

def learned():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

    
# main config
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# background
canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front = tkinter.PhotoImage(file="./images/card_front.png")
card_back = tkinter.PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 270, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

# buttons
x_image = tkinter.PhotoImage(file="./images/wrong.png")
x_button = tkinter.Button(image=x_image, highlightthickness=0, command=next_card)
x_button.grid(column=0, row=1)

o_image = tkinter.PhotoImage(file="./images/right.png")
o_button = tkinter.Button(image=o_image, highlightthickness=0, command=learned)
o_button.grid(column=1, row=1)

#text
# top_text = tkinter.Label(text="French", font=("Arial", 40, "italic"), bg="white")
# top_text.place(x=400, y=150, anchor='center')
# bottom_text = tkinter.Label(text="word", font=("Arial", 60, "bold"), bg="white")
# bottom_text.place(x=400, y=263, anchor='center')
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

next_card()

window.mainloop()