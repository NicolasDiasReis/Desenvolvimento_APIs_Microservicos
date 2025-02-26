from unidecode import unidecode

def print_lista (x):
    [print(y) for y in x] if isinstance(x, list) else print('Erro: O argumento não é uma lista.')

def maximo(x):
    if isinstance(x, list):
        maxi = x[0]
        for n in x:
            if n > maxi:
                maxi = n
        return maxi
    else:
        print('Erro: O argumento não é uma lista.')

def sum_lista(x):
    return sum(x) if isinstance(x, list) else print('Erro: O argumento não é uma lista')
    
lista = [1,2,3,4,5,6,7,8,9,0]
print(sum_lista(lista))

def cont_vogais(f):
    d = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    x = [l for l in unidecode(f.replace(' ', '').replace(',', '').lower())]
    print(x)
    for v in x:
        if v in d.keys():
            d[v] += 1
    return d