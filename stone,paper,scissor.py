def game(a,b):
    if a==b:
        return "draw"
    elif a=="stone" and b=="scissor" or a=="paper" and b=="stone" or a=="scissor" and b=="paper" :
        return "player"
    else:
        return "bot"
import random
mode=str.lower(input("mode:"))
player=str.lower(input("player:"))
if mode=="random":
 x=random.randint(1,3)
 if x==1:
  bot="stone"
 elif x==2:
  bot="paper"
 else:
  bot="scissor"
  print("bot:",bot)
elif mode=="manual":
    bot=str.lower(input("bot:"))
else:
    print('''
    mode can be manual or random
    ''')
    exit()
if player!="stone" and player!="paper" and player!="scissor":
    print('''
    input should be stone paper or scissor
    ''')
elif bot!="stone" and bot!="paper" and bot!="scissor":
    print('''
    input should be stone paper or scissor
    ''')
else:
    win=game(player,bot)
    if win=="draw":
        print('''
        draw
        ''')
    elif win=="player":
        print('''
        you win
        ''')
    else:
        print('''
        you lose
        ''')