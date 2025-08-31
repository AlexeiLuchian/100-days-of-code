import tkinter

def button_clicked():
    label["text"] = f"Aaaaah, it was you {user_input.get()}"

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

label = tkinter.Label(text="I don't know you")
label.pack()

button = tkinter.Button(text="button", command=button_clicked)
button.pack()

user_input = tkinter.Entry(width=20)
user_input.pack()

window.mainloop()