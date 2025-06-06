import random as rd

def generate_unique_number():
    while True:
        num = rd.randint(1000, 9999)
        set_num = set(str(num))
        if len(set_num) == 4:
            break
    return num



rdnum= generate_unique_number()
cows=0
bulls=0

while True:
	print("Guess a 4 digit number")
	guess=input()
    
		