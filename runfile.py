from vecLibrary import Vector, Point, scalar_product, determinant, __eq__
vec_a = Vector(Point(2,3))
vec_b = Vector(Point(4,8))

vec_c = Vector(Point(2,5))
vec_d = Vector(Point(2,5))

print(scalar_product(vec_a, vec_b))
print(determinant(vec_a, vec_b))
print(__eq__(vec_c, vec_d))
