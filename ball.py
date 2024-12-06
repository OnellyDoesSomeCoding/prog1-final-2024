import turtle
import random

class Ball:
    def __init__(self, color, size, x, y):
        self.color = color
        self.size = size
        self.x = x
        self.y = y

    def draw_ball(self):
        # draw a circle of radius equals to size at x, y coordinates and paint it with color
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.x, self.y - self.size)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def move_ball(self, i, dt, other):
        # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
        other.xpos[i] += other.vx[i] * dt
        other.ypos[i] += other.vy[i] * dt

    def update_ball_velocity(self, i, other):
        # if the ball hits the side walls, reverse the vx velocity
        if abs(other.xpos[i]) > (other.canvas_width - other.ball_radius):
            other.vx[i] = -other.vx[i]

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(other.ypos[i]) > (other.canvas_height - other.ball_radius):
            other.vy[i] = -other.vy[i]

class Run:
    def __init__(self):
        self.num_balls = 5
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.ball_radius = 0.05 * self.canvas_width
        self.xpos = []
        self.ypos = []
        self.vx = []
        self.vy = []
        self.ball_color = []

    def __str__(self):
        return f"{self.xpos}, {self.ypos}, {self.vx}, {self.vy}, {self.ball_color}"

    # create random number of balls, num_balls, located at random positions within the canvas; each ball has a random velocity value in the x and y direction and is painted with a random color
    def create_random(self):
        for i in range(self.num_balls):
            self.xpos.append(random.uniform(-1 * self.canvas_width + self.ball_radius, self.canvas_width - self.ball_radius))
            self.ypos.append(random.uniform(-1 * self.canvas_height + self.ball_radius, self.canvas_height - self.ball_radius))
            self.vx.append(10 * random.uniform(-1.0, 1.0))
            self.vy.append(10 * random.uniform(-1.0, 1.0))
            self.ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    def draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2 * self.canvas_width)
            turtle.left(90)
            turtle.forward(2 * self.canvas_height)
            turtle.left(90)
