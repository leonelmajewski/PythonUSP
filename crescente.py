n = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))
n3 = int(input("Insira o terceiro número: "))

if(n <= n2):
    if(n2 <= n3):
        print("crescente")
    else:
        print("não está em ordem crescente")
else:
    print("não está em ordem crescente")
