# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole

class Pulsator(Black_Hole): 
    counter = 30
    def __init__(self,x,y,width=20,height=20):
        Black_Hole.__init__(self, x, y, width, height)
        self._counter = 0
    def update(self,model):
        res = Black_Hole.update(self,model)
        if res:
            self._width += 1
            self._height += 1
            self._counter = 0
        else:
            self._counter += 1
        if self._counter == Pulsator.counter:
            self._width -= 1
            self._height -= 1
            self._counter = 0
        if self.get_dimension() == (0,0):
            model.remove(self)
        return res
    
    def display(self, canvas):
        canvas.create_oval(self._x-self._width/2, self._y- self._height/2, self._x+self._width/2, self._y+self._height/2,fill='black')