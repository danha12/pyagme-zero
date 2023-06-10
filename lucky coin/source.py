import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400

score = 0
game_over = False

hedgehog = Actor('hedgehog')
hedgehog.pos = 200, 200

fox = Actor('fox')
fox.pos = 100, 100

coin = Actor('coin')
coin.pos = 200, 200

def draw() :
    screen.fill('blue')
    fox.draw()
    coin.draw()
    hedgehog.draw()
    screen.draw.text('Score: ' + str(score), color = "black", topleft=(10, 10))

    if game_over :
        screen.fill("red")
        screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize = 60)

def place_coin() :
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def place_hedgehog() :
    hedgehog.x = randint(20, (WIDTH - 20))
    hedgehog.y = randint(20, (HEIGHT - 20))

def time_up() :
    global game_over
    game_over = True

def update() :
    global score

    # The fox image is 62 pixels wide and 83 pixels tall.
    if(not(game_over)):
        if keyboard.left :
            if(fox.x < 0 + 32) :    # 32 is half of fox image wide +1
                fox.x = 0 + 32
            fox.x = fox.x - 2
        elif keyboard.right :
            if(fox.x > 400 - 32) :
                fox.x = 400 - 32
            fox.x = fox.x + 2

        if keyboard.up :
            if(fox.y < 0 + 42) :    # 42 is half of fox image tall +1
                fox.y = 0 + 42
            fox.y = fox.y - 2
        elif keyboard.down :
            if(fox.y > 400 - 42) :
                fox.y = 400 - 42
            fox.y = fox.y + 2


        coin_collected = fox.colliderect(coin)
        meet_hedgehog = fox.colliderect(hedgehog)

        if coin_collected :
            score = score + 10
            place_coin()
            place_hedgehog()
            clock.unschedule(time_up)           # Cancel time_up function after 3 second
            clock.schedule(time_up, 3.0)        # Run time_up after 3 second.

        if meet_hedgehog :
            time_up()

place_hedgehog()
place_coin()

pgzrun.go()