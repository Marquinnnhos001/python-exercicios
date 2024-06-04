#Calculae a Média das Notas

def calcularMedia(nota1,nota2,nota3,nota4,):
    media = (nota1 + nota2 + nota3 + nota4)/4
    return media
#Verifique se o Aluno foi Aprovado

def verificacao(m):
    if m >=5:
      return "Você foi aprovado"
    else:
      return "Você não foi aprovado"

#Calcule a Média
print('Calculadora de Média') 
n1 = float(input('Digite a 1 nota: '))
n2 = float(input('Digite a 2 nota: '))
n3= float(input('Digite a 3 nota: '))
n4 = float(input('Digite a 4 nota: '))
m = calcularMedia(n1,n2,n3,n4)
r= verificacao(m)
print(f"Sua média é {m}, Voce foi {r}")

