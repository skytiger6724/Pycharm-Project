# 定义类
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情大电影.' % self.name)

def main():
    stu1 = Student('王大锤', 15)
    stu2 = Student('白元芳', 25)
    stu1.study('Python程序设计')
    stu2.study('思想品德')
    stu1.watch_movie()
    stu2.watch_movie()

if __name__ == '__main__':
    main()