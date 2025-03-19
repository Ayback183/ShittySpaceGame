#obj_quadrant_map.py
#This is the object file for the quadrant maps.

import random
import sys

class QuadrantMap:
    def __init__(self, name):
        self.name = name
        self.starbase = []
        self.enemies = []
        self.asteroids = []
        self.sectors = []
        self.player = []
        self.create_sectors()

    def create_sectors(self):
        self.sectors = [[0 for _ in range(8)] for _ in range(8)]

    def get_object_coords(self):
        while True:
            coords = [random.randint(0, 7), random.randint(0, 7)]
            if (coords in self.starbase or coords in self.enemies or coords in self.asteroids or coords == self.player):
                #print(f"Invalid Object Placement, Rerolling...")
                continue
            return coords
        
    def place_starbase(self):
        if self.starbase == []:
            #print (f"No starbase in Quadrant {self.name}")
            return
        elif len(self.starbase) != 2:
            print(f"Starbase Placement Error in Quadrant {self.name}")
            sys.exit("Starbase placement error - Exiting Game because if a Starbase goes missing that's really scary.")
        else:
            self.sectors[self.starbase[0]][self.starbase[1]] = "Starbase"

    def place_enemies(self):
        if self.enemies == []:
            #print(f"No enemies in Quadrant {self.name}")
            return
        for enemy in self.enemies:
            if len(enemy) != 2:
                print(f"Enemy Placement Error in Quadrant {self.name}  Maybe he crashed or something?")
                continue
            else:
                self.sectors[enemy[0]][enemy[1]] = "Enemy"
    
    def place_asteroids(self):
        if self.asteroids == []:
            #print(f"No asteroids in Quadrant {self.name}")
            return
        for asteroid in self.asteroids:
            if len(asteroid) != 2:
                print(f"Asteroid Placement Error in Quadrant {self.name}  But seriously who cares if an asteroid is missing?")
                continue
            else:
                self.sectors[asteroid[0]][asteroid[1]] = "Asteroid"
            
    def place_player(self):
        if self.player == []:
            #print(f"The player is not in this sector")
            return
        elif len(self.player) != 2:
            print(f"Player Placement Error in Quadrant {self.name}")
            sys.exit("Player Ship placement error - Exiting Game - The Universe is Doomed!")
        else:
            self.sectors[self.player[0]][self.player[1]] = "Player"

    def print_quadrant_map(self):
        print(f"\nQuadrant Map On-Screen")
        print_quadrant = ""
        for row in self.sectors:
            print_row = ""
            for col in row:
                if col == 0:
                    print_row += " . "
                elif col == "Player":
                    print_row += " % "
                elif col == "Starbase":
                    print_row += " @ "
                elif col == "Asteroid":
                    print_row += " * "
                elif col == "Enemy":
                    print_row += " E "
            print_quadrant += f"\n{print_row}"
        print(f"\nSector Map\nQuadrant {self.name}\n{print_quadrant}")





