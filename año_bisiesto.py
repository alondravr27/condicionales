def año_bisiesto(año):
    if (año % 4 == 0 and año % 100 == 0) or (año % 400 == 0):
        return True
    else:
        return False

año = int(input("Ingrse el numero del que desea saber si es bisiesto:"))

if año_bisiesto(año):
    print("El año ingresado es bisiesto ")

else:
    print("El año ingresado no es bisiesto")