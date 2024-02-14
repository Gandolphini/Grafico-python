import os
import pandas as pd
import plotly.express as px
import numpy as np
import openpyxl

diretorio = 'C:/Users/jhgandolphini/Desktop/dados_ficiticios'

lista_arquivo = [arquivo for arquivo in os.listdir(diretorio) if arquivo.endswith('.xlsx') and not arquivo.startswith('~$')]
tabela_total = pd.DataFrame()

for arquivo in lista_arquivo:
    tabela = pd.read_excel(f'C:/Users/jhgandolphini/Desktop/dados_ficiticios/{arquivo}')
    tabela_total = pd.concat([tabela_total, tabela])

tabela_total["Data"] = pd.to_datetime(tabela_total["Data"], errors="coerce", )
tabela_total = tabela_total[(tabela_total["Aproveitamento"].notnull()) & (tabela_total["Aproveitamento"] != 0)]

grafico = px.bar(tabela_total, x="Data",y="Total de chamados", color="Aproveitamento")

grafico.show()


