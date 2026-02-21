import numpy as np

# 1. Criar um dataset simulado (100 amostras, 5 sensores)
dados = np.arange(500).reshape(100, 5) 

print("--- Dados Originais (Primeiras 5 linhas) ---")
print(dados[:5])

# 2. Calcular a Média e o Desvio Padrão por COLUNA (axis=0)
medias = np.mean(dados, axis=0)
desvios = np.std(dados, axis=0)

print(f"\nMédias por coluna: {medias}")
print(f"Desvios por coluna: {desvios}")

# 3. Aplicar a Normalização Z-Score (BROADCASTING em ação!)
# O NumPy vai subtrair o vetor 'medias' (1x5) de cada linha da matriz 'dados' (100x5)
dados_normalizados = (dados - medias) / desvios #matriz(100x5)-(1x5) (permite broadcast)/(1x5) tbm;

# 4. Verificação de Sucesso
print("\n--- Dados Normalizados (Primeiras 5 linhas) ---")
print(dados_normalizados[:5])

# Prova Real: Após a normalização, a média deve ser ~0 e o desvio padrão ~1
print(f"\nNova média (deve ser 0): {np.mean(dados_normalizados, axis=0).round(4)}")
print(f"Novo desvio (deve ser 1): {np.std(dados_normalizados, axis=0).round(4)}")






