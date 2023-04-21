lista1=[1,2,3,4,5,6,7,8,9]
lista2=["1","2","3","4","5","6","7","8","9"]
#Concatenar una lista con otra usando un lambda y un map
print(list(map(lambda x,y : str(x)+str(y),lista1,lista2)))
import math
#Conseguir el area de un circulo
listaRadios=(5,10,50,15)
print(list(map(lambda radio: round(math.pi*radio**2,2),listaRadios)))

#de una lista de palabras devolver la primera y ultima letra de cada palabra concatenada
listaPalabras=["andres","miguel","famita","sergio"]
print(list(map(lambda letra: letra[0]+letra[-1] ,listaPalabras)))

#que palabra contiene la letra "a" con "True or False":
print(list(map(lambda x: "a" in x,listaPalabras)))






