from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashcards App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flashcard = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
flashcard.create_image(400, 263, image=card_front_img)
language = flashcard.create_text(400, 150, font=("Arial", 40, "italic"), text="French")
word = flashcard.create_text(400, 263, font=("Arial", 60, "bold"), text="trouve")
flashcard.grid(row=0, column=0, columnspan=2)

correct_button_img = PhotoImage(file="./images/right.png")
correct_button = Button(image=correct_button_img, highlightthickness=0)
correct_button.grid(row=1, column=0)

wrong_button_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0)
wrong_button.grid(row=1, column=1)

window.mainloop()