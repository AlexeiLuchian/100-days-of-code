import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_TIME = 25 * 60 # minutes * seconds per minute
SHORT_BREAK_TIME = 5 * 60
LONG_BREAK_TIME = 20 * 60 
CHECK_MARK = "✔️"
REPS = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():

    global REPS
    REPS += 1

    if REPS % 8 == 0:
        title_label.config(text="LONG BREAK", fg=RED)
        countdown(15)
    elif REPS % 2 == 1:
        title_label.config(text="WORK TIME", fg=GREEN)
        countdown(10)
    else:
        title_label.config(text="SHORT BREAK", fg=PINK)
        countdown(5)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):

    mins = int(count / 60)
    secs = count % 60

    if mins < 10:
        mins = f"0{mins}"
    
    if secs < 10:
        secs = f"0{secs}"

    canvas.itemconfig(timer, text=f"{mins}:{secs}")
    if count >= 0:
        window.after(1000, countdown, count - 1)
    else:
        if REPS % 2 == 1:
            checkmark_label.config(text= checkmark_label.cget("text") + CHECK_MARK)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=100, bg=YELLOW)

title_label = tkinter.Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(row=0, column=1)

canvas = tkinter.Canvas(width=200, height=224)
canvas.config(bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer = canvas.create_text(100,140,text="00:00",fill="white", font =(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

start_button = tkinter.Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset")
reset_button.grid(row=2,column=2)

checkmark_label = tkinter.Label(text="", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
checkmark_label.grid(row=3, column=1)

window.mainloop()