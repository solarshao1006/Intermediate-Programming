# A Hunter class is derived from a Pulsator and then Mobile_Simulton base.
#   It inherits updating+displaying from Pusator/Mobile_Simulton: it pursues
#   any close prey, or moves in a straight line (see Mobile_Simultion).


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2

class Hunter(Pulsator, Mobile_Simulton):
    distance_cons = 200
    def __init__(self, x, y):
        Mobile_Simulton.randomize_angle(self)
        Pulsator.__init__(self,x,y)
        self._width = self.get_dimension()[0]
        self._height = self.get_dimension()[1]
        Mobile_Simulton.__init__(self,x,y,self._width,self._height,angle=0,speed=5)
    
    def update(self,model):
        res1 = model.find(lambda x: issubclass(type(x), Prey))
        res2 = model.find(lambda x: Mobile_Simulton.distance(self, x.get_location())<=Hunter.distance_cons)
        inter = res1.intersection(res2)
        if inter:
            self._counter = 0
            target = sorted([(b, Mobile_Simulton.distance(self,b.get_location()))for b in list(inter)], key=lambda x: x[1])[0][0]
            self.set_angle(atan2(target._y-self._y, target._x-self._x))
        
            if self.contains(target.get_location()):
                self._width += 1
                self._height += 1
                model.remove(target)
        else:
            self._counter += 1
        if self._counter == Pulsator.counter:
            self._width -= 1
            self._height -= 1
            self._counter = 0
        if self.get_dimension() == (0,0):
            model.remove(self)
    
        self.move()
        self.wall_bounce()
    
    def display(self, canvas):
        Pulsator.display(self, canvas)