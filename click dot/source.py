import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400

dots = []
lines = []
next_dot = 0
timer = 15
start_click = False

for dot in range(0, 10) :
    actor = Actor('dot')
    actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
    dots.append(actor)

def draw() :

    if(next_dot == 10) :
        screen.fill('white')
        screen.draw.text('good job!', color = 'black', center = (WIDTH / 2, HEIGHT / 2), fontsize = 100)
    else :
        if(timer <= 0) :
            screen.fill('red')
            screen.draw.text('bad job!', color = 'black', center = (WIDTH / 2, HEIGHT / 2), fontsize = 100)
        else :
            screen.fill('black')
            screen.draw.text(str(round(timer, 2)), color = 'red', topleft = (10, 10), fontsize = 40)

            number = 1

            for dot in dots :
                screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 12 ))   # Make the number below the dot.
                dot.draw()
                number = number + 1

            for line in lines :
                screen.draw.line(line[0], line[1], (100, 0, 0))


def on_mouse_down(pos) :
    global next_dot
    global lines
    global start_click

    if(next_dot < 10):      # Create a limit on clicks. Reason: Because 9 is the last index number of dots.
        if dots[next_dot].collidepoint(pos) :
            start_click = True
            if next_dot :
                lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
            next_dot = next_dot + 1
        else :
            lines = []
            next_dot = 0

def update() :
    global timer

    if start_click:
        timer -= 1 / 60

pgzrun.go()