def entrada_parque(edad):
    if edad < 12:
        return "$50 pesos"
    elif edad >= 12 and edad < 17:
        return "$80 pesos"
    else:
        return "$120 pesos"

edad = int(input("Ingrese su edad opara el cobro de su entrada: "))

entrada = entrada_parque(edad)

print(f"El precio a pagar de su entrada es de {entrada}")