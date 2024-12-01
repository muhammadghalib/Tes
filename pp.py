import turtle

# Inisialisasi layar dan turtle
screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.speed(10)

def draw_petal(t, radius, angle):
    for _ in range(2):
        t.circle(radius, angle)
        t.left(180 - angle)

def draw_flower(t, num_petals, radius, angle):
    for _ in range(num_petals):
        draw_petal(t, radius, angle)
        t.left(360 / num_petals)

def draw_stem(t, length):
    t.color("green")
    t.right(90)
    t.forward(length)

# Menggambar bunga
pen.color("red", "yellow")
pen.begin_fill()
draw_flower(pen, 6, 50, 60)  # 6 kelopak bunga
pen.end_fill()

# Menggambar tangkai
pen.penup()
pen.goto(0, -50)  # Menempatkan turtle di bawah bunga
pen.pendown()
draw_stem(pen, 100)

# Menyelesaikan gambar
pen.hideturtle()
screen.mainloop()
