import random

dead = False
class item:
  def __init__(self, name, count, own):
    self.name = name
    self.count = count
    self.own = own

class weapon:
  def __init__(self, name, min, max, own):
    self.name = name
    self.min = min
    self.max = max
    self.own = own

class enemy:
  def __init__(self, name, health, attack_name, attack_damage_min, attack_damage_max):
    self.name = name
    self.health = health
    self.attack = attack_name
    self.min = attack_damage_min
    self.max = attack_damage_max

class player:
  def __init__(self, name, max_health, health, xp):
    self.name = name
    self.max_health = max_health
    self.health = health
    self.xp = xp

wings = item("wings", 0, 0)

#creating weapons
cell_phone = weapon("cell_phone", 0, 0, 0) #given
shiv = weapon("devshiv", 20, 20, 0) #starter weapon
fist = weapon("fist", 2, 5, 1) #starter for all classes
old_sword = weapon("old_sword", 10, 15, 0) #starter weapon
fireball = weapon("fireball", 10, 15, 0) #starter weapon
spark = weapon("spark", 0, 20, 0) #starter weapon
dark_blast = weapon("dark_blast", 5, 18, 0) #starter weapon
bow = weapon("bow", 15, 20, 0) #starter weapon
dagger = weapon("dagger", 15, 20, 0) #starter weapon
dev_sword = weapon("dev_sword", 2048, 4096, 0) #starter weapon
long_sword = weapon("long_sword", 20, 40, 0)
kunai = weapon("kunai", 5, 50, 0) #used
short_sword = weapon("short_sword", 20, 25, 0) #used
boomerang = weapon("boomerang", 30, 50, 0)
sword_o_slartybartfasts_gerbals_second_and_a_half_aunt = weapon("sword_o_slartybartfasts_gerbals_second_and_a_half_aunt = weapon", 150, 200, 0) #easter egg weapon because it is hard to get and hard to type. run into the middle X from the right side.
mace = weapon("mace", 55, 65, 0)
yo_yo = weapon("yo_yo", 50, 70, 0) #used
leatherman = weapon("leatherman", 70, 90, 0) #given
diamond_hoe = weapon("diamond_hoe", 100, 150, 0) #used
mini_shark = weapon("mini_shark", 50, 200, 0) #used
mozambique = weapon("mozambique", 140, 160, 0) #used
scripture_power = weapon("scripture_power", 150, 150, 0) #used


#creating enemies
john = enemy("John the mall cop", 36, "fart blast", 10, 30) #used
jimothy = enemy("Jimothy the Meh", 100, "Arrow to the Knee", 15, 25) #used
zenith = enemy("Zenith the Slow", 600, "Slap in the Face", 70, 110) #used
lenny = enemy("Lenny the Lepar", 5 , "Sickening Sneeze", 40, 60) #used
aqua = enemy("Aquafina the Scorched", 350, "Vine Whip", 60, 100) #used
pari = enemy("Pari the Beaver Duck", 30, "Splash", 2, 4) #used
angry = enemy("Angry step-father", 80, "emotional damage", 50, 150) #used
eric = enemy("Eric the Caslte", 5000, "Smolder", 0, 0) #used
self = enemy("self doubt the cripling", 1000, "fear", 0, 100) #used
adler = enemy("Adler the trash", 40, "trash throw", 40, 60)
oscar = enemy("Oscar the trash", 41, "trash throw", 40, 60)
jemimah = enemy("Jemimah the trash", 42, "trash throw", 40, 60)
big = enemy("Big Bird the trash", 43, "trash throw", 40, 60)
elmo = enemy("Elmo the trash", 44, "trash throw", 40, 60)
grover = enemy("Grover the trash", 45, "trash throw", 40, 60)
bert = enemy("Bert the trash", 46, "trash throw", 40, 60)
ernie = enemy("Ernie the trash", 47, "trash throw", 40, 60)
amy = enemy("Amy the trash", 48, "trash throw", 40, 60)
lafonda = enemy("Lafonda the trash", 49, "trash throw", 40, 60)
maxamilion = enemy("Baxamilion the trash", 50, "trash throw", 40, 60)
fletcher = enemy("Fletcher the trash", 51, "trash throw", 40, 60)
brandon = enemy("Brandon the trash", 52, "trash throw", 40, 60)
melanie = enemy("Melanie the trash", 53, "trash throw", 40, 60)
jarrin = enemy("Jarrin the trash", 54, "trash throw", 40, 60)
autumn = enemy("Atutmn the trash", 55, "trash throw", 40, 60)
aubrey = enemy("Aubrey the trash", 56, "trash throw", 40, 60)
spencer = enemy("Spencer the trash", 57, "trash throw", 40, 60)
jonah = enemy("Jonah the trash", 58, "trash throw", 40, 60)
chloe = enemy("Chloe the trash", 59, "trash throw", 40, 60)
laurel = enemy("Laurel the trash", 60, "trash throw", 40, 60)
brooklyn = enemy("Brooklyn the trash", 61, "trash throw", 40, 60)
mesmir = enemy("Mesmir the trash", 62, "trash throw", 40, 60)
sam = enemy("Sam the trash", 63, "trash throw", 40, 60)
slime = enemy("slime the slick", 30, "gup", 20, 40)
spyro = enemy("spyro the dragon,", 75, "fire breath", 30, 60)
boar = enemy("boar the boring", 30, "charge", 5, 10)
wolf = enemy("sleepy the wolf", 5, "sleep", 0, 0)
world = enemy("Hello the world", 400, "Hello world", 80, 120) #used
satan = enemy("satan the bad", 250, "bad stuff", 0, 150) #used


