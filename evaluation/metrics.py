def calcular_metrica(resultados, relevantes):
    resultados_set = set(resultados)
    relevantes_set = set(relevantes)
    
    verdadeiros_positivos = len(resultados_set & relevantes_set)
    precisao = verdadeiros_positivos / len(resultados) if resultados else 0
    revocacao = verdadeiros_positivos / len(relevantes) if relevantes else 0
    f1 = (2 * precisao * revocacao) / (precisao + revocacao) if (precisao + revocacao) > 0 else 0

    return precisao, revocacao, f1
