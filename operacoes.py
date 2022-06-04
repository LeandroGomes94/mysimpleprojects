from difflib import Match

x = 0
y = 0

while x == 0:
    try:
         x = int(input("Digite o primeiro número: "))
    except:
         x = 0
         print("Digite um valor válido para o primeiro número!")
while y == 0:
     try:    
        y = int(input("Digite o segundo número: "))
     except:
        y = 0
        print("Digite um valor válido para o segundo número!")

def soma(x,y):
    return x+y

def sub(x,y):
    return x-y

def mult(x,y):
    return x*y


def div(x,y):
    return x/y
   
op = 0

# método para selecionar e identificar a operação a ser executada

def selOp(op):
    while op == 0:
        try: op = int(input("""Qual operação será executada: 
    1 - Adição
    2 - Subtração
    3 - Multiplicação
    4 - Divisão """
    ))
        except: 
            op = 0
        match op:
            case 1:
                print("{} + {} = {}".format(x,y,soma(x,y)))
            case 2:
                print("{} - {} = {}".format(x,y,sub(x,y)))
            case 3:
                print("{} * {} = {}".format(x,y,mult(x,y)))
            case 4: 
                print("{} / {} = {}".format(x,y,div(x,y)))
            case default:
                print("Opção inválida")
                op = 0

selOp(op)