rimeira Função 
def calcular_imc(peso, altura):
    # Calcula IMC
    imc = peso / (altura ** 2)
    return imc
#Segunda Função
def classificar_imc(imc):
    # Classifica IMC
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"
#Terceira Função
def main():
    # Solicita dados do usuário
    try:
        peso = float(input("Por Favor digite seu peso: "))
        altura = float(input("Por Favor digite sua altura: "))
        
        # Calcula IMC
        imc = calcular_imc(peso, altura)
    
        # Classifica e exibe o resultado
        classificacao = classificar_imc(imc)
        print(f"Seu IMC é: {imc:.2f} - Classificação: {classificacao}")
