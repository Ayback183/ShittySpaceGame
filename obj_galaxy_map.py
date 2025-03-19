#funct_galaxy_map.py
#This is the functions that creates the 64 quadrants on the quadrant map.

from obj_quadrant_map import QuadrantMap
from obj_ship_player import Player
from lst_quadrant_names import quadrant_names
import random

class GalaxyMap:
    def __init__(self):
        self.quadrants = []
        self.create_galaxy()
        self.place_starbases()
        self.total_enemies = random.randint(10,20)
        self.place_enemies_in_quadrants()
        self.place_asteroids_in_quadrants()
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
    
    def place_enemies_in_quadrants(self):
        for _ in range(self.total_enemies):
            valid_quadrant_placement = False
            while valid_quadrant_placement == False:
                quadrant = [random.randint(0,7), random.randint(0,7)]
                quadrant_obj = self.quadrants[quadrant[0]][quadrant[1]]
                if len(quadrant_obj.enemies) < 3:
                    quadrant_obj.enemies.append(quadrant_obj.get_object_coords())
                    valid_quadrant_placement = True
    
    def place_asteroids_in_quadrants(self):
        for row in self.quadrants:
            for quadrant in row:
                total_asteroids = max(0,random.randint(0,20) - 5)
                for _ in range(total_asteroids):
                    quadrant.asteroids.append(quadrant.get_object_coords())

    def place_player_in_starting_quadrant(self, player):
        player_quadrant = [random.randint(0, 7), random.randint(0, 7)]
        quadrant_obj = self.quadrants[player_quadrant[0]][player_quadrant[1]]
        player_sector = quadrant_obj.get_object_coords()
        player.position = [player_quadrant, player_sector]
        quadrant_obj.player = player_sector  # Assign player's sector position
        quadrant_obj.place_player()          # Update sectors array
        print(f"\nUSS {player.ship_name} begins mission in Quadrant {quadrant_obj.name} at {player.position[1][0]},{player.position[1][1]}")
    

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

    def get_player_quadrant(self, player):
        quadrant_coords = player.position[0]  # This is [row, col]
        row, col = quadrant_coords[0], quadrant_coords[1]
        player_quadrant = self.quadrants[row][col]
        return player_quadrant


    def print_galaxy_map(self):
        # Testing Function, Do Not Use In Game!
        print(f"\nGalaxy Map On-Screen\n")
        for row in self.quadrants:
            map_line = []
            for quadrant in row:
                map_player = "%" if len(quadrant.player) > 0 else " "
                map_enemies = f"{len(quadrant.enemies)}" if len(quadrant.enemies) > 0 else " "
                map_starbase = "@" if len(quadrant.starbase) > 0 else " "
                map_quadrant = f"[{map_player} {map_enemies} {map_starbase}]"
                map_line.append(map_quadrant)
            print(" ".join(map_line))


    def print_all_quadrants(self):
        #Testing Function, Do Not Use In Game!
        for row in self.quadrants:
            for quadrant in row:
                quadrant.print_quadrant_map()

    
    

