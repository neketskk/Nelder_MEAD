import random
class Vector:
    x: float = 0
    y: float = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'({round(self.x, 4)}, {round(self.y, 4)})'
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __truediv__(self, other):
        x = self.x / other
        y = self.y / other
        return Vector(x, y)
    def __rmul__(self, other):
        x = self.x * other
        y = self.y * other
        return Vector(x, y)
    def __mul__(self, other):
        x = self.x * other
        y = self.y * other
        return Vector(x, y)
def area(p1: Vector, p2: Vector, p3: Vector) -> float:
    if p1 == p2 or p2 == p3 or p1 == p3:
        return 0.0
    v1 = p2 - p3
    v2 = p3 - p1
    return abs(0.5 * (v1.x * v2.y - v1.y * v2.x))
def func_r(v: Vector) -> float:
    return  100 * (v.x**2 - v.y) ** 2 + (1 - v.x) ** 2
def func_r1(v: Vector) -> float:
    return  100 * (v.y - v.x**3) ** 2 + (1 - v.x) ** 2
def Nelder_Mead(func,
                 p1: Vector,
                 p2: Vector,
                 p3: Vector,
                 alpha=float(input("Enter conditions:\nalpha=")),
                 beta=float(input("beta=")),
                 gamma=float(input("gamma=")),
                 delta=float(input("delta=")),
                 iters=int(input("iterations=")),
                 min_area: float = 1e-10,
                 precision: float = 1e-10,
                 ) -> (Vector|None, int|None):
    global i
    if area(p1, p2, p3) < min_area:
        print('\n\tYou entered three points on one line!\n EROR 404')
        exit(0)
    best_p, good_p, worst_p = p1, p2, p3
    points = [[p, func(p)] for p in [best_p, good_p, worst_p]]
    points.sort(key=lambda x: x[1])
    best_p, good_p, worst_p = (_[0] for _ in points)
    cur_worst_f = func(worst_p)
    for i in range(iters):
        prev_worst_f = cur_worst_f
        mid_p = (best_p + good_p) / 2
        p_reflection = mid_p + alpha * (mid_p - worst_p)
        if func(p_reflection) < func(good_p):
            worst_p = p_reflection
            p_expansion = mid_p + beta * (mid_p - worst_p)
            if func(p_expansion) < func(best_p):
                good_p = p_expansion
        else:
            if func(p_reflection) < func(worst_p):
                worst_p = p_reflection
            p_contraction = mid_p + gamma * (mid_p - worst_p)
            if func(p_contraction) < func(worst_p):
                worst_p = p_contraction
            else:
                good_p = best_p + delta * (good_p - best_p)
                worst_p = best_p + delta * (worst_p - best_p)
        points = [[p, func(p)] for p in [best_p, good_p, worst_p]]
        points.sort(key=lambda x: x[1])
        print("№",i+1,best_p,good_p,worst_p)
        best_p, good_p, worst_p = (_[0] for _ in points)
        cur_worst_f = func(worst_p)
        area_break = area(best_p, good_p, worst_p)
        precision_break = abs(cur_worst_f - prev_worst_f)
        if area_break < min_area or precision_break < precision:
            break
    return best_p, i
YorN = input('Enter data yourself or randomly? Y or N?\n')
if YorN == "Y":
    a, b = map(float, input('First point coordinates: ').split())
    p_1 = Vector(a, b)
    a, b = map(float, input('Second point coordinates: ').split())
    p_2 = Vector(a, b)
    a, b = map(float, input('Third point coordinates: ').split())
    p_3 = Vector(a, b)
elif YorN == "N":
    p_1 = Vector(random.randint(-10, 10), random.randint(-10, 10))
    p_2 = Vector(random.randint(-10, 10), random.randint(-10, 10))
    p_3 = Vector(random.randint(-10, 10), random.randint(-10, 10))
else:
    print("\nIncorrect data entered \n EROR 404")
    exit(0)
test=input('Select a test. 1 or 2?\n')
if test == "1":
    min_point, iteration = Nelder_Mead(func=func_r,p1=p_1,p2=p_2,p3=p_3)
    print('Algorithm completed:', iteration+1)
    print('Minimum function at a point (x, y) = ', min_point)
    print('Function value F(x, y) = ', round(func_r(min_point), 6))
elif test=="2":
    print('Algorithm completed:', iteration+1)
    print('Minimum function at a point (x, y) = ', min_point)
    print('Function value F(x, y) = ', round(func_r1(min_point), 6))
    min_point, iteration = Nelder_Mead(func=func_r1,p1=p_1,p2=p_2,p3=p_3)
else:
    print("\nIncorrect data entered \n EROR 404")
    exit(0)