print ("Enter any Character : ")
a=input()
print("Enter Range for prefix = ")
prerange=int(input())
print("Enter Range for postfix = ")
postrange=int(input())


print("Entered value = ",a)
pre=ord(a);
post=ord(a);

for i in range(0,prerange):
	
	pre-=1
	print("prefix = ",chr(pre))


for i in range(0,postrange):
	post+=1
	print("postfix = ",chr(post))
	
	
	

