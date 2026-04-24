def preprocess_text(text):
    return text.lower()


if __name__ == "__main__":
    with open("../data/abstracts.txt", "r", encoding="utf-8") as f:
        text = f.read()

    cleaned = preprocess_text(text)

    with open("../data/cleaned_abstracts.txt", "w", encoding="utf-8") as f:
        f.write(cleaned)