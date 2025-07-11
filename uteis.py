import matplotlib.pyplot as plt
from numpy.linalg import norm

def plotar_grafico_cotovelo(autovalores):
    # Plota gráfico de autovalores x componentes principais
    plt.figure(figsize=(10, 6))
    plt.bar(range(1, len(autovalores) + 1), autovalores, alpha=0.7, align='center', color='blue', label='Autovalores')
    plt.plot(range(1, len(autovalores) + 1), autovalores, 'ro-', linewidth=2, markersize=6, label='Tendência')
    plt.xlabel('Componentes Principais', fontsize=12)
    plt.ylabel('Autovalores ($\lambda$)', fontsize=12)
    plt.title('Autovalores vs Componentes PCA', fontsize=14)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

def plotar_grafico_variancia_acumulada(autovalores_percentuais):
    # Calcula a variância acumulada
    variancia_acumulada = [sum(autovalores_percentuais[:i+1]) for i in range(len(autovalores_percentuais))]
    # Plota gráfico de variância acumulada
    plt.figure(figsize=(10, 6))
    x = range(1, len(variancia_acumulada) + 1)
    plt.plot(x, variancia_acumulada, marker='o', linestyle='-', color='green', label='Variância Acumulada')
    plt.xlabel('Componentes Principais', fontsize=12)
    plt.ylabel('Variância Acumulada (%)', fontsize=12)
    plt.title('Variância Acumulada dos Autovalores', fontsize=14)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(x)  # Garante que apenas inteiros aparecem no eixo x
    plt.show()

def procurar_num_componentes(percentual_desejado, autovalores_percentuais):
    soma_percentuais = 0
    num_componentes = 0
    while(soma_percentuais < percentual_desejado):
        soma_percentuais += autovalores_percentuais[num_componentes]
        num_componentes += 1
    return num_componentes

# def obter_distancias_intra(ids, projecoes, targets):
#     distancias_intra = []

#     for id_person in ids:
#         images_id = projecoes[id_person==targets]
#         for i in range(len(images_id)):
#             for j in range(i+1, len(images_id)):
#                 distancia = norm(images_id[i] - images_id[j])
#                 distancias_intra.append(distancia)
    
#     return distancias_intra

# def obter_distancias_inter(ids, projecoes, targets):
#     distancias_inter = []
#     for id1 in ids:
#         imagens_id1 = projecoes[targets == id1]
#         for id2 in ids:
#             if id2 <= id1:  # Evitar pares duplicados (ID1 vs ID2 = ID2 vs ID1)
#                 continue
#             imagens_id2 = projecoes[targets == id2]
#             # Compara a primeira imagem de ID1 com a primeira de ID2 
#             distancia = norm(imagens_id1[0] - imagens_id2[0])
#             distancias_inter.append(distancia)
#     return distancias_inter