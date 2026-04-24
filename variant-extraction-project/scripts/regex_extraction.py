import re

VARIANT_PATTERN = r"(c\.\d+[_\d]*[a-z]*|p\.[a-z]\d+[a-z]|rs\d+)"

def extract_variants(text):
    variants = re.findall(VARIANT_PATTERN, text)

    if not variants:
        if "mutation" in text:
            variants.append("mutation")

    return list(set(variants))