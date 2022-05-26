from abc import abstractmethod


# ====1====
class Animal:
    def __init__(self, name, food, sleep):
        self.name = name
        self.food = food
        self.sleep = sleep

    def get_name(self):
        print(self.name)

    def get_food(self):
        print(self.food)

    def get_sleep(self):
        print(self.sleep)


class Dog(Animal):
    def __init__(self, name, food, sleep):
        super().__init__(name, food, sleep)

    def get_command_dog(self):
        print("Gav-Gav")


Jack = Dog("Jack", "Meat", 10)
Jack.get_name()
Jack.get_command_dog()
Jack.get_food()
Jack.get_sleep()
print(issubclass(Dog, Animal))

print("========")


class Cat(Animal):
    def __init__(self, name, food, sleep):
        super().__init__(name, food, sleep)

    def get_command_cat(self):
        print("Meow")


mrCat = Cat("mrCat", "Fish", 5)
mrCat.get_name()
mrCat.get_command_cat()
mrCat.get_food()
mrCat.get_sleep()
print(issubclass(Cat, Animal))

print("========")


class Bear(Animal):
    def __init__(self, name, food, sleep):
        super().__init__(name, food, sleep)

    def get_command_bear(self):
        print("Brrrr")


Misha = Bear("Misha", "meat", 100)
Misha.get_name()
Misha.get_command_bear()
Misha.get_food()
Misha.get_sleep()
print(issubclass(Bear, Animal))

print("========")


class Frog(Animal):
    def __init__(self, name, food, sleep):
        super().__init__(name, food, sleep)

    def get_command_frog(self):
        print("kva-kva")


CrazyFrog = Frog("CrazyFrog", "insects", 12)
CrazyFrog.get_name()
CrazyFrog.get_command_frog()
CrazyFrog.get_food()
CrazyFrog.get_sleep()
print(issubclass(Frog, Animal))

print("========")


class Duck(Animal):
    def __init__(self, name, food, sleep):
        super().__init__(name, food, sleep)

    def get_command_duck(self):
        print("krya-krya")


Scrooge = Duck("Scrooge", "insects", 22)
Scrooge.get_name()
Scrooge.get_command_duck()
Scrooge.get_food()
Scrooge.get_sleep()
print(issubclass(Duck, Animal))

# ====1a====
print("========")


class Human():
    def __init__(self, eat, sleep, study, work):
        self.eat = eat
        self.sleep = sleep
        self.study = study
        self.work = work

    def get_info_human(self):
        print(f"Eat: {self.eat}, Sleep: {self.sleep}, Study: {self.study}, Work: {self.work}")


class Centaur(Animal, Human):
    def __init__(self, name, eat, sleep, study, work):
        Animal.__init__(self, name, eat, sleep)
        Human.__init__(self, eat, sleep, study, work)

    def get_info_centaur(self):
        print(f"My name is {self.name}")


centaur = Centaur('Name', 'deer', 10, 'English', "Teacher")
centaur.get_info_human()
centaur.get_info_centaur()

print("========")


# ====2a====
class Person:
    def __init__(self, name):
        self.name = name
        call1 = Arm("9:00")
        call2 = Arm("10:00")
        call3 = Arm("11:00")
        self.calls = [call1.call, call2.call, call3.call]


class Arm:
    def __init__(self, call):
        self.call = call


arm = Person("Vitalii")
print(f"Name {arm.name} called in {arm.calls}")

print("========")


# ====2b====
class CellPhone:
    def __init__(self, screens):
        self.screeens = screens


class Screen:
    def __init__(self, content_screens):
        self.content_screens = content_screens


screens0 = Screen('Screen0')
screens1 = Screen('Screen1')
screens2 = Screen('Screen2')
screens3 = Screen('Screen3')
screens4 = Screen('Screen4')

screens = [screens0.content_screens, screens1.content_screens, screens2.content_screens,
           screens3.content_screens, screens4.content_screens]

Phone = CellPhone(screens)
print(f"My screens is {Phone.screeens}")

# ====3====
print("========")


class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex


info = Profile('Vitalii', 'Zahrebelnyi', '65465465', 'Kyiv', 'vitalii@gmail.com',
               '17/10/2001', '20', 'man')
print(info.__dict__)
print(f'Hi my name is {info.name} {info.last_name}, {info.sex}. '
      f'I am {info.age}, my birthday is {info.birthday}. '
      f'You can called me {info.phone_number} and email {info.email}. '
      f'My address is {info.address}')

print("========")


# ====4====

class Laptop:
    @abstractmethod
    def Screen(self):
        raise NotImplementedError("This method was not implemented")

    @abstractmethod
    def Keyboard(self):
        raise NotImplementedError("This method was not implemented")

    @abstractmethod
    def Touchpad(self):
        raise NotImplementedError("This method was not implemented")

    @abstractmethod
    def WebCam(self):
        raise NotImplementedError("This method was not implemented")

    @abstractmethod
    def Ports(self):
        raise NotImplementedError("This method was not implemented")

    @abstractmethod
    def Dynamics(self):
        raise NotImplementedError("This method was not implemented")


class HPLaptop(Laptop):
    def __init__(self):
        pass

    def Screen(self):
        self.screen = input('Please enter information about screen: ')
        return self.screen

    def Keyboard(self):
        self.keyboard = input('Please enter information about keyboard: ')
        return self.keyboard

    def Touchpad(self):
        self.touchpad = input('Please enter information about touchpad: ')
        return self.touchpad

    def WebCam(self):
        self.webcam = input('Please enter information about web cam: ')
        return self.webcam

    def Ports(self):
        self.ports = input('Please enter information about ports: ')
        return self.ports

    def Dynamics(self):
        self.dynamics = input('Please enter information about dynamics: ')
        return self.dynamics

    def info(self):
        self.Screen()
        self.Keyboard()
        self.Touchpad()
        self.WebCam()
        self.Ports()
        self.Dynamics()
        print(f'Information screen: {self.screen};')
        print(f'Information keyboard: {self.keyboard};')
        print(f'Information touchpad: {self.touchpad};')
        print(f'Information webcam: {self.webcam};')
        print(f'Information ports: {self.ports};')
        print(f'Information dynamics: {self.dynamics};')


comp = HPLaptop()
comp.info()
