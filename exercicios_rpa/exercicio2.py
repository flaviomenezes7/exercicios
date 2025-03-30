"""
1. Automação de Extração de Dados de um Site
Escreva um script em Python que utilize Selenium ou BeautifulSoup para extrair informações de produtos de um site de e-commerce (exemplo: nome do produto, preço e link).

site: https://www.kabum.com.br/computadores/monitores

Desafio extra: Salvar os dados em um arquivo CSV.

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time

chrome_options = Options()
chrome_options.add_argument("--headless")  # Executa o navegador em modo headless (sem interface gráfica)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Configurando o driver automaticamente com o WebDriver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

url = "https://www.kabum.com.br/computadores/monitores"

# Acessando o site
driver.get(url)
time.sleep(5)  # 5seg para aguardar o carregamento da página

# lista para armazenar os dados dos produtos
produtos = []

# Selecionando os elementos que contêm as informações dos produtos
itens = driver.find_elements(By.CLASS_NAME, "productCard")  # coletando os produtos da página pelo class name productCard

for item in itens:
    try:
        # extraindo o nome do produto
        nome = item.find_element(By.CLASS_NAME, "nameCard").text.strip()

        # extraindo o preço do produto
        preco = item.find_element(By.CLASS_NAME, "priceCard").text.strip()

        # extraindo o link do produto
        link = item.find_element(By.TAG_NAME, "a").get_attribute("href")

        # adicionando os dados do produto a lista
        produtos.append([nome, preco, link])
    except Exception as e:
        print(f"Erro ao processar um item: {e}")

# salvando tudo no excel *csv*
with open("produtos.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Nome do Produto", "Preço", "Link"])
    writer.writerows(produtos)

print(" Dados salvos em: 'produtos.csv'.")

driver.quit()