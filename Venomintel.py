#!/usr/bin/env python3
import os
import sys
import subprocess
import itertools
import time
import json
import urllib.request
from time import sleep

GREEN = "\033[97m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RED = "\033[91m"
BOLD = "\033[1m"
WHITE = "\033[97m"
RESET = "\033[0m"
MENU_WHITE = WHITE + BOLD
MATRIX = GREEN + BOLD

_SILENT_AUTO_UPDATE_PACKAGES = {

}

def _normalize_ver_silent(v):
    if not v:
        return ()
    parts = []
    for p in v.split("."):
        num = ''.join(ch for ch in p if ch.isdigit())
        try:
            parts.append(int(num) if num else 0)
        except:
            parts.append(0)
    return tuple(parts)

def _is_newer_silent(latest, current):
    if latest is None:
        return False
    if current is None:
        return True
    return _normalize_ver_silent(latest) > _normalize_ver_silent(current)

def _get_installed_version_pip_silent(pkg_name):
    try:
        proc = subprocess.run([sys.executable, "-m", "pip", "show", pkg_name],
                              stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, check=False)
        if proc.returncode != 0 or not proc.stdout:
            return None
        for line in proc.stdout.splitlines():
            if line.startswith("Version:"):
                return line.split(":", 1)[1].strip()
    except Exception:
        return None
    return None

def _get_latest_pypi_version_silent(pkg_name, timeout=4):
    url = f"https://pypi.org/pypi/{pkg_name}/json"
    try:
        with urllib.request.urlopen(url, timeout=timeout) as resp:
            if resp.status != 200:
                return None
            data = json.load(resp)
            return data.get("info", {}).get("version")
    except Exception:
        return None

def _perform_update_silent(pkg_name):
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", pkg_name],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    except Exception:
        pass

def silent_auto_update():
    try:
        for _, pkg in _SILENT_AUTO_UPDATE_PACKAGES.items():
            try:
                local = _get_installed_version_pip_silent(pkg)
                latest = _get_latest_pypi_version_silent(pkg)
                if _is_newer_silent(latest, local):
                    _perform_update_silent(pkg)
                time.sleep(0.08)
            except Exception:
                continue
    except Exception:
        pass

def show_banner():
    os.system("clear")
    print(f"""{RED}{BOLD}
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣶⣶⣶⣶⣶⣶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⢰⣿⣿⣿⣿⣿⣿⣿⣿⠿⢃⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⡈⠻⢿⣿⠿⣿⣿⣿⠇⣴⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣶⡆⠀⠀⠀⠀⠉⠀⢿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠙⢛⣉⣍⡛⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣄⣉⠛⣛⡉⠁⠀⠀⣀⣤⣶⣦⣤⣀⣶⠄⣿⣿⣿⣿⣾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⠇⠀⠀⣸⠛⠉⠉⠙⣿⣿⣿⡆⢿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⠟⠀⠀⠀⠁⠀⠀⠀⠀⢸⣿⣿⣿⣮⡻⢿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⢋⣩⣭⣉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⣠⣶⡾⣿⣟⠛⣋⠁⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠛⣩⣤⣶⣤⣄⡀⠀⢀⣼⣿⠟⠁⣩⣿⣿⢿⣿⡿⣽⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⢧⣾⣿⣿⣿⣿⣿⣿⡄⠻⠿⠁⢠⣾⣿⠟⣡⣾⣿⠛⢮⡛⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⢳⣾⣶⡄⠀⠈⢿⢸⣿⣿⣿⡟⣩⣶⣿⣿⣿⣷⣄⢿⡿⢫⣾⣿⣿⠏⣠⣼⡿⠾⣻⣽⣤⣶⡶⣦⣄⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣤⣴⣾⡿⠃⠈⠛⢿⣦⣀⣈⠈⢿⣿⡏⣼⣿⣿⣿⣿⣿⠿⣛⣂⣀⡛⢿⠟⣡⣾⣿⡿⢁⣾⣿⣿⣿⣿⡷⢹⣿⣿⣿⣿⣿⣿⡷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣾⣼⡿⠋⠉⠀⠀⠀⠀⠀⠹⢿⣼⢧⡈⠻⠀⣿⣿⣿⣿⢋⣴⣿⣿⣿⣿⣿⣷⣄⢿⡟⠋⠀⣾⣿⣿⡿⠉⠩⠷⠿⣿⣿⣿⣿⡿⣫⣶⣷⣄⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⠋⠀⢠⣶⣶⣶⣾⣿⣿⣿⣿⣷⡄⣶⣶⣆⣿⣿⣿⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⠁⣀⣤⣶⣜⢿⠁⢸⣷⡄⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣧⣄⠀⠀
⠀⠀⠀⠀⣿⡇⠀⢰⣯⣿⠉⠉⢩⣍⣉⣉⣭⣭⣥⣭⣍⣻⣥⣭⣭⣜⠿⣿⣿⣿⣿⣿⣿⣿⠿⢓⠸⢿⣿⣿⡟⠀⠀⠀⢻⣧⣀⡀⠀⠈⠐⣿⣿⣿⣿⣿⣿⣿⣿⡄
⠀⠀⢀⣼⠿⠁⠀⢸⣿⡇⠀⢸⣿⠿⠟⠿⠿⠿⠿⢿⣿⣟⠛⠛⣻⣥⣴⣶⣄⠉⠛⠿⠟⢱⣿⣿⣿⡄⣀⠈⠀⠀⠀⠀⠈⠉⠛⠁⠀⠀⠀⣹⣿⣿⣿⣿⣿⣿⣿⡇
⣠⡴⠟⠛⠁⠀⠀⢸⣿⡇⠀⣿⣿⠀⠀⢠⣼⣻⣿⣿⣿⣿⣿⣿⠾⣿⠿⠛⠁⣀⣴⣿⣷⠈⣛⠻⠟⠁⣿⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃
⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⢿⣿⡇⢀⣾⣿⡃⠉⠙⠛⠋⠁⠀⠀⠀⠀⠀⣟⡛⠻⣿⡁⠀⣿⣇⠀⠀⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡿⠟⠿⠁⠀⢤⣤⣶⠆
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠇⢸⣿⡇⠸⣿⣿⡇⠀⠀⠀⣤⠾⠻⣿⣿⣶⣿⣿⣿⣦⠻⠃⠀⠈⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠇⠀⠀⠀⢠⣼⣿⡿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠃⢸⣶⠁⢐⡿⠏⠀⠀⠀⢠⣶⣿⣷⠘⠿⠿⠿⠿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠋⠀⠀⠀⠀⣀⣼⣿⡿⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠜⠉⠀⠀⠀⢻⣧⠘⣿⣦⠀⠀⢠⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⢀⣿⣿⠟⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡏⠀⠘⣿⣧⠀⣾⣿⣿⣿⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠛⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠟⠀⠀⠀⣼⣿⠆⣿⣿⣿⣿⣿⢿⣿⣥⣴⣶⣶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠋⠀⢹⣿⣿⡟⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣠⣤⣤⣤⣤⣶⣦⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠈⣿⣿⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⠎⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣋⡉⠉⠛⠉⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⣿⣿⣿⣿⣿⠟⠉⢼⣿⣿⣦⣆⢀⣠⣴⣦⣤⡴⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠙⠛⠿⠿⠿⠿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

:::      .::..,:::::::::.    :::.    ...     .        :   ::::::.    :::.::::::::::::.,::::::   :::     
';;,   ,;;;' ;;;;''''`;;;;,  `;;; .;;;;;;;.  ;;,.    ;;;  ;;;`;;;;,  `;;;;;;;;;;;'''';;;;''''   ;;;     
 \[[  .[[/    [[cccc   [[[[[. '[[,[[     \[[,[[[[, ,[[[[, [[[  [[[[[. '[[     [[      [[cccc    [[[     
  Y$c.$$'     $$''''   $$$ 'Y$c$$$$$,     $$$$$$$$$$$'$$$ $$$  $$$ 'Y$c$$     $$      $$''''    $$'     
   Y88P       888oo,__ 888    Y88'888,_ _,88P888 Y88' 888o888  888    Y88     88,     888oo,__ o88oo,.__
    MP        ''''YUMMMMMM     YM  'YMMMMMP' MMM  M'  'MMMMMM  MMM     YM     MMM     'YUMMM'' '''YUMMM

{RESET}""")

def loading_animation_with_update():
    os.system("clear")
    spinner = itertools.cycle(["|", "/", "-", "\\"])
    print(f"{MENU_WHITE}Sistem aciliyor ", end="", flush=True)

    updates_done = False
    for _ in range(40):  
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.15)
        sys.stdout.write("\b")

        if not updates_done:
            try:
                silent_auto_update()
            except Exception:
                pass
            updates_done = True

    print(f" {GREEN}Hosgeldiniz{RESET}\n")
    sleep(1)
    os.system("clear")

