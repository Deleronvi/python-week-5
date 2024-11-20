# Superhero Class
class Superhero:
    def __init__(self, name, power, weakness):
        self.name = name
        self.power = power
        self.weakness = weakness
    
    def introduce(self):
        return f"I am {self.name}! My superpower is {self.power}."

    def reveal_weakness(self):
        return f"My weakness is {self.weakness}."

# Villain Class (inherits from Superhero)
class Villain(Superhero):
    def __init__(self, name, power, weakness, evil_plan):
        super().__init__(name, power, weakness)
        self.evil_plan = evil_plan

    def introduce(self):
        return f"I am {self.name}, the villain! Beware of my {self.power}."

    def share_evil_plan(self):
        return f"My evil plan is: {self.evil_plan}!"

# Example Usage
hero = Superhero("Captain Code", "Debugging", "Syntax Errors")
villain = Villain("Bugzilla", "Crashing Systems", "Logic Puzzles", "Take over the internet!")

print(hero.introduce())
print(hero.reveal_weakness())
print(villain.introduce())
print(villain.share_evil_plan())

