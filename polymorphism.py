class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Duck(Animal):
    def make_sound(self):
        return "Quack!"

def play_animal_sound(animal_object):
    print(animal_object.make_sound())

if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    duck = Duck()

    play_animal_sound(dog)
    play_animal_sound(cat)
    play_animal_sound(duck)
