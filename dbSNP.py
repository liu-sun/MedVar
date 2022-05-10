import xml.etree.ElementTree as ET

import requests

params = {"term": 'TMPRSS6[gene] AND Ser753Pro',
          "db": "snp", "usehistory": "y"}
# esearch
url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
response = requests.get(url, params=params)
print(response.url)
print(response.text)
root = ET.fromstring(response.text)
querykey = root.find("QueryKey").text
webenv = root.find("WebEnv").text
# efetch
url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
params = {"db": "snp", "WebEnv": webenv, "query_key": querykey}
response = requests.get(url, params=params)
print(response.url)
print(response.text)
root = ET.fromstring(response.text)
hgvs = root.find(
    "DocumentSummarySet/DocumentSummary/DOCSUM").text.removeprefix("HGVS=").split("|")[0].split(",")
spdi = root.find("DocumentSummarySet/DocumentSummary/SPDI").text
chrpos = root.find("DocumentSummarySet/DocumentSummary/CHRPOS").text
fxn_class = root.find("DocumentSummarySet/DocumentSummary/FXN_CLASS").text
allele = root.find("DocumentSummarySet/DocumentSummary/ALLELE").text
clinical_significance = root.find(
    "DocumentSummarySet/DocumentSummary/CLINICAL_SIGNIFICANCE").text
snp_class = root.find("DocumentSummarySet/DocumentSummary/SNP_CLASS").text
print(hgvs, spdi, chrpos, fxn_class, allele, clinical_significance, snp_class)
for maf in root.iter("MAF"):
    if maf.find("STUDY").text == "GnomAD" or maf.find("STUDY").text == "GnomAD_exomes":
        print(maf.find("STUDY").text, maf.find("FREQ").text)
