def extract_entities(text):
    genes = set()
    diseases = set()

    if "brca1" in text:
        genes.add("BRCA1")

    if "breast cancer" in text:
        diseases.add("breast cancer")
    elif "cancer" in text:
        diseases.add("cancer")

    return list(genes), list(diseases)