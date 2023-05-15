# Lista de funções

def maior2(a, b):
    return 0


def maior5(a, b, c, d, e):
    return 0


def quantidade_de_vogais(s):
    return 0


def impar(n):
    return False


def conta_palavras(texto):
    return 0


def intervaloab(n1, n2):
    return []


def fatorial(n):
    return 0


def divisores(n):
    return []


def primo(n):
    return False


def primos_entre_si(n1, n2):
    return False


def mdc(n1, n2):
    return 0


def mmc(n1, n2):
    return 0


def transcreve_numero(telefone):
    return ""


def coincidencia_lista(lista1, lista2):
    return []


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