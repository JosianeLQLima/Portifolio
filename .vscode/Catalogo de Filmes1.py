 import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

#Categorias dos filmes: Ação = 1  / Comédia = 0 / Ficção = 1 / Drama = 0 / Romance = 1

#Catálogo de filmes
filmes = {
    "Matrix": [1, 0, 1, 0, 1],
    "O Senhor dos Anéis": [1, 0, 1, 0, 0],
    "Interestelar": [0, 0, 1, 1, 1],
    "Titanic": [0, 0, 0, 1, 1],
    "A Vida é Bela": [0, 0, 0, 1, 0],
    "Vingadores": [1, 0, 1, 0, 0],
    "Gravidade": [1, 0, 1, 0, 0]
}

#Transformar o catálogo em duas listas, Uma com os nomes e outra com os vetores numericos.
nomes = list(filmes.keys())
vetores = np.array(list(filmes.values()))

#Mostrar os fimes disponiveis
print("Filmes disponíveis:")
for filmes in nomes:
    print("-", filmes)

#O usuario escolhe um filme
usuario = input("\nEscolha um filme da lista: ")

#Verifica se o filme está no catálogo
if usuario not in filmes:
    print("Filme não encontrado no catálogo.")
else:
    #Obter o vetor do filme escolido
    vetor_usuario = np.array(filmes[usuario]).reshape(1, -1)
    #Calcula a similaridade de conseno entre o filme escolhido e todos os outros filmes
    similaridades = cosine_similarity(vetor_usuario, vetores)[0]
    #criar uma lista de tuplas (nome do filme, similaridade)
    listas_resultados = list(zip(nomes, similaridades))
    #ordena a lista pela similaridade em ordem decrescente
    resultados = sorted(listas_resultados, key=lambda x: x[1], reverse=True)
    #Exibir os filmes mais similares
    print(f"\nFilmes similares a {usuario}:\n")
    for nomes, score in resultados:
        if nomes != usuario:
            print(f"{nomes} - Similaridade: {score: .2f}")