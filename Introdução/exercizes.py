listaVogais = ['a','e','i','o','u']
palavra = input('Digite uma palavra: ')
palavra_list = list(palavra.lower())
contador = 0

for elemento in palavra_list: 
    for elemento2 in listaVogais:
        if elemento == elemento2: 
            contador += 1 
            
print("A palavra: ", palavra, "tem" ,contador, "vogais")
