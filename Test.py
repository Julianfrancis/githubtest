class Dog:
    def __init__(self, name, breed, age = 0, friendliness = True):
        self.name = name
        self.breed = breed
        self.age = age
        self.friendliness = friendliness
        self.friends = []

    def become_friends(self, other_dog, other_other_dog):
        if(other_other_dog.friendliness):
            self.friends.append(other_dog)
            self.friends.append(other_other_dog)
            other_dog.friends.append(self)
            other_dog.friends.append(other_other_dog)
            other_other_dog.friends.append(self)
            other_other_dog.friends.append(other_other_dog)
            print("{name} became friends with {other_name} and {other_other_name}!".format(name = self.name,
                    other_name = other_dog.name, other_other_name = other_other_dog.name))
        else:
            print("{name} did not become friends with {other_name}!".format(name = self.name, other_name = other_dog.name))

dog_one = Dog("Sparky", "Husky", 5)

dog_two = Dog("Roxy", "Shepard", 6)

dog_three = Dog("Max", "sausage", 9)

dog_one.become_friends(dog_two, dog_three)

print("{name} is a {breed} and is {age} years old".format (name = dog_one.name,
            breed = dog_one.breed, age = dog_one.age))
