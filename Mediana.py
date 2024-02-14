numbers = input("inserta números:" )
Med = 0
Med1 = 0


def mediana(numbers):
   
    numbers = numbers.split()
    numbers = [eval(i) for i in numbers]
    numbers.sort()


    if int(numbers[0]) == 0:
        return None
    else:
        amount = int(numbers[0])

        if amount%2 == True:
            print("Longitud impar ")

            Med = int((len(numbers)/2)+0.5)
            print(numbers[Med])
        else:
            print("Longitud par ")

            Med = int((len(numbers)/2))
            print(Med)
            Med1 = Med + 1

            result = float((numbers[Med] + numbers[Med1])/2)
            print (result)
        
mediana(numbers)