"""Exports Turtle3D and Vec3"""
import turtle
from math import sin, cos, sqrt, radians

class Matrix:
    def __init__(self, definition):
        self._matrix = definition;
    
    @property
    def rows(self):
        return len(self._matrix)
    
    @property
    def cols(self):
        if self.rows > 0:
            return len(self._matrix[0])
        return 0

    def __getitem__(self, key):
        if isinstance(key, int):
            return self._matrix[key]
    
    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrix' did not have compatible sizes when multiplying")
        
        newRows = self.rows
        newCols = other.cols
        definition = []
        for y in range(newRows):
            row = []
            for x in range(newCols):
                total = 0
                for i in range(self.cols):
                    total += self[y][i]*other[i][x]
                row.append(total)
            definition.append(row)
        return Matrix(definition)
    
    def __repr__(self):
        return "[" + "\n ".join(
            map(
                lambda row: ",".join(
                    map(
                        lambda x: str(x),
                        row
                    )
                ),
                self._matrix
            )
        ) + "]"

class Vec3:
    def __init__(self, x=0, y=0, z=0):
        if isinstance(x, list) or isinstance(x, tuple):
            x, y, z = x
        self.set(x, y, z)

    def set(self, x=0, y=0, z=0):
        if isinstance(x, list) or isinstance(x, tuple):
            x, y, z = x
        self._coords = [round(x, 4), round(y, 4), round(z, 4)]
        self.x, self.y, self.z = self._coords
    
    def cross(self, other):
        return Vec3(
            self.y*other.z - self.z*other.y,
            self.z*other.x - self.x*other.z,
            self.x*other.y - self.y*other.x
        )

    def rotate(self, a, b=0, c=0):
        """Rotates the vector around (0,0,0). All angles in radians"""
        if isinstance(a, list) or isinstance(a, tuple):
            a, b, c = a

        # this is all the rotation matrix' from Wikipedia multiplied together
        # https://goo.gl/mdhzh7
        # could be implemented as matrix products, but meh - this saves a couple of CPU cycles
        newX = self.x*cos(b)*cos(c) + self.z*sin(b) - self.y*cos(b)*sin(c)
        newY = -self.z*cos(b)*sin(a) + self.x*(cos(c)*sin(a)*sin(b)+cos(a)*sin(c)) + self.y*(cos(a)*cos(c)-sin(a)*sin(b)*sin(c))
        newZ = self.z*cos(a)*cos(b) + self.x*(sin(a)*sin(c)-cos(a)*cos(c)*sin(b)) + self.y*(cos(c)*sin(a)+cos(a)*sin(b)*sin(c))
        self.set([newX, newY, newZ])

    @property
    def magnitude(self):
        x, y, z = self._coords
        return sqrt(x**2 + y**2 + z**2)

    @magnitude.setter
    def magnitude(self, value):
        if isinstance(value, int) or isinstance(value, float):
            x, y, z = self._coords
            ratio = value / self.magnitude
            self.set(x*ratio, y*ratio, z*ratio)

    def __add__(self, other):
        if isinstance(other, Vec3):
            x, y, z = self._coords
            i, j, k = other._coords
            return Vec3(x+i, y+j, z+k)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            x, y, z = self._coords
            return Vec3(x*other, y*other, z*other)
        return NotImplemented

    def __repr__(self):
        return "Vec3"+str(self._coords)

    def __getitem__(self, key):
        if isinstance(key, int):
            return self._coords[key]

    def __setitem__(self, key, value):
        if isinstance(key, int):
            self._coords[key] = value

class Turtle3D:
    """A turtle capable of moving in 3 dimensions.
    Heading is defined as an internal coordinate system."""
    screenZ = -100
    def __init__(self, *args, **kwargs):
        self.trtl = turtle.Turtle(*args, **kwargs)
        self._coord_sys = (
            Vec3(1, 0, 0), # forwards
            Vec3(0, 0, -1)  # left
        )
        self._pos = Vec3(0, 0, self.screenZ)
        self.trtl.penup()
        self._update()
        self.trtl.pendown()
    
    @property
    def coord_sys(self):
        # to correct for potential rounding errors, we recalculate all our vectors
        # up is calculated from forward cross left, then left is calculated from up cross forward
        forward = self._coord_sys[0]
        up = forward.cross(self._coord_sys[1])
        left = up.cross(forward)
        forward.magnitude = 1
        up.magnitude = 1
        left.magnitude = 1
        self._coord_sys = (
            forward,
            left
        )
        return (
            forward,
            left,
            up
        )
    
    def _point_to_world(self, point):
        """Converts a point expressed in our internal coordinate system
        to the world's coordinate system"""
        # based on http://www.imada.sdu.dk/~rolf/Edu/DM842/E17/notesOnChangeOfBasis.pdf
        coords = self.coord_sys
        matr = Matrix([
            [coords[0].x, coords[1].x, coords[2].x],
            [coords[0].y, coords[1].y, coords[2].y],
            [coords[0].z, coords[1].z, coords[2].z],
        ])
        converted = matr * Matrix([[point.x], [point.y], [point.z]])
        return Vec3(converted[0][0], converted[1][0], converted[2][0])

    def _world_to_screen(self, point):
        """Converts a point expressed in world's coordinate system to a screen coordinate"""
        z = point.z
        if z == 0:
            z = 0.00000001
        ratio = self.screenZ / z
        if ratio == 0:
            ratio = 0.00000001
        return (
            point.x * ratio,
            point.y * ratio
        )
    
    def _update(self):
        """Updates the position of our 2D turtle to reflect our new position"""
        screen_pos = self._world_to_screen(self._pos)
        self.trtl.goto(screen_pos)

    def left(self, angle):
        rad = radians(angle)
        leftRad = radians(angle + 90)
        newForward = Vec3(cos(rad), sin(rad), 0)
        newLeft = Vec3(cos(leftRad), sin(leftRad), 0)
        self._coord_sys = (
            self._point_to_world(newForward),
            self._point_to_world(newLeft)
        )
    def right(self, angle):
        self.left(-angle)
    def up(self, angle):
        rad = radians(angle)
        newForward = Vec3(cos(rad), 0, sin(rad))
        self._coord_sys = (
            self._point_to_world(newForward),
            self._coord_sys[1]
        )
    def down(self, angle):
        self.up(-angle)
    def roll(self, angle):
        rad = radians(angle)
        newLeft = Vec3(0, cos(rad), sin(rad))
        self._coord_sys = (
            self._coord_sys[0],
            self._point_to_world(newLeft)
        )
    lt = left
    rt = right
    ut = up
    dt = down
    yaw = left
    pitch = up

    def goto(self, x, y=0, z=-100):
        if isinstance(x, list) or isinstance(x, tuple):
            x, y, z = x
        self._pos = Vec3(x, y, z)
        self._update()

    def forward(self, length):
        self._pos += self.coord_sys[0] * length
        self._update()
    def backward(self, length):
        self.forward(-length)
    fd = forward
    bk = backward

    def __getattr__(self, name):
        """Proxies methods that aren't our own to our turtle.
        Useful for e.g. pencolor while allowing us to implement movement ourselves"""
        return getattr(self.trtl, name)

if __name__ == "__main__":
    trtl = Turtle3D()
    for i in range(5):
        trtl.forward(50)
        trtl.left(90)
        trtl.forward(50)
        trtl.up(90)
        trtl.forward(50)
        trtl.down(90)
        trtl.right(90)
    turtle.mainloop()
