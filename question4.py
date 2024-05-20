#write a program to find the sum of digits of a given number'


rem=0,sum=0
a=int(input("Enter a number to check palindrome :"))
while(a>0):
    rem=a%10
    sum+=rem
    a//=10

print("Sum of Digits :",sum)
