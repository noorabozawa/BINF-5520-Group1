import sys
import os
sys.path.append(os.path.dirname(__file__))

import json
from pubmed_search import search_pubmed, fetch_abstracts
from preprocessing import preprocess_text
from regex_extraction import extract_variants
from ner_extraction import extract_entities
from llm_extraction import structure_output
from normalization import normalize_variants
from clinvar import query_clinvar
def main():
    ids = search_pubmed("BRCA1 mutation", 20)
    text = fetch_abstracts(ids)

    if not text:
        print("No abstracts retrieved")
        return

    cleaned = preprocess_text(text)

    variants = extract_variants(cleaned)
    genes, diseases = extract_entities(cleaned)
    variants = normalize_variants(variants)
    if not variants or not genes or not diseases:
        print("No complete extraction found")
        return

results = []

for g in genes:
    for v in variants:
        for d in diseases:
            status = query_clinvar(v)

            results.append({
                "gene": g,
                "variant": v,
                "disease": d,
                "clinvar_match": status,
                "relationship": "associated_with"
            })

    with open("../results/extracted_data.json", "w") as f:
        json.dump(results, f, indent=4)


if __name__ == "__main__":
    main()