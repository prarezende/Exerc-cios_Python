#importe a biblioteca usada para consultar uma URL
import urllib.request

#importe as funções BeautifulSoup para analisar os dados retornados do site
from bs4 import BeautifulSoup

#especifique o URL
wiki = "https://pt.wikipedia.org/wiki/Lista_de_capitais_do_Brasil"

#Consulte o site e retorne o html para a variável 'page'
page = urllib.request.urlopen(wiki)

#Parse o html na variável 'page' e armazene-o no formato BeautifulSoup
soup = BeautifulSoup(page, 'html5lib')

#Insira a tag <li> e adicione sua classe
list_item = soup.find('li', attrs={'class': 'toclevel-2 tocsection-26'})
#Separe o HTML do texto com o código abaixo
name = list_item.text.strip()
print(name)

'''
import urllib.request
from bs4 import BeautifulSoup

wiki = 'https://pt.wikipedia.org/wiki/Lista_de_capitais_do_Brasil'
page = urllib.request.urlopen(wiki)
soup = BeautifulSoup(page, 'html5lib')
list_item = soup.find('li', attrs={'class': 'toclevel-2 tocsection-26'})
name = list_item.text.strip()
print(name)

Use a função “prettify” para ver a estrutura separada da página HTML
print(soup.prettify())
'''
'''
 Trabalhando com as tags HTML
soup. + Tag HTML: Retorna o conteúdo entre a tag de abertura e de fechamento, incluindo o HTML.
print (soup.title)

soup.<tag>.string: retorna somente a string dentro de cada tag HTML, sem o HTML.
print (soup.title.string)

# devemos usar o método soup.a para retornar os links da página web. Veja como fazer isso:
print(soup.find_all('a'))

# Acima, você pode ver que temos apenas uma saída. Agora, para extrair todos os links usaremosfind_all().

all_links = soup.find_all('a)
for link in all_links:
    print(link.get('href'))
    
'''
