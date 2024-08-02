from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 20
reps =0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global timer
    window.after_cancel(timer)
    #timer_text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    #title_label "timer"
    label.config(text="Timer")
    #reset check_marks
    check_label.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="long break", fg=RED)

    elif reps%2 == 0:
        count_down(short_break_sec)
        label.config(text="short break", fg=PINK)

    else:
        count_down(work_sec)
        label.config(text="Work", fg = GREEN)






# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    #to display minutes = count/60
    #math.floor(count/60)  to round of the minutes to a whole number
    #to display seconds = minutes % 60

    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec <10:
        count_sec = f"0{count_sec}"# this is due to python flexiblity in data type of a variable just by defining a different type of a variable

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000, count_down, count-1)

    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "☑"
        check_label.config(text = mark)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


#adding the tomato picture and time on that picture
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)#using canvas to add picture and overalap with the picture
tomato = PhotoImage(file="tomato.png")# using tkinter photimage for reading tomato file png and convert into appropriate data type so that it can be inputted in canvas class
canvas.create_image(100,112, image=tomato)
timer_text = canvas.create_text(100, 130 ,text ="00:00", fill="white", font =(FONT_NAME,35, "bold"))
canvas.grid(column=2, row=2)



#creating label
label = Label(text="Timer" , fg=GREEN, font=(FONT_NAME,35,"bold"), bg=YELLOW, highlightthickness=0)
label.grid(column=2, row=1)
check_label = Label(text= "", fg=GREEN, font=(FONT_NAME,25,"bold"),bg=YELLOW, highlightthickness=0)
check_label.grid(column=2, row=3)

# Creating button
start_but = Button(text="start", highlightthickness=0, command=start_timer)
reset_but = Button(text="Reset", highlightthickness=0, command=reset_timer)

start_but.grid(column=1, row=3)
reset_but.grid(column=3, row=3)


window.mainloop()
