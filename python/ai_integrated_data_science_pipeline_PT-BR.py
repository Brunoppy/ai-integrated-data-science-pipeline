import pandas as pd
import matplotlib.pyplot as plt
from pymongo import MongoClient

# Exemplo: Carregar dados de um S3 (simulado)
print("Carregando dataset...")
dados = pd.DataFrame({
    'vendas': [200, 220, 250, 270, 300],
    'lucro': [50, 60, 70, 65, 80]
})

# Análise básica
print(dados.describe())

# Visualização
plt.plot(dados['vendas'], dados['lucro'], marker='o')
plt.title('Análise de Vendas vs Lucro')
plt.xlabel('Vendas')
plt.ylabel('Lucro')
plt.show()

# Conexão MongoDB (simulada)
client = MongoClient('mongodb://localhost:27017/')
db = client['pipeline_ia']
collection = db['dados_processados']
collection.insert_one({"resumo": dados.describe().to_dict()})
print("Dados inseridos no MongoDB.")
