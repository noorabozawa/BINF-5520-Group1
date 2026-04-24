from Bio import Entrez

Entrez.email = "noorabozawa@gmail.com"

def query_clinvar(variant):
    try:
        handle = Entrez.esearch(
            db="clinvar",
            term=variant,
            retmax=1
        )
        record = Entrez.read(handle)
        handle.close()

        if record["IdList"]:
            return "found"
        else:
            return "not_found"
    except:
        return "error"