def clear_screen():
    os.system("clear")

def wait_for_enter():
    input(f"\033[1m\033[97m\nAna menuye donmek icin Enter basin...{RESET}")
    clear_screen()

def sherlok(username):
    clear_screen()
    print(f"{GREEN}[+] Username taramasi baslatiliyor...{RESET}")
    os.system(f"cd UserFinder && bash UserFinder.sh")

def holehe(email):
    clear_screen()
    print(f"{GREEN}[+] Holehe ile e-posta kontrolu baslatiliyor...{RESET}")
    os.system(f"holehe {email}")
    wait_for_enter()

def socialscan(target):
    clear_screen()
    print(f"{GREEN}[+] SocialScan ile tarama baslatiliyor...{RESET}")
    os.system(f"socialscan {target}")
    wait_for_enter()

def blackbird(email):
    clear_screen()
    print(f"{GREEN}[+] BlackBird ile e-posta kontrolu baslatiliyor...{RESET}")
    os.system(f"cd blackbird&& python3 blackbird.py --email \"{email}\"")
    wait_for_enter()

def ghunt(email):
    clear_screen()
    print(f"{GREEN}[+] GHunt ile Google hesabı analizi baslatiliyor...{RESET}")
    os.system(f"")
    wait_for_enter()

def whatsmyname(username):
    clear_screen()
    print(f"{GREEN}[+] WhatsMyName ile username kontrolu baslatiliyor...{RESET}")
    subprocess.run(["xdg-open", "https://whatsmyname.app/"])
    wait_for_enter()

