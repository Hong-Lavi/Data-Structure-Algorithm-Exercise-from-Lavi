from __future__ import annotations
class Country:
    def __init__(self, name:str, population:int, area:int):
        self.name=name
        self.population=int(population)
        self.area=int(area)

    def get_country_info(self):
        return f"Country: {self.name}\nPopulation: {self.population}\nArea: {self.area}"

    def is_larger(self, country1:Country):
        if self.area > country1.area:
            return True
        return False

    def population_density(self):
        return self.population/self.area




# Test
canada=Country("Canada", 1e9, 1e6)
usa=Country("USA",1e10,1e5)
print(canada.get_country_info())
print(canada.is_larger(usa))
print(canada.population_density())
