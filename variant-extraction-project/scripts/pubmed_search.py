from Bio import Entrez

Entrez.email = "noorabozawa@gmail.com"

QUERY = "BRCA1 mutation"
MAX_RESULTS = 30


def search_pubmed(query, max_results=5):
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results, mindate="2021", maxdate="2026", datetype="pdat")
    record = Entrez.read(handle)
    return record["IdList"]


def fetch_abstracts(id_list):
    handle = Entrez.efetch(db="pubmed", id=id_list, rettype="abstract", retmode="text")
    abstracts = handle.read()
    return abstracts


if __name__ == "__main__":
    ids = search_pubmed(QUERY, MAX_RESULTS)
    print("PubMed IDs:", ids)

    abstracts = fetch_abstracts(ids)
    print("\nAbstracts:\n")
    print(abstracts)


    with open("../data/abstracts.txt", "w") as f:
        f.write(abstracts)