#SHITTY SPACE GAME
#This game is a shitty version of Star Trek.

from obj_ship_player import Player
from obj_quadrant_map import QuadrantMap
from obj_galaxy_map import GalaxyMap

def main():
    pass

def test_obj_player():
    print(f"\nSHIP CREATION TEST\n")
    player = Player("Deep Penetrator", "Foreskin", 3000, 0, 10)

def test_obj_galaxy_map():
    print(f"\nGALAXY CREATION TEST\n")
    galaxy_map = GalaxyMap()
    galaxy_map.print_galaxy_map()

def test_damage():
    player = Player("Deep Penetrator", "Foreskin", 3000, 0, 10)
    player.damage_system("Engines")
    player.damage_system("Engines")
    player.damage_system("Life Support")
    player.damage_system("Life Support")
    player.damage_system("Life Support")
    player.damage_system("Life Support")
    player.damage_system("Life Support")
    player.damage_report()
    



def show_title():
    print("*********************************************************************************************************")
    print("*                                                                                                       *")
    print("*                                            SHITTY                                                     *")
    print("*                                          SPACE GAME                                                   *")
    print("*                                                                                                       *")
    print("*                                                                                                       *")
    print("*********************************************************************************************************")


show_title()

player = Player("Deep Penetrator", "Foreskin", 3000, 0, 10)

galaxy_map = GalaxyMap()

galaxy_map.place_player_in_starting_quadrant(player)

player_quadrant = galaxy_map.get_player_quadrant(player)

player_quadrant.print_quadrant_map()

galaxy_map.print_galaxy_map()