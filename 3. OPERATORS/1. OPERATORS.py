a = 5
b = 10
#Arithmetic Operators...
print("\nARITHMETIC OPERATORS...")
print("Addition is : ",a+b)
print("Subtraction is : ",b-a)
print("Multiplication is : ",a*b)
print("Division is : ",b/a)

#Assignment Operators...
print("\nASSIGNMENT OPERATORS...")
x = 10
x += 2
print("x+=2 : ",x)
x -= 2
print("x-=2 : ",x)
x *= 2
print("x*=2 : ",x)
x /=2
print("x /= 2 : ",x)

#Comparision Operator...
print("\nCOMAPARISION OPERATORS...")
a=(5<1)
print("5<1 is : ",a)
b=(5>1)
print("5>1 is : ",b)
c=(5<=1)
print("5<=1 is : ",c)
d=(5>=1)
print("5>=1 is : ",d)
e=(5==1)
print("5==1 is : ",e)
f=(5!=1)
print("5!=1 is : ",f)


#LOGICAL OPERATORS...
print("\nLOGICAL OPERATORS...")
a=True
b=False
#AND operator...
print("The value of A and B is : ",(a and b)) #Returns True if both statements are true...
x = 5
print(x > 3 and x < 10)
#OR operator...
print("The value of A or B is : ",(a or b))   #Returns True if one of the statements is true...
x = 5
print(x > 3 or x < 4)
#NOT operator...
print("The value of not b is : ",(not b))     #Reverse the result,returns False if the result is true...
x = 5
print(not(x > 3 and x < 10))

#1.14