class Persona:
    edad = 27
    nombre = "Victor"
    pais = "España"

doctor = Persona()
print("la edad es {}".format(doctor.edad))
print("la edad es:", getattr(doctor, "edad"))
print("el doctor tiene una edad?", hasattr(doctor, "edad"))
setattr(doctor, "nombre", "hector")
print(doctor.nombre)
delattr(Persona, "pais") #eliminar un atributo