# find if the given number is a palindrome or not?

rem=0,num=0
a=int(input("Enter a number to check palindrome :"))
while(a>0):
    rem=a%10
    num+=(rem*10)
    a//=10

if(num==a):
    print("Palindrome")
else:
    print("Not a Palindrome")
