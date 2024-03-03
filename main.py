import random

#fighter class
class street_fighter:
  def __init__(self, name, level):
    self.name = name
    self.level = level
    self.health = level * 5
    self.is_alive = True
    self.brass_knuckles = False
    self.healing_potion = False
    self.charcoal = False

#function represents the figther
  def __repr__(self):
    return "The figher {} is level {} and has {}HP!".format(self.name, self.level, self.health)
    print("")

#function allows fighters to take damage
  def take_damage(self, amount):
    self.health -= amount
    
    #if health goes in negatives it reverts back to 0
    if self.health <= 0:
      self.health = 0
    
    #if health is 0, fighter is dead
    if self.health == 0:
      self.is_alive = False

#different street fighters player can get
f1 = street_fighter("Mike Tyson", random.randint(10, 12))
f2 = street_fighter("Anderson Silva", random.randint(10, 12))
f3 = street_fighter("Jon Jones", random.randint(10, 12))
f4 = street_fighter("Oleksandr Usyk", random.randint(10, 12))
f5 = street_fighter("Demetrious Johnson", random.randint(10, 12))
f6 = street_fighter("Tom Aspinall", random.randint(10, 12))

#players class
class player():
  def __init__(self, name):
    self.name = name
    self.fighter = ()

#allows player to pick their fighter
  def pick_fighter(self, fname):
    self.fighter = fname

#represents players name and fither
  def __repr__(self):
    return "{player} is in control of {fighter}!".format(player = self.name, fighter = self.fighter.name)

#function to show that the fighter is defeated
  def defeated(self, victor):
    self.fighter.is_alive = False
    
    if self.fighter.health != 0:
      self.fighter.health = 0
    
    #defeat and victory message at end
    print("{player} has been defeated!".format(player = self.name))
    print("")
    print("{name} is victorious!".format(name = victor.name))

#function equips brass knuckles
  def equip_brass_knuckles(self):
    self.fighter.brass_knuckles = True
    print("{fighter} was given brass knuckles!".format(fighter = self.fighter.name))
    print("")

#function equips healing potion
  def equip_healing_potion(self):
    self.fighter.healing_potion = True
    print("{fighter} was given a healing potion!".format(fighter = self.fighter.name))
    print("")

#function equips charcoal
  def equip_charcoal(self):
    self.fighter.charcoal = True
    print("{fighter} was given charcoal...".format(fighter = self.fighter.name))
    print("")

#function allows to use healing potion
  def use_healing_potion(self):
    chance = random.randint(1, 2)
    
    #checks if players fighter is alive
    if self.fighter.is_alive == False:
      print("{fighter} can't heal he is defeated!".format(fighter = self.fighter.name))
      print("")
    
    #checks if players fighter has a healing potion, if so the fighter regains 25% of his maximum health
    elif self.fighter.healing_potion:
      self.fighter.health += (self.fighter.level * 5 / 4)
      
      if self.fighter.health > (self.fighter.level * 5):
        self.fighter.health = self.fighter.level * 5
      
      #50% chance potion spills
      if chance == 1:
        self.fighter.healing_potion = False
        print("{fighter} has used a healing potion, {fighter} now has {health}HP... but he spilled the rest!".format(fighter = self.fighter.name, health = round(self.fighter.health, 2)))
        print("")
      
      #50% chance potion does'nt spill
      else:
        print("{fighter} has used a healing potion, {fighter} now has {health}HP!".format(fighter = self.fighter.name, health = round(self.fighter.health, 2)))
        print("")
    
    #if player does'nt have any healing potions
    else:
      print("{fighter} does not have any healing potions in his inventory!".format(fighter = self.fighter.name))
      print("")

#function to show items in inventory
  def check_inventory(self):
    if self.fighter.brass_knuckles:
      print("{fighter} is carrying brass knuckles!".format(fighter = self.fighter.name))

    if self.fighter.healing_potion:
      print("{fighter} is carrying a healing potion!".format(fighter = self.fighter.name))

    if self.fighter.charcoal:
      print("{fighter} is carrying charcoal...".format(fighter = self.fighter.name))

    if self.fighter.brass_knuckles == False and self.fighter.healing_potion == False and self.fighter.charcoal == False:
      print("{fighter} has an empty inventory...".format(fighter = self.fighter.name))

