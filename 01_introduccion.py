## COMENTARIOS
# Este es un comentario de una línea

'''
Este es un 
comentario escrito
en multiples líneas
'''

## VARIABLES
'''
Reglas para nombrar variables en Python:
1. Empieza con una letra o guion bajo “_”
2. No puede empezar con números
3. Sólo puede contener caracteres alfanuméricos y guiones bajo
4. Es sensible a mayúsculas y minúsculas
5. No puede llamarse igual a las palabras reservadas
'''
#Nombres de variables correctos
myvar = "Oscar"
myVar = "Oscar"
MYVAR = "Oscar" 
#Es "case-sensitive" por lo que myvar, myVar y MYVAR son diferentes variables
my_var = "Oscar"
_my_var = "Oscar"
myvar123 = "Oscar"

#Nombres de variables incorrectos
# 2myvar = "Oscar"
# my-var = "Oscar"
# my var = "Oscar"

#Inicializar multiples variables
s1, s2, s3 = "texto1", "texto2", "texto3" #Se pueden inicializar multiples variables...
e1 = e2 = e3 = "Oscar" # y también asignar el mismo valor al mismo tiempo a multiples variables

# IMPRIMIR O DESPLEGAR DATOS EN PANTALLA
print("¡Hola Mundo en Python!")
print("Empezamos desplegando texto en pantalla: ") 
#También se puede escribiendo entre comillas simples
print('Así podemos desplegar "comillas dobles"') 
print("Y de esta manera desplegaremos 'comillas simples'.")
#Diagonal invertida como carácter de escape
print("Otra manera es utilizando el carácter de escape, la \"Diagonal Invertida\" -> \' \\ \' ")

# En Python podemos redefinir qué queremos utilizar de separador "sep" y qué usar para finalizar "end", quitando el default salto de línea "\n"
print("Modificándo el comportamiento de print",sep="-",end="*") 
print("Esto estaría en otra línea, si no se hubiera reemplazado el salto de línea por el asterísco")

#Imprimir variables
nombre = "OSCAR"
print("¡Bienvenido!,", nombre) # Al imprimir una variable utilizando "coma", en automático deja un espacio al concatenar
print("Te llamas:"+nombre) # pero si se utiliza el símbolo "+", lo deja pegado
print(f"Mira {nombre}, también puedo meter variales en cadenas pre-formateadas")

## TIPOS DE DATOS
cadena = 'Esto es una cadena'
cad2 = "y esta también."
entero = 2345 # Cualquier número positivo o negativo sin importar el tamaño
flotante = -12.34554365 # números con punto decimal
boleanoV = True # Boleano Verdadero
boleanoF = False # Boleano Falso   
nulo = None # Sin valor

# Con "input" podemos pedir al usuario que introduzca datos
edad = input("¿Qué edad tienes? ") # ... y lo almacenamos en una variable


