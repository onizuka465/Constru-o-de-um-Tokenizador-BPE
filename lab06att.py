from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")

vocab = {
    'l o w </w>': 5,
    'l o w e r </w>': 2,
    'n e w e s t </w>': 6,
    'w i d e s t </w>': 3
}

def get_stats (vocab):
    pairs = {}
    for palavra, frequencia in vocab.items():
        simbolos = palavra.split()
        for i in range(len (simbolos)-1):
            par = (simbolos[i], simbolos[i+1])
            pairs[par] = pairs.get(par, 0) + frequencia
    return pairs
stats = get_stats(vocab)
print(stats)
print("Par ('e','s'):", stats[('e', 's')])

def merge_vocab(pair,v_in):
    v_out = {}
    bigrama = ' '.join(pair)
    merged = ''.join (pair)
    for palavra, frequencia in v_in.items():
        nova_palavra = palavra.replace(bigrama,merged)
        v_out [nova_palavra] = frequencia
    return v_out

# Loop Principal de Treinamento do Tokenizador

for i in range(5):
    stats = get_stats(vocab)
    par_mais_frequente = max(stats, key=lambda x: stats[x])
    print(f"Iteração {i+1} - Par fundido: {par_mais_frequente}")
    vocab = merge_vocab(par_mais_frequente, vocab)
    print("Vocab atualizado:", vocab)
    print()

frase = "Os hiper-parâmetros do transformer são inconstitucionalmente difíceis de ajustar."
tokens = tokenizer.tokenize(frase)
print(tokens)