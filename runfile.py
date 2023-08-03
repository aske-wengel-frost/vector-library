import matplotlib.pyplot as plt
from vecLibrary import (
    Vector,
    Point,
    scalar_product,
    determinant,
    __eq__,
    __str__,
    difference,
)

# Create vectors
vec_a = Vector(Point(2, 3))
vec_b = Vector(Point(4, 8), color="blue")
vec_c = Vector(Point(2, 5), color="purple")
vec_d = Vector(Point(2, 5), color="purple")

# Trying out the different functions
print(scalar_product(vec_a, vec_b))
print(determinant(vec_a, vec_b))
print(__eq__(vec_c, vec_d))
print(difference(vec_b, vec_c))

# Trying out the __getitem__ function
point_1 = Point(1, 2)
x_coordinate = point_1.__getitem__(0)
print("point_1's x-coordinate:", x_coordinate)

# Create a and axes for visualization
fig, ax = plt.subplots()
vec_a.render(fig, ax)
vec_b.render(fig, ax)
vec_c.render(fig, ax)
vec_d.render(fig, ax)

# Specify plot limitations
plt.xlim(-1, 6)
plt.ylim(-1, 10)
plt.grid()

# Set the window title
# without '.manger' if running on windows.
plt.gcf().canvas.manager.set_window_title("Vector visualization")
plt.show()
