import random

import treasure_ascii as ta
import road_encounters as rs 

def introScene():
  print("Welcome to Treasure Island.")
  print("Your mission is to find the treasure.")
  print(ta.ascii_art.art_list('maps','map1'))

  while True:
    adventure = rs.Road_side()
    adventure.encounter_list()
    input()







""" 
if __name__ == "__main__":
  while True:
    print("Welcome to the Adventure Game!")
    print("As an avid traveler, you have decided to ?????.")
    print("However, during your exploration, you find yourself lost.")
    print("You can choose to walk in multiple directions to find a way out.")
    print("Let's startwith your name: ")
    name = input()
    print("Good luck, " +name+ ".")
    """
introScene()
    