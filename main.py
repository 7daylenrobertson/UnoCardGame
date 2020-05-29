#card deck: blue 0-9, +2, skip, reverse ; red 0-9 , +2, skip, reverse ; yellow 0-9, +2, skip, reverse ; green 0-9, +2, skip, reverse 
# +2 (next player gets 2+ cards added to deck unless they have a +2 to use for loop append 2 cards)
# +4 (next player gets 4 cards added to deck unless they have a +4 to use. for loop append 4 cards) 
# wild card (player inputs a color), 
#skip (continues a player in a list), 
#reverse (reverses order of players starting where that player is at .reverse[index:]) Syntax: reversed_list = os[start:stop:step]
#start with 7 cards, card goes on deck 
#list of players and dictionary with all 7 of their cards
#can add to deck of cards if end of list is same color or number as the card being placed
#input and last card in deck is shown, player says b6 or bskip, checks if that card is in list, if so, appends and removes card from list
#if input is draw, append to player deck list and remove card from deck
import random
cardCount=0
winnersList=[]
playerCount=3
a1=-1
lv=["p1","p2","p3"]
skip=False
countCards= int(input("How many cards? (Must be lower than 12 or equal to): \n"))

while countCards>12:
 if countCards>12:
  print("You heard me the first time... \n")
  countCards= int(input("How many cards? (Must be lower than 12 or equal to): \n "))

listOfPlayers= {"player 1":[],"player 2":[],"player 3":[]}
listOfCards = [
"b0","b1","b2","b3","b4","b5","b6","b7","b8","b9",  "bs", "br", "b2", "+4", "wi",
"g0","g1","g2","g3", "g4","g5","g6","g7","g8","g9", "gs", "gr", "g2", "+4", "wi",
"y0","y1","y2","y3", "y4","y5","y6","y7","y8","y9", "ys", "yr", "y2", "+4",
"r0","r1","r2","r3", "r4","r5","r6","r7","r8","r9", "rs","rr", "r2", "+4"]
drawnCards=[]
random.shuffle(listOfCards)
while cardCount < countCards:
 for player in listOfPlayers:
  rancard = random.randint(0,len(listOfCards)-1)
  listOfPlayers[player].append(listOfCards[rancard])
  listOfCards.remove(listOfCards[rancard])
 cardCount+=1
print(listOfPlayers,"\n")
print(listOfCards)
drawnCards.append(listOfCards[-1])
print(drawnCards)
while playerCount!=1:
  for players in listOfPlayers:
   if len(listOfPlayers[players])==0:
     continue
   if skip==True:
     print(str(players)+ "has been skipped!")
     skip=False
     continue
   if listOfCards==0:
     listOfCards= random.shuffle(drawnCards)
     drawnCards=[]
     drawnCards.append(listOfCards[-1])
     
   if drawnCards[-1][1]=="2":
     turn= input(str(players)+ " do you have a draw 2 card?: \n")
     if turn.lower()=="no":
       listOfPlayers[players].append(listOfCards[-1:-2])
       listOfCards.remove(listOfCards[-1:-2])
       

   print("This is your deck "+ str(players) + " " + str(listOfPlayers[players]))
   turn= input(str(players)+ " the card is: " + drawnCards[-1] + " Select a card from your deck by typing it! (Type 'done' if finished) : \n")
   if turn=="done":
     break
   if turn in listOfPlayers[players]:
     if turn[0]==drawnCards[-1][0] or turn[1]==drawnCards[-1][1]:
      if turn [1]=="s":
       drawnCards.append(turn)
       listOfPlayers[players].remove(turn)
       skip=True
      elif turn[1]=="2":
       drawnCards.append(turn)
       listOfPlayers[players].remove(turn)
      else:
        drawnCards.append(turn)
        listOfPlayers[players].remove(turn)
     elif turn=="wi" or turn=="+4":
        drawnCards.append(turn)
        listOfPlayers[players].remove(turn)
     else:
       print("That is not the card on the top of the deck "+ str(players)+ "! You lose your turn! \n ")
     if len(listOfPlayers[players])==0:
       print(str(players) + " is out!")
       playerCount-=1
       winnersList.append(players)
   elif turn=="draw":
     listOfPlayers[players].append(listOfCards[-1])
     listOfCards.remove(listOfCards[-1])

   else:
     print("That is not a card in your deck "+ str(players)+ "! You lose your turn! \n ")
