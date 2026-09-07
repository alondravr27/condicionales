def numero_mayor(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

def numero_menor(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        return num1
    elif num2 < num1 and num2 < num3:
        return num2
    else:
        return num3

num1 = int(input("Ingrese un primer numero: "))
num2 = int(input("Ingrese un segundo numero: "))
num3 = int(input("Ingrese un tercer numero: "))

mayor = numero_mayor(num1, num2, num3)
menor = numero_menor(num1, num2, num3)

print(f"El numero mayor es {mayor} y el numero menor es {menor}")