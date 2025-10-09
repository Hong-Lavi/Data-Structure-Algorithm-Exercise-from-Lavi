def mosthighP(dic:dict)->str:
    val=0
    anslst=[]
    for par,pro in dic.items():
        if pro>val:
            val=pro
            anslst=[par]
        elif pro==val:
            anslst.append(par)
        else:
            continue

    return ", ".join(anslst)


test1={'neutron': 0.55, 'proton': 0.55, 'meson': 0.03, 'muon': 0.07, 'neutrino': 0.14}

print(mosthighP(test1))
