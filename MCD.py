numbers = input("inserta números:" )

def mcd(numbers):
    numbers = numbers.split()
    numbers.sort()
    if int(numbers[0]) == 0:
        return None
    else:
        print(numbers)
        print(len(numbers))
    
mcd(numbers)