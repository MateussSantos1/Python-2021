print("-=" * 30)
print('              Analisador de triângulos')
print("-=" * 30)
s1 = float(input('Digite o primeiro segmento: '))
s2 = float(input('Digite o segundo seguimento: '))
s3 = float(input('Digite o segundo seguimento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os seguimentos formam sim um triângulo')
else:
    print('Os seguimentos não formam um triângulo!!!')