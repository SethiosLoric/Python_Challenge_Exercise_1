/* @Author: @sethiosLoric
   @Date : le 12 janvier 2023
      
      
*/
#definition de la fonction de Fibonacci
def fibonacci (n):
    base=0 #la variable base nous servira a unitialiser la base de la suite
    unitial = 1 #unitialisation du pas principal
    
    while base < n : # la boucle while fait fonction d'itterateur
        print(base)
        base, unitial = unitial, base + unitial # on affecte respectivement dans base la valeur de unitial et dans unitial la valeur de base plus unitial
        
        
print('Bienvenue dans cette Exercice !')
nombre = int(input('Enter une valeur :')) #on demander d'entrer une valeur 
fib = fibonacci (nombre) #on affiche le resultat
