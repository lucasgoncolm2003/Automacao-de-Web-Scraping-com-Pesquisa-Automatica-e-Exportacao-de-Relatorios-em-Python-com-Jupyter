#!/usr/bin/env python
# coding: utf-8

# In[13]:
# O Selenium é uma ferramenta utilizada para automatização de testes de sistemas
# que permite ao usuário reproduzi-los rapidamente no ambiente real da aplicação, 
# em função da sua integração direta com o navegador.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
navegador = webdriver.Edge(r"Endereço do Executável do Webdriver")
# webdriver.Chrome(): Abertura do Navegador
# navegador = webdriver.Chrome()
# get(): acessa o Link Indicado no Parâmetro
navegador.get("https://www.google.com/")
# ---- Cotação do Dólar
# find_element: encontra um Elemento Web em que faz-se alguma Função
navegador.find_element(By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dólar")
# send_keys: escreve um Determinado Texto através do Forçamento do Teclado
navegador.find_element(By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
# Keys.ENTER: força o teclado a pressionar a Tecla ENTER
cotacao_dolar = navegador.find_element(By.XPATH,
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value") 
# get_attribute: passa o Valor da Cotação mostrado no find_element para a Variável
print(cotacao_dolar)
# ---- Cotação do Euro
navegador.get("https://www.google.com/")
navegador.find_element(By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")
navegador.find_element(By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element(By.XPATH,
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print(cotacao_euro)
# ---- Cotação do Ouro
navegador.get("https://www.melhorcambio.com/ouro-hoje")
cotacao_ouro = navegador.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute("value")
cotacao_ouro = cotacao_ouro.replace(",", ".")
print(cotacao_ouro)
# quit(): Fecha o Navegador
navegador.quit()


# In[14]:
# ---- Importação de Base de Dados de Produtos
import pandas as pd
# read_excel: realiza a Leitura da Planilha de Produtos
tabela = pd.read_excel(r"Endereço da Planilha de Base de Dados")
# display: revela a Tabela no Display
display(tabela)

# In[15]:
# ---- Recálculo do Preço do Produto
# Atualização da Cotação onde a Coluna Moeda é Dólar, Euro ou Ouro
# Substitui a Cotação pelo Valor da Variável das Cotações
tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)
# Atualização do Preço Base Reais (Preço-Base*Cotação)
tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]
# Atualização do Preço Final (Preço-Base*Margem)
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]
# tabela["Preço de Venda"] = tabela["Preço de Venda"].map("R${:.2f}".format)
# display(): Mostra a Tabela no Display
display(tabela)

# In[16]:
# ---- Salvamento dos Novos Preços dos Produtos
tabela.to_excel(r"Endereço de Salvamento da Planilha Nova", index=False)