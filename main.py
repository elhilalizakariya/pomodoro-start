from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_marks = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    #timer_text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    #title_label"timer"
    label.config(text="Timer", fg=GREEN)
    #reset check_marks
    global check_marks
    check_marks = ""
    sign.config(text=check_marks)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        if not reps % 2 == 0:
            global check_marks
            check_marks += "✔"
            sign.config(text=check_marks)
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



# Label
label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
label.grid(row=0, column=1, padx=5, pady=5)

# Canvas with the Photo and the text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1, padx=5, pady=5)


# Buttons
button1 = Button(text="Start", command = start_timer )
button1.grid(row=2, column=0, padx=5, pady=5)
button2 = Button(text="Reset", command = reset_timer)
button2.grid(row=2, column=2, padx=5, pady=5)

#Sign
sign = Label(font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
sign.grid(row=3, column=1, padx=5, pady=5)



window.mainloop()