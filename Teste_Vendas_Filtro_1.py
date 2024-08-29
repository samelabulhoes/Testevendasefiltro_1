
import pandas as pd

# Dados fornecidos
data = {
    'Cliente': ['A', 'B', 'C', 'D', 'E'],
    'Vendas': [100, 150, 200, 50, 300],
    'Data': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']
}

# Criação do DataFrame
df = pd.DataFrame(data)

# 1. Filtrar os clientes que fizeram vendas acima de 100
df_filtrado = df[df['Vendas'] > 100]

# 2. Calcular a soma total das vendas para esses clientes filtrados
soma_vendas_filtradas = df_filtrado['Vendas'].sum()

print("Clientes com vendas acima de 100:")
print(df_filtrado)
print("\nSoma total das vendas para esses clientes filtrados:")
print(soma_vendas_filtradas)



