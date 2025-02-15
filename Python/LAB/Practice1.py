#write a program to input 2 numbers and print their sum

Number_1 = int(input("Number1:"))
Number_2 = int(input("Number2:"))

sum = Number_1+Number_2
print("sum =",sum)


#WAP to input side of a square and print its area 

side = int (input("side of the square :"))

area = side*side
print("area =",side*side)


#WAP to input 2 flaoting point numbrs & print their average 

float1 = float (input("enter float 1:"))
float2 = float (input("enter float 2:"))

average = (float1+float2)/2
print ("Average =", average)


#WAP to input 2 int numbers a and b. print true if a is greater than or equal to b if not print false.

a = int(input("enter the value of a :"))
b = int(input("enter the value of b :"))

if(a>b):{
    print("true")
}
else:{
    print("false")
}