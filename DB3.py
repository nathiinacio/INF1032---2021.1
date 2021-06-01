#Importando as bibliotecas 
import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

#Lendo o arquivo de ações 
# Lendo CSV

df = pd.read_csv("",delimiter=";")


#Filtrando uma ação 
#df_acaoqualquer = df[df['sigla_acao']==#"Colocar o ticker aqui"]

#Verificando o tipo do arquivo
#df_acaoqualquer.dtypes

# Mudar o tipo data

#df_acaoqualquer['data_pregao'] = pd.to_datetime(df_acaoqualquer['data_pregao'], format ='%Y-%m-%d')

#df_acaoqualquer.tail()


#Criando novos campos 

#Media Móvel com 5 dias e 21 dias

#df_acaoqualquer['mm5d'] = df_acaoqualquer['preco_fechamento'].rolling(5).mean()
#df_acaoqualquer['mm5d'] = df_acaoqualquer['preco_fechamento'].rolling(21).mean()
