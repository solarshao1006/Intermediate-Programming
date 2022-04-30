# A Black_Hole is derived from a Simulton base; it updates by finding+removing
#   any objects (derived from a Prey base) whose center is crosses inside its
#   radius (and returns a set of all eaten simultons); it displays as a black
#   circle with a radius of 10 (e.g., a width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey

class Black_Hole(Simulton):  
    radius = 10
    def __init__(self,x,y,width=20,height=20):
        Simulton.__init__(self, x, y, width, height)
        
    def update(self,model):
        res1 = model.find(lambda x: issubclass(type(x), Prey))
        res2 = model.find(lambda x: self.contains(x.get_location()))
        model.balls = model.balls - res1.intersection(res2)
        return res1.intersection(res2)
    
    def display(self,canvas):
        canvas.create_oval(self._x-Black_Hole.radius, self._y- Black_Hole.radius, self._x+Black_Hole.radius, self._y+Black_Hole.radius,fill='black')
    
    def contains(self, xy):
        return self.distance(xy) < self._width/2
        