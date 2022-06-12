import xml.etree.ElementTree as ET

import requests

params = {"term": 'TMPRSS6[gene] AND "refseq select"[filter] AND human[organism]',
          "db": "protein", "usehistory": "y"}
url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
response = requests.get(url, params=params)
print(response.url)
print(response.text)
root = ET.fromstring(response.text)
querykey = root.findtext("QueryKey")
webenv = root.findtext("WebEnv")
url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
params = {"db": "protein", "WebEnv": webenv,
          "query_key": querykey, "retmode": "text", "rettype": "gp"}
response = requests.get(url, params=params)
print(response.text)