def photon(url):
    clear_screen()
    print(f"{GREEN}[+] Photon ile web taramasi baslatiliyor...{RESET}")
    os.system(f"photon -u {url} --wayback")
    wait_for_enter()

def spiderfoot():
    clear_screen()
    print(f"{GREEN}[+] SpiderFoot web arayuzu aciliyor...{RESET}")
    os.system("spiderfoot -l 127.0.0.1:5001")
    print(f"{GREEN} Tarayiciyla `http://127.0.0.1:5001` acin.{RESET}")
    wait_for_enter()

def shodan():
    clear_screen()
    print(f"{GREEN}[+] Shodan websitesi aciliyor...{RESET}")
    subprocess.run(["xdg-open", "https://www.shodan.io"])
    wait_for_enter()

def maltego():
    clear_screen()
    print(f"{GREEN}[+] Maltego baslatiliyor...{RESET}")
    os.chdir(os.path.expanduser("~/Downloads/maltego_4.10.0/bin"))
    os.system("./maltego")
    wait_for_enter()
    
def face_and_storage():
    clear_screen()
    print(f"{GREEN}[+] PYM (Gorsel tarama) aciliyor...{RESET}")
    subprocess.run(["xdg-open", "https://pimeyes.com/"])
    subprocess.run(["xdg-open", "https://yandex.com/images/"])
    subprocess.run(["xdg-open", "https://mega.io/"])
    wait_for_enter()

def osint_framework():
    clear_screen()
    print(f"{GREEN}[+] OSINT Framework websitesi aciliyor...{RESET}")
    subprocess.run(["xdg-open", "https://osintframework.com/"])
    wait_for_enter()

