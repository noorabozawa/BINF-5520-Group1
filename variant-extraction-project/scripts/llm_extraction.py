def structure_output(genes, variants, diseases):
    return [
        {
            "gene": g,
            "variant": v,
            "disease": d,
            "relationship": "associated_with"
        }
        for g in genes for v in variants for d in diseases
    ]