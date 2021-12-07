from random import choice, random 
from ability import Ability
from armor import Armor
from weapon import Weapon
from team import Team

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting.health = starting_health
        self.current.health = starting_health

        self.abilities = list()
        self.armors = list()
        self.deaths = 0
        self.kills = 0 

    def fight(self, opponent):
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw!")
        else: 
            while self.current_health > 0 or opponent.current_health > 0:
                total_damage = self.attack()
                opponent.take_damage(total_damage)

                if opponent.is_alive() == True:
                    total_damage = opponent.attack()
                    self.take_damage(total_damage)

                    if self.is_alive == True:
                        total_damage = self.attack()
                        #OPPONENT TAKES DAMAGE
                        opponent.take_damage(total_damage)
                    else:
                        #SELF=DEAD, opponent wins
                        self.deaths += 1
                        opponent.kills += 1
                    return print(f"{opponent.name} defeats {self.name}!")

                elif opponent.is_alive() == False:
                    opponent.deaths += 1
                    self.kills += 1
                    return print (f"{self.name} defeats {opponent.name}!")

        #if __name__ == "__main__":
            #my_hero = Hero("Grace Hopper", 200)
            #print(my_hero.name)
            #print(my_hero.current_health)
    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        total_damage = 0 

        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
    
    def defend(self):
        total_block = 0
        if self.current_health == 0:
            return total_block
        for armor in self.armors:
            total_block += armor.block()
        return total_block
    
    def take_damage(self, damage):
        defense = self.defend()
        new_damage = damage - defense 
        if new_damage > 0:
            self.current_health -= new_damage
            return self.current_health
        else:
            return "No damage was taken"
        #print(f"{self.name} has taken damage! Current health: {self.current_health}")
    
    def is_alive(self):
        if self.current_health <= 0:
            return False
        else: 
            return True 

    def add_weapon(self, weapon):
        self.abilities.append(weapon)
    
    def add_kill(self, num_kills):
        ''' Update self.kills by num_kills amount'''
        self.kills += num_kills
    
    def add_death(self, num_deaths):
        ''' Update deaths with num_deaths'''
        # TODO: This method should add the number of deaths to self.deaths
        self.death += num_deaths

if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())


    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)