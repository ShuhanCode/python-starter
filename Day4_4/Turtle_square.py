import turtle 

class Turtle:
    # Constructor
    def __init__ (self, colorInput):
        self.timmy = turtle.Turtle()
        self.timmy.shape("turtle")
        # Speed affects the pace of the turtle's motion on the
        self.timmy.speed(1)
        self.timmy.color(colorInput)
    def ski(self, num):
        if num == 0:
            return
        else:
            self.timmy.left(-90)
            self.timmy.forward(100)
            self.ski(num -1)

Fred = Turtle("blue")
Fred.ski(50)
