def clasif_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 and lado2 == lado3:
        return "equilatero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "isosceles"
    else:
        return "escaleno"
    
lado1 = input("Ingrese el primer lado: ")
lado2 = input("Ingrese el segundo lado: ")
lado3 = input("Ingrese el tercer lado: ")

resultado = clasif_triangulo(lado1, lado2, lado3)

print("El triangulo es", resultado)