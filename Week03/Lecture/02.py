class Duck:
    def quack(self):
        print("Quack!")

def make_it_quack(obj):
    obj.quack()

duck = Duck()
make_it_quack(duck)   # Output: Quack!



class Person:
    def quack(self):
        print("I'm quacking like a duck!")
person = Person()
make_it_quack(person) # Output: I'm quacking like a duck!        