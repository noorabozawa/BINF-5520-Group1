import spacy

# load biomedical model
nlp = spacy.load("en_core_sci_sm")

text = "The BRCA1 gene has a mutation c.68_69delAG associated with breast cancer."

doc = nlp(text)

# extract named entities
for ent in doc.ents:
    print(ent.text, ent.label_)