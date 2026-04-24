def extract_entities(text):
    genes = set()
    diseases = set()

    gene_keywords = ["brca1", "tp53", "egfr"]
    disease_keywords = ["breast cancer", "lung cancer", "cancer"]

    for g in gene_keywords:
        if g in text:
            genes.add(g.upper())

    for d in disease_keywords:
        if d in text:
            diseases.add(d)

    return list(genes), list(diseases)