def P4(lst):
    lst_ans=[]
    for l in lst:
        lst_ans.append(l[0])
    lst_ans.sort()
    return lst_ans


lst=[["apple",5],["banana",6],["cup",3],["alligator",9]]

print(P4(lst))
