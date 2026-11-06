"""OSINT arac sarmalayicilari.

Orijinaldeki ciktilar/mesajlar korunur. Fark: harici komutlar os.system +
shell yerine subprocess arg listesiyle (shell'siz) calistirilir -> komut
enjeksiyonu engellenir; maltego artik os.chdir ile surec dizinini KALICI
bozmaz, subprocess cwd kullanir.
"""

import os
import subprocess

from ..ui.colors import GREEN, YELLOW, RED, MENU_WHITE, RESET
from ..config import SPIDERFOOT_ADDR, MALTEGO_BIN, URLS


def clear_screen():
    os.system("clear")


def wait_for_enter():
    input(f"\033[1m\033[97m\nAna menuye donmek icin Enter basin...{RESET}")
    clear_screen()


def _open(url):
    subprocess.run(["xdg-open", url])


def sherlock(username):
    clear_screen()
    print(f"{GREEN}[+] Username taramasi baslatiliyor...{RESET}")
    subprocess.run(["bash", "UserFinder.sh"], cwd="UserFinder")


def holehe(email):
    clear_screen()
    print(f"{GREEN}[+] Holehe ile e-posta kontrolu baslatiliyor...{RESET}")
    subprocess.run(["holehe", email])
    wait_for_enter()


def socialscan(target):
    clear_screen()
    print(f"{GREEN}[+] SocialScan ile tarama baslatiliyor...{RESET}")
    subprocess.run(["socialscan", target])
    wait_for_enter()


def blackbird(email):
    clear_screen()
    print(f"{GREEN}[+] BlackBird ile e-posta kontrolu baslatiliyor...{RESET}")
    subprocess.run(["python3", "blackbird.py", "--email", email], cwd="blackbird")
    wait_for_enter()


def ghunt(email):
    clear_screen()
    print(f"{GREEN}[+] GHunt ile Google hesabı analizi baslatiliyor...{RESET}")
    # Orijinalde komut bostu; davranis korundu (yer tutucu).
    wait_for_enter()


def whatsmyname(username):
    clear_screen()
    print(f"{GREEN}[+] WhatsMyName ile username kontrolu baslatiliyor...{RESET}")
    _open(URLS["whatsmyname"])
    wait_for_enter()


def photon(url):
    clear_screen()
    print(f"{GREEN}[+] Photon ile web taramasi baslatiliyor...{RESET}")
    subprocess.run(["photon", "-u", url, "--wayback"])
    wait_for_enter()


def spiderfoot():
    clear_screen()
    print(f"{GREEN}[+] SpiderFoot web arayuzu aciliyor...{RESET}")
    subprocess.run(["spiderfoot", "-l", SPIDERFOOT_ADDR])
    print(f"{GREEN} Tarayiciyla `http://{SPIDERFOOT_ADDR}` acin.{RESET}")
    wait_for_enter()


def shodan():
    clear_screen()
    print(f"{GREEN}[+] Shodan websitesi aciliyor...{RESET}")
    _open(URLS["shodan"])
    wait_for_enter()


def maltego():
    clear_screen()
    print(f"{GREEN}[+] Maltego baslatiliyor...{RESET}")
    # os.chdir yerine cwd: surecin calisma dizini kalici degismez.
    subprocess.run(["./maltego"], cwd=MALTEGO_BIN)
    wait_for_enter()


def face_and_storage():
    clear_screen()
    print(f"{GREEN}[+] PYM (Gorsel tarama) aciliyor...{RESET}")
    for url in URLS["pym"]:
        _open(url)
    wait_for_enter()


def osint_framework():
    clear_screen()
    print(f"{GREEN}[+] OSINT Framework websitesi aciliyor...{RESET}")
    _open(URLS["osint_framework"])
    wait_for_enter()


def waybackmachine(url):
    clear_screen()
    print(f"{GREEN}[+] WaybackMachine ile tarama baslatiliyor...{RESET}")
    _open(f"https://web.archive.org/web/*/{url}")
    wait_for_enter()


def exiftool():
    print(f"\n{YELLOW}Sorgulanacak resmin uzantısını girin:{RESET}")
    file_path = input(f"{RED}>> {RESET}").strip().strip("'").strip('"')

    clear_screen()
    print(f"{GREEN}[+] Analiz başlatılıyor...{RESET}")
    print(f"{MENU_WHITE}Hedef Dosya: {file_path}{RESET}\n")
    print("-" * 60)
    subprocess.run([
        "exiftool",
        "-GPSPosition", "-GPSLatitude", "-GPSLongitude", "-GPSAltitude",
        "-Make", "-Model", "-Software", "-Firmware", "-SerialNumber",
        "-DateTimeOriginal", "-CreateDate", "-OffsetTime",
        "-Artist", "-Creator", "-Author", "-OwnerName",
        "-UserComment", "-ImageDescription",
        file_path,
    ])
    print("-" * 60)
    wait_for_enter()
