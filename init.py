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

    Viana.addAdjacentCity(Braga,48)
    Viana.addAdjacentCity(Porto,71)
    
    Braga.addAdjacentCity(Viana,48)
    Braga.addAdjacentCity(VilaReal,106)
    Braga.addAdjacentCity(Porto,53)

    Porto.addAdjacentCity(Viana,71)
    Porto.addAdjacentCity(VilaReal,116)
    Porto.addAdjacentCity(Braga,53)
    Porto.addAdjacentCity(Viseu,133)

    VilaReal.addAdjacentCity(Porto,116)
    VilaReal.addAdjacentCity(Braganca,137)
    VilaReal.addAdjacentCity(Braga,106)
    VilaReal.addAdjacentCity(Viseu,110)
    VilaReal.addAdjacentCity(Guarda,106)

    Aveiro.addAdjacentCity(Viseu,95)
    Aveiro.addAdjacentCity(Coimbra,68)
    Aveiro.addAdjacentCity(Porto,68)
    Aveiro.addAdjacentCity(Leiria,115)

    Viseu.addAdjacentCity(VilaReal,110)
    Viseu.addAdjacentCity(Porto,133)
    Viseu.addAdjacentCity(Aveiro,95)
    Viseu.addAdjacentCity(Coimbra,96)
    Viseu.addAdjacentCity(Guarda,85)

    Guarda.addAdjacentCity(Viseu,85)
    Guarda.addAdjacentCity(CasteloBranco,106)
    Guarda.addAdjacentCity(VilaReal,157)
    Guarda.addAdjacentCity(Braganca,202)

    Coimbra.addAdjacentCity(Aveiro,68)
    Coimbra.addAdjacentCity(Viseu,96)
    Coimbra.addAdjacentCity(CasteloBranco,159)
    Coimbra.addAdjacentCity(Leiria,67)

    CasteloBranco.addAdjacentCity(Guarda,106)
    CasteloBranco.addAdjacentCity(Coimbra,159)
    CasteloBranco.addAdjacentCity(Portalegre,80)
    CasteloBranco.addAdjacentCity(Evora,203)

    Leiria.addAdjacentCity(Aveiro,115)
    Leiria.addAdjacentCity(Coimbra,67)
    Leiria.addAdjacentCity(Santarem,70)
    Leiria.addAdjacentCity(Lisboa,129)

    Santarem.addAdjacentCity(Leiria,70)
    Santarem.addAdjacentCity(Lisboa,78)
    Santarem.addAdjacentCity(Evora,117)

    Lisboa.addAdjacentCity(Santarem,78)
    Lisboa.addAdjacentCity(Leiria,129)
    Lisboa.addAdjacentCity(Setubal,50)
    Lisboa.addAdjacentCity(Evora,150)
    Lisboa.addAdjacentCity(Faro,299)

    Setubal.addAdjacentCity(Lisboa,50)
    Setubal.addAdjacentCity(Evora,103)
    Setubal.addAdjacentCity(Beja,142)
    Setubal.addAdjacentCity(Faro,249)

    Portalegre.addAdjacentCity(CasteloBranco,80)
    Portalegre.addAdjacentCity(Evora,131)

    Evora.addAdjacentCity(Portalegre,131)
    Evora.addAdjacentCity(Lisboa,150)
    Evora.addAdjacentCity(Setubal,103)
    Evora.addAdjacentCity(Beja,78)

    Beja.addAdjacentCity(Evora,78)
    Beja.addAdjacentCity(Faro,152)
    Beja.addAdjacentCity(Setubal,142)

    Faro.addAdjacentCity(Beja,152)
    Faro.addAdjacentCity(Setubal,249)
    Faro.addAdjacentCity(Lisboa,299)

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
