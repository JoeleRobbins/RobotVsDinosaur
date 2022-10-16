class Weapon:

    def __init__(self, name):
        self.weapon_name = name
        self.attack_power = 25
        
class Robot:

    def __init__(self, name):
        self.robo_name = name
        self.robo_health = 200
        self.active_weapon = self.weapon_name

class Dinosaur:

    def __init__(self, name):
        self.name = name
        self.health = 200
        self.attack_power = 25
        
        
class Battlefield:

        def __init__ (self):
            self.attack = robot_health - dinosaur_attack

        def battling (self):
            if robot_health > 0:
                self.attack
            else:
                print ("The Dinosaur has won!")

        