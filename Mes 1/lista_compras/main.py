lista_compras = []
menu_texto = "Elija una opcion:\n" \
        "1.- Ver lista de compras\n" \
        "2.- Agregar algo\n" \
        "3.- Eliminar un elemento\n" \
        "4.- Salir\n"
separador = "###############################################"

def main():
    while(True):
        menu_eleccion = input(menu_texto)
        print(separador)
            
        if menu_eleccion in "1234":
            if menu_eleccion == "1":
                ver_lista()
            elif menu_eleccion == "2":
                agregar_elemento()
            elif menu_eleccion == "3":
                eliminar_elemento()
            else:
                return
        else:
            print("Opcion invalida. Intente de nuevo.")

def ver_lista():
    for index, elemento in enumerate(lista_compras):
        print(f"{index + 1}.- {elemento}")

def agregar_elemento():
    while(True):
        elemento = input("Escriba lo que quiere agregar: ")
        while(True):
            validacion = input(f"Esto es lo que desea agregar? {elemento} \n"
                            "1.- Si \n"
                            "2.- No\n")
            if validacion == "1":
                lista_compras.append(elemento)
                print("Elemento actualizado con exito!!!")
                return
            elif validacion == "2":
                break
            else:
                print("Valor invalido. Intente de nuevo.")

def eliminar_elemento():
    while(True):
        ver_lista()
        print(separador)
        elemento = input("Escriba el nombre del elemento a borrar de la lista: ")
        if elemento in lista_compras:
            while(True):
                validacion = input(f"Esto es lo que desea eliminar? {elemento} \n"
                                "1.- Si \n"
                                "2.- No\n")
                if validacion == "1":
                    lista_compras.remove(elemento)
                    print("Elemento borrado con exito!!!")
                    return
                elif validacion == "2":
                    break
                else:
                    print("Valor invalido. Intente de nuevo.")
        else:
            print("Elemento no encontrado. \n"
            "Verifique escribir el elemento tal cual se imprime en consola.")

if __name__ == "__main__":
    main()