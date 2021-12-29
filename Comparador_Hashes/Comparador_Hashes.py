import  hashlib


arq1 = 'a.txt'
arq2 = 'b.txt'



has1 = hashlib.new('ripemd160')
has2 = hashlib.new('ripemd160')

has1.update(open(arq1,'rb').read())
has2.update(open(arq2,'rb').read())


if has1.digest() != has2.digest():
    print("Arquivos diferentes")
else:
    print("Arquivos compativeis")