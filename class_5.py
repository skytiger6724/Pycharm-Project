class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, name):
        self._name = name

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self.age <= 16:
            print('%s正在玩飞行棋.' % self.name)
        else:
            print('%s正在玩斗地主.' % self.name)

def main():
    person = Person('王大��', 12)
    person.play()
    person.name = '白元芳'
    person.play()

if __name__ == '__main__':
    main()
