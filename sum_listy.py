list=[]
sum=0
def sum(n1):
	print("Enter the elements of list  ")
	for i in range(0,n1):
   		ele = int(input())
    	sum=sum+ele
    	list.append(ele)
	print("Sum of list is : ",sum)
n1 = int(input("Enter the length of list  : "))
sum(n1)
