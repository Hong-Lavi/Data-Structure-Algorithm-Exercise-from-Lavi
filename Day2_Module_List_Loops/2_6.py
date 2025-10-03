def sum_until_thres(lst,K):
    sum=0
    for i in range(len(lst)):
        try:
            float(lst[i])
        except ValueError:
            continue

        sum+=float(lst[i])

        if sum>=K:
            return sum, i

    return -1, None


lst=[1,2.5,"3","4.5",5,"abc",6]
print(sum_until_thres(lst,30))






