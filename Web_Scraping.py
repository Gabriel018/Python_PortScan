import requests
from bs4 import BeautifulSoup



site = requests.get('https://www.climatempo.com.br/previsao-do-tempo/agora/cidade/321/riodejaneiro-rj').content

requisicao = BeautifulSoup(site,'html.parser')
#print(requisicao.prettify())

titulo = requisicao.find("p", class_="title")


print(titulo.string)
print(requisicao.p)
