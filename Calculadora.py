#Função para realizar o cálculo do IMC.
def calcular_imc(peso,altura):
    altura_metros=altura
    imc=peso/(altura_metros*2)
    return imc
    
# Função para Classificar o Resultado obtido.
def classificar_imc(imc):
    if imc < 18.5:
        return "abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso Normal"
    elif 25<=imc<29.9:
        return "Sobre Peso"
    else:
        return "Obesidade"

#Função para gerar campo de preenchimento dos dados a serem calculados.
peso=float(input("Porfavor digite seu peso:"))
altura=float(input("Porfavor digite sua altura:"))
resultado_imc=calcular_imc(peso,altura)
classificação=classificar_imc(resultado_imc)

#Função para exibir mensagem com resultado e classificação.
print(f"Seu IMC é {resultado_imc:.2f}")
print(f"Classificação:{classificação}")
