numbers = input("inserta números:" )
mcds = []


def mcd(numbers):
    numbers = numbers.split()
    numbers.sort()
    numbers = [eval(i) for i in numbers]
    last = len(numbers) - 1
    if int(numbers[0]) == 0:
        return None
    else:
        for i in range(last, 0, -1):
            print(numbers[i])
            for n in range(int(numbers[last]), 0, -1):
                print(n)
                if n % numbers[i] == 0:
                    mcds.append(n)
                    print(str(n) + " " + str(numbers[i]) + " are mcd")


        print(numbers)
        print(mcds)
   
mcd(numbers)
