"""Merkezi yapilandirma: adresler ve harici arac yollari."""

import os

# SpiderFoot web arayuzu adresi
SPIDERFOOT_ADDR = "127.0.0.1:5001"

# Maltego kurulum dizini (kendine gore degistir)
MALTEGO_BIN = os.path.expanduser("~/Downloads/maltego_4.10.0/bin")

# xdg-open ile acilacak adresler
URLS = {
    "whatsmyname": "https://whatsmyname.app/",
    "shodan": "https://www.shodan.io",
    "osint_framework": "https://osintframework.com/",
    "pym": [
        "https://pimeyes.com/",
        "https://yandex.com/images/",
        "https://mega.io/",
    ],
}