map = [
  ['$', 'W', '*', '_', '_', '_', '_', '*'],
  ['$', '=', '_', 'X', '_', '_', '_', '_'], 
  ['$', 'W', '_', 'X', '*', '_', 'T', 'T'],
  ['$', 'W', '_', 'X', '_', 'T', 'T', 'T'],
  ['$', 'W', '_', '_', 'T', 'T', 'T', 'T'],
  ['$', 'W', '_', '_', 'T', 'T', 'T', '*'],
  ['$', 'W', '_', '_', 'T', 'T', 'T', 'T'],
  ['$', 'W', '_', '_', 'T', 'T', 'T', 'T'],
  ['$', 'W', '_', '_', '*', 'T', 'T', 'T'],
  ['$', 'W', '*', '_', '_', '_', 'T', '*'],
  ['$', 'W', '_', '_', '_', '_', 'T', '*']
]


p_location = [5, 2]

r_map = map
r_map[p_location[0]][p_location[1]] = '@'

def display_weapons():
  disp = ""
  if fist.own == 1:
    disp += "fist"
  if cell_phone.own == 1:
    disp += ", cell_phone"
  if shiv.own == 1:
    disp += ", shiv"
  if old_sword.own == 1:
    disp += ", old_sword"
  if fireball.own == 1: 
    disp += ", fireball"
  if spark.own == 1:
    disp += ", spark"
  if dark_blast.own == 1:
    disp += ", dark_blast"
  if bow.own == 1:
    disp += ", bow"
  if dagger.own == 1:
    disp += ", dagger"
  if dev_sword.own == 1:
    disp += ", dev_sword"
  if long_sword.own == 1:
    disp += ", long_sword"
  if kunai.own == 1:
    disp += ", kunai"
  if short_sword.own == 1:
    disp += ", short_sword"
  if boomerang.own == 1:
    disp += ", boomerang"
  if sword_o_slartybartfasts_gerbals_second_and_a_half_aunt.own == 1:
    disp += ", sword_o_slartybartfasts_gerbals_second_and_a_half_aunt"
  if mace.own == 1:
    disp += ", mace"
  if yo_yo.own == 1:
    disp += ", yo_yo"
  if leatherman.own == 1:
    disp += ", leatherman"
  if diamond_hoe.own == 1:
    disp += ", diamond_hoe"
  if mini_shark.own == 1:
    disp += ", mini_shark"
  if mozambique.own == 1:
    disp += ", mozambique"
  if scripture_power.own == 1:
    disp += ", scripture_power"
  print(disp)

def level_up():
  print("Congrats, you leveled up!")
  jordan.max_health *= 1.5
  jordan.health = jordan.max_health
  print(f"You are fully healed and your new max health is {jordan.max_health}")

def show_map(r_map):
  x = 0
  print(" ---------------------------------")
  while x != 10:
   print(f" | {r_map[x][0]} | {r_map[x][1]} | {r_map[x][2]} | {r_map[x][3]} | {r_map[x][4]} | {r_map[x][5]} | {r_map[x][6]} | {r_map[x][7]} |")
   print(" ---------------------------------")
   x += 1