#function performs punch
  def punch_attack(self, other_player):
    #punch variables
    chanceBP = random.randint(1, 4)
    Pdmg = 4
    damage_dealt = round(self.fighter.level * Pdmg * 0.15, 2)
   
    #program checks if both fighters are alive, if they are it proceeds 
    if self.fighter.is_alive == False:
      print("{fighter} can't attack, he is defeated!".format(self.fighter.name))
      print("")
    elif other_player.fighter.is_alive == False:
      print("{opp} is already defeated!".format(opp = other_player.fighter.name))
      print("")
    
    else:
      #checks if player has brass knuckles, if he does his damage increases 25%
      if self.fighter.brass_knuckles:
        damage_dealt = round(damage_dealt * 1.25, 2)

      #player gives other players fighter damage
      other_player.fighter.take_damage(damage_dealt)
      print("{you} has attacked {opp} with a punch!, {opp} was dealt {damage} damage!".format(you = self.fighter.name, opp = other_player.fighter.name, damage = damage_dealt))
      print("")
      
      if self.fighter.brass_knuckles:
        #25% chance of brass knuckles breaking
        if chanceBP == 2:
          self.fighter.brass_knuckles = False
          print("WOW! {fighter} used brass knuckles, his attack did 25% more damage!... but they broke :(".format(fighter = self.fighter.name))
          print("")
        #75% of brass knuckles not breaking
        else:
          print("WOW! {fighter} used brass knuckles, his attack did 25% more damage!".format(fighter = self.fighter.name))
          print("")
      
      #displays opponents health
      print("{opp} now has {opp_health}HP!".format(opp = other_player.fighter.name, opp_health = round(other_player.fighter.health, 2)))
      print("")

#function performs hook
  def hook_attack(self, other_player):
    #hook variables
    chanceBH = random.randint(1, 4)
    chanceH = random.randint(1, 10)
    Hdmg = random.randint(5, 7)
    damage_dealt = round(self.fighter.level * Hdmg * 0.15, 2)
    
    #program checks if both fighters are alive, if they are it proceeds   
    if self.fighter.is_alive == False:
      print("{fighter} can't attack, he is defeated!".format(self.fighter.name)) 
      print("")
    elif other_player.fighter.is_alive == False:
      print("{opp} is already defeated!".format(opp = other_player.fighter.name))
      print("")
    
    else:
      #40% chance of hook missing
      if chanceH <= 4:
        print("{fighter} has attempted to throw a hook... but missed!".format(fighter = self.fighter.name))
        print("")
      
      #60% chance of hook landing
      else:
        #checks if player has brass knuckles, if he does his damage increases 25%
        if self.fighter.brass_knuckles:
          damage_dealt = round(damage_dealt * 1.25, 2)
        
        #player gives other players fighter damage
        other_player.fighter.take_damage(damage_dealt)  
        print("{fighter} has attacked {opp} with a hook!, {opp} was dealt {damage} damage!".format(fighter = self.fighter.name, opp = other_player.fighter.name, damage = damage_dealt))
        print("")

        if self.fighter.brass_knuckles:
          #25% chance of brass knuckles breaking
          if chanceBH == 2:
            self.fighter.brass_knuckles = False
            print("WOW! {fighter} used brass knuckles, his attack did 25% more damage!... but they broke :(".format(fighter = self.fighter.name))
            print("")

          #75% chance of brass knuckles not breaking
          else:
            print("WOW! {fighter} used brass knuckles, his attack did 25% more damage!".format(fighter = self.fighter.name))
            print("")

        #displays opponents health
        print("{opp} now has {opp_health}HP!".format(opp = other_player.fighter.name, opp_health = round(other_player.fighter.health, 2)))
        print("")

#function performs uppercut
  def uppercut_attack(self, other_player):
    
    #variables for uppercut
    chanceBU = random.randint(1, 4)
    chanceU = random.randint(1, 10)
    Udmg = random.randint(5, 7)
    damage_dealt = round(self.fighter.level * Udmg * 0.15, 2)

    #program checks if both fighters are alive, if they are it proceeds
    if self.fighter.is_alive == False:
      print("{fighter} can't attack, he is defeated!".format(self.fighter.name)) 
      print("")
    elif other_player.fighter.is_alive == False:
      print("{opp} is already defeated!".format(opp = other_player.fighter.name))
      print("")
    
    else:
      #40% chance of uppercut missing
      if chanceU <= 4:
        print("{fighter} has attempted to throw a uppercut... but missed!".format(fighter = self.fighter.name))
        print("")
      
      #60% chance of uppercut landing
      else:
        #checks if player has brass knuckles, if he does his damage increases 25%
        if self.fighter.brass_knuckles:
          damage_dealt = round(damage_dealt * 1.25, 2)
        
        #player gives other players fighter damage
        other_player.fighter.take_damage(damage_dealt)  
        print("{fighter} has attacked {opp} with a uppercut!, {opp} was dealt {damage} damage!".format(fighter = self.fighter.name, opp = other_player.fighter.name, damage = damage_dealt))
        print("")
        
        if self.fighter.brass_knuckles:
          #25% chance of brass knuckles breaking
          if chanceBU == 2:
            self.fighter.brass_knuckles = False
            print("WOW! {fighter} used brass knuckles, his attack did 25% more damage!... but they broke :(".format(fighter = self.fighter.name))
            print("")
        
        #75% chance of brass knuckles not breaking
          else:
            print("WOW! {fighter} used brass knuckles, his attack did 25% more damage!".format(fighter = self.fighter.name))
            print("")
        
        #displays opponents health
        print("{opp} now has {opp_health}HP!".format(opp = other_player.fighter.name, opp_health = round(other_player.fighter.health, 2)))
        print("")

