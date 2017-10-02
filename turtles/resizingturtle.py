"""Exports ResizingTurtle"""
import turtle
import math

class ResizingTurtle(turtle.Turtle):
    """A turtle that resizes the world coordinates so that everything
    it has drawn is always visible inside the window."""

    _timerRunning = False
    _boundingBox = [
        [-0, -0], # lower left [x,y]
        [0, 0], # upper right [x,y]
    ]
    _coordinates = ()
    _lastCoordinates = ()
    resizeDelay = 16 # ms between updates to world coordinates - useful for performance
    padding = 10
    ratio = 1 # width / height

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        turtle.mode("world")
        self._resize()
        self._applyresize()

    def _update(self):
        super()._update()
        pos = self._position
        x = int(pos[0])
        y = int(pos[1])

        resized = False
        if x < self._boundingBox[0][0]:
            self._boundingBox[0][0] = x
            resized = True
        if x > self._boundingBox[1][0]:
            self._boundingBox[1][0] = x
            resized = True
        if y < self._boundingBox[0][1]:
            self._boundingBox[0][1] = y
            resized = True
        if y > self._boundingBox[1][1]:
            self._boundingBox[1][1] = y
            resized = True

        if resized:
            self._resize()

    def _resize(self):
        minX = self._boundingBox[0][0]
        maxX = self._boundingBox[1][0]
        minY = self._boundingBox[0][1]
        maxY = self._boundingBox[1][1]

        width = maxX - minX
        height = maxY - minY
        size = max(max(width, height * (1 / self.ratio)), 1)
        size = math.ceil(size / self.padding) * self.padding + (2 * self.padding)

        leftX = minX - (size - width)/2
        leftY = minY - (size - height)/2

        _coordinates = (leftX, leftY, leftX + size, leftY + size)
        if _coordinates != self._coordinates:
            self._coordinates = _coordinates
            if not self._timerRunning:
                if self.resizeDelay:
                    self._timerRunning = True
                    turtle.ontimer(self._applyresize, self.resizeDelay)
                else:
                    self._applyresize()
    
    def _applyresize(self):
        self._timerRunning = False
        if self._coordinates != self._lastCoordinates:
            self._lastCoordinates = self._coordinates
            turtle.setworldcoordinates(*self._coordinates)

if __name__ == "__main__":
    bob = ResizingTurtle()
    bob.speed("fast")
    length = 50
    while True:
        bob.forward(length)
        bob.left(90)
        length = length + 10
    turtle.mainloop()
