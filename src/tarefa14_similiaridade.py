from rbm import RBM
import numpy as np


# Instancia a RBM
rbm = RBM(num_visible=6, num_hidden=3)

base = np.array([[0, 1, 1, 1, 0, 1],
                 [1, 1, 0, 1, 1, 1],
                 [0, 1, 0, 1, 0, 1],
                 [0, 1, 1, 1, 0, 1],
                 [1, 1, 0, 1, 0, 1],
                 [1, 1, 0, 1, 1, 1]])
# Nome dos filmes
filmes = ["Freddy x Jason", "O Ultimato Bourne", "Star Trek",
          "Exterminador do Futuro", "Norbit", "Star Wars"]

# Treinar
rbm.train(base, max_epochs=5000)
# Valores do leunardo
leonardo = np.array([[0, 1, 0, 1, 0, 0]])
# Retorna o que deve ser indicado para o usuário
camada_escondida = rbm.run_visible(leonardo)
# Monta uma nova extrutura com base em quais filmes deve apresentar
recomendacao = rbm.run_hidden(camada_escondida)

for i in range(len(leonardo[0])):
    if leonardo[0, i] == 0 and recomendacao[0, i] == 1:
        print(filmes[i])
