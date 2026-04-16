from Bio import Entrez

Entrez.email = "noorabozawa@gmail.com"

QUERY = "BRCA1 mutation"
MAX_RESULTS = 5

def search_pubmed(query, max_results=5):
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    record = Entrez.read(handle)
    return record["IdList"]

if __name__ == "__main__":
    ids = search_pubmed("BRCA1 mutation")
    print(ids)