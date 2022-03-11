class persona:
    doctor = "victor"

print(persona.doctor)
#cuando se presiona un punto, se tienen disponibles todos los objetos pertenecientes a una clase

class jugador:
    j1 = "messi"
    j2 = "c.ronaldo"

print(jugador.j1)

class equipo:
    e2 = "barcelona"
    e3 = "real madrid"

print(equipo.e3)

class nombre:
    pass

victor = nombre()
maria = nombre()

victor.edad = 30
victor.sexo = "masculino"
victor.pais = "España"

maria.edad = 25
maria.sexo = "femenino"
maria.pais = "Portugal"

print(victor.edad, victor.sexo, victor.pais)


#objeto.atributo = valor