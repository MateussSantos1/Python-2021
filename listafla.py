# Lista de funções

def maior2(a, b):
    if a > b:
        return a
    else:
        return b


def maior5(a, b, c, d, e):
    if a > b and a > c and a > d and a > e:
        return a
    if b > a and b > c and b > d and b > e:
        return b

    if c > a and c > b and c > d and c > e:
        return c
    if d > a and d > b and d > c and d > e:
        return d
    else:
        return e

def verifivogal(c):
    vogais = 'aeiouAEIOU'
    result = 0
    for char in c:
        if char in vogais:
            result = result + 1
    return result




def quantidade_de_vogais(s):




    s = s.lower()
    soma = 0
    for c in s:
        if (verifivogal(c) == True):
            soma += 1
        return soma


def impar(n):
    if n % 2 == 0:
        return False
    else:
        return True


def conta_palavras(texto):
    texto = removpont(texto)
    lista = texto.split()
    return len(lista)



def removpont(s):
        pont ='. , : ; ! ?'
        for p in pont:
            s = s.replace(p, ' ')
        return s


def intervaloab(n1, n2):
    lst = list(range(n1,n2 + 1))
    return lst


def fatorial(n):
    from math import factorial
    f = factorial(n)
    return f


def divisores(n):
    n = n
    for i in range(1, n//2+1):
        if n % i == 0:
            yield i
    yield n
    return (list(divisores(n)))


def primo(n):
    for val in range(2,n):
        if n%val == 0:
            return False

    return True


def primos_entre_si(n1, n2):
    for val in range(2, n1 and n2):
        if n1%val == 0 and n2%val ==0:
            return False
    return True


def mdc(n1, n2):
    while (n2 != 0):
        resto = n1%n2
        n1 = n2
        n2 = resto
    return n1


def mmc(n1, n2):
    a = n1
    b = n2

    resto = None
    while resto != 0:
        resto = a % b
        a = b
        b = resto
    return (n1*n2/ a)



def transcreve_numero(telefone):
    return ""


def coincidencia_lista(lista1, lista2):
    lista1 = [1,2,3,4]
    lista2 = [0,2,6,8]

    list_difference = []
    for element in lista1:
        if element not in lista2:
            list_difference.append(element)
    for element in lista2:
        if element not in lista1:
            list_difference.append(element)

    return [list_difference]


# Testes

def checar(a):
    if a:
        return "\u001b[32mPassou!\u001b[0m"
    return "\u001b[31mFalhou!\u001b[0m"


print("Questao 01", checar(maior2(2, 3) == 3))
print("Questao 02", checar(maior5(6, 8, -1, 2, 4) == 8))
print("Questao 03", checar(quantidade_de_vogais("Abc e america") == 6))
print("Questao 04", checar(impar(7)))
print("Questao 05", checar(conta_palavras("Isto é um texto") == 4))
print("Questao 06", checar(intervaloab(2, 7) == [2, 3, 4, 5, 6, 7]))
print("Questao 07", checar(fatorial(4) == 24))
print("Questao 08", checar(divisores(8) == [1, 2, 4, 8]))
print("Questao 09", checar(primo(11)))
print("Questao 10", checar(primos_entre_si(8, 15)))
print("Questao 11", checar(mdc(6, 10) == 2))
print("Questao 12", checar(mmc(6, 10) == 30))
print("Questao 13", checar(transcreve_numero("12") == ["um", "dois"]))
print("Questao 14", checar(coincidencia_lista([1, 2, 3, 4], [0, 2, 6, 8]) == 1))