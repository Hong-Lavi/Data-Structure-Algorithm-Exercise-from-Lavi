def read_csv(csv):
    ansdic={}
    with open(csv, "r") as f:
        headers=f.readline().strip().split(",")
        for header in headers:
            ansdic.setdefault(header,[])


        for line in f.readlines():
            linelst=line.strip().split(",")
            for header,inp in zip(headers, linelst):
                ansdic[header].append(inp)
    return ansdic



csv="contacts.csv"

print(read_csv(csv))
