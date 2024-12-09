
import turtle

def draw_star(x, y, radius):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.forward(radius)
    turtle.left(144)
    turtle.pendown()
    for _ in range(5):
        turtle.forward(2 * radius * (3 ** 0.5))
        turtle.right(144)

def main():
    turtle.speed(10)
    turtle.bgcolor("red")
    
    # Draw the flag
    turtle.begin_fill()
    turtle.fillcolor("yellow")
    turtle.penup()
    turtle.goto(-300, 200)
    turtle.pendown()
    turtle.forward(600)
    turtle.right(90)
    turtle.forward(400)
    turtle.right(90)
    turtle.forward(600)
    turtle.right(90)
    turtle.forward(400)
    turtle.end_fill()
    
    # Draw the big star
    big_star_position = (-200, 150)
    big_star_radius = 50
    draw_star(big_star_position[0], big_star_position[1], big_star_radius)
    
    # Draw the four small stars
    small_stars_positions = [(-120, 180), (-120, 120), (-120, 60), (-120, -20)]
    small_star_radius = 20
    for pos in small_stars_positions:
        draw_star(pos[0], pos[1], small_star_radius)
    
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
