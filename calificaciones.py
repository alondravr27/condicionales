def clasificacion_calif(calif):
    if calif >= 90:
        return "A"
    elif calif >= 80:
        return "B"
    elif calif >= 70:
        return "C"
    elif calif >= 60:
        return "D"
    else:
        return "F"

calif = int(input("Ingrse su calificacion:"))

letra = clasificacion_calif(calif)

print(f"La equivalencia a su calificacion es: {letra}")