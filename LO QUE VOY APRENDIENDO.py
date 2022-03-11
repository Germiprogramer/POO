class pokemon:
    class pikachu:
        potencia = 20
        vida = 60
        def atacar(potencia):
            daño = potencia
            return daño
    class charmander:
        potencia = 25
        vida = 50
        def atacar(potencia):
            daño = potencia
            return daño

vidanueva = pokemon.charmander.vida - pokemon.pikachu.potencia

print(vidanueva)