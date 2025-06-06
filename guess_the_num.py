from random import *

ran=randint(1,10)
count=0
while True :
 count+=1
 print("Enter any number (1-10):",end=" ")
 num=int(input())
 if num<ran : print("actual number is greater")
 if num>ran : print("actual number is smaller")
 if num==ran :
  print("\nyou guessed correctly")
  print("random number was",ran)
 
  break
print("count = " ,count)