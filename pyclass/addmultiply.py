a=int(input("enter value of a"))
b=int(input("enter value of b"))
x=input("enter the operation")
def add(a,b):
    return a+b
def multiply(a,b):
    return a*b
if x=="+":
    ans= add(a,b)
    print(ans)

elif x=="*":
    ans=multiply(a,b)
    print(ans)

else :
    print("invalid")






    