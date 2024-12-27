class Dog:
    species = "German Shepherd"
    species2 = "Golden Retreiver"
    def __init__(self, name, age, stat, gender):
        self.name = name
        self.age = age
        self.stat = stat
        self.gender = gender
Bingo = Dog("Bingo", 8, "brave", "male")
Joey = Dog("Joey", 5, "playful", "male")
print("Bingo is a {}".format(Bingo.species))
print("Joey is a {}".format(Joey.species2))
print("{} is {} years old".format(Bingo.name, Bingo.age))
print("{} is {} years old".format(Joey.name, Joey.age))
print("{} is {}".format(Bingo.name, Bingo.stat))
print("{} is {}".format(Joey.name, Joey.stat))
print("{} is a {}".format(Bingo.name, Bingo.gender))
print("{} is also a {}".format(Joey.name, Joey.gender))