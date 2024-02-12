import random

import treasure_ascii as ta

class Tresure_Island():
   
  ...

class Outside():
   

  ...

class Inside():
   
   ...
   
def main():


  road_types = [{'description':'you are at a crossroad', 'actions':['Go right', 'Go left']},
                {'description':'you are at a intersection', 'actions':['Go right', 'Go left','Go stright']},
                {'description':'you are at a T', 'actions':['Go stright', 'Go left']},
                {'description':'you are at a Y', 'actions':['Go stright', 'Go right']}
                ]
  land_types = [{'description':'you are at a lake', 'actions':['wait for boat', 'swim']},
                {'description':'you are at a river', 'actions':['wait for boat', 'swim']},
                {'description':'you are at a T', 'actions':['Go over', 'Go around']},
                {'description':'you are at a forest', 'actions':['Go through', 'Turn around']}
                ]
  house_types = [{'description':'you are at a house', 'actions':['Go in', 'Go around']},
                {'description':'you are at a cabin', 'actions':['Go in', 'Go around']},
                {'description':'you are at a cave', 'actions':['Go in', 'Go around']},
                {'description':'you are at a hole', 'actions':['Go down', 'Go around']}
                ]
    
  list_stuff = [house_types,land_types,road_types,'treasure found']

  #.print("Welcome to Treasure Island.")
  #print("Your mission is to find the treasure.")
  #print(ta.ascii_art.art_list('maps','map1'))
    
  while True:
      selection = random.choice(list_stuff)
      selected_item = random.choice(selection)

      if selection == 'treasure found':
          print("Description: You found the treasure chest")
          print(ta.ascii_art.treasure_chest('chest','chest2'))
          break
      else:
          print(f"Description: {selected_item['description']}")
          

          print(f"Available actions: {', '.join(selected_item['actions'])}")

          input()

def inside():
  rooms = [{"description": "You are in a dark room.",
          "actions": ["Go east", "Go west"]},
          {"description": "You are in a brightly lit room.",
          "actions": ["Go west", "Go north"]},
          { "description": "You are in a narrow hallway.",
          "actions": ["Go south", "Go east"]}
          ]










main()
