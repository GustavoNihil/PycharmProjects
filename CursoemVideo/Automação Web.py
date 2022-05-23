from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

navegador = webdriver.Chrome()
navegador.get("https://www.google.com/")
navegador.find_element(By.XPATH,
                       "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("cotação dolar")
navegador.find_element(By.XPATH,
                       "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(Keys.ENTER)
cotaçãoD = navegador.find_element(By.XPATH,
                       '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print('Cotação Dolar {}'.format(cotaçãoD))
navegador.get("https://www.google.com/")
navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro",Keys.ENTER)
cotaçãoE = navegador.find_element(By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print('Cotação Euro {}'.format(cotaçãoE))
navegador.get('https://dolarhoje.com/ouro-hoje/#:~:text=A%20cota%C3%A7%C3%A3o%20do%20grama%20do,de%20R%24%20321%2C28.')
cotaçãoO = navegador.find_element(By.XPATH,'//*[@id="nacional"]').get_attribute('value')

cotaçãoO = cotaçãoO.replace(',','.')
print('Cotação Ouro {}'.format(cotaçãoO))
navegador.quit()    #fechar o navegador

planilha = pd.read_excel('Produtos.xlsx')


planilha.loc[planilha["Moeda"] == "Dolar","Cotação"] = float(cotaçãoD)
planilha.loc[planilha["Moeda"] == "Euro","Cotação"] = float(cotaçãoE)
planilha.loc[planilha["Moeda"] == "Ouro","Cotação"] = float(cotaçãoO)

planilha['Preço de Compra'] = planilha['Preço Original'] * planilha['Cotação']
planilha['Preço de Venda'] = planilha['Preço de Compra'] * planilha['Margem']

print(planilha)

