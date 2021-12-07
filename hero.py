from random import choice, random 
from ability import Ability
from armor import Armor
from weapon import Weapon
from team import Team

class Arena:
    def __init__(self):
        self.team_one = Team("Team One")
        self.team_two = Team("Team Two")
    # TODO: create instance variables named team_one and team_two that
    # will hold our teams.

    def create_ability(self):
        name = input("What is the ability name?  ")
        max_damage = input("What is the max damage of the ability?  ")

        return Ability(name, max_damage)

    def create_weapon(self):
        name = input("What is the name of this weapon?  ")
        max_damage = input("What is the max damage of this weapon?  ")

        return Weapon(name, max_damage)

    def create_armor(self):
        name = input("What is the armor name? > ")
        max_block = input("What is the max block of the armor? > ")

        return Armor(name, max_block)

    def create_hero(self):
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None

        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                hero.add_ability(self.create_ability())
            elif add_item == "2":
                hero.add_weapon(self.create_weapon())
            elif add_item == "3":
                hero.add_armor(self.create_armor())
        return hero

    def build_team_one(self):
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")

        team_kills = 0
        team_deaths = 0
        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_one.name + " average K/D was: " + str(team_kills/team_deaths))

        for hero in self.team_two.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_two.name + " average K/D was: " + str(team_kills/team_deaths))

        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_one.name + ": " + hero.name)

        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_two.name + ": " + hero.name)

    if __name__ == "__main__":
        game_is_running = True

        # Instantiate Game Arena
        arena = Arena()

        #Build Teams
        arena.build_team_one()
        arena.build_team_two()

        while game_is_running:

            arena.team_battle()
            arena.show_stats()
            play_again = input("Play Again? Y or N: ")

            #Check for Player Input
            if play_again.lower() == "n":
                game_is_running = False

            else:
                #Revive heroes to play again
                arena.team_one.revive_heroes()
                arena.team_two.revive_heroes()

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