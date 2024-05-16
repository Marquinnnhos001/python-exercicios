# Solicite ao Usuário que Informe o Número Inteiro
n= int(input("informe um número inteiro positivo N:"))

#Verifique se o número informado é positivo
while n<=0:
    n = int(input("Por favor, informe um número inteiro positivo N:"))

#Variavel Soma
soma=0

#Solicite ao úsuario que digite N números e os soma
for i in range(n):
    numero =float(input("Digite um número:"))
    soma += numero

#Calcule a média aritmetica dos N números digitados
media= soma/n

#Imprime a Média
print("A média dos números digitados é:",media)
