import turtle
import ball
from seven_segments_proc import  Segment

turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
print(ball.Run().canvas_width, ball.Run().canvas_height)
ball_radius = 0.05 * ball.Run().canvas_width
turtle.colormode(255)

dt = 0.2 # time step
b1 = ball.Run()
b1.create_random()
while (True):
    turtle.clear()
    b1.draw_border()
    Tom = turtle.Turtle()
    tom_color = (255, 0, 0)
    sgm = Segment(Tom, tom_color)
    # sgm.clear(Tom)
    for j in range(8):
        sgm.draw(j)
    for i in range(ball.Run().num_balls):
        bb = ball.Ball(b1.ball_color[i], b1.ball_radius, b1.xpos[i], b1.ypos[i])
        bb.draw_ball()
        bb.move_ball(i, dt, b1)
        bb.update_ball_velocity(i, b1)
    turtle.update()

# hold the window; close it by clicking the window close 'x' mark
turtle.done()
