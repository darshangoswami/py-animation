from tkinter import *
from ball import *
import time

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball = ball(canvas, 0, 0, 100, 1, 1, "white")
tennis_ball = ball(canvas, 0, 0, 50, 2, 3, "yellow")
basket_ball = ball(canvas, 0, 0, 200, 4, 5, "orange")

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()