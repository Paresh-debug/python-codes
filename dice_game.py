import random as rd

print("...Dice Game...")
count=0

while True :
	count+=1
	p1=rd.randint(1,6)
	print("Player 1: ",p1)
	if p1==6 :
		print("Player 1 got another chance")
		p1=rd.randint(1,6)
		print("player 1: ",p1)
		if p1==6 :
			
			print("Player 1 Won....")
			break
	p2=rd.randint(1,6)
	print("Player 2: ",p2)
	if p2==6 :
		print("Player 2 got another chance")
		p2=rd.randint(1,6)
		print("player 2: ",p2)
		if p2==6 :
			print("Player 2 Won....")
			break
print("...Game Ends...")
print("count = ",count)
