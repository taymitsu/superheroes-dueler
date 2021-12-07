from ability import Ability
from armor import Armor
import random

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting.health = starting_health
        self.current.health = starting_health

    def fight(self, opponent):
        heroes = [self,opponent]
        if random.choice(heroes) == self: 
            print(f"{self.name} defeats {opponent.name}!")

        else:
            print(f"{opponent.name} defeats {self.name}!")

        #if __name__ == "__main__":
            #my_hero = Hero("Grace Hopper", 200)
            #print(my_hero.name)
            #print(my_hero.current_health)

