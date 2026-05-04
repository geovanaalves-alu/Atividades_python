'''Crie uma função chamada saudacao(nome) que receba um nome como
argumento e imprima "Olá, [nome]!".1'''
def saudacao(name):
 print(f"Olá, {name}")

#name = input("Qual é o seu nome?\n")

'''Escreva uma função calcular_area(base, altura) que retorne a área de um
retângulo.'''
def area_retangulo(base,altura):
 area = base * altura 
 return area
#base, altura = input("Iremos calcular a área do retângulo, por favor me diga a base e a altura, respectivamente \n").split(" ")
#print (f" O resultado é {area_retangulo(int (base), int(altura))}\n")
valores = []

'''Faça uma função maior_valor(a, b) que receba dois números e retorne o
maior deles.'''
def maior_valor(valores):
 return max(valores)
#valores = input("Vamos brincar de saber qual é o maior valor, digite quantos números quiser, lembre-se de " \
#"separá-los por vírgulas\n").split(",")
#print(f"O maior valor é {maior_valor(valores)}")

'''Crie uma função verificar_par(numero) que retorne True se o número for par e
False caso contrário.'''
def impar_par(numero):
 conta = int(numero) % 2
 if conta != 0:
  resultado = f"O número  {numero} é impar\n"
 else:
  resultado = f"O número {numero} é par\n"

 return resultado
#numero = input("Escolha um número e direi se ele é ímpar ou par\n")
#print(impar_par(int(numero)))

'''Escreva uma função que receba três notas e retorne a média aritmética
simples entre elas.'''
#nota1,nota2,nota3 = input("Me diga as suas notas do três semestres anteriores e" \
#"te direi a média\n").split(' ')
def media(nota1, nota2, nota3):
 conta = (float(nota1) + float(nota2) + float(nota3))/3
 return conta
#print(f"A média foi {media(nota1, nota2, nota3)}")

'''Crie uma função calcular_media(notas) que recebe uma lista de notas e
retorna a média, usando sum() e len()'''
notas = []
notas_numericas = []
def calcular_media(notas_numericas):
 dividendo = len(notas_numericas)
 total_notas = sum(notas_numericas)
 media = total_notas/dividendo
 return media
#sum, len  = soma total de lista 
#notas = input("Digite as suas notas!Separe as notas por vírgula\n").split(",")
#for i in notas:
#notas_numericas.append(int(i)) ## O input agregar oa valores ao tipo string
#print (f"Essa é a sua média {calcular_media(notas_numericas)}\n")

'''Escreva uma função que converta Celsius para Fahrenheit:'''
def conversao(celsius):
 celsius = celsius * 1.8 + 32
 return celsius

#celsius = float(input("Diga o valor em celsius e transformarei para fahrenheit\n"))
#print(f"O valor é {conversao(celsius)}°\n")
'''Quantidade de vogais'''
vogais = ["a","e","i","o","u"]
def vogais_existentes(palavra):
 soma = 0
 palavra.lower()
 for i in palavra:
  if i in vogais:
   soma = soma + 1
 return soma 

#palavra = input("Escolha uma palavra\n")
#print (f"A quantidade de vogais é {vogais_existentes(palavra)}\n")

'''Fatorial'''
def fatorial_operacao(numero): 
 fatorial = 4 - 1
 while numero > 1:
  fatorial *= numero 
  numero = numero - 1  
  print (fatorial, numero)
 #return fatorial, numero
 
#fatorial = 4 - 1 
#print(fatorial_operacao(4))
'''Função de inversão'''
def inverso(palavra):
 inversao = palavra[::-1]
 return inversao

#palavra = input("Escolha uma palavra\n")
#print (f"A palavra invertida é {inverso(palavra)}\n")

'''Crie uma função leiaInt() que funciona como a função input(), mas só aceita
valores numéricos inteiros, ignorando letras ou símbolos.'''
def leiaInt(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            return int(n)
        else:
            print('ERRO! Digite um número inteiro válido.')

# Programa Principal
#n = leiaInt('Digite um número: ')
#print(f'Você acabou de digitar o número {n}')]
def configurar_perfil(nome, idade, cidade="Desconhecida"):
    print("-" * 30)
    print(f"NOME: {nome}")
    print(f"IDADE: {idade}")
    print(f"CIDADE: {cidade}")
#configurar_perfil("Lucas", 25, "São Paulo")
#configurar_perfil("Maria", 30)

'''Fibonnacci'''
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
termo = 7
print(f"O {termo}º termo de Fibonacci é: {fibonacci(termo)}")

'''Exercício 4'''
var_global = "Eu sou GLOBAL"
def demonstrar_escopo():
    var_local = "Eu sou LOCAL"
    print(var_local)
    print(var_global)
demonstrar_escopo()
print(var_global)
try:
    print(var_local)
except NameError:
    print("A variável 'var_local' não pode ser acessada fora da função.")

'''Exercicio 5'''
def produto_mais_caro(lista_produtos):
    mais_caro = lista_produtos[0]
    for produto in lista_produtos:
        if produto['preco'] > mais_caro['preco']:
            mais_caro = produto
    return mais_caro
carrinho = [
    {"nome": "Celular", "preco": 2500},
    {"nome": "Notebook", "preco": 4500},
    {"nome": "Fone", "preco": 200}
]
resultado = produto_mais_caro(carrinho)
print(f"Produto mais caro: {resultado['nome']} custando R${resultado['preco']}")
