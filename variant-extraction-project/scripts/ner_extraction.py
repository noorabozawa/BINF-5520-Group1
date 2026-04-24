# ner_extraction.py

import spacy
import json

# Load model once
nlp = spacy.load("en_core_sci_sm")


def extract_entities(text):
    """
    Extract genes and diseases from text
    """
    doc = nlp(text)

    genes = []
    diseases = []

    for ent in doc.ents:
        entity_text = ent.text

        # simple rules (can improve later)
        if "BRCA" in entity_text:
            genes.append(entity_text)

        if "cancer" in entity_text:
            diseases.append(entity_text)

    return genes, diseases


# 🔹 Run independently (optional)
if __name__ == "__main__":
    input_path = "../data/abstracts.txt"
    output_path = "../results/ner_entities.json"

    # Read file
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Extract
    genes, diseases = extract_entities(text)

    # Structure results
    results = {
        "genes": genes,
        "diseases": diseases
    }

    # Save JSON
    with open(output_path, "w") as f:
        json.dump(results, f, indent=4)

    print("✅ NER results saved to results/ner_entities.json")