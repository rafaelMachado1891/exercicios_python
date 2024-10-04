# escreva um programa que leia o nome e o preço de varios produtos. No final mostre o total da compra,
#  quantos produtos custam mais de R$ 1.000,00 e o nome do produto mais barato. 
p = c = b = 0
total = p * c
n = ''
produtos = 0
menor = 0
nome = ''
r= 'S'
c=0

while True:
    
    n = str(input('Digite o nome do produto: '))
    p = float(input('digite o preço do produto: '))
    r = str(input('Deseja cadastrar mais intens? [S/N]: ')).upper().strip()[0]
    total+=p
    c+=1
    if p >= 1000:
       produtos+=1
<<<<<<< HEAD
    if c ==1:
       menor = n
    else:
       if p < menor:
          menor = n
        
=======
    if c ==1 or p < menor:
       menor = p
       nome = n
    
>>>>>>> 169c616ebed3d93be6945728030fb1223288aae1
    while r not in 'NS':
        r = str(input('Deseja cadastrar mais intens? [S/N]: ')).upper().strip()[0]
    if r in 'N':
     break
    else:
       pass

<<<<<<< HEAD
print(f'O total das compras é R${total:.2f}, são {produtos} produtos com valor acima de R$ 1,000.00, o produto com o menor valor é {menor}')
=======
print(f'O total das compras é R${total:.2f}, são {produtos} produtos com valor acima de R$ 1,000.00, o produto com o menor valor é {nome} que custa R${menor:.2f}')
>>>>>>> 169c616ebed3d93be6945728030fb1223288aae1
