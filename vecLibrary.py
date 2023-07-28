from __future__ import annotations
from math import cos, sin, atan, radians, sqrt, pi
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge 

# Converts string to float. There may occur errors during rounding. 
# This is caused by python's rounding-method.
def strToFloat(s:str):
    stringSplit:list[str] = s.split(".")
    if len(stringSplit)==1:
        return int(stringSplit[0])+0.0
    return int(stringSplit[0])+(int(stringSplit[1][0])/10)

class Point:
    '''
    Represents a 2D point with x and y coordinates.

    Attributes:
        x (float): The x-coordinate of the point.
        y (float): The y-coordinate of the point.

    Methods:
        __init__(self, x: float, y: float)
            Initialize a Point object with the given x and y coordinates.

        __getitem__(self, key: int) -> float
            Returns the value of the coordinate corresponding to the given index.
            Index 0 corresponds to the x-coordinate, and index 1 corresponds to the y-coordinate.

        __setitem__(self, key: int, value: float)
            Sets the value of the coordinate corresponding to the given index.
            Index 0 corresponds to the x-coordinate, and index 1 corresponds to the y-coordinate.

        __str__(self) -> str
            Returns a string representation of the Point object in the format "(x; y)" with two decimal places.

    Example:
        point = Point(3.5, 2.0)
        print(point)  # Output: (3.50; 2.00)
    '''
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
    Represents a 2D vector with various methods for calculation and visualization.

    Attributes:
        pos (Point): The starting point (origin) of the vector.
        end (Point): The endpoint of the vector.
        length (float): The magnitude (length) of the vector.
        angle (float): The angle (in degrees) between the vector and the positive x-axis.
        color (str): The color used for rendering the vector (default is "red").

    Methods:
        __init__(self, pos: Point = None, end: Point = None, length: float = None,
                 angle: float = None, color: str = "red")
            Create a Vector object using one of the following methods:
                1. Specify length and angle to calculate the endpoint from the starting point.
                2. Specify both the starting and endpoint directly.
                3. Specify x and y components to calculate the length and angle.

        __str__(self) -> str
            Returns a string representation of the vector with rounded values.

        render(self, p, ax)
            Renders the vector using matplotlib.pyplot and matplotlib.axes.Axes.

        scalar_product(self, value: Vector) -> float
            Calculates and returns the scalar product (dot product) of two vectors.

        determinant(self, value: Vector) -> float
            Calculates and returns the determinant (cross product) of two vectors.

        __eq__(self, value: Vector) -> bool
            Returns True if the x and y values of both vectors are the same, ignoring position.
        
        __len__(self) -> float:
            Returns the length of the vector
      
        difference(self, value:Vector) -> Vector:
            Returns the result of two vectors subtracted.

    Example:
        # Create a vector using length and angle
        vector1 = Vector(length=5.0, angle=30.0)

        # Create a vector with specified start and endpoint
        start_point = Point(1.0, 2.0)
        end_point = Point(4.0, 6.0)
        vector2 = Vector(pos=start_point, end=end_point)

        # Create a vector using x and y components
        vector3 = Vector(2.0, 3.0)

        # Perform vector operations
        scalar_product_result = vector1.scalar_product(vector2)
        determinant_result = vector1.determinant(vector3)
    ''' 
    def __init__(self, pos:Point=None, end:Point=None, length:float=None,
                 angle:float=None,color:str="red"):
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
        # Calculates length using pythagoras theorem.
        self.length = sqrt(self.x**2+self.y**2)  
        self.angle = atan(self.y/self.x)*(180/pi)

    def __str__(self) -> str:
        '''Returns a string of the vector's values rounded'''
        return (f"Position: {self.pos}, Endpoint: {self.end}," + f" Size: [x:{self.x:.2f}, y:{self.y:.2f}],r: {self.length:.2f}, Angle: {self.angle:.2f}")

    def render(self, p, ax):
        """Renders vector using matplotlib.pyplot and
matplotlib.fig/ax"""
        plt.quiver([self.pos[0]], [self.pos[1]], [self.x], [self.y], angles='xy',
                 scale_units='xy', scale=1, color=self.color)

        # Length text
        plt.text(self.pos[0]+self.x/2,self.pos[1]+self.y/2+0.3,color=self.color,
               s=f"r: {self.length:.2f}",rotation=self.angle,
               horizontalalignment='center', verticalalignment='center')

        # Startpoint text
        plt.text(self.pos[0],self.pos[1]+0.3,color=self.color, s=self.pos,
               horizontalalignment='center', verticalalignment='center')

        # Endpoint text
        plt.text(self.end[0],self.end[1]+0.4,color=self.color, s=self.end,
               horizontalalignment='center', verticalalignment='center')

        # Angle-text and semi-circle
        direction = -1 if self.x<0 else 1 #   Where to write the text
        angle_patch = None

        #  It only makes wedges counterclockwise, so figuring out where the 
        #  start and end-angles are.
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

        # Makes the wedge and adds it to the figure
        angle_patch = Wedge([self.pos.x,self.pos.y], 0.6,start_angle, end_angle,
                            alpha=0.3, color=self.color)
        ax.add_patch(angle_patch)

        # Angle-text
        plt.text(self.pos.x+direction,self.pos.y,color=self.color,
               s=f"θ: {self.angle:.2f}°",horizontalalignment='center', 
               verticalalignment='center')

def scalar_product(self, value=Vector) -> float:
    '''Calculates and returns the scalarproduct of two given vectors.'''
    return((self.x*value.x)+(self.y*value.y))

def determinant(self, value=Vector) -> float:
    '''Returns determinant of given vectors'''
    return((self.x*value.y)-(self.y*value.x))

def __eq__(self, value=Vector) -> float:
    '''Returns True if the x and y values of both vectors are the same. 
    Ignoring position completely'''
    return(self.x == value.x and self.y == value.y)

def __len__(self) -> float:
    '''Returns the length of the vector'''
    return(self.length)

def difference(self, value:Vector) -> Vector:
    '''Returns the result of two vectors subtracted.'''
    if type(value) != type(self):
        raise ValueError(f"Can't subtract {type(value)} from the vector")
    self.x -= value.x
    self.y -= value.y
    self.angle = atan(self.y/self.x)*(180/pi)
    self.end = Point(self.pos.x+self.x, self.pos.y+self.y)
    return(self)
