
def main():
    character_name = "Julian Antonio De la Cruz Garcia"
    character_age = 25
    objetive_age = 100.0

    character_name = input("¿Cuál es tu nombre? ")
    character_age = int(input("¿Cuántos años tienes? "))
    objetive_age = int(input("¿CUantos años quieres vivir? "))

    if character_age <= 0:
        print(f"{character_name}, Tienes que nacer primero!!!.")
        exit(1)

    if objetive_age <= 0:
        print(f"{character_name}, No seas tan pesimista, recuerda los buenos momentos :).")
        exit(1)

    if objetive_age <= character_age:
        print(f"{character_name}, Ya has vivido lo suficiente, disfruta el presente :)")
        exit(1)

    needed_lifes = calculate_needed_lifes(objetive_age, character_age)
    print(f"Hola {character_name}, tienes {character_age} años.")
    print(f"Solo tienes que vivir {round(needed_lifes)} veces mas, para tener {objetive_age} años.")
    return 0


def calculate_needed_lifes(objetive_age, character_age):
    needed_lifes = objetive_age / character_age
    needed_lifes = max(0, needed_lifes)

    return needed_lifes

if __name__ == "__main__":
    main()
