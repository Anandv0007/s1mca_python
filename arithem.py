print("1.Addition \n2.Substraction \n3.Multiplication \n4.Divion \n5.Modulus\n")
choice = int(input("Enter the choice :"))
a=int(input("Enter first number : \n"))
b=int(input("Enter second number : \n"))
if(choice == 1):
	sum=a+b
	print("Sum is : ",sum)
elif(choice == 2):
	diff=a-b
	print("Difference is : ",diff)
elif(choice == 3):
	mul=a*b
	print("Product is : ",mul)
elif(choice == 4):
	div=a/b
	print("Answer is : ",div)
elif(choice == 5):
	rem=a%b
	print("Remainder is : ",rem)
else:
	print("Invalid choice")
	


