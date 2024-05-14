# Solicita ao usuário para inserir a resistência e a corrente
resistencia = float(input("Digite o valor da resistência em ohms (Ω): "))
corrente = float(input("Digite o valor da corrente em amperes (A): "))

# Calcula a tensão usando a fórmula U = R * i
tensao = resistencia * corrente

# Exibe o resultado da tensão
print("A tensão é:", tensao, "volts (V)")
