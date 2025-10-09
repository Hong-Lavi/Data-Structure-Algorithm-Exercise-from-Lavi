def checkdic(dic:dict)->int:

    firstval=next(iter(dic.values()))
    checkset=set(firstval.keys())

    for key, val in dic.items():
        if set(val.keys())!=checkset:
            return 0
    return 1

test1={'a': {'aa':123, 'ab': [1,2]}, 'b': {'aa': 'bb', 'ab': 'cc'}}
test2={'A': {1: 'a', 2: 'b'}, 'B': {2: 'c', 3: 'd'}}

testlst=[test1, test2]
for case in testlst:
    print(checkdic(case))
