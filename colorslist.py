a=input("enter color list1:")
list1=a.split()

b=input("enter color list2:")
list2=b.split()

s=set(list1)
w=set(list2)
print(s-w)



