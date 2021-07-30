#  Υλοποιήση cmd για r,p,s game
from random import randint
from random import seed
import datetime

def seed_r():
   time=datetime.datetime.now()
   strtime=time.strftime("%H:%M:%S")
   list=strtime.split(":")
   return 3600*int(list[0])+60*int(list[1])+int(list[2])

def valid_move(move):
    move=move.upper()
    if(move=="R"):
        return True
    elif move=="S":
        return True
    elif move=="P":
        return True
    else:
        return False

def find_winner(player,computer):
    if player=="R" and computer=="S":
       return 1
    elif player=="P" and computer=="R":
        return 1
    elif player=="S" and computer=="P":
        return 1
    elif player==computer:
        return 0
    else:
        return 2


class game:
    def __init__(self):
       self.player=0
       self.computer=0
       self.tie=0
    def rounds(self):
        rnds=7
        moves=["R","P","S"]
        seed(seed_r())
        for i in range(0,7):
           x=input("Give Players move:")
           while(valid_move(x)==False):
             x=input("Not A Valid Move(R-P-S)-Give Players move")
           computer=moves[randint(0,2)]
           winner=find_winner(x,computer)
           print("------------------------Round "+str(i+1)+" ----------------------------------")
           print("Players Move:"+x)
           print("Computers Move:"+computer)
           if winner==1:
               print("Player Wins!!")
               self.player+=1
           elif winner==2:
               print("Computer wins!!")
               self.computer+=1
           else:
               print("Tie Game")
               self.tie+=1
           print("------------------------------------------------------------------")
           print("\n")
           if int(self.player)-int(self.computer)>int(rnds)-i+1:
               print("*********** Total Score **************")
               print("Player:"+str(self.player))
               print("Computer:"+str(self.computer))
               print("---------------")
               print("Player wins!!!!!!!")
               print("---------------")
               print("**************************************")
               break
           elif int(self.computer)-int(self.player)>int(rnds)-i+1:
                print("*********** Total Score **************")
                print("Player:"+str(self.player))
                print("Computer:"+str(self.computer))
                print("---------------")
                print("Computer wins!!!!!!!")
                print("---------------")
                print("**************************************")
                break
        if int(self.player)>int(self.computer):
               print("*********** Total Score **************")
               print("Player:"+str(self.player))
               print("Computer:"+str(self.computer))
               print("---------------")
               print("Player wins!!!!!!!")
               print("---------------")
               print("**************************************")
        elif int(self.computer)>int(self.player):
                print("*********** Total Score **************")
                print("Player:"+str(self.player))
                print("Computer:"+str(self.computer))
                print("---------------")
                print("Computer wins!!!!!!!")
                print("---------------")
                print("**************************************")
        else:
            print("*********** Total Score **************")
            print("Player:"+str(self.player))
            print("Computer:"+str(self.computer))
            print("---------------")
            print("Tie Game")
            print("---------------")
            print("**************************************")

g=game()
g.rounds()