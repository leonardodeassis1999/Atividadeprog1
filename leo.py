nome = ("Leonardo")
idade = ("27")
cidade = ("Fraiburgo")
print(f"olá, meu nome é {nome}, tenho {idade} anos e moro em {cidade}!")
    
numero01 = float(input("Digite um número:"))
numero02 = float(input("Digite um número:"))

print(numero01 + numero02)
print(numero01 - numero02)
print(numero01 * numero02)
print(numero01 / numero02)

número = int(input("Digite um número:"))
for i in range(1,11,):
    print(número * i)
    
numero = ""
senha = 2

while numero != senha:
    numero = int(input("Digite um número:"))
    
    if numero < senha:
        print("É um numero maior!")
        
    elif numero > senha:
        print("É um numero menor!")
        
    else:
        numero = senha
        print("Acertou a senha!")