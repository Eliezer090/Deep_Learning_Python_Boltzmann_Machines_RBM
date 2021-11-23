# Deep Learning Python Boltzmann Machines(RBM)
Tudo sobre as Boltzmann Machines e seu poder para realizar recomendações com base em valores 0 e 1 que são passada para ela. Nessa sessão foi desenvolvido um sistema de recomendação de filmes, onde é passado uma lista de usuários com suas respectivas notas para cada filme:
<p>
  <p>Extrutura da rede neural</p>
  <img src="https://github.com/Eliezer090/Deep_Learning_Python_Boltzmann_Machines_RBM/blob/97a49d4af0dac8a01caf3f6651823d8e7e106ca2/files/Imagens/Captura%20de%20Tela%202021-11-22%20%C3%A0s%2021.07.07.png" width="750" title="Extrutura da rede neural">
  <p>Sobre o print abaixo, precisamos intender 3 coisas antes: <br>
    1- O primeiro array é os nomes dos filmes.<br>
    2- O segundo array é se sobre os usuários, as notas que diferentes pessoas derem para esses filmes.<br>
    3- Se contem o valor 1 quer dizer que o usuário olhou o filme e gostou, se contem o valor 0 ou o usuário nao viu o filme ou nao gostou do mesmo.<br>
  </p>
  <img src="https://github.com/Eliezer090/Deep_Learning_Python_Boltzmann_Machines_RBM/blob/97a49d4af0dac8a01caf3f6651823d8e7e106ca2/files/Imagens/Captura%20de%20Tela%202021-11-22%20%C3%A0s%2021.08.39.png" width="400" title="Código sobre os valores que a rede neural vai usar para aprender">
  <p>Notas que o usuário que queremos prever derem para os filmes: </p>
  <img src="https://github.com/Eliezer090/Deep_Learning_Python_Boltzmann_Machines_RBM/blob/35c4069cc79b55bdcd83db6195703dfdd4cad2ac/files/Imagens/Captura%20de%20Tela%202021-11-22%20%C3%A0s%2021.25.24.png" width="400" title="Notas que o usuário que queremos prever derem para os filmes">
  <p>Resultado: </p>
  <img src="https://github.com/Eliezer090/Deep_Learning_Python_Boltzmann_Machines_RBM/blob/35c4069cc79b55bdcd83db6195703dfdd4cad2ac/files/Imagens/Captura%20de%20Tela%202021-11-22%20%C3%A0s%2021.26.42.png" width="400" title="Resultado">
  <p>
    Mas como o usuário2 tem o filme "O chamado" se ele tem o valor 0 ou a cetegoria de filme que ele gosta nem é essa? <br> 
    Pois com base nos valores que passamos de treinamento para o algoritimo e com base no resultado que o usuario1 recebeu, acaba influenciando para que o usuário2 receba essa recomendação desse filme, da mesma forma que a Netflix faz, recomenda filmes que as vezes nem gostamos tanto assim mas como tem varias pessoas que gostaram acaba influenciando o algoritimo. Este é o caso da Tarefa 14 que temos uma base de dados onde irá influenciar um usuário a receber recomendação de um filme por mais que ele nao tenha valor para esse filme: 
  <p>
    <img src="https://github.com/Eliezer090/Deep_Learning_Python_Boltzmann_Machines_RBM/blob/8ae0738fba7ccd64c859035ac608974764714a11/files/Imagens/Captura%20de%20Tela%202021-11-22%20%C3%A0s%2021.36.22.png"  width="400" title="Tarefa 14"><br>
    <img src="https://github.com/Eliezer090/Deep_Learning_Python_Boltzmann_Machines_RBM/blob/8ae0738fba7ccd64c859035ac608974764714a11/files/Imagens/Captura%20de%20Tela%202021-11-22%20%C3%A0s%2021.36.48.png"  width="400" title="tarefa 14"><br>
        <img src="https://github.com/Eliezer090/Deep_Learning_Python_Boltzmann_Machines_RBM/blob/8ae0738fba7ccd64c859035ac608974764714a11/files/Imagens/Captura%20de%20Tela%202021-11-22%20%C3%A0s%2021.37.28.png"  width="400" title="tarefa 14"><br>
   
</p>

# Conteudo
## Teoria sobre Boltzmann Machines
93. Introdução a Boltzmann Machines<br>
94. Restricted Boltzmann Machines (RBM) - aprendizagem<br>
95. Restricted Boltzmann Machines (RBM) - recomendação<br>
Teste 5: Teoria sobre Boltzmann Machines<br>
96. Referências complementares<br>
## Recomendação de filmes
97. Criação da RBM (Restricted Boltzmann Machine)<br>
98. Recomendação de filmes com RBM<br>
Tarefa 14: RBM x filtragem colaborativa<br>

# Links

[Link do curso](https://www.udemy.com/course/deep-learning-com-python-az-curso-completo/)
