from __future__ import annotations
from math import cos, sin, atan, radians, sqrt
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge


# Converts string to float.
# There may occur errors during rounding. This is caused by python's rounding-method.
def strToFloat(s: str):  # Takes string
    stringSplit: list[str] = s.split(".")
    if len(stringSplit) == 1:
        return int({0}) + 0.0  # "+0.0" converts given input to string
    return int(stringSplit[0]) + sum([int(stringSplit[1][_ - 1]) / 10 ** _ for _ in range(1, len(
        stringSplit[1]) + 1)])  # Takes sum of 10th, 100th and 1000th and so on.


class Point:
    def __init__(self, x: float, y: float):
        """Initialize a point using (x) and (y)-coordinates."""
        self.x = x
        self.y = y

    # Returns value or item of given index.
    def __getitem__(self, key: int) -> float:
        """Returns value or item of given index."""
        if key == 0:
            return self.x
        if key == 1:
            return self.y
        raise IndexError

    def __setitem__(self, key: int, value: float):
        """Makes sure item is within range of the init-method."""
        if key > 1:
            raise IndexError
        if key == 0:
            self.x = value
        if key == 1:
            self.y = value

    def __str__(self) -> str:
        """Returns string with 2 digits."""
        return f"({self.x:2.f};{self.y:2.f})"


class Vector:
    """
    Takes given input in form of points (using the class: Points), or length and angle in order to calculate or visualize.
    """


def __init__(self, pos: Point = None, end: Point = None, length: float = None, angle: float = None,
             colour: str = "red"):
    """
        Create a vector using either length and angle, start- and endpoint or x- and y-length.
        This method takes minimum amount of information.

        Examples: 
        // Position vectors: Vector(pos: Point) Vector(length: float, angle: float) // Connection vectors:
        Vector(pos: Point, end: Point)
        """
    self.colour = colour
    self.pos = pos
    self.end = end
    self.length = length
    self.angle = angle

    # Angle and length
    if angle is not None:
        if self.pos is None:
            self.pos = Point(0, 0)
        self.end = Point(self.pos.x + (length * cos(radians(angle))), self.pos.y + (length * sin(radians(angle))))

    elif end is None:
        self.pos = Point(0, 0)
        self.end = Point(pos.x, pos.y)
    self.x = self.end.x - self.pos.x
    self.y = self.end.y - self.pos.y
    self.length = sqrt(self.x ** 2 + self.y ** 2)  # calculates length using pythagoras theorem.


def __str__(self) -> str:
    """Returns a string of the given vector's value rounded."""
    return f"Position: {self.pos}, endpoint: {self.end}, " + f"size: [x{self.x:.2f}, y: {self.y:.2f}], length: {self.length:.2f}, angle: {self.angle:.2f}"


def render(self, pyplot, ax):
    """Renders vector using matplotlib.pyplot and matplotlib.fig/ax"""
    pyplot.quiver([self.pos[0]], [self.pos[1]], [self.x], [self.y], angles="xy", scale_units="xy", scale=1,
                  color=self.color)

    # Length-text
    pyplot.text(self.pos[0] + self.x / 2, self.pos[1] + self.y / 2 + 0.3, color=self.color,
                s=f"length: {self.length:.2f}", rotation=self.angle, horizontalalignment="center",
                verticalalignment="center")

    # Startpoint-text
    pyplot.text(self.pos[0], self.pos[1] + 0.3, color=self.color, s=self.length, horizontalalignment="center",
                verticalalignment="center")

    # Endpoint-text
    pyplot.text(self.end[0], self.end[1] + 0.04, color=self.color, s=self.end, horizontalalignment="center",
                verticalalignment="center")

    #Angl-text and semmi-circle
    direction = -1 if self.x<0 else 1
    aScrav1 = None
    
