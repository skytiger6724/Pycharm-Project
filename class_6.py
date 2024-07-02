# 验证三条边长是否可以构成三角形
from math import sqrt
class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

def main():
    a, b, c = 3, 4, 5
    # 如果三条边长不能构成三角形
    if not Triangle.is_valid(a, b, c):
        print('无法构成三角形.')
        return
    # 计算三角形的周长和面积
    triangle = Triangle(a, b, c)
    print('周长: %f' % triangle.perimeter())
    print('面积: %f' % triangle.area())

if __name__ == '__main__':
    main()

