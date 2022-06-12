import requests

params = {"hgvs": "NP_001361433.1:p.Asp512Asn"}
url = f"https://reg.genome.network/allele"
r = requests.get(url, params=params)
print(r.url)
print(r.text)
