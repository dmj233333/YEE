import random
import turtle
screen=turtle.Screen()
screen.delay(10)
o_turtle=turtle.Turtle()
o_turtle.shape('square')
o_turtle.penup()
sprite=turtle.Turtle()
sprite.penup()
sprite.speed(0)
sprite.ht()
player=sprite.clone()
player.shape('turtle')
player.color('red')
player.seth(90)
player.goto(0,-180)
player.st()
cars=[]
for i in range(30):
    car=sprite.clone()
    car.shape('square')
    car.color('yellow')
    if i %2:
        car.seth(0)
    else:
        car.seth(180)
    car.goto(random.randint(-300,300),-120+i*30)
    car.st()
    cars.append(car)


def update():
    player.fd(10)
    if player.ycor()<200:
        for c in cars:
            c.fd(10)
            if c.distance(player)<20:
                player.write('you lose')
                break
            elif c.xcor()<-200 or c.xcor()>200:
                c.left(180)
        else:
            screen.ontimer(update,50)
    else:
        player.write('you win')
update()
def z():
    x=random.randint(-240,240)
    y=random.randint(-180,180)
    o_turtle.goto(x,y)
    
def right():
    player.seth(0)
    
def up():
    player.seth(90)
def left():
    player.seth(180)
def down():
    player.seth(270)
def l():
    player.forward(30)
def j():
    for v in range(5):
        player.forward(50)
        player.backward(50)
        player.right(15+3)
screen.ontimer(z,1000)
screen.onkey(right,'Right')
screen.onkey(left,'Left')
screen.onkey(up,'Up')
screen.onkey(down,'Down')
screen.onkey(l,'R')
screen.onkey(j,'J')
screen.listen()

