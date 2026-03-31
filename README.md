# Constru-o-de-um-Tokenizador-BPE
Resolução de atividade facultativa.

Para o código rodar devidamente, deve se ter a biblioteca dos Transformers instalado, e um programa tenha Python 3.0 ou uma versão mais recente.
O código teve partes feitas com auxilio da I.A Claude, onde utilizei ela para as sintaxes nos codigos, principalmente na construção das funções do get_stats o merge_vocab e na construção da lógica utilizada. Revisadas por mim (Guilherme De Assis Rodrigues Bomfim)

O sinal ## nos tokens indica que aquele fragmento é uma continuação 
da palavra anterior, não o início de uma nova palavra. Por exemplo, 
"inconstitucionalmente" é quebrada em 'in', '##cons', '##tit', 
'##uc', '##ional', '##mente' — onde 'in' é o início e os demais 
fragmentos são continuações.

O uso de sub-palavras evita o travamento do modelo diante de palavras 
desconhecidas porque palavras novas são decompostas em fragmentos 
menores já conhecidos pelo vocabulário. Em vez de aprender cada palavra 
do zero, o modelo reutiliza pedaços que já conhece como base, mantendo 
o vocabulário otimizado sem perder a capacidade de representar palavras 
raras ou novas.

