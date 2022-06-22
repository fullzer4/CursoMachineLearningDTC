import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_credit = pd.read_csv("./dados/credit_data.csv")
base_credit.tail(10)
#head - tail (primeiros - ultimos)
base_credit.describe()
#retorna
#contagem
#media
#desvio padrao
#minimo (menos)
#25%
#50%
#75%
#maximo (mais)
base_credit[base_credit['income'] >= 69995.685578] #pegar o usuario/s com o valor x (filtro por coluna)

print(np.unique(base_credit['default'], return_counts=True))