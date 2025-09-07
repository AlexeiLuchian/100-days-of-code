from tkinter import *
from tkinter import messagebox
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"
CURRENT_CARD = None

def flip_card():
    global CURRENT_CARD
    flashcard.itemconfig(card, image=card_back_img)
    flashcard.itemconfig(language, text="English", fill="white")
    flashcard.itemconfig(word, text=CURRENT_CARD["English"], fill="white")

def next_card(pressed_button):
    global CURRENT_CARD, flip_timer
    window.after_cancel(flip_timer)
    try:
        if pressed_button == "correct":
                vocabulary.remove(CURRENT_CARD)

        dataframe = pandas.DataFrame(vocabulary)
        dataframe.to_csv("./data/words_to_learn.csv", index=False)

        CURRENT_CARD = choice(vocabulary)
        flashcard.itemconfig(card, image=card_front_img)
        flashcard.itemconfig(language, text="French", fill="black")
        flashcard.itemconfig(word, text=CURRENT_CARD["French"], fill="black")
        flip_timer = window.after(3000, flip_card)
    except:
        messagebox.showinfo(title="Congratulations", message="You've learned the top 100 most used french words.\nThere are no other words in the bank.")

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except:
    data = pandas.read_csv("./data/french_words.csv")
finally:
    vocabulary = data.to_dict(orient="records")    

window = Tk()
window.title("Flashcards App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

flashcard = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card = flashcard.create_image(400, 263, image=card_front_img)
language = flashcard.create_text(400, 150, font=("Arial", 40, "italic"), text="")
word = flashcard.create_text(400, 263, font=("Arial", 60, "bold"), text="")
flashcard.grid(row=0, column=0, columnspan=2)

correct_button_img = PhotoImage(file="./images/right.png")
correct_button = Button(image=correct_button_img, highlightthickness=0, command=lambda: next_card(pressed_button="correct"))
correct_button.grid(row=1, column=0)

wrong_button_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=lambda: next_card(pressed_button="wrong"))
wrong_button.grid(row=1, column=1)

next_card("")
window.mainloop()

