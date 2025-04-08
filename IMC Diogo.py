print("--------------------CACULADORA DE IMC--------------------")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = peso / (altura * altura)
print("Sua altura: ", altura)
print("Seu peso: ", peso) 
print("Seu IMC: ", imc)

if imc <= 16:
    print("Nível de IMC: Magreza grau III")
elif imc >= 16 and imc <= 16.9:
    print("Nível de IMC: Magreza grau II")
elif imc >= 17 and imc <= 18.4:
    print("Nível de IMC: Magreza grau I")
elif imc >= 18.5 and imc <= 24.9:
    print("Nível de IMC: Eutrofia")
elif imc >= 25 and imc <= 29.9:
    print("Nível de IMC: Pré-obesidade")
elif imc >= 30 and imc <= 34.9:
    print("Nível de IMC: Obesidade moderada(Grau I)")
elif imc >= 35 and imc <= 39.9:
    print("Nível de IMC: Obesidade severa(Grau II)")
elif imc >= 40:
    print("Nível de IMC: Obesidade muito severa(Grau III)")