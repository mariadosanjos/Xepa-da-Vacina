# Xepa-da-Vacina
Projeto que faz um sorteio de doses remanescentes em uma lista de candidatos.
1. Introdução

Em tempos de pandemia e dificuldade de compra de vacinas por parte do governo, nenhuma
dose pode ser perdida quando um determinado grupo prioritário estiver sendo atendido.
Entretanto, muitos governos permitem que uma parcela da população possa se vacinar antes
da data prevista por meio das doses remanescentes de vacinas, chamadas popularmente de
“xepa”, por sobrarem nos frascos já abertos ao fim dos dias de imunização.
Esta estratégia ajuda a combater o desperdício, já que depois que um frasco de vacina é aberto,
sua validade é reduzida para de 6 a 48 horas dependendo do tipo do imunizante.
Então, consideremos que o Governo do Estado fictício de Bitópolis adotou a estratégia de
cadastrar cidadãos interessados em tomarem as sobras das vacinas. Eles devem se cadastrar,
todos os dias, a partir das 14h, e estarem presentes às 17h (caso seja contemplado) para
tomarem as doses de vacina que, diga-se de passagem, não vai dar para atender a todos da
lista.

Ao final do dia, quando já se sabe a quantidade de doses remanescentes nos frascos abertos,
inicia-se a execução de um algoritmo que vai determinar quais cidadãos serão contemplados.

2. Sorteio da Vacina

A lógica para o sorteio é determinada da seguinte forma: uma pessoa da lista é escolhida
aleatoriamente como o número 1 (pointer) e os demais numerados sequencialmente. Se o
final da lista for alcançado e ainda restarem cidadãos que não foram numerados no início da
lista, a numeração segue de forma contínua até o nome que aparece antes do pointer 

A princípio, deve ser determinado um quantitativo total de vacinas disponíveis q, com q > 0,
de acordo com as doses remanescentes de cada fabricantes. Por exemplo, digamos que
sobraram 3 doses da Pfizer e 3 da AstraZeneca. Logo, teremos um q = 6.

Partindo do pointer e movendo-se no sentido horário da lista, conta-se uma quantidade k de
avanços, previamente definida, e retira-se um candidato para tomar a vacina. O candidato é
anunciado e contemplado com a vacina do fabricante especificado, sendo retirado da lista logo
em seguida. O pointer passa a ser, então, o próximo elemento da sequência. O processo segue
repetidamente até que a quantidade q de vacinas seja atingida. 

##

Vamos considerar um k=4 e q=6. De acordo com a ilustração abaixo, o processo inicia com a
definição de Pedro como pointer. Avançando k pessoas adiante, no sentido horário, o primeiro
a sair é Daniel. Este é removido para tomar a vacina e o pointer é avançado para o elemento
seguinte, Pedro. Seguindo a lógica, avançando 4 elementos, o elemento a ser removido é
Pedro. O pointer é avançado para o elemento seguinte, Amanda, e o processo segue
adiante até que as q doses sejam aplicadas.

![title](img\sorteio.png)