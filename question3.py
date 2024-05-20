#write a program to find the factorial of a nummber

a=int(input("Enter the number to find factorial"))

def fact(int a):
    if(a==1):
        return 1
    else:
        return a*fact(a-1)


print("Factorial :",fact(a))