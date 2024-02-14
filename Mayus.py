frase = input("escribe una frase: ")
vocals = ["A","E","I","O","U"]
def consUpper(frase):
    
    frase = frase.upper()

    arr = list(frase)
    
    for i in range(len(arr)):
        for n in range(len(vocals)):
         if arr[i] == vocals[n]:
            arr[i] = vocals[n].lower()  

    result = "".join(arr)

    if frase.isnumeric():
       result = ""
       
    print(result)
            
consUpper(frase)