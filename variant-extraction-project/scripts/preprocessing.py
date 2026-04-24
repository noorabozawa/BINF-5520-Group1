import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-z0-9.\-\s]", "", text)

    return text


if __name__ == "__main__":
    with open("../data/abstracts.txt", "r") as f:
        raw_text = f.read()
    cleaned_text = clean_text(raw_text)
    with open("../data/cleaned_abstracts.txt", "w") as f:
        f.write(cleaned_text)

    print("Preprocessing complete. Cleaned file saved.")

def preprocess_text(text):
    return text.lower()