import random as rd
print("Enter goal to achieve : ")
goal=int(input())
sump1=0
sump2=0
while True:
	input()
	p1=rd.randint(1,6)

	if((sump1+p1)<=goal):
		sump1=sump1+p1
		print("turn for player 1 : ",p1,"\t\t\t\tplayer 1 total = ",sump1)
	else:
		print("turn for player 1 : ",p1,"\t\t\t\tplayer 1 total = ",sump1)
		
	if(sump1==goal):
		print("\t\t\t...PLAYER 1 WON...")
		break

	if(p1==6):
		print("player 1 got another chance")
		p1=rd.randint(1,6)
		if((sump1+p1)<=goal):
			sump1=sump1+p1
			print("turn for player 1 : ",p1,"\t\t\t\tplayer 1 total = ",sump1)
		else:
			print("turn for player 1 : ",p1,"\t\t\t\tplayer 1 total = ",sump1)
			
	if(sump1==goal):
		print("\t\t\t...PLAYER 1 WON...")
		break

	input()
	p2=rd.randint(1,6)

	if((sump2+p2)<=goal):
		sump2=sump2+p2
		print("turn for player 2 : ",p2,"\t\t\t\tplayer 2 total = ",sump2)
	else:
		print("turn for player 2 : ",p2,"\t\t\t\tplayer 2 total = ",sump2)
	if(sump2==goal):
		print("\t\t\t...PLAYER 2 WON...")
		break
	if(p2==6):
		print("player 2 got another chance")
		p2=rd.randint(1,6)

		if((sump2+p2)<=goal):
			sump2=sump2+p2
			print("turn for player 2 : ",p2,"\t\t\t\tplayer 2 total = ",sump2)
		else:
			print("turn for player 2 : ",p2,"\t\t\t\tplayer 2 total = ",sump2)
			
	if(sump2==goal):
		print("\t\t\t...PLAYER 2 WON...")
		break

	
