
def structure_output(genes, variants, diseases):
    """
    Combine extracted components into structured output
    """

    results = []

    for gene in genes:
        for variant in variants:
            for disease in diseases:
                result = {
                    "gene": gene,
                    "variant": variant,
                    "disease": disease,
                    "relationship": "associated_with"
                }
                results.append(result)

    return results


if __name__ == "__main__":
    genes = ["BRCA1"]
    variants = ["c.68_69delAG"]
    diseases = ["breast cancer"]

    output = structure_output(genes, variants, diseases)

    print("Structured Output:")
    for item in output:
        print(item)