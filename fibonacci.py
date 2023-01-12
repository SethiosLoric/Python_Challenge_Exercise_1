/* @Author: @sethiosLoric
   @Date : le 12 janvier 2023
      
      
*/
#definition de la fonction de Fibonacci
def fibonacci (n):
    base=0 #la variable base nous servira a unitialiser la base de la suite
    unitial = 1
    
    while base < n :
        print(base)
        base, unitial = unitial, base + unitial
        
        
print('Bienvenue !')
nombre = int(input('Enter a value :'))
fib = fibonacci (nombre)
