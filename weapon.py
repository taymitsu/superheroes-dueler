from ability import Ability
import random

class Weapon(Ability):
  def attack(self):
    """  This method returns a random value
    between one half to the full attack power of the weapon.
    """
    # TODO: Use integer division to find half of the max_damage value
    # then return a random integer between half of max_damage and max_damage
    random_value = random.randint((self.max_damage // 2 )), self.max_damage
    return random_value