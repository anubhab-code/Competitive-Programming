def chinese_zodiac(year):
    animalDiff =  year-1924
    CurrentAnimal=animals[animalDiff%len(animals)]
    CurrentElement= elements[(animalDiff//2)%len(elements )]
    return " ".join([CurrentElement]+[CurrentAnimal])