import tkinter

def calculate():
    number = entry.get()
    if number.isnumeric():
        number_label.config(text=round(1.60934*float(number),2))
    else:
        number_label.config(text=0.0)

window = tkinter.Tk()
window.title("Miles to Km Converter")
window.config(padx=50, pady=50)

entry = tkinter.Entry(width=10)
entry.insert("0","0")
entry.grid(row=0, column=1)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(row=1,column=0)

number_label = tkinter.Label(text=0.0)
number_label.grid(row=1,column=1)

km_label = tkinter.Label(text="Km")
km_label.grid(row=1,column=2)

button = tkinter.Button(text="Calculate", command=calculate)
button.grid(row=2,column=1)


window.mainloop()