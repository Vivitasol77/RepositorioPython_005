#ingresar dos números, mostrar la suma y multiplicación de ambos 

a=int(input("Digite un numero: "))
b=int(input("Digite otro numero: "))
suma=a+b
multi=a*b
print("La suma de " + str(a) + " y de " + str(b) + " Es igual a: " + str(suma))
print("La multiplicación de " + str(a) + " y de " + str(b) + " Es igual a: " + str(multi))
#estructura if
if(a>b):
    print("El numero " + str(a)+ " Es mayor que: " + str(b))
elif (a<b):
    print("El numero " + str(b)+ " Es mayor que: " + str(a))
else:
    print("Los numeros son iguales!")
    