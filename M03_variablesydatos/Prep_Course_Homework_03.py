#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:
num = 5
print(num)


# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:
print(type(8.5))



# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:
print(type(num))



# 4) Crear una variable que contenga tu nombre

# In[2]:
name = 'Luz'



# 5) Crear una variable que contenga un número complejo

# In[3]:
num_complejo = 2 + 3j




# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:
print(type(num_complejo))




# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:
# import math
# pi_round = round(math.pi, 4)

pi = 3.1416



# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:
valor1 = 'True'
valor2 = True




# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:
print(type(valor1))
print(type(valor2))



# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:
sum = 3 + 1.3
print(sum)



# 11) Realizar una operación de suma de números complejos

# In[2]:
comp1 = 2 + 3j
comp2 = 3 + 2j
sum2 = comp1 + comp2
print(sum2)


# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:
num_real = 4
num_complj = 2 + 3j
sum_comp = num_real + num_complj
print(sum_comp)


# 13) Realizar una operación de multiplicación

# In[5]:
mult = 4 * 3
print(mult)



# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:
pont = 2 ** 8
print(pont)


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:
cociente = 27 / 4
print(cociente)



# 16) De la división anterior solamente mostrar la parte entera

# In[9]:
cociente_entero = int(cociente)
print(cociente_entero)



# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:
resto = 27 % 4
print(resto)



# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:
result = 4 * cociente_entero + resto
print(result)



# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:
var3 = 'Hola '
var4 = 'Mundo'
print(var3 + var4)


# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:
'2' == 2




# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:
int('2') == 2
'2' == str(2)



# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:
a = float('3.8')




# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:
var5 = 3
var5 -= 1
print(var5)


# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:
1 << 2




# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:
# 2 + '2'
# 2 + int('2')
str(2) + '2'



# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:
numero_entero = 5
cadena_texto = "Hola "

resultado = cadena_texto * numero_entero
print(resultado)


# %%
