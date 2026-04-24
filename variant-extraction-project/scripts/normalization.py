def normalize_variant(variant):
    if variant.startswith("c.") or variant.startswith("p.") or variant.startswith("rs"):
        return variant
    return "c." + variant


def normalize_variants(variants):
    return [normalize_variant(v) for v in variants]