#function performs high kick
  def high_kick_attack(self, other_player):
    
    #variables for high kick
    chanceHK = random.randint(1, 10)
    dmgHK = random.randint(8, 10)
    damage_dealt = round(self.fighter.level * dmgHK * 0.15, 2)

    #program checks if both fighters are alive, if they are it proceeds
    if self.fighter.is_alive == False:
      print("{fighter} can't attack, he is defeated!".format(fighter = self.fighter.name))
      print("")
    elif other_player.fighter.is_alive == False:
      print("{opp} is already defeated!".format(opp = other_player.fighter.name))
      print("")

    else:
      #40% chance of a high kick missing
      if chanceHK <= 4:
        print("{fighter} has thrown a high kick... but missed!".format(fighter = self.fighter.name))
        print("")
        
        #20% chance of a high kick missing and player slipping and taking 4 damage
        if chanceHK <= 2:
          self.fighter.take_damage(4)
          print("{fighter} has also slipped and taken {damage} damage upon impact".format(fighter = self.fighter.name, damage = 4))
          print("")
          print("{fighter} now has {fighter_health}HP!".format(fighter = self.fighter.name, fighter_health = round(self.fighter.health, 2)))
     
      #60% chance high kick lands
      else:

        #player gives other player damage
        other_player.fighter.take_damage(damage_dealt)
        print("{fighter} has attacked {opp} with a high kick!, {opp} was dealt {damage} damage!".format(fighter = self.fighter.name, opp = other_player.fighter.name, damage = damage_dealt))

        #displays opponents health
        print("")
        print("{opp} now has {opp_health}HP!".format(opp = other_player.fighter.name, opp_health = round(other_player.fighter.health, 2)))
        print("")

#players choose their names
print("")
print("Welcome to Fight Club. The first rule of Fight Club is you do not talk about Fight Club!")
print("")
p1_name = input("Player 1 enter your name: ")
print("")
p2_name = input("Player 2 enter your name: ")

#spacing
print("")
print("---------------------------------------------------------------------------------------------------")
print("")

#made the object variables for player1 and player2
p1 = player(p1_name)
p2 = player(p2_name)

#player1 choose their fighter
print("{player1} select one of the following fighters: {f_1}, {f_2}, {f_3}, {f_4}, {f_5}, {f_6}".format(player1 = p1_name, f_1 = f1.name, f_2 = f2.name, f_3 = f3.name, f_4 = f4.name, f_5 = f5.name, f_6 = f6.name))
print("")
p1_fighter = input("Input here: ")

#error message if player1 did'nt pick one of the fighters listed
while p1_fighter != f1.name and p1_fighter != f2.name and p1_fighter != f3.name and p1_fighter != f4.name and p1_fighter != f5.name and p1_fighter != f6.name:
  print("")
  print("You have not entered in the name of a selectable fighter, please try again!")
  print("")
  p1_fighter = input("Input here: ")

#assigns fighter chosen to player1
if p1_fighter == "Mike Tyson":
  p1.pick_fighter(f1)
elif p1_fighter == "Anderson Silva":
  p1.pick_fighter(f2)
elif p1_fighter == "Jon Jones":
  p1.pick_fighter(f3)
elif p1_fighter == "Oleksandr Usyk":
  p1.pick_fighter(f4)
elif p1_fighter == "Demetrious Johnson":
  p1.pick_fighter(f5)
elif p1_fighter == "Tom Aspinall":
  p1.pick_fighter(f6)

#spacing
print("")
print("---------------------------------------------------------------------------------------------------")
print("")

#player2 chooses their fighter
print("{player2} select one of the following fighters: {f_1}, {f_2}, {f_3}, {f_4}, {f_5}, {f_6}".format(player2 = p2_name, f_1 = f1.name, f_2 = f2.name, f_3 = f3.name, f_4 = f4.name, f_5 = f5.name, f_6 = f6.name))
print("")
p2_fighter = input("Input here: ")

