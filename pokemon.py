pokemon = {
    "nombre" : "Ratata",
    "vida_actual" : 50,
    "vida_maxima" : 100,
    "muerto" : False,
    "vivo" : True,
    "estat" : "Normal", #"Congelat","Dormit","Enverinat","Paralitzat","Cremat","Debilitat")
}


pocions = {
    "pocio_default" : +20,
    "SuperPoció" : +50,
    "Hiperpoció" : +150,
    "Antiquemar" : "no Cremat",
    "Despertar" : "no Dormit",
    "Antídot" : "no Envernitat",
    "Descongelar" : "no Congelat",
    "Antiparalitzar" : "no Paralitzat",
    "Reviure" : True,
    "Cura Total" : "Normal",
    "Restaura Tot" : "Normal",
}

print(pokemon)

print(json.dumps(pocions, sort_keys=False, indent=4))