# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


#from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random

class Floater(Prey): 
    radius = 5
    def __init__(self,x,y,width=radius*2,height=radius*2):
        Prey.__init__(self, x, y, width, height,0, 5)
        Prey.randomize_angle(self)
        
    def update(self, model):
        incre = random() - 0.5
        while self._speed + incre > 7 or self._speed + incre < 3:
            incre = random() - 0.5
        
        Prey.set_speed(self, self._speed + incre)
        Prey.set_angle(self, self._angle + random() - 0.5)
        self.move()
        self.wall_bounce()
        
    def display(self,canvas):
        canvas.create_oval(self._x-Floater.radius      , self._y- Floater.radius,
                                self._x+Floater.radius, self._y+Floater.radius,
                                fill='red')

if __name__ == '__main__':
    f = Floater(1,115,300,300,2)
    f.update()
    print(f._speed, f._angle)
    