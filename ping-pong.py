from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.speed = 3
        self.angle = random.choice([-45, 45])  # Случайный угол отскока мяча
        self.x = self.speed * -1 if random.random() < 0.5 else self.speed
        self.y = self.speed * -1 if random.random() < 0.5 else self.speed
        self.canvas_height = self.canvas.winfo_height()

    def draw(self):
        if self.canvas:
            self.canvas.move(self.id, self.x, self.y)
            poss = self.canvas.coords(self.id)
            if poss[1] <= 0:
                self.y = self.speed
            if poss[3] >= self.canvas_height:
                self.y = -self.speed
            if poss[0] <= 0:
                self.x = self.speed
            if poss[2] >= self.canvas_height:
                self.x = -self.speed

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)

    def draw(self, event):
        if self.canvas:
            self.canvas.move(self.id, event.x - self.canvas.coords(self.id)[0], 0)

tk = Tk()
tk.title("ping-pong")
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=400, height=400, bd=0, highlightthickness=0)
canvas.configure(bg='yellow')
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'red')
ball = Ball(canvas, 'green')

canvas.bind("<Motion>", paddle.draw)
canvas.focus_set()

while True:
    try:
        ball.draw()
        paddle_pos = canvas.coords(paddle.id)
        ball_pos = canvas.coords(ball.id)
        if paddle_pos[0] <= ball_pos[2] <= paddle_pos[2] and paddle_pos[1] <= ball_pos[3] <= paddle_pos[3]:
            ball.y = -ball.speed
            ball.angle = random.choice([-45, 45])
            ball.x = ball.speed * -1 if random.random() < 0.5 else ball.speed
            ball.y = ball.speed * -1 if random.random() < 0.5 else ball.speed
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
    except TclError:
        break
