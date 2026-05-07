regla = {
    "a" : "@", "A" : "@",
    "u" : "5", "U" : "5",
    "e" : "3", "E" : "3",
    "i" : "1", "I" : "1",
    "o" : "0", "O" : "0"
}

regla_mejor = str.maketrans({
    "a" : "@", "A" : "@",
    "u" : "5", "U" : "5",
    "e" : "3", "E" : "3",
    "i" : "1", "I" : "1",
    "o" : "0", "O" : "0"
})

def main():
    oracion_traducir = input("Ingrese la oracion a traducir: ")
    print(oracion_traducir.translate(regla_mejor))
    print(traductor(oracion_traducir))
    return

def traductor(oracion):
    resultado = ""
    for letra in oracion:
        coincide = regla.get(letra, False)
        if coincide != False:
            resultado += coincide
        else:
            resultado += letra
    return resultado

if __name__ == "__main__":
    main()