#Import and set basic values
import sys
import random
from time import sleep
ph = 200
mh = 0
mon = True
monp = True
bp = 0
bm = 0
bp == 0
bm == 0

n = "north"
s = "south"

def combat():
  global m
  def pwin(x, y):
    global mh
    global ph
    global bp
    global bm
    bdp = random.randint(1,10)
    bdm = random.randint(1,10)
    blp = random.randint(1,100)
    blm = random.randint(1,100)
    ed = random.randint(6,10)
    pd = random.randint(11,20)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")
    print("Player chooses to",x,"and deals",pd,"Damage!")
    if bm == 0:
      if blm <= 10:
        print("FATAL HIT! Monster is now bleeding")
        bm = 1
    if pd == 20:
      print("### CRTITCAL! ###")
      print("")
      print(m,"chooses to",y,"and deals",ed,"Damage!")
    if bp == 0:
      if blp <= 5:
        print("FATAL HIT! You are now bleeding")
        bp = 1
    ph = int(ph) - int(ed)
    mh = int(mh) - int(pd)
    print("")
    if bp == 1:
      print("You take",bdm,"bleeding damage!")
      ph = int(ph) - int(bdp)
      print("")
  
    if bm == 1:
      print(m,"takes",bdm,"bleeding damage!")
      mh = int(mh) - int(bdm)
      print("")
    
    print("Player has",ph,"health!")
    print("")
    print(m,"has",mh,"health!")
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  
  def plose(x, y):
    global mh
    global ph
    global bp
    global bm
    bdp = random.randint(1,10)
    bdm = random.randint(1,10)
    ed = random.randint(11,20)
    pd = random.randint(1,5)
    blp = random.randint(1,100)
    blm = random.randint(1,100)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")
    print("Player chooses to",x,"and deals",pd,"Damage!")
    if bm == 0:
      if blm <= 5:
        print("FATAL HIT! Monster is now bleeding")
        bm = 1
    print("")
    print(m,"chooses to",y,"and deals",ed,"Damage!")
  
    if bp == 0:
      if blp <= 10:
        print("FATAL HIT! You are now bleeding")
        bp = 1
  
    if ed == 20:
      print("### CRTITCAL! ###")
    ph = int(ph) - int(ed)
    mh = int(mh) - int(pd)
    print("")
    if bp == 1:
      print("You take",bdm,"bleeding damage!")
      ph = int(ph) - int(bdp)
      print("")
  
    if bm == 1:
      print(m,"takes",bdm,"bleeding damage!")
      mh = int(mh) - int(bdm)
      print("")
    print("Player has",ph,"health!")
    print("")
    print(m,"has",mh,"health!")
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      
  def pdraw(x, y):
    global mh
    global ph
    global bp
    global bm
    bdp = random.randint(1,10)
    bdm = random.randint(1,10)
    ed = random.randint(6,10)
    pd = random.randint(6,10)
    blp = random.randint(1,100)
    blm = random.randint(1,100)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")
    print("Player chooses to",x,"and deals",pd,"Damage!")
    if bm == 0:
      if blm <= 7:
        print("FATAL HIT! Monster is now bleeding")
        bm = 1
    print("")
    print(m,"chooses to",y,"and deals",ed,"Damage!")
    if bp == 0:
      if blp <= 7:
        print("FATAL HIT! You now bleeding!")
        bp = 1
    ph = int(ph) - int(ed)
    mh = int(mh) - int(pd)
    if bp == 1:
      print("")
      print("You take",bdm,"bleeding damage!")
      ph = int(ph) - int(bdp)
      print("")
    
    if bm == 1:
      print(m,"takes",bdm,"bleeding damage!")
      mh = int(mh) - int(bdm)
    print("")
    print("Player has",ph,"health!")
    print("")
    print(m,"has",mh,"health!")
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      

  replyr = "rush"
  replyc = "counter"
  replys = "strike"

  print("""
  ###################
  
   COMBAT INITIATED
   
  ###################
  """)
  print("Rules: rush > strike > counter > rush")

  while mon: 
    if int(mh) >= 1:
      attack = input("Choose your attack! (help to repeat Rules) ")
      if attack.lower() == "help":
        print("")
        print("Rules: rush > strike > counter > rush")
        print("")
      

    
      if attack.lower() == replyr:
        ma = random.randint(1,3)
        if ma == 1:
          pc = 'rush'
          mc = 'rush'
          pdraw(pc, mc)
        if ma == 2:
          pc = 'rush'
          mc = 'counter'
          plose(pc, mc)
        if ma == 3:
          pc = 'rush'
          mc = 'strike'
          pwin(pc, mc)
      

    
      if attack.lower() == replyc:
        ma = random.randint(1,3)
        if ma == 1:
          pc = 'counter'
          mc = 'rush'
          pwin(pc, mc)
        if ma == 2:
          pc = 'counter'
          mc = 'counter'
          pdraw(pc, mc)
        if ma == 3:
          pc = 'counter'
          mc = 'strike'
          plose(pc, mc)

    
      if attack.lower() == replys:
        ma = random.randint(1,3)
        if ma == 1:
          pc = 'strike'
          mc = 'rush'
          plose(pc, mc)
        if ma == 2:
          pc = 'strike'
          mc = 'counter'
          pwin(pc, mc)
        if ma == 3:
          pc = 'strike'
          mc = 'strike'
          pdraw(pc, mc)
    if ph <= 0:
      print("You died, GAME OVER")
      sys.exit()
    
    if mh <= 0:
      print("Congratulations, you win!")
      break
    
d1 = input("Where u gonna go? (north or south?")
if d1.lower() == n:
  print ("You go north, but theres an orc!")
  m = 'orc'
  mh = random.randint(50,70)
  combat()
if d1.lower() == s:
  print("you go south but theres Avinay!")
  mh = random.randint(50,70)
  m = 'Avinay'
  combat()
  
d2 = input("you finally defeat that beast, where do you wish to go next? (east or west)?")