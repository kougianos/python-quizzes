# Minion Game
# Quiz URL:
# 	https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    # your code goes here
    Player_A=0
    Player_B=0
    vowels='AEIOU'

    for i in range(len(string)):
      if string[i] in vowels:
        Player_A+=len(string)-i  
      else:
        Player_B+=len(string)-i

    if Player_A == Player_B:
      print("Draw")
    elif Player_A>Player_B:
      print("{} {}".format("Kevin", Player_A))
    elif Player_A<Player_B:
      print("{} {}".format("Stuart", Player_B))


minion_game("BAANANAS")