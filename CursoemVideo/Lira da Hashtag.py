import pandas as pd #Associação de outro nome para a variável
import plotly.express as px
#Uma empresa teve 26% das assinaturas canceladas.
#Passo 1: Importar a base de dados para o Python
#Passo 2: Visualizar essa base de dados
#Entender as informações que você tem disponível
#Descobrir os problemas da vase de dados
#Passo 3: Tratamento de dados
#Passo 4: Parte de análise (Inicial ou Global) - conferir os dados fornecidos pelo gerente sobre os cancelamentos
#Passo 5: Análise detalhada - busca por causas e soluções

tabela = pd.read_csv('telecom_users.csv')
tabela = tabela.drop('Unnamed: 0',axis=1)
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"],errors="coerce")
tabela = tabela.dropna(how="all",axis=1)
tabela = tabela.dropna(how="any",axis=0)

#Quantos cancelaram e quantos não cancelaram
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map('{:.2%}'.format))
#Criar gráfico
#for coluna in tabela.columns:
    grafico = px.histogram(tabela,x=coluna,color="Churn")
    grafico.show()
#Os clientes dos primeiros meses costumam cancelar muito mais
#Casados cancelaram menos
#Contrato mensal cancelaram mais
#Boleto cancelaram mais
print(tabela.info())
print(tabela)





