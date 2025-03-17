#obj_ship_player.py
#This file defines the player's ship.

#position = [[QuadrantX,QuadrantY],[SectorX,SectorY]]

import random

class Player:
    def __init__(self, ship_name, captain_name, energy_max, shields, torpedoes_max):
        self.energy_max = energy_max
        self.energy = energy_max
        self.shields = shields
        self.torpedoes_max = torpedoes_max
        self.torpedoes = torpedoes_max
        self.position = [[5,5],[5,5]]
        self.systems = {}
        self.set_all_systems_to_ok()
        self.ship_name = ship_name
        self.captain_name = captain_name
        print(f"Ship Created")
        self.print_status()

    def print_status(self):
        print(f"USS {self.ship_name}, Captain {self.captain_name} commanding.")
        print(f"Energy: {self.energy}/{self.energy_max}  Torpedoes: {self.torpedoes}/{self.torpedoes_max}")
        print(f"Shields: {self.shields}")
        print(f"Position - Quadrant: {self.position[0][0]}, {self.position[0][1]}  Sector {self.position[1][0]},{self.position[1][1]}")

    def damage_report(self):
        for system, status in self.systems.items():
            print (f"{system}  {status}")        

    def refill_energy(self):
        self.energy = self.energy_max
        print ("Energy Refilled.")

    def refill_torpedoes(self):
        self.torpedoes = self.torpedoes_max
        print ("Torpedoes Refilled.")

    def add_energy_to_shields(self, add_energy):
        if self.energy < add_energy:
            print("Not enough energy")
        else:
            self.energy -= add_energy
            self.shields += add_energy
            print (f"{add_energy} energy transferred to shields")

    def set_all_systems_to_ok(self):
        self.systems = {
            "Engines": "OK",
            "Shields": "OK",
            "Weapons": "OK",
            "Sensors": "OK",
            "Life Support": "OK",
            "Warp Drive": "OK",
            "Communications": "OK"
        }
        print (f"All systems nominal.")

    def repair_system(self, system):
        if self.systems[system] == "OK":
            print(f"{system} is already functioning normally.")
        else:
            self.systems[system] = "OK"
            print(f"{system} repaired.")

    def launch_torpedo(self):
        if self.torpedoes <= 0:
            print("Out of torpedoes.")
        else:
            self.torpedoes -= 1
            print("Torpedo launched.")
            #result of firing will be handled in outside function

    def fire_phasors(self, phasor_energy):
        if phasor_energy > self.energy:
            print("Not enough energy")
        else:
            self.energy -= phasor_energy
            print("Firing phasors.")
            #result of firing will be handled in outside function

    def damage_shields(self, damage):
        self.shields -= damage
        if self.shields <= 0:
            self.shields = 0
        print(f"Damage to shields: {damage}!  Shields remaining: {self.shields}.")
        if self.shields == 0:
            print(f"Shields are down!")

    def damage_system(self, system):
        if self.systems[system] == "Damaged":
            print(f"{system} is already damaged.")
        else:
            self.systems[system] = "Damaged"
            print(f"{system} has been damaged!")

    def get_system_by_index(self, index):
        system_keys = list(self.systems.keys())
        return system_keys[index]

    def hit_system(self):
        system_hit = random.randint(0,len(self.systems) -1 )
        self.damage_system(self.get_system_by_index(system_hit))
        print(f"{self.get_system_by_index(system_hit)} has been hit!")




    



