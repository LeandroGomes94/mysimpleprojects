def geraTabuada():
    x = int(input("Digite o número para gerar a tabuada correspondente: "))
    y = int(input("Digite a quantidade de números a ser calculada: "))
    for i in range(y+1):
        print("{0} X {1} = {2}".format(x,i,x*i))

def geraTodasTabuadas():
    for i in range(11):
        print("\n\n")
        for n in range(11):
            print("{0} X {1} = {2}".format(i,n,i*n))

geraTodasTabuadas()