#A special Hunter that user can use 'W A S D' to control the moving direction; If the ball touches any edge
#of the window, an warning message will pop-up, indicating the user loses and asking whether to start over.
#If yes, the window will reset automatically; If no, the window will close.
import model
from hunter import Hunter
import math 
from pulsator import Pulsator


class Special(Hunter):
    def __init__(self,x,y):
        Hunter.__init__(self, x, y)
        self.set_speed(10)
        
    def update(self,model):
        res = Pulsator.update(self,model)
        if model.key == 'W':
            self.set_angle(3*math.pi/2)
        if model.key == 'S':
            self.set_angle(math.pi/2)
        if model.key == 'A':
            self.set_angle(math.pi)
        if model.key == 'D':
            self.set_angle(0)
        
        self.move()
        res = self.wall_bounce()
        return res
    def display(self, canvas):
        canvas.create_oval(self._x-self._width/2, self._y- self._height/2, self._x+self._width/2, self._y+self._height/2,fill='green')
        
    def wall_bounce(self):
        x,y      = self.get_location()
        w,h      = self.get_dimension()
        mw,mh    = model.world()
        
        left_x   = x - w/2
        right_x  = x + w/2
        top_y    = y - h/2
        bottom_y = y + h/2

        if left_x < 0 or right_x > mw or top_y < 0 or bottom_y > mh:
            
            return 'lose'
