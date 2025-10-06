import openpyxl

planilha = openpyxl.load_workbook('Pasta1.xlsx')
pagina_clientes = planilha['Planilha1'] # A variável 'workbook' não existe, substitua por 'planilha'

# Use .iter_rows() para iterar no openpyxl
for linha in pagina_clientes.iter_rows(min_row=1):
    nome = linha[1].value
    print(f"nome do cliente: {nome}")