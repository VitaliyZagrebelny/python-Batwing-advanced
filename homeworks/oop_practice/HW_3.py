from abc import abstractmethod, ABC
import random


class Person(ABC):
    def __init__(self, name, age, availability_of_money, own_home):
        self.name = name
        self.age = age
        self.availability_of_money = availability_of_money
        self.own_home = own_home

    @abstractmethod
    def info(self):
        raise NotImplementedError("This method is not realized")

    @abstractmethod
    def make_money(self, house):
        raise NotImplementedError("This method is not realized")

    @abstractmethod
    def buy_house(self, house):
        raise NotImplementedError("This method is not realized")


class Human(Person):
    def __init__(self, name, age, availability_of_money, own_home):
        super().__init__(name, age, availability_of_money, own_home)

    def info(self):
        print(f'Hello, my name {self.name}, i am {self.age}')

    def make_money(self, house):
        while self.availability_of_money < house.cost:
            print("I go working")
            self.availability_of_money += 7000

    def buy_house(self, house):
        if self.own_home == 0:
            print(f'{self.name}, i want buy house')
            self.make_money(house)
            self.availability_of_money = self.availability_of_money - house.cost
            print(f'{self.name}, buy {house.name} and now has  {self.availability_of_money}')
            self.own_home = 1
        else:
            print(f'{self.name} i can house')


class House:
    def __init__(self, name, area, cost):
        self.name = name
        self.cost = cost
        self.area = area

    def house_info(self):
        print(f'{self.name}: Area of house {self.area}, and it cost {self.cost}')

    def discount(self):
        if self.area >= 60:
            print(f'{self.name} has 20% discount')
            self.cost = self.cost * 0.8
        elif self.area >= 40 and self.area < 60:
            print(f'{self.name} has 10% discount')
            self.cost = self.cost * 0.9
        else:
            print(f'{self.name} not discount')


class SmallHouse(House):
    def __init__(self, name, area, cost):
        super().__init__(name, area, cost)
        if area > 40:
            self.__class__ = House


class RealtorMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMeta):
    def __init__(self, name, houses, discount: bool):
        self.name = name
        self.houses = houses
        self.discount = discount

    def realtor_info(self):
        print(f'Hello, my name is {self.name}, i can help you with buying')

    def houses_info(self):
        for house in self.houses:
            house.house_info()

    def make_discount(self, houses):
        if self.discount is True:
            houses.discount()

    def steal_money(self, person):
        if random.randrange(11) == 10:
            person.availability_of_money = 0
            print(f'{self.name}, he was able to steal money from {person.name}')
        else:
            print("He did not succeed steal money")


person1 = Human("Vitalii", 25, 5500, 0)
person2 = Human("Vitya", 50, 2000, 1)
person3 = Human("Vasya", 22, 6000, 0)

person1.info()
person2.info()
person3.info()

houses1 = House("Cottage", 30, 4500)
houses2 = House("Mansion", 45, 3000)
houses3 = House("Penthouse", 60, 5500)

realtor = Realtor("Jonh", [houses1, houses2, houses3], True)

realtor.realtor_info()
print("=" * 20)
realtor.houses_info()
print("=" * 20)

person1.buy_house(houses1)
print("=" * 20)
realtor.make_discount(houses2)
person2.buy_house(houses2)
print("=" * 20)
person3.buy_house(houses3)
print("=" * 20)
realtor.steal_money(random.choice([houses1, houses2, houses3]))
