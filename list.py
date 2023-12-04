a=input("enter list 1:")
list1=a.split()
print(list1)

b=input("enter list 2:")
list2=b.split()
print(list2)
if(len(list1))==(len(list2)):
	print("lists are of same lengths")
else:
	print("lists are of different lengths")
	
sum1=0
for i in list1:
	sum1=sum1+int(i)
sum2=0
for i in list2:
	sum2=sum2+int(i)
if sum1==sum2 :
	print("sum of lists are same")
else:
	print("sum of lists are not same")
for e in list1:
	for f in list2:
		if e==f:
			print("duplicate",e)
	
	
