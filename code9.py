import math
def ball_collide(ball1,ball2):
    d = math.sqrt((x2-x1)**2+(y2-y1)**2)
    if d<=(r1+r2):
        return True
    else:
        return False

x1 = float(input("enter x for the ball1:"))
y1 = float(input("enter y for the ball1:"))
r1 = float(input("enter r for the ball1:"))
ball1 = (x1,y1,r1)

x2 = float(input("enter x for the ball2:"))
y2 = float(input("enter y for the ball2:"))
r2 = float(input("enter r for the ball2:"))
ball2 = (x2,y2,r2)

collison = ball_collide(ball1,ball2)
print("balls are colliding:",collison)

                
