# Arquivo rbm.py
from rbm import RBM
import numpy as np

rbm = RBM(num_visible=6, num_hidden=2)
'''
num_visible = Numero de entradas
num_hidden = NUmero de neuronios na camada escondida
'''

filmes = ['A bruxa', 'Invocação do mal', 'O chamado',
          'Se beber não case', 'Gente Grande', 'American pie']

''' 
Criando a base, valores que os usuarios derem para cada filme
3 primeiros valores sao de filmes de terror
3 ultimos sao de comédia
'''
base = np.array([[1, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0],
                 [1, 1, 1, 0, 0, 0],
                 [0, 0, 1, 1, 1, 1],
                 [0, 0, 0, 1, 1, 1],
                 [0, 0, 1, 1, 0, 1],
                 [0, 0, 0, 1, 0, 1],
                 [0, 0, 0, 1, 1, 1],
                 [1, 1, 0, 0, 0, 0],
                 [0, 0, 0, 1, 1, 1]])
'''
1 - olhou e gostou do filme
0 - olhou mas não gostou do filme
vazio - nao temos pq o RBM nao perite ali :(
'''

# Treinar a rede neural
rbm.train(base, max_epochs=5000)
'''
Primiero parametro é a base
max_epochs = Qnt de épocas que vamos treinar
'''
# Visualizar os pesos
rbm.weights
'''
1º coluna e 1º linha é para a unidade de baies
cada uma das linhas a partir da segunda equivale a um filme

##Colunas##
2º coluna é o 1º neuronio
3º coluna é o 2º neuroronio

Iremos considerar os valores positivos maiores que o outro neurônio

obs: Neurônio numero 2 ta se tornando em detectar filmes de terror, já o 1º em comédia
    nao estamos indicando nada do filme só os valores isso é algo muito legal pois a rede neural que está adivinhano o que é o que.

'''

# Usuario que a rede vai prever qual filme indicar para ele.
usuario1 = np.array([[1, 1, 0, 1, 0, 0]])
usuario2 = np.array([[0, 0, 0, 1, 1, 0]])
# Executa e retorna 0 e 1 e diz quais filme deve indicar para o usuário.
usr1 = rbm.run_visible(usuario1)
'''
Retorno: array([[0., 1.]])
Conclusão: deve indicar filme de terror para esse usuario1
'''

usr2 = rbm.run_visible(usuario2)
'''
Retorno: array([[1., 0.]])
Conclusão: deve indicar filme de comedia para esse usuario2
'''

##### Recomendação #######
'''
User 1
'''
camada_escondida = np.array(usr1)
recomendacao = rbm.run_hidden(camada_escondida)
'''
obs: O retorno pode variar...
usr1_notas: [1, 1, 0, 1, 0, 0]
retorno_rec:[1, 1, 1, 0, 0, 0]
Deve ser recomendado o 3 filme para esse usuário, os outros não
'''

# Recomendação para o usuario1
for i in range(len(usuario1[0])):
    # print(usuario1[0,i])
    # Percorre o usuario se mudou o valor remenda
    if usuario1[0, i] == 0 and recomendacao[0, i] == 1:
        print(f'Filmes usuario1: {filmes[i]}')

# User 2
camada_escondida = np.array(usr2)
recomendacao = rbm.run_hidden(camada_escondida)
'''
obs: O retorno pode variar...
usuario = [0, 0, 0, 1, 1, 0]
Retorno = [0, 0, 0, 1, 1, 1]
Deve ser recomendado o sexto filme para esse usuário
'''
# Recomendação Usuario2
for i in range(len(usuario2[0])):
    # print(usuario1[0,i])
    # Percorre o usuario se mudou o valor remenda
    if usuario2[0, i] == 0 and recomendacao[0, i] == 1:
        print(f'Filmes usuario2: {filmes[i]}')
