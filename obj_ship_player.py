#obj_ship_player.py
#This file defines the player's ship.

#position = [[QuadrantX,QuadrantY],[SectorX,SectorY]]

import random
from lst_flavor_text import flavor_text_damage

class Player:
    def __init__(self, ship_name, captain_name, energy_max, shields, torpedoes_max):
        self.energy_max = energy_max
        self.energy = energy_max
        self.shields = shields
        self.torpedoes_max = torpedoes_max
        self.torpedoes = torpedoes_max
        self.position = []
        self.systems = {}
        self.set_all_systems_to_ok()
        self.ship_name = ship_name
        self.captain_name = captain_name
        print(f"Ship Created")
        self.print_status()
        self.damage_report()

    def print_status(self):
        print(f"USS {self.ship_name}, Captain {self.captain_name} commanding.")
        print(f"Energy: {self.energy}/{self.energy_max}  Torpedoes: {self.torpedoes}/{self.torpedoes_max}")
        print(f"Shields: {self.shields}")

    def damage_report(self):
        print(f"\nDamage Report:\n")
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

    def remove_energy_from_shields(self, remove_energy):
        if self.shields < remove_energy:
            print("Not enough energy in shields.")
        else:
            self.energy += remove_energy
            self.shield -= remove_energy
            print(f"{remove_energy} transferred from the shields.")

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
            if flavor_text_damage == []:
                damage_text = "Lights flickering, explosion noises, etc..."
            else:
                damage_text = flavor_text_damage.pop(random.randint(0,len(flavor_text_damage) - 1))
            print(f"{damage_text}")
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




    



