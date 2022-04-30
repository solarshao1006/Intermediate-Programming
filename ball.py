# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10). 


from prey import Prey
class Ball(Prey): 
    radius = 5
    def __init__(self,x,y,width=10, height=10):
        Prey.__init__(self,x,y,width,height,0,0)
        Prey.randomize_angle(self)
        self._speed = 5
        
    def update(self,model):
        self.move()
        self.wall_bounce()
    
    def display(self,canvas):
        canvas.create_oval(self._x-Ball.radius, self._y- Ball.radius, self._x+Ball.radius, self._y+Ball.radius,fill='blue')

if __name__ == '__main__':
    pass