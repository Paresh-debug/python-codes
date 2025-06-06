print("1- Stone")
print("2- Paper")
print("3- Scissors")

print("player 1 : ")
p1=int(input())
print("player 2 :")
p2=int(input())

if p1==p2:
    print("Draw")

if p1==1 and p2==2:
    print("Player 2 wins")

if p1==1 and p2==3:
    print("Player 1 wins")

if p1==2 and p2==1:
    print("Player 1 wins")

if p1==2 and p2==3:
    print("Player 2 wins")

if p1==3 and p2==1:
    print("Player 2 wins")

if p1==3 and p2==2:
    print("Player 1 wins")
