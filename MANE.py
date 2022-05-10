import xml.etree.ElementTree as ET

import requests

# https://www.ncbi.nlm.nih.gov/refseq/MANE/
# https://www.ncbi.nlm.nih.gov/refseq/refseq_select/
params = {"term": 'TMPRSS6[gene] AND "refseq select"[filter] AND human[organism]',
          "db": "protein", "usehistory": "y"}
# esearch
url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
response = requests.get(url, params=params)
print(response.url)
print(response.text)
root = ET.fromstring(response.text)
querykey = root.find("QueryKey").text
webenv = root.find("WebEnv").text
# efetch
url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
params = {"db": "protein", "WebEnv": webenv,
          "query_key": querykey, "retmode": "text", "rettype": "gp"}
response = requests.get(url, params=params)
print(response.text)
"""
import xml.etree.ElementTree as ET

import requests

# https://www.ncbi.nlm.nih.gov/refseq/MANE/
# https://www.ncbi.nlm.nih.gov/refseq/refseq_select/
params = {"term": 'TMPRSS6[gene] AND "refseq select"[filter] AND human[organism]',
          "db": "nucleotide", "usehistory": "y"}
# esearch
url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
response = requests.get(url, params=params)
print(response.url)
print(response.text)
root = ET.fromstring(response.text)
querykey = root.find("QueryKey").text
webenv = root.find("WebEnv").text
# efetch
url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
params = {"db": "nucleotide", "WebEnv": webenv,
          "query_key": querykey, "retmode": "text", "rettype": "gb"}
response = requests.get(url, params=params)
print(response.text)

"""
