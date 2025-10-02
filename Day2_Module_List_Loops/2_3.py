def starflag(n):
    for i in range(1,n):
        print("*"*(i))
    for i in range(n,0,-1):
        print("*"*i)
    return "HaHa"

print(starflag(3))

#2
def Star_Z(n):
    for i in range(1,n+1):
        if i==1 or i==n:
            print("*"*n)
        else:
            print(" "*(n-i)+"*"+" "*(i-1))
    return "GoodNight"

print(Star_Z(5))
