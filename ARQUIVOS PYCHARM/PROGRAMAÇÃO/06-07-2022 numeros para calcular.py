operacao = input("qual operação voce deseja?")
if operacao=="soma":
    numero1 = float(input("informe a primeira nota"))
    numero2 = float(input("informe a segunda nota"))
    resultado = numero1+numero2
    print(resultado)
elif operacao == "div":
        numero1 = float(input("informe a primeira nota"))
        numero2 = float(input("informe a segunda nota"))
        resultado = numero1 / numero2
        print(numero1 / numero2)
elif operacao=="sub":
    numero1 = float(input("informe a primeira nota"))
    numero2 = float(input("informe a segunda nota"))
    resultado = numero1-numero2
    print(numero1/numero2)
elif operacao=="mult":
    numero1 = float(input("informe a primeira nota"))
    numero2 = float(input("informe a segunda nota"))
    resultado = numero1*numero2
    print(numero1*numero2)