#error message if player2 did'nt pick of the fighters listed
while p2_fighter != f1.name and p2_fighter != f2.name and p2_fighter != f3.name and p2_fighter != f4.name and p2_fighter != f5.name and p2_fighter != f6.name:
  print("")
  print("You have not entered in the name of a selectable fighter, please try again!")
  print("")
  p2_fighter = input("Input here: ")
  #error message if player2 picked the same fighter as player1
  while p1_fighter == p2_fighter:
    print("")
    print("You have selected the same fighter as {player1}, please select another fighter!".format(player1 = p1_name))
    print("")
    p2_fighter = input("Input here: ")


#error message if player2 picked the same fighter as player1
while p1_fighter == p2_fighter:
  print("")
  print("You have selected the same fighter as {player1}, please select another fighter!".format(player1 = p1_name))
  print("")
  p2_fighter = input("Input here: ")
  #error message if player2 did'nt pick of the fighters listed
  while p2_fighter != f1.name and p2_fighter != f2.name and p2_fighter != f3.name and p2_fighter != f4.name and p2_fighter != f5.name and p2_fighter != f6.name:
    print("")
    print("You have not entered in the name of a selectable fighter, please try again!")
    print("")
    p2_fighter = input("Input here: ")
    
#spacing
print("")
print("---------------------------------------------------------------------------------------------------")
print("")

#assigns fighter chosen to player2
if p2_fighter == "Mike Tyson":
  p2.pick_fighter(f1)
elif p2_fighter == "Anderson Silva":
  p2.pick_fighter(f2)
elif p2_fighter == "Jon Jones":
  p2.pick_fighter(f3)
elif p2_fighter == "Oleksandr Usyk":
  p2.pick_fighter(f4)
elif p2_fighter == "Demetrious Johnson":
  p2.pick_fighter(f5)
elif p2_fighter == "Tom Aspinall":
  p2.pick_fighter(f6)

#show what fighter is under control by each player
print(p1)
print("")
print(p2)

#spacing
print("")
print("---------------------------------------------------------------------------------------------------")
print("")

#Program that randomly distributes the 3 equipable items to players fighters
item_chance = random.randint(1, 3)
if item_chance == 1:
  p1.equip_brass_knuckles()
  p2.equip_healing_potion()
elif item_chance == 2:
  p1.equip_healing_potion()
  p2.equip_brass_knuckles()
elif item_chance == 3:
  p1.equip_charcoal()
  p2.equip_brass_knuckles()
elif item_chance == 4:
  p1.equip_charcoal()
  p2.equip_healing_potion()
elif item_chance == 5:
  p1.equip_brass_knuckles()
  p2.equip_charcoal()
elif item_chance == 6:
  p1.equip_healing_potion()
  p2.equip_charcoal()

#spacing
print("---------------------------------------------------------------------------------------------------")
print("")

#host starts the fight
print("Type \"begin\" to start the fight!")
print("")
ready_message = input("Input here: ")

#error message if host fails to type "begin"
while ready_message != "begin":
  print("")
  ready_message = input("""You have not typed \"begin\", type \"begin\" to start the fight!
Input here: """)

#fight begin message with spacing
print("")
print("---------------------------------------------------------------------------------------------------")
print("""
._. ___________ .__           .__       __             
| | \_   _____/ |__|   ____   |  |__  _/  |_           
| |  |    __)   |  |  / ___\  |  |  \ \   __\          
 \|  |     \    |  | / /_/  > |   Y  \ |  |            
 __  \___  /    |__| \___  /  |___|  / |__|            
 \/      \/        /_____/        \/                 
__________                  __                 ._.
\______   \  ____    ____  |__|  ____    ______| |
 |    |  _/_/ __ \  / ___\ |  | /    \  /  ___/| |
 |    |  \ \  ___/ / /_/ | |  ||   |  \ \___ \  \|
 |______  / \__>   \___  / |__||___|  //____  > __
                  /_____/           \/      \/  \/""")
print("")
print("---------------------------------------------------------------------------------------------------")
print("")

