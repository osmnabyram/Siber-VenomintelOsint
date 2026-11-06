"""Ana akis. Orijinal main() ile ayni menu/davranis.

Secenekler veri-odakli iki tablodan yonlendirilir: girdi alanlar ve almayanlar.
"""

import os
import sys
from time import sleep

from .ui.animation import loading_animation_with_update
from .ui.menu import show_menu
from .ui.colors import GREEN, WHITE, RED, RESET
from .core import tools

# choice -> (prompt, handler)  (girdi alan secenekler; orijinal prompt metinleri)
INPUT_HANDLERS = {
    "1": (": ", tools.sherlock),
    "2": ("E-posta: ", tools.holehe),
    "3": ("Username/E-posta: ", tools.socialscan),
    "4": ("E-posta: ", tools.blackbird),
    "5": ("E-posta: ", tools.ghunt),
    "6": ("Username: ", tools.whatsmyname),
    "7": ("Website URL: ", tools.photon),
    "13": ("Website URL: ", tools.waybackmachine),
}

# choice -> handler  (girdi almayan secenekler)
NOINPUT_HANDLERS = {
    "8": tools.spiderfoot,
    "9": tools.shodan,
    "10": tools.maltego,
    "11": tools.face_and_storage,
    "12": tools.exiftool,
}


def run():
    loading_animation_with_update()
    while True:
        show_menu()
        choice = input(f"\n{GREEN}Seciminiz (0-13): {RESET}")

        if choice == "0":
            tools.clear_screen()
            print(f"{RED}Cikis yapiliyor...{RESET}")
            break
        elif choice in INPUT_HANDLERS:
            prompt, handler = INPUT_HANDLERS[choice]
            value = input(f"{WHITE}{prompt}{RESET}")
            handler(value)
        elif choice in NOINPUT_HANDLERS:
            NOINPUT_HANDLERS[choice]()
        else:
            tools.clear_screen()
            print(f"{RED}Hatali girdi!{RESET}")

        sleep(1)


def main():
    getuid = getattr(os, "getuid", None)
    if getuid is not None and getuid() != 0:
        print(f"{RED}[!] Root yetkisi gerekli! (sudo){RESET}")
        sys.exit(1)
    run()


if __name__ == "__main__":
    main()
