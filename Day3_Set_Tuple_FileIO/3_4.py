def menu(text):
    anslst=[]
    with open(text,"r") as menu:
        lines=menu.readlines()

        for line in lines:
            line.strip()
            ans=line.split()
            anslst.append(ans)
    return anslst


def reversemenu(text):
    anslst=[]
    with open(text,"r") as menu:
        lines=menu.readlines()
        ind=len(lines)
        for lin_ind in range(ind-1,-1,-1):

            line=lines[lin_ind].strip()
            anslst.append(line)
    return anslst


#reverse menu optimization by ChatGPT
def gptreverse(text):
    with open(text,"r") as menu:
        anslst=[line.strip() for line in reversed(menu.readlines())]
    return anslst


text="/Users/lavi/DataStructure_Algorithm_Exercise/Day3_Set_Tuple_FileIO/menu.txt"
print(menu(text))
print(reversemenu(text))
print(gptreverse(text))



