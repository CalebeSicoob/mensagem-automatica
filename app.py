import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui

webbrowser.open('https://web.whatsapp.com/')
sleep(30)

planilha = openpyxl.load_workbook('Pasta1.xlsx')
pagina_clientes = planilha['Planilha1'] # A variável 'workbook' não existe, substitua por 'planilha'

# Use .iter_rows() para iterar no openpyxl
for linha in pagina_clientes.iter_rows(min_row=1):
    nome = linha[1].value
    telefone = linha[2].value
    vencimento = linha[3].value
    mensagem = f'Olá, tudo bem?'
    print(nome, telefone, vencimento)
   
    try:  
        link_mensagem_wats = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
        webbrowser.open(link_mensagem_wats)
        sleep(10)                  
        seta = pyautogui.locateCenterOnScreen('seta.png')
        sleep(15)
        pyautogui.click(seta)
        sleep(10)
    except:
        print(f'Não foi posssivel mandar msg para {nome}')
        with open ('erros.csv', 'a', newline='', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome}, {telefone}')
  

