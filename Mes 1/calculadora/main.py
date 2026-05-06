import re

def main():
    operacion = input("Ingrese la operacion: \n")
    operacion = operacion.replace(" ", "")
    resultado = calcular(operacion)
    print(resultado)

def calcular(operacion):
    anterior = None
    valor = ""
    valor_aux = ""
    operador = ""

    for i in operacion:
        if es_numero(i):
            valor_aux += i
            anterior = i
        else:
            if(es_numero(anterior)):
                if(es_operador(i)):
                    if(valor != ""):
                        if(valor_aux != ""):
                            valor = realizar_calculo(float(valor), float(valor_aux), operador)
                            valor_aux = ""
                            operador = i
                    else:
                        valor = valor_aux
                        valor_aux = ""
                        operador = i
                else:
                    valor = "Syntax ERROR"
                    return valor
            else:
                valor = "Syntax ERROR"
                return valor
        
    if(valor_aux != "" and valor != "" and operador != ""):
        valor = realizar_calculo(float(valor), float(valor_aux), operador)

    return valor

def realizar_calculo(val1, val2, operacion):
    if(operacion == "+"):
        return val1 + val2
    elif(operacion == "-"):
        return val1 - val2
    elif(operacion == "*"):
        return val1 * val2
    elif(operacion == "/"):
        return val1 / val2
    elif(operacion == "%"):
        return val1 % val2
    elif(operacion == "^"):
        return val1 ** val2
    
def es_operador(dato):
    operadores = ["+", "-", "*", "/", "%", "^"]

    if dato not in operadores:
        return False
    else:
        return True
    
def es_numero(dato):
    try: 
        float(dato)
        return True
    except: 
        return False

if __name__ == "__main__":
    main()