def battle(name, health, attack, min, max):
  print("\n")
  print(f"A wild {name} appears. they have {health} HP and appear to use the attack called, {attack}.")
  print(f"You currently have {jordan.health} HP left")
  while jordan.health > 0 and health > 0:
    repeat = 0
    while repeat == 0:
      repeat = 1
      tool = input("What would you like to attack with (type \'inventory\' for a list of your weapons)?\n>>> ")

      if tool.lower() == 'inventory':
        display_weapons()
        repeat = 0

      elif tool.lower() == 'shiv' and shiv.own == 1:
        p_attack = random.randint(shiv.min, shiv.max)

      elif tool.lower() == 'fist' and fist.own == 1:
        p_attack = random.randint(fist.min, fist.max)

      elif tool.lower() == 'old_sword' and old_sword.own == 1:
        p_attack = random.randint(old_sword.min, old_sword.max)

      elif tool.lower() == 'fireball' and fireball.own == 1:
        p_attack = random.randint(fireball.min, fireball.max)

      elif tool.lower() == 'spark' and spark.own == 1:
        p_attack = random.randint(spark.min, spark.max)

      elif tool.lower() == 'dark_blast' and dark_blast.own == 1:
        p_attack = random.randint(dark_blast.min, dark_blast.max)

      elif tool.lower() == 'bow' and bow.own == 1:
        p_attack = random.randint(bow.min, bow.max)

      elif tool.lower() == 'dagger' and dagger.own == 1:
        p_attack = random.randint(dagger.min, dagger.max)

      elif tool.lower() == 'dev_sword' and dev_sword.own == 1:
        p_attack = random.randint(dev_sword.min, dev_sword.max)

      elif tool.lower() == 'cell_phone' and cell_phone.own == 1:
        p_attack = random.randint(cell_phone.min, cell_phone.max)

      elif tool.lower() == 'long_sword' and long_sword.own == 1:
        p_attack = random.randint(long_sword.min, long_sword.max)

      elif tool.lower() == 'kunai' and kunai.own == 1:
        p_attack = random.randint(kunai.min, kunai.max)

      elif tool.lower() == 'short_sword' and short_sword.own == 1:
        p_attack = random.randint(short_sword.min, short_sword.max)

      elif tool.lower() == 'boomerang' and boomerang.own == 1:
        p_attack = random.randint(boomerang.min, boomerang.max)

      elif tool.lower() == 'sword_o_slartybartfasts_gerbals_second_and_a_half_aunt' and sword_o_slartybartfasts_gerbals_second_and_a_half_aunt.own == 1:
        p_attack = random.randint(sword_o_slartybartfasts_gerbals_second_and_a_half_aunt.min, sword_o_slartybartfasts_gerbals_second_and_a_half_aunt.max)

      elif tool.lower() == 'mace' and mace.own == 1:
        p_attack = random.randint(mace.min, mace.max)

      elif tool.lower() == 'yo_yo' and yo_yo.own == 1:
        p_attack = random.randint(yo_yo.min, yo_yo.max)

      elif tool.lower() == 'leatherman' and leatherman.own == 1:
        p_attack = random.randint(leatherman.min, leatherman.max)

      elif tool.lower() == 'diamond_hoe' and diamond_hoe.own == 1:
        p_attack = random.randint(diamond_hoe.min, diamond_hoe.max)

      elif tool.lower() == 'mini_shark' and mini_shark.own == 1:
        p_attack = random.randint(mini_shark.min, mini_shark.max)

      elif tool.lower() == 'mozambique' and mozambique.own == 1:
        p_attack = random.randint(mozambique.min, mozambique.max)

      elif tool.lower() == 'scripture_power' and scripture_power.own == 1:
        p_attack = random.randint(scripture_power.min, scripture_power.max)
        
      else:
        print("try again with a weapon that you currently have unlocked")
        repeat = 0

    health -= p_attack
    print(f"you do {p_attack} damage to {name}. They are at {health} HP.")
    if health > 0:
      e_attack = random.randint(min, max)
      jordan.health -= e_attack
      print(f"{name} uses {attack}, it does {e_attack} damage to you. You now are at {jordan.health} HP.")
      if jordan.health <= 0:
        print(f"{jordan.name} has perished to {name}.")
  if jordan.health > 0:
    print(f"You defeated{name}.")
    jordan.xp += 1
    if jordan.xp % 3 == 0:
      level_up()
  print("\n")


def wing():
  wings.count += 1
  if wings.count == 24:
    print("Congrats! You unlocked wings because you murdered every single trash person!")
    wings.own = 1

prior_x = 5
prior_y = 2
jump_off = 0
woo = 0


def forest():
    print("Welcome to the trash forest.\nThe forest used to be a landfill, but due to the movie Wall-E people stopped producing trash and replaced all the land fills with forests.\nDue to their lack of trash, the trash people that called the landfills their home have started lashing out at anyone stupid enough to wander into their forest.")
    enter = input("Please press ENTER to continue your adventure")


