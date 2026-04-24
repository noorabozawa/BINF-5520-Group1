import sys
import os
sys.path.append(os.path.dirname(__file__))

import json
from pubmed_search import search_pubmed, fetch_abstracts
from preprocessing import preprocess_text
from regex_extraction import extract_variants
from ner_extraction import extract_entities
from llm_extraction import structure_output


def main():
    ids = search_pubmed("BRCA1 mutation", 20)
    text = fetch_abstracts(ids)

    if not text:
        print("No abstracts retrieved")
        return

    cleaned = preprocess_text(text)

    variants = extract_variants(cleaned)
    genes, diseases = extract_entities(cleaned)

    if not variants or not genes or not diseases:
        print("No complete extraction found")
        return

    results = structure_output(genes, variants, diseases)

    with open("../results/extracted_data.json", "w") as f:
        json.dump(results, f, indent=4)


if __name__ == "__main__":
    main()