def P1(lst):
    sum=0
    for i in lst:
        if i<0:
            continue
        else:
            sum+=i
    return sum


lst1=[1,2,5,6,3,4]
lst2=[1,2,-3]
lst3=[0,-1]

test_ls=[lst1,lst2,lst3]

for lst in test_ls:
    print(P1(lst))


