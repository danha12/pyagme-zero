import pgzrun
from random import randint



apple = Actor('apple')
orange = Actor('orange')
count = 0
point = 0

def draw() :
    screen.clear()
    apple.draw()
    orange.draw()

def place_apple() :
    apple.x = randint(10, 800)      # 10 until 800 random int
    apple.y = randint(10, 600)      # 10 until 600 random int

def place_orange() :
    orange.x = randint(10, 800)
    orange.y = randint(10, 600)
    

def on_mouse_down(pos) :            # happen when click mouse
    global count, point

    if(apple.collidepoint(pos)) :    # when click apple 
        place_apple()
        place_orange()
        point = point +1
    elif(orange.collidepoint(pos)) :
        print('You clicked wrong fruit!')
        print("Final score :", point)
        quit()
    else :
        place_apple()
        place_orange()
        count = count + 1
        if(count > 3) :
            print("Your life ended")
            print("Final score :", point)
            quit()

place_apple()
place_orange()

pgzrun.go()