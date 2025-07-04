class circle():
    def __init__(self,diameter):
        self.diameter = diameter
        self.radius = diameter/2
        
    def get_area(self):
        d=self.diameter
        return (3.14*d**2)/4

c1= circle(4)
c2 = circle(5)
print(c1.get_area())
print(c2.get_area())
