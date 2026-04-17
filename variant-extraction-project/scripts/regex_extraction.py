import re

# Example
VARIANT_PATTERN = r"[pc]\.\d+[A-Z]>[A-Z]"


def extract_variants(text):
    variants = re.findall(VARIANT_PATTERN, text)
    return variants


if __name__ == "__main__":
    with open("../data/abstracts.txt", "r") as f:
        text = f.read()

    variants = extract_variants(text)

    print("Extracted Variants:")
    print(variants)