print("\t---THE RIVER OF DARKNESS---")
change = 'yes'
while change.lower() == 'yes':
    loop = 0
    while loop != 1:
        loop = 1
        typ = input("(1.WARRIOR)   (2.WIZARD)   (3.ARCHER)   (4.ASSASSIN)\n\tWhat class would you like to choose? ")
        typ = typ.lower()
        old_sword.own = 0
        fireball.own = 0
        spark.own = 0
        dark_blast.own = 0
        bow.own = 0
        dagger.own = 0
        dev_sword.own = 0
        if typ.lower() == 'warrior' or typ == '1':
            x = 1
            health = 200
            old_sword.own = 1
            typ = 'warrior'
        elif typ.lower() == 'wizard' or typ == '2':
            x = 2
            health = 200
            fireball.own = 1
            spark.own = 1
            dark_blast.own = 1
            typ = 'wizard'
        elif typ.lower() == 'archer' or typ == '3':
            x = 3
            health = 200
            bow.own = 1
            typ ='archer'
        elif typ.lower() == 'assassin' or typ == '4':
            x = 4
            health = 200
            dagger.own = 1
            typ = 'assassin'
        elif typ.lower() == 'dev' or typ == '5':
            x = 5
            health = 9001
            dev_sword.own = 1
            typ = 'dev'
        else:
            loop = 0
            y = input(f"{typ} is not a valid class, please PRESS ENTER and try again\n")


    print(f"\nYou have picked the {typ} class.")

    if x == 1:
        print("\tThe warrior starts with an old_sword")
    if x == 2:
        print("\tthe wizard starts with fireball, spark, and dark_blast")
    if x == 3:
        print("\tThe archer starts with a bow")
    if x == 4:
        print("\tThe assassin starts with a dagger")
    if x == 5:
        print("\tThe dev is only supposed to be used by someone trying to get through my video game quickly. they start with a dev_sword")
    change = input("\nWould you like to change your class? (yes/no) ")

name = input(f"What do you want your {typ}'s name to be? ")

jordan = player(name, health, health, 0)

print(f"{jordan.name} the {typ} is trying to make their way to the other side of a the river of darkness to the land of promise (indicated by the \'$\' sign).\nThere is a sign next to you that says there is a bridge to the north (indicated by the \'=\' symbol),\nThe river of darkness is on your west (indicated by the \'W\' symbols), \nthere is a forest to your east (indicated by the \'T\' symbols?)\nIt doesn't seem like there is much to the south\nHowever, to the north next to the river is a steep mountainside which is not marked on the sign(indicated by the \'X\' symbols)")