#while loop that continiously offers players attacks turn by turn, until one of the players if defeated
while p1.fighter.is_alive == True and p2.fighter.is_alive == True:

  #attack offers if player1 has a healing potion
  if p1.fighter.healing_potion:
    print("{player1} Your turn pick your attack! : Punch, Hook, Uppercut, High Kick or Heal :".format(player1 = p1.name))
    print("")
    player1_choice = input("Input here: ")
    
    #error message if player1 does'nt type in an available attack
    while player1_choice != "Punch" and player1_choice != "Hook" and player1_choice != "Uppercut" and player1_choice != "High Kick" and player1_choice != "Heal":
      print("")
      print("{player1} you have not picked a selectable attack!".format(player1 = p1.name))
      print("")
      print("{player1} Your turn pick your attack! : Punch, Hook, Uppercut, High Kick or Heal :".format(player1 = p1.name))
      print("")
      player1_choice = input("Input here: ")
  
  #standard attack offers if player1 doesnt possess a healing potion
  else:
    print("{player1} Your turn pick your attack! : Punch, Hook, Uppercut, High Kick :".format(player1 = p1.name))
    print("")
    player1_choice = input("Input here: ")
    
    #error message if player1 does'nt type in an available attack
    while player1_choice != "Punch" and player1_choice != "Hook" and player1_choice != "Uppercut" and player1_choice != "High Kick":
      print("")
      print("{player1} you have not picked a selectable attack!".format(player1 = p1.name))
      print("")
      print("{player1} Your turn pick your attack! : Punch, Hook, Uppercut, High Kick :".format(player1 = p1.name))
      print("")
      player1_choice = input("Input here: ")

#program triggers the attack selected by player1
  if player1_choice == "Punch":
    print("")
    p1.punch_attack(p2)
  elif player1_choice == "Hook":
    print("")
    p1.hook_attack(p2)
  elif player1_choice == "Uppercut":
    print("")
    p1.uppercut_attack(p2)
  elif player1_choice == "High Kick":
    print("")
    p1.high_kick_attack(p2)
  elif player1_choice == "Heal":
    print("")
    p1.use_healing_potion()

#checks if player2 is alive, if he is while loop keeps going, if he isn't it breaks
  if p2.fighter.is_alive:
    print("---------------------------------------------------------------------------------------------------")
    print("")
  else:
    print("---------------------------------------------------------------------------------------------------")
    print("")
    p2.defeated(p1)
    break
  
  #attack offers if player2 has a healing potion
  if p2.fighter.healing_potion:
    print("{player2} Your turn pick your attack! : Punch, Hook, Uppercut, High Kick or Heal :".format(player2 = p2.name))
    print("")
    player2_choice = input("Input here: ")
    
    #error message if player1 does'nt type in an available attack
    while player2_choice != "Punch" and player2_choice != "Hook" and player2_choice != "Uppercut" and player2_choice != "High Kick" and player2_choice != "Heal":
      print("")
      print("{player2} you have not picked a selectable attack!".format(player2 = p2.name))
      print("")
      print("{player2} Your turn pick your attack! : Punch, Hook, Uppercut, High Kick or Heal :".format(player2 = p2.name))
      print("")
      player2_choice = input("Input here: ")
  
  #standard attack offers if player2 doesnt possess a healing potion
  else:
    print("{player2} Your turn pick your attack! : Punch, Hook, Uppercut, High Kick :".format(player2 = p2.name))
    print("")
    player2_choice = input("Input here: ")
    
    #error message if player1 does'nt type in an available attack
    while player2_choice != "Punch" and player2_choice != "Hook" and player2_choice != "Uppercut" and player2_choice != "High Kick":
      print("")
      print("{player2} you have not picked a selectable attack!".format(player2 = p2.name))
      print("")
      print("{player2} Your turn pick your attack! : Punch, Hook, Uppercut, High Kick :".format(player2 = p2.name))
      print("")
      player2_choice = input("Input here: ")

#program triggers the attack selected by player1
  if player2_choice == "Punch":
    print("")
    p2.punch_attack(p1)
  elif player2_choice == "Hook":
    print("")
    p2.hook_attack(p1)
  elif player2_choice == "Uppercut":
    print("")
    p2.uppercut_attack(p1)
  elif player2_choice == "High Kick":
    print("")
    p2.high_kick_attack(p1)
  elif player2_choice == "Heal":
    print("")
    p2.use_healing_potion()

#checks if player1 is alive, if he is while loop keeps going, if he isn't it breaks(while loop should close automatically this is just in case)
  if p1.fighter.is_alive:
    print("---------------------------------------------------------------------------------------------------")
    print("")
  else:
    print("---------------------------------------------------------------------------------------------------")
    print("")
    p1.defeated(p2)
    break

#end good game message
print("""
 ░▒▓██████▓▒░  ░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░       ░▒▓█▓▒░        
░▒▓█▓▒▒▓███▓▒░░▒▓█▓▒▒▓███▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓██████▓▒░  ░▒▓██████▓▒░  
""")