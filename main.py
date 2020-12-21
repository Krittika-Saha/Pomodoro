from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_SEC = 25*60
SHORT_BREAK_SEC = 300
LONG_BREAK_SEC = 1200
current_time = 0
reps = 1
do_continue = True
count_min = 0
count_sec = 0
# ---------------------------- START AND STOP MECHANISM ------------------ #
def start_timer():
  global do_continue
  do_continue = True
  start_command()
def stop_timer():
  global do_continue
  do_continue = False

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM --------------------------- # 
def start_command():
  global reps

  if do_continue:
    if current_time != 0:
      count_down(current_time)
    else:
      if reps % 2 != 0:
        timer.configure(text='Work', fg=RED)
        count_down(WORK_SEC)
        reps += 1
      elif reps % 2 == 0 and reps % 8 != 0:
        timer.configure(text='Short Break', fg=PINK)
        count_down(SHORT_BREAK_SEC)
        reps += 1
      elif reps % 8 == 0:
        timer.configure(text='Long Break', fg=GREEN)
        count_down(LONG_BREAK_SEC)
        reps += 1
  elif do_continue == False:
    reps -= 1
  
  
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
  global reps
  current_time = count-1
  if do_continue:
    count_min = count // 60
    count_sec = count % 60 
    if count_sec < 10 and count_sec >= 0:
      count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
      window.after(1000, count_down, count - 1) 
    else:
      start_command()
  
  elif do_continue == False:
    reps -= 1
  
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
start.config(command=start_timer)
start.grid(column=0, row=2)

stop = Button(text='Stop', highlightthickness=0)
stop.config(command=stop_timer)
stop.grid(column=1, row=4)
reset = Button(text='Reset', highlightthickness=0)
reset.grid(column=2, row=2)

#Checkmarks

check_marks = Label(text='✔', fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
