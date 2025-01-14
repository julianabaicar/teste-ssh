# Contém a função principal e coordena a execução do programa.

from assinatura import le_assinatura, le_textos
from processamento import separa_sentencas, separa_frases, separa_palavras, n_palavras_unicas, n_palavras_diferentes, compara_assinatura

def main():
    assinatura_infectado = le_assinatura()
    textos = le_textos()

    for i, texto in enumerate(textos):
        sentencas = separa_sentencas(texto)
        frases = [frase for sentenca in sentencas for frase in separa_frases(sentenca)]
        palavras = [palavra for frase in frases for palavra in separa_palavras(frase)]

        tamanho_medio_palavra = sum(len(palavra) for palavra in palavras) / len(palavras)
        type_token_ratio = n_palavras_diferentes(palavras) / len(palavras)
        hapax_legomana_ratio = n_palavras_unicas(palavras) / len(palavras)
        tamanho_medio_sentenca = sum(len(sentenca) for sentenca in sentencas) / len(sentencas)
        complexidade_sentenca = len(frases) / len(sentencas)
        tamanho_medio_frase = sum(len(frase) for frase in frases) / len(frases)

        assinatura_texto = [tamanho_medio_palavra, type_token_ratio, hapax_legomana_ratio, tamanho_medio_sentenca, complexidade_sentenca, tamanho_medio_frase]

        grau_similaridade = compara_assinatura(assinatura_texto, assinatura_infectado)
        print(f"Grau de similaridade do texto {i + 1}: {grau_similaridade}")

if __name__ == "__main__":
    main()