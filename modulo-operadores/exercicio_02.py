# crie um programa que verica se o numero é impar ou par

numero = int(input("insira uma valor aqui: "))

def paridade(numero):
    if numero % 2 == 0: 
      return "par"
    else:
      return "impar"
        
resultado =  paridade(numero)     

print(resultado)
        