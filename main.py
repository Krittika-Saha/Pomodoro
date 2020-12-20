from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_command():
  count_down(62)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

  count_min = count // 60
  count_sec = count % 60 
  if count_sec < 10 and count_sec >= 0:
    count_sec = f'0{count_sec}'
  canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
  if count > 0:
    window.after(1000, count_down, count - 1) 
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)
#Timer Label

timer=Label(text='Timer')
timer.configure(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40))
timer.grid(column=1, row=0)

#Canvas
canvas = Canvas(width=280, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.gif')
canvas.create_image(140, 112, image=tomato_img)
timer_text = canvas.create_text(140, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)
#Buttons

start = Button(text='Start', highlightthickness=0)
start.config(command=start_command)
start.grid(column=0, row=2)

reset = Button(text='Reset', highlightthickness=0)
reset.grid(column=2, row=2)

#Checkmarks

check_marks = Label(text='✔', fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()