import module_4_2_1 as m

class Continent:
    def __init__(self, name:str, countries:list):
        self.name=name
        self.countries=countries

    def tot_population(self):
        tot=0
        for country in self.countries:
            tot+=country.population
        return tot

# Test
canada=m.Country("Canada", 1e9, 1e6)
usa=m.Country("USA",1e10,1e5)
mexico=m.Country("Mexico",1e8,1e4)

countries=[canada,usa,mexico]
northamerica=Continent("North America", countries)
print(northamerica.tot_population())

