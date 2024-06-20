import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle
flower = turtle.Turtle()
flower.speed(0)

def draw_petal(color):
    flower.color(color)
    flower.begin_fill()
    flower.circle(100, 60)
    flower.left(120)
    flower.circle(100, 60)
    flower.left(120)
    flower.end_fill()

def draw_flower():
    # Draw white petals
    flower.penup()
    flower.goto(0, -100)
    flower.pendown()
    flower.setheading(-30)
    for _ in range(6):
        draw_petal("green")
        flower.left(60)

    # Draw green leaves behind petals
    flower.penup()
    flower.goto(0, -100)
    flower.pendown()
    flower.setheading(-60)
    for _ in range(6):
        draw_petal("red")
        flower.left(60)

   
draw_flower()

# Hide turtle and display the window
flower.hideturtle()
screen.mainloop()
