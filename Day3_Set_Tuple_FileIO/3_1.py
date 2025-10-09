def findDuplic(lst:list)->set:
    outset=set()
    findset=set()
    for ele in lst:
        if ele not in findset:
            findset.add(ele)
        else:
            outset.add(ele)
    return outset


lst=[1,2,3,4,3,2,1,5]

print(findDuplic(lst))




