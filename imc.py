peso = float(input("Qual o seu peso? (Kg) "))
altura = float(input("Qual a sua altura? (m) "))
imc = peso / (altura ** 2)

idealMin = (18.5 * (altura * altura))
idealMax = (25.0 * (altura * altura))

print("O IMC da pessoa é de {:.2f}".format(imc))
if imc < 15:
    print("Extremamente abaixo do peso!")
if imc >= 15 and imc < 16:
    print("Gravemente abaixo do peso!")
if imc >= 16 and imc < 18.5:
    print("Abaixo do peso ideal!")
if imc >= 18.5 and imc < 25:
    print("PARABÉNS, Faixa de peso ideal!")
if imc >= 25 and imc < 30:
    print("Sobrepeso!")
if imc >= 30 and imc < 35:
    print("Obesidade grau 1!")
if imc >= 35 and imc < 40:
    print("Obesidade grau 2 (GRAVE)!")
if imc >= 40:
    print("Obesidade grau 3 (MÓRBIDA)!")
print("O peso ideal para você é entre {:.2f} Kg e {:.2f} Kg ".format(idealMin, idealMax))

