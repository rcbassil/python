#!/usr/bin/python3
# beauty_soup.py

import re
import requests
import bs4
from urllib.request import urlopen

url = "https://nvd.nist.gov/vuln/detail/CVE-2022-35638"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = bs4.BeautifulSoup(html, "html.parser")

print(soup.get_text())

#print(soup.find("a", {"id": "Cvss3CnaCalculatorAnchor"}))
#print(soup.find("div", {"id": "vulnCvssPanel"}))

print(soup.find_all("span", attrs={"class": "severityDetail"}))

print(soup.body.findAll(string="CVE ID Not Found"))

