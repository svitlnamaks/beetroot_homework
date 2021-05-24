# Task 1
# Method overloading.
# Create a base class named Animal with a method called talk and then create two subclasses:
# Dog and Cat, and make their own implementation of the method talk be different.
# For instance, Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.

# Also, create a simple generic function, which takes as input instance of a Cat or Dog classes
# and performs talk method on input parameter.

class Animal :
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def talk(self) :
        return 'We cannot use this option'


class Dog(Animal) :
    def talk(self) :
        return f'{self.name} say woof woof'


class Cat(Animal) :
    def talk(self) :
        return f'{self.name} say meow'


def talk_fun(animals) :
    sound = input('What should the animal say ?\n')
    return f'{animals} say {sound}'


if __name__ == '__main__' :
    pet1 = Cat('Leo', 4)
    pet2 = Dog('Bleck', 8)
    pet3 = Animal('Milka', 5)

    print(pet1.talk())
    print(pet2.talk())
    print(pet3.talk())

    print(talk_fun(pet1.name))
