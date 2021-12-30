import itertools

palavra  = input("Digite a palavra a ser permutada")

result = itertools.permutations(palavra,3)

for i in result:
    print(''.join(i))