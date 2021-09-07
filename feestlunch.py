Croissant = 0.39
hoeveelCroissant = 17
Stokbrood = 2.78
hoeveelStokbrood = 2
Kortingsbon = 0.50
hoeveelKortingsbon = 3

if hoeveelKortingsbon >= 0.01: 
    Prijs = hoeveelCroissant*Croissant + hoeveelStokbrood*Stokbrood - hoeveelKortingsbon*Kortingsbon
    print("De feestlunch kost je bij de bakker", Prijs, "euro voor de", hoeveelCroissant,  "croissantjes en de", hoeveelStokbrood, "stokbroden als de", hoeveelKortingsbon, "kortingsbonnen nog geldig zijn!")
else:
    Prijs = hoeveelCroissant*Croissant + hoeveelStokbrood*Stokbrood
    print("De feestlunch kost je bij de bakker", Prijs, "euro voor de", hoeveelCroissant,  "croissantjes en de", hoeveelStokbrood, "stokbroden!")
