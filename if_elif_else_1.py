'''
def numero_mayor(a,b,c):
    if (a>b) and (a>c):
        return f'El numero mayor es {a}'
    elif (b>a) and (b>c):
        return f'El numero mayor es {b}'
    else:
        return f'El numero mayor es {c}'

print(numero_mayor(10,20,30))'''
##################################################################
# Ejercicio 1
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
'''
edad=int(input('Ingrese su edad '))
if edad  <18:
    print('Usted es menor de edad')
elif edad >18:
    print('Usted es mayor de edad')
print('Fin del programa')
'''
######################################################################
# Ejercicio 2
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida
# por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
'''
password="hola"

contraseña=input('ingrese contraseña: ')

if password==contraseña:
    print('La contraseña es correcta')
else:
    print('La contraseña es inválida.')

print("Fin del programa.")'''
#############################################################
# Ejercicio 3
# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
'''
a = int(input('Ingrese un número: '))
b = int(input('Ingrese otro número: '))

if b==0:
    print('No se puede dividir por 0')
else:
    print(int(a/b))'''
#############################################################
# Ejercicio 4
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
'''
num1=int(input('Ingrese un número: '))
if num1%2==0:
    print('El numero es par.')
else:
    print('El numero es impar.')
'''
#############################################################
# Ejercicio 5

def estacion(x):
    if x == 1 or 2 or 3 :
        return 'Verano'
    elif x == 4 or 5 or 6 :
        return 'Otoño'
    elif x == 7 or 8 or 9 :
        return 'Invierno'
    elif x == 10 or 11 or 12 :
        return 'Primavera'
x=(3)
print(estacion(x))
