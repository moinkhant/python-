print("To find largest among  three numbers and display in ascending order")
a=int(input("Enter first number :"))
b=int(input("Enter Second number :"))
c=int(input("Enter Third number :"))
if a>b and a>c:
	print("Largest number is :",a)
elif b>a and b>c:
	print("Largest number is :",b)
else:
	print("Largest number is :",c)
asc=[a,b,c]
asc.sort()
print("Ascending Order is :",asc)
