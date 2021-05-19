#Pandas é uma biblioteca que já vem pronta, trabalhando com bastante informações
#Sempre que qusier algum código do pandas, usaremos sempre no incio o Pd.
##Deve-se criar uma variável para "receber", ou seja, fazer a leitura 
#DataFrame e como fosse uma tabela com linhas e colunas 
#Ex:
## Quando pega o codigo 'vendas-df['ID Produto'][0], mostra que vai pegar nessa coluna o primeiro valor 
## Quando pega o codigo 'vendas-df['ID Produto'][:0], significa que vai pegar até o valor dessa coluna especifico
#temos o nome.info()--> te dá uma visão geral 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import pandas_datareader.data as web 
from pandas import DataFrame
 


#lendo a carteira.xlsx
carteira = pd.read_excel('Carteira.xlsx')
print(carteira)

#Criando o dataframe de cotações 

cotacoes_carteira=pd.DataFrame()
cotacoes_carteira = cotacoes_carteira

for ativo in carteira['Ativos']:
    cotacoes_carteira[ativo]= web.DataReader('{}.SA'.format(ativo),data_source='yahoo',start='2021-05-18',end='2021-05-18')['Adj Close']

print(cotacoes_carteira)
#devemos preencher esses dados, porém devemos fazer um ajuste, existe a possibilidade de copiar com o valor anterior 
df_media = cotacoes_carteira.mean()
cotacoes_carteira = cotacoes_carteira.fillna(df_media)
#preenchendo os dados no dataframe, usamos o "fillna" que irá preencher os dados vazios, usamos o df_media para preencher esses vazios 
# o ffill preenche com o método anterior
cotacoes_carteira = cotacoes_carteira.ffill()
cotacoes_carteira.info()
print(df_media)
# comparando os valores agora, sabendo que os valores estão em escalas diferentes, devemos normalizar o processo 
#  pegando os valores de cotação, pegando como cotação inicial, o valor inicial
# normalizando significa basicamente é colocar todo mundo na mesma base 
#carteira_norm = cotacoes_carteira / cotacoes_carteira[0]
#carteira_norm.plot(figsize=(15,5))
#plt.show()

#comparando com a b3
cotacoes_b3 = web.DataReader('^BVSP', data_source='yahoo',start='2021-05-18',end='2021-05-18')
print(cotacoes_b3)
valor_investido = pd.DataFrame()
for ativo in carteira['Ativos']:
    valor_investido[ativo] = cotacoes_carteira[ativo] * carteira.loc[carteira['Ativos']=='MGLU3', 'Qtde'].values[0]
print(carteira.loc[carteira['Ativos']==ativo,'Qtde'].values[0])
print(valor_investido)

#cotacoes_carteira.to_csv('cotacoes_carteira.csv',sep=';')