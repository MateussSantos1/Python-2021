'''lista1 = [0,1]
lista2 = [0,2]

list_difference = []
for element in lista1:
    if element not in lista2:
        list_difference.append(element)

print(list_difference)
n = 200
def divisores(n):
    print([i for i in range(1, n//2+1) if n%i==0])'''

def divisores(num):
    for i in range(1, num//2+1):
        if num % i == 0:
            yield i
    yield num

num = 8


print(list(divisores(num)))


'''def verifivogal(c):
    vogais = 'aeiouAEIOU'
    result = 0
    for char in c:
        if char in vogais:
            result = result + 1
             print(resul'''
