from __future__ import annotations
from math import cos, sin, atan, radians, sqrt
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge 

# Converts string to float. There may occur errors during rounding. This is caused by python's rounding-method.
pi = 22/7
def strToFloat(s:str):
    stringSplit:list[str] = s.split(".")
    if len(stringSplit)==1:
        return int(stringSplit[0])+0.0
    return int(stringSplit[0])+(int(stringSplit[1][0])/10)

class Point:

    def __init__(self, x:float, y:float):
        '''Initialize a point with an x- and y-coordinate'''
        self.x = x
        self.y = y
    
    # Returns value or item of given index.
    def __getitem__(self, key:int) -> float:
        if key == 0:
            return self.x
        if key == 1:
            return self.y
        raise IndexError

    def __setitem__(self, key:int, value:float):
        if key > 1:
            raise IndexError
        if key == 0:
            self.x = value
        if key == 1:
            self.y = value

    def __str__(self):
        return f"({self.x:.2f};{self.y:.2f})"

class Vector:
    '''
    Takes given input in form of points (using the class: Points),
or length and angle in order to calculate or visualize. 
    '''
    def __init__(self, pos:Point=None, end:Point=None, length:float=None,angle:float=None,color:str="red"):
        '''
        Create a vector
             using either length and angle, start- and endpoint or x- and
             y-length. This method takes minimum amount of information.

        Examples: // Position vectors: Vector(pos: Point) Vector(length: float,
        angle: float) // Connection vectors: Vector(pos: Point, end: Point)
        '''
        self.color = color
        self.pos = pos
        self.end = end

        #  Angle and Length 
        if angle is not None:
            if self.pos == None:
                self.pos = Point(0,0)
            self.end = Point(self.pos.x + ( length * cos(radians(angle))),
                        self.pos.y + ( length * sin(radians(angle))))

            self.angle = angle
            self.length = length

        elif end is None:
            self.pos = Point(0,0)
            self.end = Point(pos.x,pos.y)
        self.x = self.end.x-self.pos.x
        self.y = self.end.y-self.pos.y
        self.length = sqrt(self.x**2+self.y**2) # calculates length using pythagoras theorem. 
        self.angle = atan(self.y/self.x)*(180/pi)

    def __str__(self) -> str:
        '''Returns a string of the vector's values rounded'''
        return (f"Position: {self.pos}, Endpoint: {self.end},"
                + f" Size: [x:{self.x:.2f}, y:{self.y:.2f}], r: {self.length:.2f}, Vinkel: {self.angle:.2f}")

    def render(self, p, ax):
        """Renders vector using matplotlib.pyplot and
matplotlib.fig/ax"""
        p.quiver([self.pos[0]], [self.pos[1]], [self.x], [self.y], angles='xy', scale_units='xy', scale=1, color=self.color)

        # Length text
        p.text(self.pos[0]+self.x/2,self.pos[1]+self.y/2+0.3,color=self.color,
                s=f"r: {self.length:.2f}",rotation=self.angle,horizontalalignment='center', verticalalignment='center')

        # Startpoint text
        p.text(self.pos[0],self.pos[1]+0.3,color=self.color,
                s=self.pos,horizontalalignment='center', verticalalignment='center')

        # Endpoint text
        p.text(self.end[0],self.end[1]+0.4,color=self.color,
                s=self.end,horizontalalignment='center', verticalalignment='center')

        # Angle-text and semi-circle
        direction = -1 if self.x<0 else 1#   Where to write the text
        angle_patch = None

        #   It only makes wedges counterclockwise, so figuring out where the start and end-angles
        start_angle = 0
        end_angle = self.angle
        
        if self.x<0:
            if self.angle < 0:
                startA = 180+self.angle
                end_angle = 180
            else:
                startA = 180
                end_angle = 180+self.angle
        else:
            if self.angle<0:
                startA = 0+self.angle
                end_angle = 0

        #       Make the wedge and add it to the figure
        aScrav1 = Wedge([self.pos.x,self.pos.y], 0.6,startA,end_angle, alpha=0.3, color=self.color)
        ax.add_patch(aScrav1)

        #       Angle text
        p.text(self.pos.x+_dir,self.pos.y,color=self.color,
                s=f"θ: {self.angle:.2f}°",horizontalalignment='center', verticalalignment='center')

# Calculates and returns the scalar product of two given vectors.
def scalar_product(self, value=Vector) -> float:
    return((self.x*value.x)+(self.y*value.y))
