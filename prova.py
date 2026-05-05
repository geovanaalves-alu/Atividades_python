'''Uma empresa de telefonia cobra uma taxa fixa de R$ 20,00
mais R$ 0,50 por minuto de ligação. Crie uma função em Python que receba a
quantidade de minutos e retorne o valor total da fatura.'''
fixo = 20
variavel = 0.5
def fatura(minutos):
  #inutos = float(minutos)
    conta = (minutos*0.5) + 20
    return conta
#minutos = float(input("Quantos minutos você utilizou nesse mês?\n"))
#print(f"O valor da total da fatura é R${fatura(minutos)}\n")

'''A produção de uma fábrica segue a função \(P(x) = -x^2 +
10x + 50\), onde \(x\) é o número de máquinas. Crie uma função que receba
\(x\) e retorne a produção. Além disso, a função deve retornar 0 se o número de
máquinas for negativo. Construa a Fluxograma'''
def quadratica(x):
    if( x < 0):
        print("0")
    else:
      producao = ((x*-1)**2)+(10*x)+(50)
    return producao
#x = int(input("Digite o valor de máquinas para que eu diga o valor da produção\n"))
#print(f"O valor da produção foi R${quadratica(x)}")
    
def verificar_nivel(valor):
    if valor < 0:
        return "negativo"
    elif valor < 10:
        return "Baixo"
    else:
        return "Alto"
'''O que será impresso
print(verificar_nivel(5)) -> Baixo
print(varificar_nivel(15)) -> Alto
print(varificar_nivel(5)) -> Negativo

''' 
'''Contagem de Palavras em Arquivos'''
lista = []
def contagem_string(palavra_alvo):
 total = 0
 with open("3.txt","r") as arquivo:
  palavra = arquivo.read()
  lista = palavra.split(",")
  for i in lista:
     if(i == palavra_alvo):
        total = total + 1
 return total
palavra_alvo = input("Digite a palavra a ser buscada: ").lower()
print(f"A palavra escolhida e total de vezes que ela apareceu foi: {contagem_string(palavra_alvo)}")
Arquivo escolhido: 

'''voto, bla, bla, bla, bla,bla, bla,bla,
voto, lqqv, votos, votos,vots,'''
