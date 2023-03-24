from Map import Map
from City import City


def loadCities(Map):
    print("Adding cities to map...")

    Viana = City("Viana do Castelo")
    Braga = City("Braga")
    Porto = City("Porto")
    VilaReal = City("Vila Real")
    Braganca = City("Braganca")
    Aveiro = City("Aveiro")
    Viseu = City("Viseu")
    Guarda = City("Guarda")
    Coimbra = City("Coimbra")
    CasteloBranco = City("Castelo Branco")
    Leiria = City("Leiria")
    Santarem = City("Santarém")
    Lisboa = City("Lisboa")
    Setubal = City("Setúbal")
    Portalegre = City("Portalegre")
    Evora = City("Évora")
    Beja = City("Beja")
    Faro = City("Faro")

    Viana.addAdjacentCity(Braga)
    Viana.addAdjacentCity(Porto)

    Porto.addAdjacentCity(Viana)
    Porto.addAdjacentCity(VilaReal)
    Porto.addAdjacentCity(Braga)
    Porto.addAdjacentCity(Viseu)

    VilaReal.addAdjacentCity(Porto)
    VilaReal.addAdjacentCity(Braganca)
    VilaReal.addAdjacentCity(Braga)
    VilaReal.addAdjacentCity(Viseu)
    VilaReal.addAdjacentCity(Guarda)

    Aveiro.addAdjacentCity(Viseu)
    Aveiro.addAdjacentCity(Coimbra)
    Aveiro.addAdjacentCity(Porto)
    Aveiro.addAdjacentCity(Leiria)

    Viseu.addAdjacentCity(VilaReal)
    Viseu.addAdjacentCity(Porto)
    Viseu.addAdjacentCity(Aveiro)
    Viseu.addAdjacentCity(Coimbra)
    Viseu.addAdjacentCity(Guarda)

    Guarda.addAdjacentCity(Viseu)
    Guarda.addAdjacentCity(CasteloBranco)
    Guarda.addAdjacentCity(VilaReal)
    Guarda.addAdjacentCity(Braganca)

    Coimbra.addAdjacentCity(Aveiro)
    Coimbra.addAdjacentCity(Viseu)
    Coimbra.addAdjacentCity(CasteloBranco)
    Coimbra.addAdjacentCity(Leiria)

    CasteloBranco.addAdjacentCity(Guarda)
    CasteloBranco.addAdjacentCity(Coimbra)
    CasteloBranco.addAdjacentCity(Portalegre)
    CasteloBranco.addAdjacentCity(Evora)

    Leiria.addAdjacentCity(Aveiro)
    Leiria.addAdjacentCity(Coimbra)
    Leiria.addAdjacentCity(Santarem)
    Leiria.addAdjacentCity(Lisboa)

    Santarem.addAdjacentCity(Leiria)
    Santarem.addAdjacentCity(Lisboa)
    Santarem.addAdjacentCity(Evora)

    Lisboa.addAdjacentCity(Santarem)
    Lisboa.addAdjacentCity(Leiria)
    Lisboa.addAdjacentCity(Setubal)
    Lisboa.addAdjacentCity(Evora)

    Setubal.addAdjacentCity(Lisboa)
    Setubal.addAdjacentCity(Evora)
    Setubal.addAdjacentCity(Beja)
    Setubal.addAdjacentCity(Faro)

    Portalegre.addAdjacentCity(CasteloBranco)
    Portalegre.addAdjacentCity(Evora)

    Evora.addAdjacentCity(Portalegre)
    Evora.addAdjacentCity(Lisboa)
    Evora.addAdjacentCity(Setubal)
    Evora.addAdjacentCity(Beja)

    Beja.addAdjacentCity(Evora)
    Beja.addAdjacentCity(Faro)
    Beja.addAdjacentCity(Setubal)

    Faro.addAdjacentCity(Beja)
    Faro.addAdjacentCity(Setubal)

    Map.addCity(Viana)
    Map.addCity(Braga)
    Map.addCity(Porto)
    Map.addCity(VilaReal)
    Map.addCity(Braganca)
    Map.addCity(Aveiro)
    Map.addCity(Viseu)
    Map.addCity(Guarda)
    Map.addCity(Coimbra)
    Map.addCity(CasteloBranco)
    Map.addCity(Leiria)
    Map.addCity(Santarem)
    Map.addCity(Lisboa)
    Map.addCity(Setubal)
    Map.addCity(Portalegre)
    Map.addCity(Evora)
    Map.addCity(Beja)
    Map.addCity(Faro)

    print("All cities added to map!")
