from tkinter import *
import time
import random

tk = Tk()
tk.title('прыг скок')
tk.resizable(0, 0)#запрещаем менять размеры окна
tk.wm_attributes("-topmost", 1)#игровое окно помещаем впереди всех открытых окон

canvas = Canvas(tk, height=400, width=400, bd=0, highlightthickness=0)#создаем холст, где будет игра
canvas.pack()#говорим, что у каждого элемента будут свои координаты
tk.update()#обновляем окно

class Ball:
    def __init__(self, canvas, colour, r, score):
        self.canvas = canvas
        self.r = r
        self.score = score
        self.bottom = False
        self.acd = canvas.create_oval(8, 8, 20, 20, fill=colour)#создаем шарик
        self.canvas.move(self.acd, 200, 200)#помещаем шарик в точку с координатами
        coord_x = [-2, 0, -1, 2]
        random.choice(coord_x)
        self.x = coord_x[0]
        self.y = -2
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def hit(self, position):
        new = self.canvas.coords(self.r.acd)
        if position[2] >= new[0] and position[0] <= new[2]:
            if position[3] >= new[1] and position[3] <= new[3]:
                self.score.hit()
                return True
        return False

    def move_ball(self):
        self.canvas.move(self.acd, self.x, self.y)
        position = self.canvas.coords(self.acd)
        if position[1] <= 0:
            self.y = 2
        if position[3] >= self.canvas_height:
            self.bottom = True
            canvas.create_text(200, 150, text='Вы проиграли', fill='red')
        if position[0] <= 0:
            self.x = 2
        if position[2] >= self.canvas_width:
            self.x = -2
        if self.hit(position) == True:
            self.y = -2


class Racket:
    def __init__(self, canvas, colour):
        self.canvas = canvas
        self.acd = canvas.create_rectangle(0, 0, 120, 12, fill=colour)#создаем ракетку
        s = [40, 300, 220, 25, 186]
        random.choice(s)
        self.star = s[0]
        self.canvas.move(self.acd, self.star, 330)#помещаем ракетку в точку с координатами
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)#присваиваем клавиши для управления ракетки(правая)
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.started = True
        self.canvas.bind_all('<KeyPress-Return>', self.start_game)
    def turn_right(self, event):
        self.x = 5

    def turn_left(self, event):
        self.x = -5
    def start_game(self, event):
        self.started = True

    def move_racket(self):
        self.canvas.move(self.acd, self.x, 0)
        position = self.canvas.coords(self.acd)
        if position[0] <= 0:
            self.x = 0
        if position[2] >= self.canvas_width:
            self.x = 0
class Score:
    def __init__(self, canvas, colour):
        self.canvas = canvas
        self.score = 0
        self.acd = canvas.create_text(200, 15, text=self.score, fill=colour)
    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.acd, text=self.score)

r = Racket(canvas, 'light green')
score = Score(canvas, 'green')
b = Ball(canvas, "dark green", r, score)

while True:
    if b.bottom == False:
        b.move_ball()
        r.move_racket()
    else:
        break
    tk.update_idletasks()# обновляем поле
    tk.update()
    time.sleep(0.01)
    # показывает, что мы правильно сделали
time.sleep(3)


