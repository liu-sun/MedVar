import pprint

import requests

hgvs = "NP_001361433.1:p.Asp512Asn"
# url = f"https://rest.ensembl.org/variant_recoder/human/{hgvs}"
# params = {"content-type": "application/json"}
# response = requests.get(url, params=params)
# print(response.url)
# pprint.pprint(response.json())
# url = f"https://rest.ensembl.org/variation/human/{hgvs}"
# params = {"content-type": "application/json"}
# response = requests.get(url, params=params)
# print(response.url)
# pprint.pprint(response.json())
url = f"https://rest.ensembl.org/vep/human/hgvs/{hgvs}"
params = {"content-type": "application/json"}
response = requests.get(url, params=params)
print(response.url)
pprint.pprint(response.json())