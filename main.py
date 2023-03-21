#------------------------------------------------------------------------------
#    File name: Simple Map
#    Author: Han Wang
#    Date created: 3/13/2023
#    Date last modified: 3/16/2023
#------------------------------------------------------------------------------
'''   Description: Simple game Map '''
#------------------------------------------------------------------------------
#Create a variable "row" with a value of 0
row = 0  
col = 0
max_row = 3
max_col = 3

#Create a list called inventory
inventory = []

playing = True

# tile information
#Create a list called tile
#The first assignment is "start", which means that tile[0] is "start", and so on
tile = ["Start", "PlainSpace", "ThrownRoom", "SpookySpace"]
tiles = {
  tile[0]: {
    "Description": "Your in the Ammunition"
  },
  tile[1]: {
    "Description": "Your are in a empty room."
  },
  tile[2]: {
    "Description": "You are at the office"
  },
  tile[3]: {
    "Description": "This room is very weird!"
  },
}

map = [[tile[0], tile[1], tile[2], tile[3]],
       [tile[1], tile[3], tile[1], tile[1]],
       [tile[2], tile[1], tile[3], tile[2]],
       [tile[3], tile[2], tile[1], tile[3]]]

# Functions ------------------------------------------------------------------
def walkto():
  global playing, row, col, max_row, max_col
  orientating = playing
  while orientating:
   print("Choose a direction: ")
   canUp = False
   canDown = False
   canRight = False
   canLeft = False

   if row > 0:
     canUp = True
     print("you can go up - type:'up'")

   if row < max_row:
     canDown = True
     print("you can go down - type:'down'")

   if col < max_col:
     canRight = True
     print("you can go right - type:'right'")

   if col > 0:
     canLeft = True
     print("you can go left - type:'left'")
   orientating = False

#Create a variable called "waychoice" and assign it to user input (input(f"Choice: ")), then change the user input to lowercase (.lower())
   waychoice = input("Choice: ").lower()
   if waychoice == "up" and canUp:
        row = row - 1 
     
   elif waychoice == "down" and canDown:
        row = row + 1

   elif waychoice == "right" and canRight:
        col = col + 1
     
   elif waychoice == "left" and canLeft:
        col = col - 1
   elif waychoice == "quit":
        playing = False

   else:
        print("Sorry you can not move to there.")
        waychoice = True 
    

def MainMenu():
  global playing
  orientating = playing
  while orientating:
    print("Choose to move to another room or look around:")
    Choose = ["walk", "look"]
    for do in Choose:
      print((f"- {do.title()}"))
    userInput = input("You choice: ").lower()
    orientating = False
    if userInput == Choose[0]:
      print("You walk to another room.")
      walkto()
    
    elif userInput == Choose[1]:
      print("You look around.")
    
    elif userInput == "quit":
      playing = False
    else:
      print("Invalid input!")
      orientating = True

# Main -----------------------------------------------------------------------
print("Welcome to my bunker!")
print("Goal is to find a key to escape.")
print("You in the foyer of the bunker.")

while playing:
  location_description =  map[row][col]
  for tile in tiles:
    if tile == location_description:
      print(tiles[tile]["Description"])
  MainMenu()
