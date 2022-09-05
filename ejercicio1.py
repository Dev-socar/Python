""""Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. 
Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman."""

def verificarRima(cadena1, cadena2):
    endTresCadena1 =  cadena1[-3] #obtenemos las tres últimas letras de la primera cadena
    endTresCadena2 = cadena2[-3]#obtenemos las tres últimas letras de la segunda cadena

    endDosCadena1 = cadena1[-2] #obtenemos las dos últimas letras de la primera cadena
    endDosCadena2 = cadena2[-2] #obtenemos las dos últimas letras de la segunda cadena

    if endTresCadena1 == endTresCadena2:#Comparamos si son iguales las 3 ultimas
        return print("Riman")
    elif endDosCadena1 == endDosCadena2:#Comparamos si son iguales las 3 ultimas
        return print("Riman pero poco")
    else:   
        return print("No riman")


palabra1 = input("Ingrese la primera palabra ->")#Pedimos la primera palabra
palabra2 = input("Ingrese la segunda palabra ->")#Pedimos la segunda palabra

verificarRima(palabra1.lower(), palabra2.lower())#Llamamos la funcion y le pasamos las palabras en minúsculas.


    