def waybackmachine(url):
    clear_screen()
    print(f"{GREEN}[+] WaybackMachine ile tarama baslatiliyor...{RESET}")
    subprocess.run(["xdg-open", f"https://web.archive.org/web/*/{url}"])
    wait_for_enter()

def exiftool():
    print(f"\n{YELLOW}Sorgulanacak resmin uzantısını girin:{RESET}")
    file_path = input(f"{RED}>> {RESET}").strip()
    
    file_path = file_path.strip("'").strip('"')

    clear_screen()
    print(f"{GREEN}[+] Analiz başlatılıyor...{RESET}")
    print(f"{MENU_WHITE}Hedef Dosya: {file_path}{RESET}\n")
    print("-" * 60)
    
    os.system(f'exiftool -GPSPosition -GPSLatitude -GPSLongitude -GPSAltitude -Make -Model -Software -Firmware -SerialNumber -DateTimeOriginal -CreateDate -OffsetTime -Artist -Creator -Author -OwnerName -UserComment -ImageDescription "{file_path}"')
    
    print("-" * 60)
    wait_for_enter()

def menu():
    clear_screen()
    show_banner()
    print(f"{WHITE}1) Username Tarama {RESET}")
    print(f"{WHITE}2) E-posta Kontrol (Holehe){RESET}")
    print(f"{WHITE}3) SocialScan Tarama (S+H){RESET}")
    print(f"{WHITE}4) BlackBird (Email Taraması){RESET}")
    print(f"{WHITE}5) BOS{RESET}")
    print(f"{WHITE}6) WhatsMyName{RESET}")
    print(f"{WHITE}7) Photon Web Tarama{RESET}")
    print(f"{WHITE}8) SpiderFoot Baslat{RESET}")
    print(f"{WHITE}9) Shodan{RESET}")
    print(f"{WHITE}10) Maltego{RESET}")
    print(f"{WHITE}11) PYM{RESET}")
    print(f"{WHITE}12) Exiftool{RESET}")
    print(f"{WHITE}13) WaybackMachine{RESET}")
    print(f"""{WHITE}
• Tikanirsan Osint Framework{RESET}""")
    print(f"{WHITE}• Tikanirsan epieos.com (Email - Phone){RESET}")
    print(f"""{RED}{BOLD}
0)Cikis{RESET}""")

def main():
    loading_animation_with_update()
    while True:
        menu()
        choice = input(f"\n{GREEN}Seciminiz (0-13): {RESET}")

        if choice == "0":
            clear_screen()
            print(f"{RED}Cikis yapiliyor...{RESET}")
            break
        elif choice == "1":
            username = input(f"{WHITE}: {RESET}")
            sherlok(username)
        elif choice == "2":
            email = input(f"{WHITE}E-posta: {RESET}")
            holehe(email)
        elif choice == "3":
            target = input(f"{WHITE}Username/E-posta: {RESET}")
            socialscan(target)
        elif choice == "4":
            email = input(f"{WHITE}E-posta: {RESET}")
            blackbird(email)
        elif choice == "5":
            email = input(f"{WHITE}E-posta: {RESET}")
            ghunt(email)
        elif choice == "6":
            username = input(f"{WHITE}Username: {RESET}")
            whatsmyname(username)
        elif choice == "7":
            url = input(f"{WHITE}Website URL: {RESET}")
            photon(url)
        elif choice == "8":
            spiderfoot()
        elif choice == "9":
            shodan()
        elif choice == "10":
            maltego()
        elif choice == "11":
            face_and_storage()
        elif choice == "12":
            exiftool()
        elif choice == "13":
            url = input(f"{WHITE}Website URL: {RESET}")
            waybackmachine(url)
        else:
            clear_screen()
            print(f"{RED}Hatali girdi!{RESET}")

        sleep(1)

if __name__ == "__main__":
    if os.getuid() != 0:
        print(f"{RED}[!] Root yetkisi gerekli! (sudo){RESET}")
        sys.exit(1)
    main()
