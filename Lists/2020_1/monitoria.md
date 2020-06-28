# 4 

Tentar sempre definir bem as coisas básicas: o espaço amostral, os eventos, etc. 

Ideia: Criar uma variável indicadora da existencia de uma cobra na imagem.

O que queremos encontrar é a probabilidade estar na imagem dado que o algoritmo disse que ela está lá. Então temos que pegar a informação de temos do alpha i e aplicar bayers. 

POdemos assumir que a cobra pode estar com probabilidade igual em cada uma das imagens (1/3) e que não há falsos positivos. 



# 8 

Definir uma variável auxiliar para ser usada no cálculo da esperança

Quero saber E[N_k]. No entanto, podemos definir uma outra variável aleatória Y que mostra quando que a 1a coroa ocorre. A intuição 

Y: mostra onde ocorreu a primeira coroa (geométria em coroa)

Y segue uma distribuição geométrica, onde o evento de interesse é sair uma coroa. Essa distribuição tem parametro 1 - p.

Sabemos da distribuição geométrica que ela segue uma probabilidade  p^{k-1}(1-p)

