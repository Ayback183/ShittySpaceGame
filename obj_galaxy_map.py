#funct_galaxy_map.py
#This is the functions that creates the 64 quadrants on the quadrant map.

from obj_quadrant_map import QuadrantMap
from lst_quadrant_names import quadrant_names
import random

class GalaxyMap:
    def __init__(self):
        self.quadrants = []
        self.create_galaxy()
        self.place_starbases()
        self.total_enemies = random.randint(10,20)
        self.get_enemy_quadrants()
        self.place_all_enemies()
        self.place_all_asteroids()        

    def create_galaxy(self):
        self.quadrants = []
        for row in range(8):
            quadrants_line = []
            for col in range(8):
                new_quadrant = QuadrantMap(quadrant_names.pop(random.randint(0,len(quadrant_names) - 1)))
                quadrants_line.append(new_quadrant)
            self.quadrants.append(quadrants_line)
        print(f"\nGalaxy Map Created")

    def get_starbase_quadrants(self):
        starbase_1_quadrant = [random.randint(0,3), random.randint(0,3)]
        starbase_2_quadrant = [random.randint(4,7), random.randint(0,3)]
        starbase_3_quadrant = [random.randint(0,3), random.randint(4,7)]
        starbase_4_quadrant = [random.randint(4,7), random.randint(4,7)]
        return [starbase_1_quadrant, starbase_2_quadrant, starbase_3_quadrant, starbase_4_quadrant]

    def place_starbases(self):
        starbase_quadrants = self.get_starbase_quadrants()
        for quadrant_coordinates in starbase_quadrants:
            row, col = quadrant_coordinates
            if 0 <= row < 8 and 0 <= col < 8:
                quadrant = self.quadrants[row][col]
                quadrant.starbase = [row, col]
                quadrant.place_starbase()
            else:
                print(f"(Galaxy Map) Invalid starbase placement at {quadrant_coordinates}")
        print(f"\nStarbase Placement Complete")

    def get_enemy_quadrants(self):
        #print (f"Placing {self.total_enemies} Enemy Ships.")
        placed_enemies = 0
        for enemy in range(self.total_enemies):
            valid_quadrant_placement = False
            while valid_quadrant_placement == False:
                if placed_enemies >= self.total_enemies:
                            break
                quadrant = [random.randint(0,7), random.randint(0,7)]
                quadrant_obj = self.quadrants[quadrant[0]][quadrant[1]]
                if len(quadrant_obj.enemies) < 3 and 0 <= quadrant[0] < 8 and 0 <= quadrant[1] < 8:
                    valid_sector_placement = False
                    while valid_sector_placement == False:
                        sector = [random.randint(0,7), random.randint(0,7)]
                        if sector == quadrant_obj.starbase or sector in quadrant_obj.enemies or not (0 <= sector[0] < 8 and 0 <= sector[1] < 8):
                            print (f"Invalid enemy placement in Quadrant {quadrant_obj.name}")
                        else:
                            quadrant_obj.enemies.append(sector)
                            #print (f"Enemy placed in {quadrant_obj.name}")
                            valid_sector_placement = True
                            placed_enemies += 1

    def place_all_enemies(self):
        print(f"\nDeploying the Enemy Fleet...")
        print(f"Mobilizing {self.total_enemies} enemy ships...")
        for row in self.quadrants:
            for quadrant in row:
                quadrant.place_enemies()

    def place_all_asteroids(self):
        print (f"\nPlacing Asteroids...")
        for row in self.quadrants:
            for quadrant in row:
                quadrant.place_asteroids()

    def print_galaxy_map(self):
        print (f"\nGalaxy Map On-Screen\n")
        map_complete = []
        for row in self.quadrants:
            map_line = []
            for quadrant in row:
                map_enemies = f"{len(quadrant.enemies)}"
                if len(quadrant.enemies) == 0:
                    map_enemies = " "
                if quadrant.starbase is not None:
                    map_starbase = "@"
                else:
                    map_starbase = " "
                map_quadrant = f"[{map_enemies} {map_starbase}]"
                map_line.append(map_quadrant)
            print(" ".join(map_line))
            map_complete.append(map_line)
        
                



    def print_all_quadrants(self):
        #Testing Function, Do Not Use In Game!
        for row in self.quadrants:
            for quadrant in row:
                quadrant.print_quadrant_map()

    
    

