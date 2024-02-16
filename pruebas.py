number = input("insert: ")
def prueba(number):
    number = number.split()
    number = [eval(i) for i in number]
    print(number)
    if (number[0] % number[1]) == 0:
        print(" divisores")
    else:
        print(" no divisores")
prueba(number)
