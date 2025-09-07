from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"

def flip_card(random_word):
    flashcard.itemconfig(card, image=card_back_img)
    flashcard.itemconfig(language, text="English", fill="white")
    flashcard.itemconfig(word, text=random_word["English"], fill="white")

def next_card():
    random_word = choice(vocabulary)
    flashcard.itemconfig(card, image=card_front_img)
    flashcard.itemconfig(language, text="French", fill="black")
    flashcard.itemconfig(word, text=random_word["French"], fill="black")
    window.after(3000, flip_card, random_word)

with open("./data/french_words.csv") as file:
    data = pandas.read_csv(file)
    vocabulary = data.to_dict(orient="records")    

window = Tk()
window.title("Flashcards App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flashcard = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card = flashcard.create_image(400, 263, image=card_front_img)
language = flashcard.create_text(400, 150, font=("Arial", 40, "italic"), text="")
word = flashcard.create_text(400, 263, font=("Arial", 60, "bold"), text="")
flashcard.grid(row=0, column=0, columnspan=2)

correct_button_img = PhotoImage(file="./images/right.png")
correct_button = Button(image=correct_button_img, highlightthickness=0, command=next_card)
correct_button.grid(row=1, column=0)

wrong_button_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=1)

next_card()
window.mainloop()
