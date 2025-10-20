from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urllib.parse import quote
import openpyxl
from time import sleep

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
wait = WebDriverWait(driver, 30)
sleep(20)

planilha = openpyxl.load_workbook('Pasta1.xlsx')
pagina_clientes = planilha['Planilha1']

def clicar(driver, wait):
    for linha in pagina_clientes.iter_rows(min_row=2, values_only=True):
        nome, telefone, vencimento = linha[1], linha[2], linha[3]
        mensagem = f'Olá, tudo bem? Seu vencimento é no dia {vencimento} agradecemos a compreenção!'
        print(nome, telefone, vencimento)

        try:
            link_mensagem_wats = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
            driver.get(link_mensagem_wats)
            sleep(10)
            seta = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[4]/div/span/div/div/div[1]/div[1]/span')))
            seta.click()
            sleep(10)
        except:
            print(f'Não foi possível mandar msg para {nome}')
            with open('erros.csv', 'a', encoding='utf-8') as arquivo:
                arquivo.write(f'{nome}, {telefone}\n')

clicar(driver, wait)