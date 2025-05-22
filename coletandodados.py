#Requisição do HTML

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://books.toscrape.com/'
response = requests.get(url)

todos_livros = []  # Initialize the list

#status códigos de HTTP:

#200 → ✅ Sucesso! A página foi encontrada e o conteúdo foi entregue.
#301 → 🔁 Redirecionamento.
#403 → ⛔ Proibido (o site bloqueou a requisição).
#404 → ❌ Não encontrado (a página não existe).
#500 → ⚠️ Erro interno do servidor.

if response.status_code == 200: 
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.prettify()) #mostrando html formatado
    
    #Extraindo informações

    livros = soup.find_all('article', class_='product_pod')
    
    for livro in livros:
        titulo = livro.h3.a['title']
        preco = livro.find('p', class_='price_color').text
        todos_livros.append({'titulo': titulo, 'preco': preco})

    #criando dataframe

    df = pd.DataFrame(todos_livros)
    try:
        df.to_csv('livros.csv', index=False)
        print("Dados salvos em livros.csv")
    except Exception as e:
        print(f"Falha ao salvar dados em livros.csv: {e}")
else:
    print(f"Falha ao acessar a página. Código de status: {response.status_code}")

