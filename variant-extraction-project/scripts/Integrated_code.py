# integrated_code.py

from preprocessing import preprocess_text
from ner_extraction import extract_entities
from regex_extraction import extract_variants
from llm_extraction import structure_output

import json


def main():
    text = "The BRCA1 gene has a mutation c.68_69delAG associated with breast cancer."

    # 1. Preprocessing
    cleaned_text = preprocess_text(text)

    # 2. NER
    genes, diseases = extract_entities(cleaned_text)

    # 3. Regex
    variants = extract_variants(cleaned_text)

    # 4. Structure output
    results = structure_output(genes, variants, diseases)

    # 5. Save to JSON
    with open("../results/extracted_data.json", "w") as file:
        json.dump(results, file, indent=4)

    print("✅ Results saved to results/extracted_data.json")


if __name__ == "__main__":
    main()