while dead == False:
  show_map(r_map)
  r_map[p_location[0]][p_location[1]] = '.'

  prior_x = p_location[0]
  prior_y = p_location[1]
  exception = False
  move = input("Where do you want to move (up/left/down/right or WASD)? ")
  if(move.lower() == 'up' or move.lower() == 'w') and p_location[0] != 0:
    p_location[0] -= 1
  elif(move.lower() == 'down' or move.lower() == 's') and p_location[0] != 9:
    p_location[0] += 1
  elif(move.lower() == 'left' or move.lower() == 'a') and p_location[1] != 0:
    p_location[1] -= 1
  elif(move.lower() == 'right' or move.lower() == 'd') and p_location[1] != 7:
    p_location[1] += 1
  else:
    jump_off += 1
    if jump_off != 5:
      print("This is a small world flat world. You do not want to jump off of it")
    else:
      print("You were so insistant about jumping off the world that you finally musterd the currage to do so. You jumped over the side of the world and fell until you shattered into a bunch of 1's and 0's")
      dead = True
      p_location[1] = 0
      p_location[0] = 10
    
    exception = True

  traveled = r_map[p_location[0]][p_location[1]]
  r_map[p_location[0]][p_location[1]] = '@'
  
  if traveled == '.':
    if exception == False:
      print("There is nothing to see here, you have already traveled on this path")

  elif  p_location[0] == 0:
    
    if p_location[1] == 0:
      dead = True
      print("Congrats! You beat the game by murdering all the trash people!")

    elif p_location[1] == 1:
      sure = input("Are you sure that you want to jump in the river (yes/no)? ")
      if sure.lower() == 'yes' and wings.own == 0:
        dead = True
        print("You jumped into the river and drowned like a crazy person.")
      elif sure.lower() == 'yes' and wings.own == 1:
        print("you jumped into the river and instead of drowning like a crazy person you fly above the water with your new wings.")
      else:
        print("You made the right choice. for sure")
        p_location[0] = prior_x
        p_location[1] = prior_y
        r_map[p_location[0]][p_location[1]] = '@'
        r_map[0][1] = 'W'


    elif p_location[1] == 2:
      battle(zenith.name, zenith.health, zenith.attack, zenith.min, zenith.max)
      ("After you beat Zenith you found a mini_shark in a chest\n You pick it up and put it in your inventory")
      mini_shark = 1

    elif p_location[1] == 3:
      battle(slime.name, slime.health, slime.attack, slime.min, slime.max)

    elif p_location[1] == 4:
      battle(slime.name, slime.health, slime.attack, slime.min, slime.max)
    
    elif p_location[1] == 5:
      battle(slime.name, slime.health, slime.attack, slime.min, slime.max)

    elif p_location[1] == 6:
      battle(slime.name, slime.health, slime.attack, slime.min, slime.max)

    elif p_location[1] == 7:
      battle(eric.name, eric.health, eric.attack, eric.min, eric.max)

      if jordan.health > 0:
        print("After completely pumbeling a defensless castle you wait awhile for the dust to clear.\n you step into the ruins and see a leatherman\nYou pick it up and put it in your inventory")
        leatherman.own = 1
    
    else:
      print("")
      


  elif  p_location[0] == 1:

    if p_location[1] == 0:
      dead = True
      print("Congrats! You beat the game!")
      

    elif p_location[1] == 1:
      print("You finally made it to the bridge, you are so close to the other side.\nWho knew that it would be such a hard journey?\nYou notice that the bridge is blocked off by some rails\nThere is a sign on one of the rails that say,\nTRY OUR FREE APP ON THE APP STORE\nNOW WITH A FEATURE TO MOVE THESE PESKY RAILS")
      if cell_phone.own == 1:
        print("Good thing I got my phone back from my step father\nYou download the app and move the rails and access the bridge")
        enter = input("Please press ENTER to continue your journey")
        print("You start walking onto the bridge and feel a pit in your stomach.\nWith each step it gets worse and worse until it finally envelopes you\nYou pass out and fall onto the ground\n")
        battle(self.name, self.health, self.attack, self.min, self.max)
        if jordan.health > 0:
          print("You defeated the final boss of the game,\nyour self.\nNow that you are a master of the river and of your own body,\ntake the next step to victory.")
      else:
        print("You reach for your cell_phone and realize that your step father stole it from you because you are grounded, you better go find it.")
        
        p_location[0] = prior_x
        p_location[1] = prior_y
        r_map[p_location[0]][p_location[1]] = '@'
        r_map[1][1] = '='
        enter = input("Please press ENTER to continue your journey")
    

    elif p_location[1] == 2:
      battle(slime.name, slime.health, slime.attack, slime.min, slime.max)

    elif p_location[1] == 3:
      p_location[0] = prior_x
      p_location[1] = prior_y
      r_map[p_location[0]][p_location[1]] = '@'
      r_map[1][3] = 'X'

    elif p_location[1] == 4:
      battle(slime.name, slime.health, slime.attack, slime.min, slime.max)
    
    elif p_location[1] == 5:
      battle(slime.name, slime.health, slime.attack, slime.min, slime.max)

    elif p_location[1] == 6:
      battle(slime.name, slime.health, slime.attack, slime.min, slime.max)

    elif p_location[1] == 7:
      battle(slime.name, slime.health, slime.attack, slime.min, slime.max)
    
    else:
      print("")
      

    
  elif  p_location[0] == 2:

    if p_location[1] == 0:
      dead = True
      print("Congrats! You beat the game by murdering all the trash people!")

    elif p_location[1] == 1:
      sure = input("Are you sure that you want to jump in the river (yes/no)? ")
      if sure.lower() == 'yes' and wings.own == 0:
        dead = True
        print("You jumped into the river and drowned like a crazy person.")
      elif sure.lower() == 'yes' and wings.own == 1:
        print("you jumped into the river and instead of drowning like a crazy person you fly above the water with your new wings.")
      else:
        print("You made the right choice. for sure")
        p_location[0] = prior_x
        p_location[1] = prior_y
        r_map[p_location[0]][p_location[1]] = '@'
        r_map[2][1] = 'W'

    elif p_location[1] == 2:
      battle(slime.name, slime.health, slime.attack, slime.min, slime.max)

    elif p_location[1] == 3:
      p_location[0] = prior_x
      p_location[1] = prior_y
      r_map[p_location[0]][p_location[1]] = '@'
      r_map[2][3] = 'X'

    elif p_location[1] == 4:
      battle(slime.name, slime.health, slime.attack, slime.min, slime.max)
    
    elif p_location[1] == 5:
      battle(slime.name, slime.health, slime.attack, slime.min, slime.max)

    elif p_location[1] == 6:
      if woo == 0:
        forest()
        woo = 1
      battle(adler.name, adler.health, adler.attack, adler.min, adler.max)
      wing()

    elif p_location[1] == 7:
      if woo == 0:
        forest()
        woo = 1
      battle(oscar.name, oscar.health, oscar.attack, oscar.min, oscar.max)
      wing()
    
    else:
      print("")
      


  elif  p_location[0] == 3:

    if p_location[1] == 0:
      dead = True
      print("Congrats! You beat the game by murdering all the trash people!")

    elif p_location[1] == 1:
      sure = input("Are you sure that you want to jump in the river (yes/no)? ")
      if sure.lower() == 'yes' and wings.own == 0:
        dead = True
        print("You jumped into the river and drowned like a crazy person.")
      elif sure.lower() == 'yes' and wings.own == 1:
        print("you jumped into the river and instead of drowning like a crazy person you fly above the water with your new wings.")
      else:
        print("You made the right choice. for sure")
        p_location[0] = prior_x
        p_location[1] = prior_y
        r_map[p_location[0]][p_location[1]] = '@'
        r_map[3][1] = 'W'


    elif p_location[1] == 2:
      battle(slime.name, slime.health, slime.attack, slime.min, slime.max)

    elif p_location[1] == 3:
      p_location[0] = prior_x
      p_location[1] = prior_y
      r_map[p_location[0]][p_location[1]] = '@'
      r_map[3][3] = 'X'

    elif p_location[1] == 4:
      battle(satan.name, satan.health, satan.attack, satan.min, satan.max)

      if jordan.health > 0:
        print("You learned the skill scripture_power from defeating satan himself")
        scripture_power.own = 1
    
    elif p_location[1] == 5:
      if woo == 0:
        forest()
        woo = 1
      battle(jemimah.name, jemimah.health, jemimah.attack, jemimah.min, jemimah.max)
      wing()

    elif p_location[1] == 6:
      if woo == 0:
        forest()
        woo = 1
      battle(big.name, big.health, big.attack, big.min, big.max)
      wing()

    elif p_location[1] == 7:
      if woo == 0:
        forest()
        woo = 1
      battle(elmo.name, elmo.health, elmo.attack, elmo.min, elmo.max)
      wing()
    
    else:
      print("")
      

  elif  p_location[0] == 4:

    if p_location[1] == 0:
      dead = True
      print("Congrats! You beat the game by murdering all the trash people!")

    elif p_location[1] == 1:
      sure = input("Are you sure that you want to jump in the river (yes/no)? ")
      if sure.lower() == 'yes' and wings.own == 0:
        dead = True
        print("You jumped into the river and drowned like a crazy person.")
      elif sure.lower() == 'yes' and wings.own == 1:
        print("you jumped into the river and instead of drowning like a crazy person you fly above the water with your new wings.")
      else:
        print("You made the right choice. for sure")
        p_location[0] = prior_x
        p_location[1] = prior_y
        r_map[p_location[0]][p_location[1]] = '@'
        r_map[4][1] = 'W'


    elif p_location[1] == 2:
      battle(slime.name, slime.health, slime.attack, slime.min, slime.max)

    elif p_location[1] == 3:
      battle(slime.name, slime.health, slime.attack, slime.min, slime.max)

    elif p_location[1] == 4:
      if woo == 0:
        forest()
        woo = 1
      battle(grover.name, grover.health, grover.attack, grover.min, grover.max)
      wing()
    
    elif p_location[1] == 5:
      if woo == 0:
        forest()
        woo = 1
      battle(bert.name, bert.health, bert.attack, bert.min, bert.max)
      wing()

    elif p_location[1] == 6:
      if woo == 0:
        forest()
        woo = 1
      battle(ernie.name, ernie.health, ernie.attack, ernie.min, ernie.max)
      if jordan.health > 0:
        kunai = 1
        print("You found a kunai in the remains of ernies corps\n You put it in your inventory")
      wing()

    elif p_location[1] == 7:
      if woo == 0:
        forest()
        woo = 1
      battle(amy.name, amy.health, amy.attack, amy.min, amy.max)
      wing()
    
    else:
      print("")
     


  elif  p_location[0] == 5:

    if p_location[1] == 0:
      dead = True
      print("Congrats! You beat the game by murdering all the trash people!")

    elif p_location[1] == 1:
      sure = input("Are you sure that you want to jump in the river (yes/no?) ")
      if sure.lower() == 'yes' and wings.own == 0:
        dead = True
        print("You jumped into the river and drowned like a crazy person.")
      elif sure.lower() == 'yes' and wings.own == 1:
        print("you jumped into the river and instead of drowning like a crazy person you fly above the water with your new wings.")
      else:
        print("You made the right choice. for sure")
        p_location[0] = prior_x
        p_location[1] = prior_y
        r_map[p_location[0]][p_location[1]] = '@'
        r_map[5][1] = 'W'


    elif p_location[1] == 2:
      print("Congrats! You beat the game by murdering all the trash people!")
    elif p_location[1] == 3:
      pari.health = 30
      battle(pari.name, pari.health, pari.attack, pari.min, pari.max)
      print("You notice the start of the forest is on your right.\nYou feel as though there are lots of smelly creatures staring at you.\nAnd you feel as though there is something familiar and disaproving of you inside.\nSomething that, if you face, will increase your confidence.")

    elif p_location[1] == 4:
      if woo == 0:
        forest()
        woo = 1
      battle(lafonda.name, lafonda.health, lafonda.attack, lafonda.min, lafonda.max)
      wing()
    
    elif p_location[1] == 5:
      if woo == 0:
        forest()
        woo = 1
      battle(maxamilion.name, maxamilion.health, maxamilion.attack, maxamilion.min, maxamilion.max)
      wing()

    elif p_location[1] == 6:
      if woo == 0:
        forest()
        woo = 1
      battle(fletcher.name, fletcher.health, fletcher.attack, fletcher.min, fletcher.max)
      wing()

    elif p_location[1] == 7:
      print("You have made your way into the heart of the forest. You feel like something has lead you to this point. You notice someone sitting on the only stump in the forest. You start to approach the figure.")
      battle(angry.name, angry.health, angry.attack, angry.min, angry.max)
      if jordan.health >= 0:
        print("With your Angry Step Father defeated you are finally able to get ungrounded and get your phone back.")
        cell_phone.own = 1

    
    else:
      print("")
      


  elif  p_location[0] == 6:

    if p_location[1] == 0:
      dead = True
      print("Congrats! You beat the game by murdering all the trash people!")

    elif p_location[1] == 1:
      sure = input("Are you sure that you want to jump in the river (yes/no)? ")
      if sure.lower() == 'yes' and wings.own == 0:
        dead = True
        print("You jumped into the river and drowned like a crazy person.")
      elif sure.lower() == 'yes' and wings.own == 1:
        print("you jumped into the river and instead of drowning like a crazy person you fly above the water with your new wings.")
      else:
        print("You made the right choice. for sure")
        p_location[0] = prior_x
        p_location[1] = prior_y
        r_map[p_location[0]][p_location[1]] = '@'
        r_map[6][1] = 'W'


    elif p_location[1] == 2:
      battle(john.name, john.health, john.attack, john.min, john.max)

    elif p_location[1] == 3:
      battle(wolf.name, wolf.health, wolf.attack, wolf.min, wolf.max)

    elif p_location[1] == 4:
      if woo == 0:
        forest()
        woo = 1
      battle(brandon.name, brandon.health, brandon.attack, brandon.min, brandon.max)
      wing()
    
    elif p_location[1] == 5:
      if woo == 0:
        forest()
        woo = 1
      battle(melanie.name, melanie.health, melanie.attack, melanie.min, melanie.max)
      wing()

    elif p_location[1] == 6:
      if woo == 0:
        forest()
        woo = 1
      battle(jarrin.name, jarrin.health, jarrin.attack, jarrin.min, jarrin.max)
      wing()

    elif p_location[1] == 7:
      if woo == 0:
        forest()
        woo = 1
      battle(autumn.name, autumn.health, autumn.attack, autumn.min, autumn.max)
      wing()
    
    else:
      print("")
      


  elif  p_location[0] == 7:

    if p_location[1] == 0:
      dead = True
      print("Congrats! You beat the game by murdering all the trash people!")

    elif p_location[1] == 1:
      sure = input("Are you sure that you want to jump in the river (yes/no)? ")
      if sure.lower() == 'yes' and wings.own == 0:
        dead = True
        print("You jumped into the river and drowned like a crazy person.")
      elif sure.lower() == 'yes' and wings.own == 1:
        print("you jumped into the river and instead of drowning like a crazy person you fly above the water with your new wings.")
      else:
        print("You made the right choice. for sure")
        p_location[0] = prior_x
        p_location[1] = prior_y
        r_map[p_location[0]][p_location[1]] = '@'
        r_map[7][1] = 'W'

    elif p_location[1] == 2:
      battle(lenny.name, lenny.health, lenny.attack, lenny.min, lenny.max)
      print("That was a mercy killing.\nYou found a short_sword next to poor lenny.\nYou put it in your inventory")
      short_sword.own = 1

    elif p_location[1] == 3:
      battle(boar.name, boar.health, boar.attack, boar.min, boar.max)

    elif p_location[1] == 4:
      if woo == 0:
        forest()
        woo = 1
      battle(aubrey.name, aubrey.health, aubrey.attack, aubrey.min, aubrey.max)
      wing()
    
    elif p_location[1] == 5:
      if woo == 0:
        forest()
        woo = 1
      battle(spencer.name, spencer.health, spencer.attack, spencer.min, spencer.max)
      wing()

    elif p_location[1] == 6:
      if woo == 0:
        forest()
        woo = 1
      battle(jonah.name, jonah.health, jonah.attack, jonah.min, jonah.max)
      wing()

    elif p_location[1] == 7:
      if woo == 0:
        forest()
        woo = 1
      battle(chloe.name, chloe.health, chloe.attack, chloe.min, chloe.max)
      wing()
    
    else:
      print("")
      


  elif  p_location[0] == 8:

    if p_location[1] == 0:
      dead = True
      print("Congrats! You beat the game by murdering all the the trash people!")

    elif p_location[1] == 1:
      sure = input("Are you sure that you want to jump in the river (yes/no)? ")
      if sure.lower() == 'yes' and wings.own == 0:
        dead = True
        print("You jumped into the river and drowned like a crazy person.")
      elif sure.lower() == 'yes' and wings.own == 1:
        print("you jumped into the river and instead of drowning like a crazy person you fly above the water with your new wings.")
      else:
        print("You made the right choice. for sure")
        p_location[0] = prior_x
        p_location[1] = prior_y
        r_map[p_location[0]][p_location[1]] = '@'
        r_map[8][1] = 'W'


    elif p_location[1] == 2:
      battle(boar.name, boar.health, boar.attack, boar.min, boar.max)

    elif p_location[1] == 3:
      battle(boar.name, boar.health, boar.attack, boar.min, boar.max)

    elif p_location[1] == 4:
      battle(world.name, world.health, world.attack, world.min, world.max)
      if jordan.health > 0:
        print("You beat the programmers first program, here is your reward.\nYou recieved the mozambique")
        mozambique.own = 1
    
    elif p_location[1] == 5:
      if woo == 0:
        forest()
        woo = 1
      battle(laurel.name, laurel.health, laurel.attack, laurel.min, laurel.max)
      wing()

    elif p_location[1] == 6:
      if woo == 0:
        forest()
        woo = 1
      battle(brooklyn.name, brooklyn.health, brooklyn.attack, brooklyn.min, brooklyn.max)
      wing()

    elif p_location[1] == 7:
      if woo == 0:
        forest()
        woo = 1
      battle(mesmir.name, mesmir.health, mesmir.attack, mesmir.min, mesmir.max)
      wing()
    
    else:
      print("")
      


  elif  p_location[0] == 9:

    if p_location[1] == 0:
      dead = True
      print("Congrats! You beat the game by murdering all the trash people!")

    elif p_location[1] == 1:
      sure = input("Are you sure that you want to jump in the river (yes/no)? ")
      if sure.lower() == 'yes' and wings.own == 0:
        dead = True
        print("You jumped into the river and drowned like a crazy person.")
      elif sure.lower() == 'yes' and wings.own == 1:
        print("you jumped into the river and instead of drowning like a crazy person you fly above the water with your new wings.")
      else:
        print("You made the right choice. for sure")
        p_location[0] = prior_x
        p_location[1] = prior_y
        r_map[p_location[0]][p_location[1]] = '@'
        r_map[9][1] = 'W'


    elif p_location[1] == 2:
      print("as soon as you enter this place you start to feel confused.\nNothing feels right and nothing makes sense.\nIt is like an anti mirage.\n It looks like a sand dune, but you know it is a hill\n You make your way to the top of the hill and find upside down tress and the dark river seems to be in the sky.")
      battle(aqua.name, aqua.health, aqua.attack, aqua.min, aqua.max)
      if jordan.health > 0:
        print("You feel like you did something important, but you aren't quite sure what it was.\nas the elemental enemy died it left behind a diamond_hoe.\nYou pick it up and put it in your inventory")
      

    elif p_location[1] == 3:
      battle(boar.name, boar.health, boar.attack, boar.min, boar.max)

    elif p_location[1] == 4:
      battle(boar.name, boar.health, boar.attack, boar.min, boar.max)
    
    elif p_location[1] == 5:
      battle(boar.name, boar.health, boar.attack, boar.min, boar.max)

    elif p_location[1] == 6:
      if woo == 0:
        forest()
        woo = 1
      battle(sam.name, sam.health, sam.attack, sam.min, sam.max)
      wing()

    elif p_location[1] == 7:
      print("You come across the most generic looking house you have ever seen. It appears as though it was taken right out of a kindergarteners drawing. You approach it and open the door.")
      battle(jimothy.name, jimothy.health, jimothy.attack, jimothy.min, jimothy.max)
      if jordan.health > 0:
        print("After you beat the most average person in the world you discovered a yo_yo in the middle of his plain dinning room table. \n You pick it up and put it in your inventory.")
        yo_yo.own = 1
    else:
      print("")
      
  else:
    print("")

  if(p_location[0] == 1 and p_location[1] == 0) or jordan.health <= 0:
    dead = True

show_map(r_map)

print("Thanks for playing the game!")
enter = input("Press ENTER to exit the game. Relaunch if you want to play again")